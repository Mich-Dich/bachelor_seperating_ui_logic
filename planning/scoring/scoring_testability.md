## Testability

| Description | Evaluates how easy it is to test business logic in isolation. |
|-|-|
| Sub-factors | Support for unit testing <br> Support for integration/system testing without UI <br> Availability of mocks/stubs for external dependencies |
| Metrics | Percentage of logic testable without UI <br> Time required to set up automated tests |


### Model-View-Controller (MVC)
MVC enables unit testing of the Model component in isolation, as it contains no references to UI concerns. However, the Controller presents significant testability challenges, as it frequently mixes business logic with UI flow control and often requires emulation of HTTP requests or UI events to be exercised [14]. The View-Controller coupling creates dependencies that complicate pure unit testing without UI automation frameworks. Integration testing remains possible but requires more elaborate setup due to the bidirectional communication between components. While the Model achieves reasonable test coverage, the substantial logic residing in Controllers reduces the overall percentage of code testable without UI involvement.

**Pros:**
- Model can be unit tested independently
- Clear separation allows focused tests on data logic

**Cons:**
- Controllers require UI emulation for testing
- View-Controller coupling complicates isolation
- Business logic often embedded in controllers

**Score: 5/10**

### Model-View-Presenter (MVP)
MVP significantly improves testability by introducing a Presenter that communicates with the View through an interface, enabling complete isolation of presentation logic from the UI framework [9]. The View becomes passive and can be replaced with test doubles (mocks or stubs), allowing the Presenter to be unit tested without any UI automation. All user interactions are routed through the Presenter, which can be exercised programmatically. Integration testing benefits from the interface-based contract between View and Presenter, though the Presenter still maintains references to both layers. The pattern achieves high controllability as dependencies can be injected during test setup.

**Pros:**
- Presenter testable through View interface mocks
- Complete separation of UI from presentation logic
- High controllability via dependency injection

**Cons:**
- Presenter maintains bidirectional coupling
- Increased test setup complexity with interface mocks

**Score: 8/10**

### Model-View-ViewModel (MVVM)
MVVM achieves exceptional testability by eliminating the View's direct reference to the ViewModel [11]. The ViewModel exposes state and commands through observables without any knowledge of the UI framework, enabling pure unit testing of all presentation logic. Data binding handles communication declaratively, removing imperative UI manipulation code that would otherwise require UI automation. The ViewModel can be instantiated and tested in isolation with simple mock objects for services, achieving nearly 100% coverage of presentation logic without UI involvement [10]. Research on mobile application architectures confirms MVVM as superior for testability compared to MVC and MVP alternatives [9] [9].

**Pros:**
- ViewModel completely independent of UI framework
- All presentation logic testable without UI automation
- Excellent controllability through dependency injection

**Cons:**
- Data binding debugging can complicate test failure analysis
- Requires understanding of observable patterns for test verification

**Score: 9/10**

### Hexagonal Architecture (Ports and Adapters)
Hexagonal Architecture represents the gold standard for testability by placing business logic at the core, entirely isolated from external concerns through ports (interfaces) and adapters [8]. All dependencies point inward, ensuring the domain logic has no knowledge of databases, APIs, or UI frameworks. Tests become trivial because any external dependency can be replaced with in-memory stubs or lambda implementations of the port interfaces [8]. Controllability is maximized through constructor injection of all dependencies, allowing test scenarios to set any desired state. Observability is enhanced as core logic returns values rather than producing side effects. The pattern enables testing of business logic in milliseconds without any infrastructure setup.

**Pros:**
- Complete isolation of domain logic from infrastructure
- Dependencies injected, enabling trivial stubbing [8]
- Single-method ports allow lambda implementations in tests

**Cons:**
- Increased number of interfaces requires more test setup code
- Adapter testing still requires integration with real technologies

**Score: 10/10**

### Plugin System
Plugin architecture enables independent testing of each plugin module, as plugins are developed and deployed separately from the core system. The core defines stable extension interfaces, allowing plugins to be unit tested against those contracts with mock core implementations. Integration testing requires careful management of plugin isolation, as runtime loading introduces complexity [13]. Observability can be challenging when multiple plugins interact, as side effects may span module boundaries. The pattern supports testability through clear module boundaries, though verifying compatibility across plugin versions requires additional integration testing effort.

**Pros:**
- Each plugin testable independently from core
- Clear interface contracts enable mock-based testing
- Plugins can be tested in isolation before deployment

**Cons:**
- Runtime plugin loading complicates integration testing [13]
- Cross-plugin interactions difficult to observe
- Compatibility testing requires matrix of plugin combinations

**Score: 8/10**

