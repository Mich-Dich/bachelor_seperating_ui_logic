
## Hexagonal Architecture (Ports and Adapters) [Source](https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29)

Hexagonal Architecture, also known as *Ports and Adapters*, is a pattern that emphasizes isolating the business logic from external systems such as UI frameworks, databases, or messaging systems by defining interfaces (ports) and implementation adapters.

* **Core Idea:** Instead of organizing code into strict vertical layers, this architecture places the **business logic at the center** of a hexagon. All interactions with the outside world happen through abstract *ports* (interfaces) and *adapters* (implementations).
* **Ports:** Define what the core business logic needs from the outside world (e.g., persistence, UI interaction).
* **Adapters:** Are the concrete implementations that fulfill those port interfaces (e.g., REST API, database connector, CLI handler).
* **Benefits:** Allows the core logic to be developed and tested independently from UI or infrastructure concerns, improves flexibility to swap technologies, and supports robust testing with mocks or stubs.
* **Drawbacks:** Initial design can be more complex and conceptual compared to traditional layered approaches, requiring careful interface design.

### Pros of Hexagonal Architecture
* Strong isolation of business logic from external systems.
* Makes automated testing much easier because dependencies can be mocked.
* Encourages flexible swapping of UI, storage, or communication mechanisms.

### Cons of Hexagonal Architecture
* May require more upfront design effort.
* Adapters add indirection that can increase complexity for small systems.
