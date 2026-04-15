---
bibliography: code/refs.bib
---

**Pros:**

**Cons:**


[@team2023architec] [@stackoverflowblog2023keep] [@educativeionodatemvc] [@mehrotranodateundersta] [@chowdhurynodatepros]





**Pros:**
- **Superior memory efficiency and load times in simple applications**: Empirical research demonstrates that MVC, particularly when paired with Plain HTML/JS, achieves the fastest load times and the best memory efficiency among architectural patterns. This makes MVC an excellent choice for resource-constrained environments and simple applications where overhead must be minimized.
- **Faster initial page rendering through streamlined server-side processing**: Real-world benchmarks show that MVC setups often yield up to 15% faster initial page rendering compared to alternative patterns, due to a leaner pipeline and streamlined server-side processing. This advantage is especially pronounced in simpler CRUD applications, where MVC provides near-instant page loads even under heavy concurrent user loads.
- **Performance mitigation through mature caching strategies**: MVC frameworks leverage mature routing and caching mechanisms that effectively mitigate latency. Proper implementation enables caching at multiple levels-model data caching, partial view caching, and output caching-which can reduce server load and enhance throughput. In data-driven scenarios, judicious caching within MVC can improve performance by up to 50%.
- **Lightweight implementation in constrained environments**: The MVC pattern, when implemented without excessive framework bloat, can be highly lightweight. For instance, the Spring MVC framework can be deployed in a JAR file of only 1MB, and its processing overhead is considered negligible. This makes MVC suitable for embedded systems and environments with limited memory and storage capacity.

**Cons:**
- **Higher memory consumption compared to MVVM and MVP**: Comparative analysis of Android native application architectures reveals that both MVP and MVVM patterns demonstrate superior performance in terms of memory usage. Experiments confirm that MVC consumes more memory than its more modern counterparts, which can be a critical limitation in memory-constrained mobile and embedded systems.
- **Controller bottleneck leading to performance degradation**: In complex applications with numerous user interactions, the controller can become a performance bottleneck. When controllers become excessively large, they may cause performance degradation, increased memory usage, and slower response times. Additionally, Spring MVC exhibits blocking behavior from the server down to the dispatcher servlet, which limits its ability to handle high traffic efficiently.
- **Performance overhead from additional indirection**: The flexibility and separation of concerns that MVC provides come at a cost: the pattern introduces additional levels of indirection. This indirection can complicate the design and incur a performance penalty, as each layer adds processing overhead that may not be justified for simpler applications.
- **Verbose code and lack of native data binding**: MVC provides less support for data binding compared to patterns like MVVM, which can lead to verbose code and increased maintenance effort. While this is primarily a maintainability concern, verbose code can indirectly affect performance by increasing the application's footprint and potentially introducing inefficiencies in the rendering pipeline.

**Sources**:
- https://www.educative.io/answers/mvc-vs-mvp-vs-mvvm
- https://ieeexplore.ieee.org/document/10957712
- https://moldstud.com/articles/p-the-impact-of-mvc-and-mvvm-on-aspnet-application-performance-a-comprehensive-analysis
- https://aaltodoc.aalto.fi/items/510b5360-2bc0-4ee7-b635-ffdfe7ce2594/full
- https://browse.library.kiwix.org/content/stackoverflow.com_en_all_2023-11/questions/16542932/when-not-to-use-mvp-mvc