### Onion Architecture
Onion Architecture enforces strict dependency inversion, ensuring all dependencies point inward toward the domain core [12]. The domain layer contains only business logic with no references to infrastructure or UI, making it fully testable in isolation. Application services orchestrate use cases and can be tested with mocked repository interfaces. The concentric layer structure provides clear separation where outer layers depend on inner layers, never the reverse. This design achieves maximum controllability as all external dependencies are injected through interfaces defined by the inner layers. Testing can proceed from innermost domain logic outward, with each layer independently verified.

**Pros:**
- Domain layer completely testable with zero dependencies
- Application services testable with mocked repositories
- Layered structure enables incremental test construction

**Cons:**
- Multiple abstraction layers increase test complexity
- Requires careful design of interface boundaries

**Score: 10/10**

### Front Controller Pattern
The Front Controller pattern centralizes request handling but does not fundamentally improve testability of business logic. Controllers typically contain application logic that mixes routing, authentication, and business operations, making isolated unit testing difficult [14]. Testing requires emulation of HTTP requests, session state, and request parameters. Business logic embedded in controllers cannot be exercised without UI simulation frameworks. While the centralized handler can be tested as a single unit, the lack of separation between control logic and business logic severely limits the percentage of code testable without UI involvement.

**Pros:**
- Single entry point simplifies request flow testing
- Centralized location for cross-cutting concerns

**Cons:**
- Controllers require HTTP request emulation
- Business logic often mixed with control logic
- No enforced separation between UI and business concerns

**Score: 3/10**

### Backend-for-Frontend (BFF)
BFF improves testability by isolating UI-specific backend concerns from core business services. Each BFF can be tested independently with mocked core service dependencies, enabling thorough testing of data aggregation, transformation, and protocol adaptation logic without involving the UI. Core business services remain unaffected by UI changes and can be tested separately with their own test suites. However, the BFF layer itself requires integration testing to verify correct API contracts with its corresponding frontend. The pattern supports both unit testing of individual BFF components and integration testing across the frontend-BFF-core service chain.

**Pros:**
- BFF logic testable with mocked core services
- Core business services tested independently
- Clear separation of UI-specific from domain logic

**Cons:**
- Multiple BFFs increase overall testing effort
- Contract testing required between BFF and frontend

**Score: 8/10**

### Model-View-Adapter (MVA)
MVA introduces an Adapter layer that translates between Model and View, providing moderate testability improvements over basic MVC. The Adapter can be unit tested independently as it contains transformation logic without UI references. However, the View typically retains direct references to the Adapter, creating coupling that complicates isolated testing. The Model remains testable, but presentation logic often splits between Adapter and View, reducing the percentage of code testable without UI frameworks. The pattern lacks the clear separation achieved by MVP or MVVM.

**Pros:**
- Adapter layer testable without UI dependencies
- Model remains independently testable

**Cons:**
- View couples to Adapter, complicating isolation
- Presentation logic split across multiple components
- Less established testing patterns than MVVM

**Score: 6/10**

### Microkernel Architecture
Microkernel architecture enhances testability by separating the minimal core from extensible modules, allowing each component to be tested independently. The core system can be unit tested without any plugins loaded, verifying essential business logic in isolation. Plugins are developed against stable extension interfaces and can be tested with mock core implementations. However, testing interactions between the core and plugins requires careful integration testing, and preemptive concurrency in microkernel-based systems can introduce verification complexity [13]. Formal verification methodologies have been developed to address these challenges in safety-critical contexts.

**Pros:**
- Core testable without any plugins
- Plugins testable with mock core implementations
- Clear module boundaries enable independent testing

**Cons:**
- Integration testing requires coordinated core and plugin execution
- Runtime module loading complicates test automation
- Concurrency in microkernel systems adds verification complexity

**Score: 8/10**




### Sources:
[7]: [https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
[8]: [https://martinfowler.com/eaaDev/uiArchs.html](https://martinfowler.com/eaaDev/uiArchs.html)
[9]: [https://neu-pdi.github.io/cs3100-public-resources/lecture-slides/l16-testability/](https://neu-pdi.github.io/cs3100-public-resources/lecture-slides/l16-testability/)
[10]: [https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=izkab&paperid=902&option_lang=eng](https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=izkab&paperid=902&option_lang=eng)
[11]: [https://visualstudiomagazine.com/articles/2011/04/01/pfcov_silverlight-mvvm-tips.aspx](https://visualstudiomagazine.com/articles/2011/04/01/pfcov_silverlight-mvvm-tips.aspx)
[12]: [https://github.com/david-torosyan/Onion-Architecture](https://github.com/david-torosyan/Onion-Architecture)
[13]: [https://link.springer.com/chapter/10.1007/978-3-031-57259-3_9](https://link.springer.com/chapter/10.1007/978-3-031-57259-3_9)
[14]: [https://lists.owasp.org/pipermail/owasp_php_security_project/2013-September/000440](https://lists.owasp.org/pipermail/owasp_php_security_project/2013-September/000440)



