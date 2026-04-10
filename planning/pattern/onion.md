
## Onion Architecture [Source](https://www.clarity-ventures.com/articles/onion-based-software-architecture)

Onion Architecture is closely related to Clean Architecture and organizes the system into **concentric layers centered around the domain model**, emphasizing that the **core business logic is completely isolated from infrastructure and UI concerns**.
* **Core Idea:** The domain model sits at the center, surrounded by layers like services, infrastructure, and UI. ([Clarity Ventures][2])
* **Dependency Rule:** All dependencies point inward toward the domain.
* **Layers:**

  * Domain (core logic)
  * Application services
  * Infrastructure (DB, APIs)
  * Presentation (UI)
* **Goal:** Protect the domain logic from external changes.

### Pros:
* Strong decoupling of UI and infrastructure from core logic.
* Encourages domain-driven design.
* Highly maintainable and testable.

### Cons:
* Conceptually similar to Clean/Hexagonal.
* Can introduce unnecessary layers in simple applications.
