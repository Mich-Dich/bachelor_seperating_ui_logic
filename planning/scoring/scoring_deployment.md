## Deployment Flexibility

| Description | Ability to deploy the system across different environments (desktop, embedded, CI/CD). |
|-|-|
| Sub-factors | Multi-platform support <br> Ability to produce different binaries from the same core <br> Remote vs local execution capability |
| Metrics | Number of supported platforms <br> Ease of cross-compilation for embedded targets |


### Model-View-Controller (MVC)
MVC provides limited deployment flexibility. While the Model can theoretically be reused across platforms, the Controller's tight coupling to specific UI frameworks typically requires substantial reimplementation when targeting different environments. Web MVC frameworks assume HTTP request handling, desktop MVC assumes event-driven UI, and embedded deployments often require stripping Controllers entirely. Cross-platform frameworks like Xamarin have largely moved beyond MVC toward MVVM due to these limitations [26]. The pattern does not naturally support producing different binaries from the same core without significant adaptation layers.

**Pros:**
- Model can be shared across platforms with careful design
- Multiple Views can be created for different form factors

**Cons:**
- Controller tightly coupled to UI framework
- Reimplementation required for each target platform
- Embedded deployments require significant adaptation

**Score: 5/10**

### Model-View-Presenter (MVP)
MVP improves deployment flexibility over MVC through interface-based communication between Presenter and View. The Presenter, containing presentation logic, can be shared across platforms while View implementations are platform-specific. This enables targeting iOS, Android, and web from a shared codebase when combined with frameworks like Kotlin Multiplatform [30]. However, the bidirectional communication between Presenter and View creates platform-specific interface requirements that must be implemented per target. Deployment to embedded systems may require simplification of the Presenter layer.

**Pros:**
- Presenter reusable across multiple UI platforms
- Interface contracts enable platform-specific View implementations
- Supports cross-platform development with appropriate tooling

**Cons:**
- Bidirectional interface must be implemented per platform
- Embedded targets may require simplified Presenter
- Increased deployment complexity compared to MVC

**Score: 7/10**

### Model-View-ViewModel (MVVM)
MVVM achieves exceptional deployment flexibility through the ViewModel's complete ignorance of the View implementation. The ViewModel contains presentation logic in a platform-agnostic form, enabling reuse across iOS, Android, Windows, and web from a single shared codebase Xamarin and .NET MAUI frameworks explicitly leverage MVVM for cross-platform mobile and desktop development, demonstrating production-ready multi-platform deployment [26]. Data binding mechanisms vary across platforms (XAML, SwiftUI bindings, Jetpack Compose state), requiring platform-specific View layers, but the shared ViewModel core remains unchanged. This architecture supports producing different binaries for different targets while maintaining business logic integrity.

**Pros:**
- Single ViewModel core across all platforms
- Proven in production cross-platform frameworks (Xamarin, .NET MAUI)
- View layer fully replaceable per platform

**Cons:**
- Data binding mechanisms differ across platforms
- Platform-specific View implementation still required
- Testing requires platform-agnostic setup

**Score: 9/10**

### Hexagonal Architecture (Ports and Adapters)
Hexagonal Architecture provides maximum deployment flexibility by placing business logic at the core, completely isolated from all external interfaces through ports and adapters. Any number of UI adapters—REST APIs, CLI tools, desktop applications, mobile interfaces, or embedded system controllers—can be attached to the same core without modification [32]. The core can be compiled once and deployed across environments with different adapter configurations. This approach enables running the same business logic locally for development, in containers for production, and on embedded devices with minimal resource footprints by substituting lightweight adapters. Real-world implementations demonstrate simultaneous support for HTTP and CLI interfaces from identical domain code [27].

**Pros:**
- Unlimited UI adapters from single core
- Core compiles once, deploys to multiple environments
- Lightweight adapters for embedded deployments

**Cons:**
- Adapter development required per target platform
- Upfront interface design requires architectural investment

**Score: 10/10**

### Plugin System
Plugin systems enable flexible deployment by allowing different combinations of plugins to be bundled for different environments. A core system can be deployed with a minimal plugin set for embedded devices, with a full feature set for desktop, and with specialized plugins for server environments—all from the same codebase [33]. Plugins can be dynamically loaded at runtime, enabling runtime environment adaptation without redeployment. This architecture is particularly effective for applications requiring extensive customization per deployment scenario, such as CI/CD tools and IDEs [10]. However, plugin compatibility must be managed across deployment targets.

**Pros:**
- Different plugin bundles per deployment environment
- Dynamic loading enables runtime adaptation
- Core unchanged across all deployment scenarios

**Cons:**
- Plugin compatibility matrix complexity
- Runtime classloading adds deployment overhead
- Embedded deployments may lack dynamic loading support

**Score: 9/10**

### Onion Architecture
Onion Architecture achieves equivalent deployment flexibility to Hexagonal Architecture through concentric layers with inward-pointing dependencies. The domain core and application services contain all business logic with no references to infrastructure or UI, enabling the same core to support any number of presentation layers [27]. The presenter layer explicitly manages input/output for different interfaces—HTTP APIs, CLI tools, and desktop applications can all be attached to the same core [27]. This architecture naturally supports producing different binaries for different platforms by swapping outer layers while preserving the inner layers intact. The clear separation allows embedded deployments to use lightweight infrastructure adapters without affecting domain logic.

