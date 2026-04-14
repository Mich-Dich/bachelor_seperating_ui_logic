## Front Controller Pattern

Separation measures how well the pattern isolates UI from business logic. The Front Controller pattern generally improves separation by funneling all requests through a single handler, which then delegates to dedicated actions or page controllers. This keeps cross‑cutting concerns (security, logging) out of the UI and business layers. However, the centralised nature can backfire: if the controller accumulates too many responsibilities, it becomes a “god object” that tightly couples logic that should remain separate. Moreover, support for multiple UI platforms is not explicitly discussed in the sources, so the pattern’s out‑of‑the‑box separation for different front‑ends is limited.

### Pros:

- **Decouples request handling from business logic** – The front controller delegates to separate command or action objects, so the UI (views) and business rules stay isolated. [2]
- **Centralises cross‑cutting concerns** – Authentication, authorisation, logging, and session management are handled in one place, preventing them from leaking into UI or model code. [3]
- **Improves testability** – Because the controller’s logic is independent of the final view, you can unit‑test routing and filters without a real web server or UI framework. [2]
- **Reduces code duplication across UI entry points** – Without a front controller, each page would repeat common checks; the pattern extracts these into a single module, strengthening separation of concerns. [3]

### Cons:

- **Risk of becoming a “god object”** – If the controller is not carefully designed, it can absorb too many responsibilities (routing, security, view selection, logging), creating tight coupling and blurring the boundary between UI and business logic. [1]
- **Scalability Issues**: A front controller is not easily scalable; it forces all requests through a single entry point, making it difficult to scale individual parts of an application independently. [5]
- **Increased Complexity and Maintenance Costs**: Implementing a Front Controller is more complex than using a Page Controller, often requiring a custom-built controller that increases maintenance costs and the time needed for developers to become familiar with the solution. This additional complexity is unnecessary for simple applications, where it adds overhead without a clear benefit. [4]
- **Performance Bottleneck**: Since all requests are channeled through the same controller, it can become a performance bottleneck. The single controller may perform a great deal of work, and its handlers can introduce bottlenecks, especially if they involve database or document queries. [5]

**Score: XX/10**

**Reasoning:**









## An Introduction to the Front Controller Pattern, Part 1
- [1]: https://www.sitepoint.com/front-controller-pattern-1
| Link | https://www.sitepoint.com/front-controller-pattern-1/ |
|-|-|
| Retrieved | 2026-04-13 |
| Quote for [scoring/separation/front_controller/pro/Risk of becoming a “god object] | "a front controller can end up with too many responsibilities" |

## An Introduction to the Front Controller Pattern, Part 2
- [2]: https://www.sitepoint.com/front-controller-pattern-2/
| Link | https://www.sitepoint.com/front-controller-pattern-2/ |
|-|-|
| Retrieved | 2026-04-13 |
| Quote for [scoring/separation/front_controller/pro/Decouples request handling from business logic] | "..., it improves modularity and separation of concerns by decoupling the handling of requests from their processing" |
| Quote for [scoring/separation/front_controller/pro/Improves testability] | "the whole request/response cycle will be independently handled by a couple of reusable classes, which naturally you’ll be able to tweak at will" |

## Web Presentation Patterns: Front Controller
- [3]: https://medium.com/@ac2021070020/patterns-of-enterprise-application-architecture-front-controller-4849bff8318a
| Link | https://medium.com/@ac2021070020/patterns-of-enterprise-application-architecture-front-controller-4849bff8318a |
|-|-|
| Retrieved | 2026-04-13 |
| Quote for [scoring/separation/front_controller/pro/Centralises cross‑cutting concerns] | "Ease of Implementing Cross-Cutting Concerns: Functions such as authentication, authorization, or error handling can be implemented in one place, ensuring consistency and reducing code duplication." |
| Quote for [scoring/separation/front_controller/pro/Reduces code duplication across UI entry points] | "Functions such as authentication, authorization, or error handling can be implemented in one place, ensuring consistency and reducing code duplication" |

## Front Controller
- [4]: https://learn.microsoft.com/sl-si/previous-versions/msp-n-p/ff648617(v=pandp.10)#liabilities
| Link | https://learn.microsoft.com/sl-si/previous-versions/msp-n-p/ff648617(v=pandp.10)#liabilities |
|-|-|
| Retrieved | 2026-04-13 |
| Quote for [scoring/separation/front_controller/pro/Increased Complexity and Maintenance Costs] | "Increased complexity. Front Controller is more complicated than Page Controller. It often involves replacing the built-in controller with a custom built Front Controller. Implementing this solution increases the maintenance costs and the time it takes for developers to orient themselves to the solution." |

## Front Controller Vs Page Controller in .Net
- [5]: https://challadotnetfaq.blogspot.com/2013_11_30_archive.html?m=1
| Link | https://challadotnetfaq.blogspot.com/2013_11_30_archive.html?m=1 |
|-|-|
| Retrieved | 2026-04-13 |
| Quote for [scoring/separation/front_controller/pro/Scalability Issues] | "The single front controller can end up being a bottleneck since it answers to all requests." |
| Quote for [scoring/separation/front_controller/pro/Performance Bottleneck] | "The single front controller can end up being a bottleneck since it answers to all requests." |
