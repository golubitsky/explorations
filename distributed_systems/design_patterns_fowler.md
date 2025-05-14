# 📚 Study Plan: 25 Essential Distributed Systems Patterns

This study order builds your knowledge step-by-step, starting with core concepts like time and coordination, and progressing toward replication, scaling, and fault-tolerance. Each pattern is linked for direct access.

---

## ⏱️ 1. Time & Ordering (Start Here)

Understand how distributed systems reason about time and ordering of events.

- [Lamport Clock](https://lnkd.in/g6Ma6VyB)
- [Hybrid Clock](https://lnkd.in/gCkgTjQh)
- [Generation Clock](https://lnkd.in/gQ3ZCNgX)
- [Clock Bound Wait](https://lnkd.in/g5xXEsyb)

---

## 🧭 2. Leader Election & Coordination

Learn how systems coordinate roles and ensure only one node is acting as a leader at a time.

- [Heartbeat](https://lnkd.in/gF-tRnQR)
- [Emergent Leader](https://lnkd.in/gBmu2Z7h)
- [Leader Follower](https://lnkd.in/gPwejHqP)
- [Lease](https://lnkd.in/gxqrdgBw)

---

## 🗳️ 3. Consensus & Replication

Dive into consistency guarantees, replication mechanics, and achieving agreement.

- [Majority Quorum](https://lnkd.in/gXYHNniN)
- [Replicated Log](https://lnkd.in/gqjWa9tw)
- [Paxos](https://lnkd.in/gm6qqNPc)
- [Consistent Core](https://lnkd.in/gPBKWucA)
- [Follower Reads](https://lnkd.in/gVVSCYvN)

---

## 🧩 4. Partitioning & Scalability

Explore how distributed systems scale out and manage data across partitions.

- [Fixed Partitions](https://lnkd.in/gHtg_wZ6)
- [Key Range Partitions](https://lnkd.in/gzJDEMt9)

---

## 💬 5. Communication Patterns

Design efficient request flows and queueing systems to reduce bottlenecks.

- [Request Pipeline](https://lnkd.in/gKjhZ8cK)
- [Request Batch](https://lnkd.in/g2MBCiE3)
- [Request Waiting List](https://lnkd.in/gRB_kBZS)
- [Single Socket Channel](https://lnkd.in/gYz9Nsvi)
- [Singular Update Queue](https://lnkd.in/gKd_zK-N)

---

## 🪣 6. State Progress & Watermarks

Used in systems like Kafka or Flink to track processing and replay status.

- [High Watermark](https://lnkd.in/gJBUrcgm)
- [Low Watermark](https://lnkd.in/gp7neH2D)
- [Segmented Log](https://lnkd.in/g7k9wJkX)

---

## 🔁 7. Resilience & Dissemination

Patterns for ensuring reliable retries and efficient information propagation.

- [Idempotent Receiver](https://lnkd.in/gPJCscbj)
- [Gossip Dissemination](https://lnkd.in/gFbuxsQZ)

---

## 🧠 Study Tips

- ✔️ Study 1–2 patterns per day.
- 📝 Write your own summary and example use case.
- 🖍️ Draw a diagram to visualize the concept.
- 🎯 Apply 3+ patterns to a mock system design (e.g., Dropbox, Kafka).
- 🔄 Revisit and explain to a peer to reinforce understanding.

---