**Pros:**
- Multiple presenter types from single domain core
- Outer layers replaceable per deployment target
- Embedded and full-scale deployments from same core

**Cons:**
- Multiple layers add complexity for simple deployments
- Requires disciplined dependency direction enforcement

**Score: 10/10**

### Front Controller Pattern
The Front Controller pattern offers minimal deployment flexibility as it is inherently tied to HTTP request handling in web environments [34]. The pattern centralizes request routing through a single entry point, which is suitable for web applications but not transferable to desktop, mobile, or embedded environments. Deployment to different platforms requires complete reimplementation of the control layer, as the pattern assumes HTTP semantics. While the business logic may be extracted, the Front Controller itself does not contribute to multi-platform capability.

**Pros:**
- Centralized request handling simplifies web deployment
- Can be combined with other patterns for multi-platform support

**Cons:**
- Tied to HTTP/web environments
- No inherent support for non-web platforms
- Reimplementation required for each deployment target

**Score: 4/10**

### Backend-for-Frontend (BFF)
The BFF pattern enhances deployment flexibility by isolating frontend-specific concerns into dedicated backend services, enabling independent deployment of different frontend platforms. A mobile BFF, web BFF, and embedded BFF can evolve and deploy separately while sharing the same core domain services. This approach allows teams to optimize each BFF for its target platform's constraints—mobile APIs can be tuned for bandwidth, web APIs for caching, embedded for minimal payload sizes [29]. However, the pattern increases operational complexity with multiple services to maintain, and organizations may eventually outgrow the BFF layer as team size scales [29]. Deployment requires orchestration across multiple services.

**Pros:**
- Independent deployment per frontend platform
- Platform-specific optimization per BFF
- Core services unchanged across frontends

**Cons:**
- Multiple services increase deployment complexity
- Operational overhead scales with number of BFFs
- May lead to duplication across BFF implementations

**Score: 8/10**

### Model-View-Adapter (MVA)
MVA introduces an Adapter layer that translates between Model and View, providing moderate improvement over basic MVC for multi-platform deployment. The Adapter can be implemented per target platform while the Model remains shared, enabling some code reuse across environments. However, the View's direct coupling to the Adapter creates platform-specific dependencies that limit true separation. The pattern's lower adoption means fewer established patterns and tooling support for cross-platform deployment compared to MVVM. Embedded deployments may find the additional abstraction layer introduces unnecessary overhead.

**Pros:**
- Adapter can be platform-specific while Model is shared
- Cleaner separation than MVC for multi-platform targets

**Cons:**
- View-Adapter coupling limits flexibility
- Lower adoption reduces cross-platform tooling support
- Extra abstraction may be overhead for embedded deployments

**Score: 6/10**

### Microkernel Architecture
Microkernel architecture achieves high deployment flexibility through a minimal core system that can be deployed with varying sets of plugins for different environments. This architecture is proven in operating systems where the same kernel supports diverse hardware through device driver plugins (embedded Linux, L4, WinCE) [28] [33]. For applications, the core can be deployed to cloud, on-premise, or edge devices with plugin sets tailored to each environment's constraints and capabilities. Plugins can be dynamically loaded or statically compiled, supporting both resource-constrained embedded deployments and feature-rich desktop environments from the same codebase [10]. The primary deployment challenge is managing plugin dependencies and versioning across environments.

**Pros:**
- Same core deploys to cloud, edge, and embedded
- Plugin selection per deployment environment
- Dynamic or static plugin loading options

**Cons:**
- Plugin dependency management across deployments
- Version compatibility matrix complexity
- Runtime overhead from plugin communication

**Score: 10/10**






### Sources:
[25]: [https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
[26]: [https://martinfowler.com/eaaDev/uiArchs.html](https://martinfowler.com/eaaDev/uiArchs.html)
[27]: [https://github.com/ericjeker/nestjs-onion-architecture](https://github.com/ericjeker/nestjs-onion-architecture)
[28]: [https://developer.aliyun.com/article/1546694](https://developer.aliyun.com/article/1546694)
[29]: [https://wundergraph.com/blog/cosmo-casestudy-luxury-presence](https://wundergraph.com/blog/cosmo-casestudy-luxury-presence)
[30]: [https://assets.carolus.raywenderlich.com/books/kotlin-multiplatform-by-tutorials/v1.0/chapters/7-app-architecture](https://assets.carolus.raywenderlich.com/books/kotlin-multiplatform-by-tutorials/v1.0/chapters/7-app-architecture)
[31]: [https://martinfowler.com/articles/microservice-trade-offs.html](https://martinfowler.com/articles/microservice-trade-offs.html)
[32]: [https://link360.io/t/tabela-comparativa-com-trade-offs-de-arquiteturas/28852](https://link360.io/t/tabela-comparativa-com-trade-offs-de-arquiteturas/28852)
[33]: [https://blog.csdn.net/wangyi463295828/article/details/145726090](https://blog.csdn.net/wangyi463295828/article/details/145726090)
[34]: [https://mahocommerce.com/maho-for-devs/controller-dispatch/](https://mahocommerce.com/maho-for-devs/controller-dispatch/)




