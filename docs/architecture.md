# Architecture

```mermaid
flowchart LR
    Input[Config Input] --> Parser[Format Parser]
    Parser --> Schema[JSONSchema Validator]
    Schema --> Serializer[Format Serializer]
    Serializer --> Output[Converted File]
```
