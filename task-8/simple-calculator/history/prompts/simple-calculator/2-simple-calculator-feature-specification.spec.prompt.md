---
ID: 2
TITLE: Simple Calculator Feature Specification
STAGE: spec
DATE_ISO: 2025-12-02
SURFACE: agent
MODEL: claude-sonnet-4-5-20250929
FEATURE: simple-calculator
BRANCH: main
USER: user
COMMAND: /sp.specify
LABELS: ["specification", "feature-definition"]
LINKS:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
FILES_YAML: []
TESTS_YAML: []
---
### PROMPT TEXT
```
/sp.specify
Features Specification:
1. Ask user for first number
2. Ask user for operator (+, -, *, /)
3. Ask user for second number
4. Perform calculation
5. Display result
6. Loop until user enters 'exit'
7. Handle invalid input and division by zero properly

CLI Flow:
- "Enter first number:"
- "Enter operator:"
- "Enter second number:"
- "Result: ..."
```
### RESPONSE TEXT
Created PHR for the Simple Calculator feature specification.
