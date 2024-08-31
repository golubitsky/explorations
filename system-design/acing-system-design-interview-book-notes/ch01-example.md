- **Definitions**

  - **Scalability of a service:**
    - The ability to easily and cost-effectively vary resources allocated to it.
    - Applies to varying user numbers and/or requests to the system.
  - **Latency:**
    - The time it takes for data to travel from the source to the destination, often measured as the delay between a request and the start of a response.
    - Measured in milliseconds (ms) or seconds.
    - Lower latency means faster response times.
  - **Throughput:**
    - The amount of data transmitted over a network or processed by a system within a given time period.
    - Measured in bits per second (bps), requests per second, or transactions per second.
    - Higher throughput indicates a greater volume of data handled efficiently.
  - **Reliability:**
    - The ability of a system or network to consistently perform its intended function without failure.
    - Measured in percentage of uptime (e.g., 99.9%).
    - High reliability means fewer interruptions and more stable service.

- **Services**

  - Backend
  - Frontend
  - Mobile
  - DB

- **Basic techniques for scaling a service**

  - **DNS:**
    - GeoDNS is a DNS service that routes users to different servers based on their geographic location to optimize performance and reduce latency.
  - **Caching**
  - **CDN:**
    - Store copies of static assets on hosts around the world.
    - Remove bottleneck of downloading static assets from a single app server.

- **Load balancer**

- **Idempotent services**

  - Allow horizontal scaling.
  - End-to-end idempotency

- **CI/CD**

  - **Gradual rollouts and rollbacks:**
    - **Gradual rollout:**
      - Canary releases
      - Feature flags
      - Blue-green deployment
      - **For UX:**
        - Use feature flags to enable:
          - A/B testing
          - Multivariate testing
    - **Monitoring:**
      - Bugs
      - Crashes
      - Increased latency or timeouts
      - Memory leaks
      - Increased resource consumption (CPU, memory, storage)
      - User churn
      - SLI/SLO/SLAs
    - **Rollback:**
      - Automatic
      - Manual

- **Functional partitioning and centralization of cross-cutting concerns**

  - **Logging:**
    - Log-based message broker (e.g., ELK stack, Splunk)
    - OpenTelemetry is a robust choice if you need a comprehensive solution that integrates tracing with metrics and logging, while Jaeger and Zipkin can be simpler choices if your focus is strictly on tracing.
    - Span IDs enable distributed tracing.
  - **Monitoring/alerting**
  - **Search (e.g., Elasticsearch)**

- **API gateway**

  - Reverse proxy
  - Implements common functionality to avoid duplication:
    - Authentication/authorization
    - Logging/monitoring/alerting at request level
    - Rate limiting
    - Billing
    - Analytics

- **Service mesh**

  - Sidecar containers
  - Sidecar-less
    - https://cloud.google.com/blog/topics/developers-practitioners/traffic-director-explained

- **CQRS (command query responsibility segregation)**

  - Command/write operations and query/read operations partitioned onto separate services
    - Write/read services can be scaled separately
  - Examples: message brokers and ETL jobs
  - Any design where data is written to one table and then transformed and inserted into another table

- **Batch and streaming ETL (extract, transform, load)**

  - Spread out the processing of traffic spikes over a longer time period, reducing required cluster size.
  - **Use cases:**
    - Some requests require large queries to DB:
      - Instead, periodically preprocess certain data (e.g., top 10 most-frequently accessed data).
    - Acceptable to show users statistics that are out of date by a few hours.
    - Writes that do not have to be executed immediately (e.g., logging) can be placed on a queue.
  - **Asynchronous approach**

- **Serverless (FaaS - functions as a service)**

  - Exchange decreased cost of running servers for limited functionality (short-lived, stateless, simple dependencies)
  - **Endpoints:**
    - Infrequently-used
    - With no strict latency requirements
  - **API gateway is necessary**
  - **Pro:**
    - Deployment/scaling need not be managed

- **Scaling**
  - **Frontend:**
    - Serves same browser app
    - Simple scalability: adjust cluster size and use GeoDNS
  - **Backend:**
    - Dynamic, can serve different responses
    - Scalability techniques are more varied/complex
