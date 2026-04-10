
## Front Controller Pattern [Source](https://www.oracle.com/java/technologies/front-controller.html)

Front Controller is a pattern where **all UI requests go through a single centralized handler**, which then delegates to business logic components.

* **Core Idea:** One entry point for all UI interactions.
* **Flow:**
  * User → Front Controller → Business Logic → Response → View
* **Purpose:** Centralize control, routing, and preprocessing.

### Pros:
* Simplifies UI handling logic.
* Central place for authentication, logging, etc.

### Cons:
* Can become a bottleneck.
* Doesn’t fully decouple UI from business logic (only partially).

This is more of a **UI control pattern**, but still relevant for separation discussions.
