## Design Goals

- Develop and deploy multiple services developed in one or more separate repos.
- PUB/SUB
- HTTP
- Zero-downtime deployment
- Develop in production-like environment
- Limited to one language -- Python -- to keep things simple.
- Dedicated scripts for
  - Deploying all services
  - Deploying one service
  - Testing all services (i.e. integration test)
  - Testing one service (i.e. development)

### Implementation

- Development environment should
