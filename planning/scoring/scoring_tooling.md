## Tooling and Language Support

| Description | How well the architecture fits the chosen language, compiler, and development tools. |
|-|-|
| Sub-factors | IDE/framework support for pattern <br> Compiler/linker support for optimizations (dead code elimination, function sections) <br> Build automation support |
| Metrics | Number of tools/frameworks supporting the pattern <br> Complexity of build scripts |



### Model-View-Controller (MVC)
MVC enjoys excellent tooling support across both C++ and Python ecosystems. C++ frameworks such as Qt provide mature MVC implementations through model/view programming [58], while Python web frameworks like Django and Flask offer robust MVC patterns. The pattern imposes no special compiler or linker requirements beyond standard C++ and Python toolchains. Build automation using CMake or setuptools integrates seamlessly. The primary limitation is that MVC's observer pattern implementation for UI updates requires manual callback management in C++, lacking the declarative binding systems found in .NET-based MVC implementations.

**Pros:**
- Extensive framework support in Qt, Django, Flask
- No special compiler/linker requirements
- Straightforward build automation

**Cons:**
- Manual observer pattern implementation in C++
- Less declarative UI binding than .NET alternatives

**Score: 8/10**

### Model-View-Presenter (MVP)
MVP tooling support is moderate in C++ and Python contexts. The pattern relies on interface-based contracts, which map naturally to C++ abstract base classes and Python protocols. However, MVP lacks dedicated framework support comparable to MVC or MVVM in these languages. Implementation typically requires custom infrastructure for view interfaces and presenter orchestration. The pattern's testability advantages require mocking frameworks (Google Mock, pytest-mock), which are well-supported. Compiler optimizations are unaffected, as MVP adds no runtime indirection beyond standard virtual dispatch or Python method calls.

**Pros:**
- Interface-based design maps to C++ abstract classes
- Mocking frameworks well-supported
- No runtime overhead beyond standard dispatch

**Cons:**
- No dedicated frameworks in C++/Python
- Custom infrastructure required

**Score: 7/10**

### Model-View-ViewModel (MVVM)
MVVM presents significant tooling challenges in C++ and Python due to its reliance on data binding frameworks and observable patterns that are native to .NET environments. While Qt's QML and model-view framework provide some MVVM-like capabilities, the pattern's full implementation requires property notification systems and command infrastructure that lack standardized C++ implementations. Python's dynamic nature can partially compensate through property observers, but no mature MVVM frameworks exist for the Python ecosystem with ImGui integration. The pattern's heavy reliance on reflection and declarative UI markup makes it poorly suited for the user's C++/ImGui toolchain without substantial custom infrastructure development.

**Pros:**
- Qt provides partial MVVM-like capabilities
- Python properties can simulate observability

**Cons:**
- No mature C++ MVVM frameworks for ImGui
- Heavy reliance on .NET-specific data binding
- Custom infrastructure required for Python

**Score: 4/10**

### Hexagonal Architecture (Ports and Adapters)
Hexagonal Architecture enjoys excellent support across both C++ and Python ecosystems. Python frameworks like Sincpro provide dedicated hexagonal architecture infrastructure with dependency injection, DTO validation using Pydantic, and type-hinting support for IDE autocompletion [59]. C++ implementations benefit from the pattern's interface-based design mapping naturally to abstract base classes, with no special compiler requirements. The pattern's emphasis on dependency inversion aligns perfectly with CMake's modular library structure and Python's packaging systems. Build automation remains straightforward as the architecture adds no toolchain complexity beyond standard module organization.

**Pros:**
- Dedicated Python frameworks available [59]
- Interfaces map naturally to C++ and Python
- No special compiler/linker requirements

**Cons:**
- C++ lacks dedicated frameworks (manual implementation)
- Type introspection limited in C++

**Score: 9/10**

### Onion Architecture
Onion Architecture tooling support mirrors Hexagonal Architecture, with strong Python framework support and reasonable C++ implementation capabilities. The pattern's concentric layer structure maps to Python packages and C++ namespaces without requiring specialized tooling. Build automation can enforce layer dependencies using CMake's target_link_libraries restrictions or Python's import linting tools. However, the pattern's conceptual complexity makes IDE support for architecture enforcement limited, requiring manual discipline. The multiple abstraction layers remain transparent to compilers and linkers, imposing no performance penalties.

**Pros:**
- Maps naturally to Python packages
- CMake can enforce layer dependencies
- No special compiler requirements

**Cons:**
- IDE architecture enforcement limited
- Less dedicated framework support than Hexagonal

**Score: 7/10**

