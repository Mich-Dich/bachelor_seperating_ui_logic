
## Backend-for-Frontend (BFF) [Source](https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends)

BFF is an architectural pattern where **each UI gets its own backend tailored to its needs**, while the core business logic remains separate.
* **Core Idea:** Separate backend layers for different UIs (desktop, mobile, embedded).
* **Structure:**
  * Core services (business logic)
  * Multiple BFF layers (UI-specific logic)
* **Goal:** Decouple UI-specific concerns from core logic.

### Pros:
* Perfect for multiple frontends.
* Keeps UI-specific logic out of core business logic.

### Cons:
* More services to maintain.
* Adds architectural overhead.
