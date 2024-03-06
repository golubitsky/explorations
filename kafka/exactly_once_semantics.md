How does Apache Kafka implement a guarantee to deliver each message sent through it exactly once?

## Background

The essence of the problem is acknowledgement in distributed systems. We can have these message semantics when producing messages:

- at least once delivery
  - if ack fails to be received, retry until ack is received
  - result: producer may publish a duplicate message
- at most once delivery

  - if ack fails to be received, do not retry
  - result: message may be dropped

- exactly once delivery

  - Traditionally,

    - > The way we achieve exactly-once delivery in practice is by faking it. Either the messages themselves should be idempotent, meaning they can be applied more than once without adverse effects, or we remove the need for idempotency through deduplication.

      - [source (great blog, links to other blogs and primary sources)](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/)

  - In Kafka Streams specifically
    - > So effectively Kafka supports exactly-once delivery in Kafka Streams, and the transactional producer/consumer can be used generally to provide exactly-once delivery when transferring and processing data between Kafka topics. Exactly-once delivery for other destination systems generally requires cooperation with such systems, but Kafka provides the offset which makes implementing this feasible (see also Kafka Connect). Otherwise, Kafka guarantees at-least-once delivery by default, and allows the user to implement at-most-once delivery by disabling retries on the producer and committing offsets in the consumer prior to processing a batch of messages.
    - [source (Kafka docs)](https://kafka.apache.org/documentation/#semantics)

So it's important to note that the **exactly-once semantics are guaranteed by Kafka only when using Kafka Streams**, which store data on Kafka topics.

## Exactly-once semantics in Kafka Streams

From the [Kafka Streams docs](https://kafka.apache.org/documentation/streams/):

- Kafka Streams is a client library for processing and analyzing **data stored in Kafka**.
- Supports exactly-once processing semantics to guarantee that each record will be processed once and only once even when there is a failure on either Streams clients or Kafka brokers in the middle of processing.

A read-process-write stream processing application is composed of **three steps that all need to happen exactly once in EOS**:

A function F is triggered for each message A read from the input Kafka topics. F is composed of three key steps:

1. Update the application state from S to S’.
2. Write result messages B1, … Bn to output Kafka topic(s) TB.
3. Commit offset of the processed record A on the input Kafka topic TA.

In Kafka Streams, this atomicity problem is simplified:

1. **Step 3 above becomes just publishing to a topic** (the offsets topic)
2. In the Kafka Streams library, all state stores capture their updates by default into some special Kafka topics called the changelog topics. So **step 1 also is simplified to publishing to a topic**.

Therefore, the atomicity problem becomes a matter of atomically sending records to the various topics in steps 1-3 above.

That is why the Kafka transactions feature is the second piece, along with the idempotent producer (both described in the notes below, including failure modes), required to achieve exactly-once semantics (EOS).

> By using this mechanism, Kafka Streams can ensure that records are sent to to the sink topics, the changelog topics, and the offset topics atomically.

[source](https://www.confluent.io/blog/enabling-exactly-once-kafka-streams/)

## [Kafka - Exactly once semantics with Matthias J. Sax (YouTube)](https://www.youtube.com/watch?v=twgbAL_EaQw)

My notes on this video:

- Different guarantees
  - At least once
  - At most once
  - Exactly once
    - tailored to "stream processing" and not really "message delivery" use cases
- "exactly once semantics"
  - every message is processed exactly once
  - results published exactly once
  - semantically exactly once
    - same result as-if no errors happened, no retry needed
- Kafka Streams is a stateful stream-processing library
- Kafka Streams implements exactly once semantics using lower level Kafka APIs (producer and consumer)
  - to use lower level APIs is more complex
  - Kafka Streams is recommended as default implementation
- exactly once is provable not solvable"
- **problem**: how can producer know for sure the broker has committed the message?

  - an ack can be lost on the way to the producer by after message has been committed by broker
  - solution: **idempotent producer**

    - assign unique ID to every message sent to broker
      - how to assign UUIDs?
      - get a producerID from kafka
    - broker also stores the ID in the partition using hashmap
    - now broker can avoid storing same message n times, ultimately an ack _will_ make it to producer
    - so it's not "exactly once delivery" but rather "exactly once semantics"
    - every part of a system has to be "exactly once"

  - **remaining problem**

    - if producer goes down before receiving ack, still possible for Kafka to receive two identical messages with different UUIDs

  - solution: **Kafka transactions**
    - Kafka transaction is a multi-topic multi-partition atomic write
    - flow
      - producer
        - (on start) register itself as transactional producer
        - register a transaction UUID, unique across cluster
        - register which partition will be used to send message(s) in transaction
        - send message
      - transaction coordinator
        - track which partitions and topics are involved in the transaction
        - track status of transaction (open, committed, timeout, etc.)
        - transaction states are written to a special internal topic, kind of like a write-ahead log (WAL)
          - this topic is compacted based on unique ID of corresponding producer
            - saves data on completed transactions
      - consumer:
        - depending on transaction isolation, read message only if committed
        - but messages with pending status cannot be determined alone by consumer
        - broker has a **high watermark**
          - messages with higher offset are not replicated yet, not safe to deliver to consumer
          - a bound to which point a consumer is allowed to read
      - failure modes
        - if producer fails during transaction (leaving the transaction in pending)
          - **producer is not fault-tolerant**
          - new producer registers itself with same producer id
          - transaction coordinator knows that the old producer might have died
          - transaction coordinator aborts the transaction
          - if producer doesn't come up for a long time
            - the broker will timeout a pending transaction
              - reason: high watermark cannot be advanced
        - if broker dies
          - no problem, automatic failover to new coordinator
            - producer needs to reach transaction coordinator and retries until it has come back online
            - transaction coordinator has already recorded all the transaction state changes into internal topic
            - that topic has been replicated
            - after leader election
              - new transaction coordinator reads the topic to rebuild the state for in-memory cache
              - resume transaction
            - **broker _is_ fault-tolerant**
  - testing
    - system tests with random fault injection
      - kill brokers
      - kill Kafka Streams applications
      - assert expected state based on dedicated workload
    - idempotent consumers are still important
      - while you are inside Kafka (with Kafka Streams) you are covered by enabling
  - Why not enable exactly once by default?
    - idempotent producer _is_ enabled by default
    - Kafka transactions
      - there is nothing to enable; developer opts in by starting a transaction
  - Use Cases
    - highly sensitive data
      - financial processing
    - duplicate processing can impact your business
      - e.g., you want to send money from account A to account B
    - when is it **not** needed?
      - if you ensure end-to-end idempotency
        - "at least once delivery" is enough; exactly once not needed
        - https://microservices.io/patterns/communication-style/idempotent-consumer.html
        - https://www.lydtechconsulting.com/blog-kafka-idempotent-consumer.html
      - damage that you're doing is low
        - send a promotion package twice — nothing really bad happened

## Resources

- 3 blogs about the exactly-once semantics for Apache Kafka Streams

  - https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/
  - https://www.confluent.io/blog/transactions-apache-kafka/
  - https://www.confluent.io/blog/enabling-exactly-once-kafka-streams/
    - What is Exactly-Once for Stream Processing?
    - Exactly-Once: Why is it so Hard?

- https://kafka.apache.org/documentation/#semantics

- [Exactly Once Delivery and Transactional Messaging in Kafka Design Doc](https://docs.google.com/document/d/11Jqy_GjUGtdXJK94XGsEIK7CP1SnQGdp2eF0wSw9ra8/edit)

- [Introducing Exactly Once Semantics in Apache Kafka (Video and slides)](https://www.confluent.io/kafka-summit-nyc17/introducing-exactly-once-semantics-in-apache-kafka/)
- https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/
  - > The way we achieve exactly-once delivery in practice is by faking it. Either the messages themselves should be idempotent, meaning they can be applied more than once without adverse effects, or we remove the need for idempotency through deduplication.
    - (I think this is what is also referred to as "exactly-once semantics")
  - https://www.slideshare.net/TylerTreat/from-mainframe-to-microservice-an-introduction-to-distributed-systems-41004778#23
  - https://bravenewgeek.com/understanding-consensus/

Additional blogs:

- https://oleg0potapov.medium.com/how-kafka-achieves-exactly-once-semantics-57fdb7ad2e3f
- https://oleg0potapov.medium.com/event-patterns-idempotent-consumer-or-inbox-b2812bf6656a
