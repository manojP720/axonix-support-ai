
# Axonix Support AI

An AI-powered customer support automation platform built using n8n and locally hosted LLMs.

## Overview

Axonix Support AI aims to automate customer support operations by understanding customer queries, providing relevant answers, and assisting with support workflows.

## Technology Stack

- **Workflow Automation:** n8n
- **Local AI Runtime:** Ollama
- **Language Model:** Llama 3.2 3B
- **Frontend:** React
- **Backend:** FastAPI
- **Database:** PostgreSQL

## Planned Features

1. AI Customer Chat
2. FAQ Knowledge Base
3. Conversation Memory
4. Order Tracking
5. Support Ticket Creation
6. Human Escalation
7. Admin Dashboard

## Architecture

Customer → React → n8n → AI Agent → Ollama

## Project Status

<text>🚧 Initial development — architecture and local AI integration setup.</text>

## Getting Started

Prerequisites:
- Node.js
- Python
- n8n
- Ollama

Pull the model:

```bash
ollama pull llama3.2:3b
```

Start Ollama:

```bash
ollama serve
```

## License

MIT

