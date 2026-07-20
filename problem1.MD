```mermaid
flowchart TD
    A([Start]) --> B[/Input Grade/]
    B --> C{Grade >= 90?}
    C -->|Yes| D[Excellent]
    C -->|No| E{Grade >= 85?}
    E -->|Yes| F[Very Good]
    E -->|No| G{Grade >= 80?}
    G -->|Yes| H[Good]
    G -->|No| I{Grade >= 75?}
    I -->|Yes| J[Passed]
    I -->|No| K[Failed]
    D --> L([End])
    F --> L
    H --> L
    J --> L
    K --> L
```
