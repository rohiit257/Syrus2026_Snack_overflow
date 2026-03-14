# PS-03 Architecture

```text
User
  |
  v
Chat Interface (Chainlit / CLI)
  |
  v
Onboarding Engine
  |
  +--> Stage 1: Persona Detection
  |      - Extract role, experience level, tech stack
  |      - Ask follow-up questions when details are missing
  |
  +--> Stage 2: Checklist Manager
  |      - Build personalized onboarding path
  |      - Track progress, evidence, and next action
  |
  +--> Stage 3: RAG Retrieval
  |      - Retrieve grounded answers from markdown knowledge base
  |      - Return citations or fallback escalation contact
  |
  +--> Stage 4: Task Execution
  |      - Mock/local computer-use automation
  |      - Browser open-and-capture flows
  |
  +--> Stage 5: HR Notification
         - Generate HTML + JSON completion report
         - Include timestamp and confidence score

Knowledge Base: datset/*.md
Persistence: outputs/sessions/*.json
Reports: outputs/completion_reports/*
```