### Front Controller Pattern
Front Controller pattern tooling is primarily web-focused, with implementations in Python web frameworks (Flask, Django) and C++ web servers. For the user's desktop ImGui application context, the pattern offers limited relevance and tooling support. Implementation requires manual request routing and controller infrastructure. The pattern adds no compiler or linker complexities, as it represents application-level organization rather than low-level architecture. Build automation remains unaffected. The pattern's value is diminished in GUI applications where event loops rather than HTTP requests drive interactions.

**Pros:**
- Well-supported in Python web frameworks
- No compiler/linker complexity

**Cons:**
- Primarily web-focused tooling
- Limited relevance for ImGui desktop applications
- Custom implementation required

**Score: 6/10**

### Backend-for-Frontend (BFF)
BFF pattern tooling support is strong in Python through frameworks like Flask and FastAPI, which provide straightforward API endpoint implementation. For C++ desktop applications, BFF is typically implemented as a local service layer rather than distributed services. The pattern adds significant build automation complexity due to multiple service components requiring separate build configurations and deployment artifacts. Python implementations benefit from extensive HTTP client/server libraries. C++ implementations require HTTP library integration (cpprestsdk, Boost.Beast) and process management infrastructure. The pattern's distributed nature introduces build complexity that may outweigh benefits for single-executable desktop applications.

**Pros:**
- Python Flask/FastAPI provide excellent BFF support
- Mature HTTP libraries in both languages

**Cons:**
- Multiple services increase build complexity
- C++ implementation requires significant infrastructure
- Overhead for single-executable desktop apps

**Score: 7/10**

### Model-View-Adapter (MVA)
MVA lacks dedicated framework support in both C++ and Python ecosystems, as the pattern remains less widely adopted than MVC or MVVM. Implementation requires custom Adapter infrastructure with manual data transformation logic. The pattern's tooling profile is similar to MVP, with interface-based design mapping naturally to C++ abstract classes and Python protocols. However, the absence of established frameworks means developers must build supporting infrastructure from scratch. Build automation remains straightforward, and no special compiler requirements exist. The pattern's low adoption also limits available examples and community knowledge for troubleshooting.

**Pros:**
- Interface design maps to language abstractions
- No special compiler/linker requirements

**Cons:**
- No dedicated frameworks in C++/Python
- Custom infrastructure required
- Low adoption limits examples

**Score: 6/10**

### Microkernel Architecture
Microkernel architecture tooling in C++ focuses on inter-process communication (IPC) and shared library loading, with established libraries for message passing. Python's multiprocessing and socket libraries provide similar capabilities. The pattern's minimal core design enables aggressive dead code elimination for the kernel, while plugins remain independently buildable. C++ implementations require careful cross-platform handling of shared library loading, similar to plugin systems, with symbol visibility management [62]. Build automation for microkernel systems involves coordinating multiple build artifacts (core executable, plugin libraries) with careful installation path configuration. The pattern's complexity requires robust CMake or Makefile infrastructure for managing dependencies between components.

Modern compilers (GCC, Clang) and linkers provide strong support for the needed optimizations: LTO, dead‑code elimination, function sections, and conditional linking via preprocessor or build scripts. IDEs and build systems (CMake, Make) can handle multiple targets and plugin management.

**Pros:**
- Minimal core enables aggressive dead code elimination
- Compiler optimizations are fully usable with static linking.
- Build automation can generate desktop, CI/CD, and embedded variants from the same codebase.
- Languages with good module systems (e.g., C++, Rust) naturally support plugin interfaces.
- No mandatory framework – you design the plugin API to suit your needs.

**Cons:**
- No standard framework; you must implement the plugin infrastructure manually.
- Dynamic plugin loading may require platform‑specific code (e.g., dlopen on Linux, LoadLibrary on Windows).
- Conditional static linking demands careful management of build scripts and preprocessor symbols.

**Score: 8/10**






### Sources:
[57]: [https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
[58]: [https://martinfowler.com/eaaDev/uiArchs.html](https://martinfowler.com/eaaDev/uiArchs.html)
[59]: [https://pypi.org/project/sincpro-framework/](https://pypi.org/project/sincpro-framework/)
[60]: [https://github.com/elliotcmorris/OpenAssetIO/commit/ed773bb](https://github.com/elliotcmorris/OpenAssetIO/commit/ed773bb)
[61]: [https://github.com/samuelpanzera/turning-back](https://github.com/samuelpanzera/turning-back)
[62]: [https://github.com/elliotcmorris/OpenAssetIO/commit/aee3b3a](https://github.com/elliotcmorris/OpenAssetIO/commit/aee3b3a)





