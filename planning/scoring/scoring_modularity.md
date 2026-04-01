## Modularity / Separation of Concerns
| Description | Measures how well the pattern isolates UI from business logic. |
|-|-|
| Sub-factors | Degree of coupling (tight vs loose) <br> Ease of replacing one module without affecting others <br> Support for multiple UI platforms |
| Metrics | Number of dependencies between layers <br> Lines of code that need to change when modifying logic/UI |


### Model-View-Controller (MVC)
MVC establishes a foundational separation between UI (View), business logic (Model), and flow control (Controller). The Model remains independent of the View, enabling multiple visual representations of the same data [0]. However, the Controller often becomes tightly coupled with both the View and Model, creating a bottleneck in complex applications. Replacing the UI requires modifications to the Controller, which reduces modularity compared to more modern patterns. The pattern supports multiple UI platforms through shared Models but requires significant effort to fully decouple.

**Pros:**
- Clear separation between data (Model) and presentation (View)
- Multiple Views can share a single Model
- Independent development of components possible

**Cons:**
- Controller often becomes a bottleneck and tightly coupled
- View and Controller frequently maintain direct references
- Modifying UI may require Controller changes

**Score: 7/10**

### Model-View-Presenter (MVP)
MVP improves upon MVC by making the View completely passive and removing its direct dependency on the Model. The Presenter mediates all communication, enabling better testability through interface-based contracts. The View communicates exclusively through the Presenter, which isolates business logic from UI concerns. However, the Presenter often maintains direct references to both layers, creating a tight coupling that can complicate UI replacement. Multiple UI platforms are supported through separate View implementations sharing a common Presenter.

**Pros:**
- Complete decoupling of View from Model
- Enhanced testability through interface-based design
- Passive View simplifies unit testing

**Cons:**
- Presenter maintains references to both View and Model
- Increased complexity and boilerplate code
- Communication overhead between components

**Score: 8/10**

### Model-View-ViewModel (MVVM)
MVVM achieves superior separation through data binding and the ViewModel's complete ignorance of the View. The ViewModel exposes observable properties and commands without any direct reference to UI components, enabling full testability and platform independence [1]. The View binds declaratively to ViewModel properties, eliminating imperative UI manipulation code. This design allows complete replacement of the UI layer without modifying business logic. Multiple UI platforms can share the same ViewModel with platform-specific Views, making it ideal for cross-platform development.

**Pros:**
- View has no reference to ViewModel (only bindings)
- Complete testability of ViewModel in isolation
- Excellent support for multiple UI platforms

**Cons:**
- Data binding complexity can increase debugging difficulty
- Requires understanding of observable patterns (INotifyPropertyChanged)

**Score: 9/10**

### Hexagonal Architecture (Ports and Adapters)
Hexagonal Architecture achieves perfect separation by placing business logic at the core, completely isolated from UI concerns through ports (interfaces) and adapters [2]. The UI interacts exclusively through defined ports, allowing any UI technology to be swapped without affecting core logic. Dependencies point inward toward the domain, ensuring UI modifications never impact business rules. Multiple UI platforms are supported simultaneously through different adapter implementations. This architecture enables complete independence of UI from business logic.

**Pros:**
- Complete isolation of business logic from UI
- Any UI technology can be plugged in via adapters
- Core logic testable without any UI dependencies

**Cons:**
- Increased upfront design complexity
- Indirection may be overengineering for simple applications

**Score: 10/10**

### Plugin System
Plugin architecture achieves exceptional separation by treating UI components as independently deployable modules that extend a core system [3]. The core defines extension points through well-defined interfaces, allowing UI plugins to be developed, tested, and replaced without modifying the core application. This dynamic loading capability enables runtime UI replacement and independent versioning. However, careful interface design is required to maintain separation, and plugin compatibility must be managed. Multiple UI paradigms can coexist through different plugin sets.

**Pros:**
- Dynamic addition/removal of UI components
- Independent development and deployment of UI modules
- Core remains completely unaware of specific UI implementations

**Cons:**
- Plugin interface design must be stable
- Compatibility management adds complexity
- Potential for version conflicts between plugins

**Score: 9/10**

### Onion Architecture
Onion Architecture organizes concentric layers with domain logic at the center, enforcing the dependency rule that all dependencies point inward [4]. UI concerns reside in the outermost layer, with no direct references from core layers to UI components. This inversion ensures that UI changes never impact business logic. Application services act as intermediaries, providing clear separation between presentation and domain. The architecture supports multiple UI platforms through interchangeable outer layers while maintaining domain integrity.

