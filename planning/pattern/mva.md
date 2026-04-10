
## Model-View-Adapter (MVA) [Source](https://martinfowler.com/eaaDev/uiArchs.html)

MVA is a variation of MVC where an **adapter layer sits between the model and view**, translating data formats and interactions.
* **Core Idea:** Introduce an adapter to decouple UI representation from business logic.
* **Structure:**
  * Model (business logic)
  * Adapter (transformation layer)
  * View (UI)

### Pros:
* Cleaner separation than basic MVC.
* Useful when UI representation differs significantly from data model.

### Cons:
* Adds extra abstraction layer.
* Not as widely adopted as MVVM.
