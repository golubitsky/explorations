# 📘 25 Essential Distributed Systems Design Patterns
Curated from Martin Fowler's blog and related sources. Grouped by category for focused study.

---

## ⏱️ Time & Ordering

These patterns help maintain temporal consistency and order across distributed components.

- [Clock Bound Wait](https://lnkd.in/g5xXEsyb)
- [Generation Clock](https://lnkd.in/gQ3ZCNgX)
- [Hybrid Clock](https://lnkd.in/gCkgTjQh)
- [Lamport Clock](https://lnkd.in/g6Ma6VyB)

---

## 🧭 Coordination & Leadership

For handling leadership election, failover, and control flow among distributed nodes.

- [Emergent Leader](https://lnkd.in/gBmu2Z7h)
- [Leader Follower](https://lnkd.in/gPwejHqP)
- [Lease](https://lnkd.in/gxqrdgBw)
- [Heartbeat](https://lnkd.in/gF-tRnQR)

---

## 🧩 Partitioning & Scalability

Key to distributing workloads and scaling effectively.

- [Fixed Partitions](https://lnkd.in/gHtg_wZ6)
- [Key Range Partitions](https://lnkd.in/gzJDEMt9)

---

## 🔁 Replication & Consistency

Foundational to data durability, fault tolerance, and consensus across replicas.

- [Consistent Core](https://lnkd.in/gPBKWucA)
- [Follower Reads](https://lnkd.in/gVVSCYvN)
- [Majority Quorum](https://lnkd.in/gXYHNniN)
- [Replicated Log](https://lnkd.in/gqjWa9tw)
- [Paxos](https://lnkd.in/gm6qqNPc)

---

## 💬 Communication & Message Handling

Patterns focused on batching, pipelining, and managing request lifecycles.

- [Request Batch](https://lnkd.in/g2MBCiE3)
- [Request Pipeline](https://lnkd.in/gKjhZ8cK)
- [Request Waiting List](https://lnkd.in/gRB_kBZS)
- [Single Socket Channel](https://lnkd.in/gYz9Nsvi)
- [Singular Update Queue](https://lnkd.in/gKd_zK-N)

---

## 📡 Dissemination & Gossip

How information is propagated across systems in a decentralized manner.

- [Gossip Dissemination](https://lnkd.in/gFbuxsQZ)

---

## ✅ Idempotency & Fault Handling

Designing for safe retries and avoiding duplication.

- [Idempotent Receiver](https://lnkd.in/gPJCscbj)

---

## 🪣 Watermarks & Progress Tracking

Helps track the state of processing, especially in streaming or log-based systems.

- [High Watermark](https://lnkd.in/gJBUrcgm)
- [Low Watermark](https://lnkd.in/gp7neH2D)
- [Segmented Log](https://lnkd.in/g7k9wJkX)

---

## 🧠 Study Tip

For each pattern:
- Summarize in your own words
- Draw a diagram
- Identify a real-world system that uses it (e.g., Kafka, Raft, Cassandra)
- Practice explaining trade-offs in mock interviews

---