**Pros:**
- Strict dependency inversion ensures UI isolation
- Domain layer completely unaware of presentation concerns
- Highly maintainable and testable core logic

**Cons:**
- Multiple layers may introduce unnecessary abstraction
- Conceptual complexity higher than layered architecture

**Score: 10/10**

### Front Controller Pattern
Front Controller centralizes request handling but does not fundamentally decouple UI from business logic [5]. The pattern provides a single entry point for all UI requests, which can centralize cross-cutting concerns like authentication and logging. However, business logic often remains embedded in or tightly coupled to the controller. Replacing the UI typically requires significant modifications to the controller logic. This pattern is better characterized as a UI control mechanism rather than a separation architecture.

**Pros:**
- Centralized request handling simplifies routing
- Single point for cross-cutting concerns
- Reduces duplicate code across views

**Cons:**
- Does not enforce separation between UI and business logic
- Controller often becomes tightly coupled to both
- UI replacement requires controller modifications

**Score: 5/10**

### Backend-for-Frontend (BFF)
BFF achieves strong separation by creating dedicated backend services for each UI platform, isolating UI-specific concerns from core business logic [6]. Each BFF tailors responses to its specific client (web, mobile, embedded), allowing UI requirements to evolve independently. Core business services remain unchanged regardless of UI modifications. This pattern excels in multi-platform scenarios where each UI has distinct data and interaction patterns. However, operational overhead increases with multiple BFF services.

**Pros:**
- Complete isolation of UI-specific logic from core
- Each UI platform can evolve independently
- Core services remain agnostic to presentation needs

**Cons:**
- Multiple services increase operational complexity
- Potential for code duplication across BFFs
- Requires additional infrastructure management

**Score: 9/10**

### Model-View-Adapter (MVA)
MVA introduces an adapter layer between Model and View to handle data transformation and presentation logic, improving decoupling over basic MVC. The Adapter translates domain objects into UI-friendly representations, allowing the Model to remain presentation-agnostic. However, the View often maintains references to the Adapter, creating coupling that complicates UI replacement. Multiple UI platforms can share Models with platform-specific Adapters, though additional abstraction layers increase complexity.

**Pros:**
- Adapter isolates Model from presentation concerns
- Multiple UI representations through different Adapters
- Improved decoupling compared to MVC

**Cons:**
- View still couples to Adapter
- Additional layer increases complexity
- Less widely adopted with less community support

**Score: 7/10**

### Microkernel Architecture
Microkernel architecture separates a minimal core system from extensible modules, enabling UI components to be implemented as pluggable modules [3]. The core provides only essential business logic while UI modules extend functionality through defined interfaces. This design allows complete UI replacement without core modifications, as different UI implementations can be loaded as separate modules. The pattern excels in applications requiring multiple UI paradigms or where UI customization is a primary requirement.

**Pros:**
- Core system completely independent of UI implementation
- possible dynamic loading of UI modules at runtime
- Multiple UI paradigms can coexist

**Cons:**
- Complex plugin lifecycle management
- Debugging across modules can be challenging
- Requires stable interface definitions

**Score: 9/10**


### Sources:
[0]: [https://zh.wikipedia.org/zh-tw/MVC](https://zh.wikipedia.org/zh-tw/MVC)
[1]: [https://learn.microsoft.com/en-us/training/modules/design-mvvm-viewmodel/2-what-is-mvvm?WT.mc_id=friends-0000-jamont&ns-enrollment-type=learningpath&ns-enrollment-id=learn.dotnet-maui.build-apps-with-dotnet-maui](https://learn.microsoft.com/en-us/training/modules/design-mvvm-viewmodel/2-what-is-mvvm?WT.mc_id=friends-0000-jamont&ns-enrollment-type=learningpath&ns-enrollment-id=learn.dotnet-maui.build-apps-with-dotnet-maui)
[2]: [https://www.finclip.com/news/f/31516.html](https://www.finclip.com/news/f/31516.html)
[3]: [https://soft.zhiding.cn/software_zone/2008/0113/706390.shtml](https://soft.zhiding.cn/software_zone/2008/0113/706390.shtml)
[4]: [https://github.com/yuntai229/Onion-Architecture-Go](https://github.com/yuntai229/Onion-Architecture-Go)
[5]: [https://docs.oracle.com/cd/E19786-01/817-2334/03_design_issues.html](https://docs.oracle.com/cd/E19786-01/817-2334/03_design_issues.html)
[6]: [https://learn.microsoft.com/zh-hk/azure/architecture/patterns/backends-for-frontends](https://learn.microsoft.com/zh-hk/azure/architecture/patterns/backends-for-frontends)



