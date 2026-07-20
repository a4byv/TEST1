flowchart TD
    A([Start]) --> B[/Input Temperature Celsius/]
    B --> C{Temperature >= 35?}
    C -->|Yes| D[Hot]
    C -->|No| E{Temperature >= 25?}
    E -->|Yes| F[Warm]
    E -->|No| G{Temperature >= 15?}
    G -->|Yes| H[Cool]
    G -->|No| I[Cold]
    D --> J([End])
    F --> J
    H --> J
    I --> J
