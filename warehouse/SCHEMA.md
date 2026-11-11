# Atlas Warehouse record format

Atlas Warehouse is a **version-controlled inventory of verified, reusable knowledge**, not an autonomous AI model.

A record is one UTF-8 JSON document under warehouse/records/<kind>/<id>.json.

Required fields:
- id: stable, deterministic lowercase slug; generated from kind + title
- kind: collection name, e.g. pixel-art, engine, workflow
- title: short identifying title
- summary: concrete lesson, procedure, or decision
- tags: keyword array
- source: where the information came from (test, review, documentation)
- confidence: unverified, tested, or reviewed
- visibility: always public in this repository
- created_at, updated_at: UTC timestamps

Tested means a repeatable test was run; reviewed means a human checked it. Those labels are not proof that any model has learned or improved. A new record is not marked tested without evidence.

## Safety and privacy

The repository is PUBLIC. Do not commit private chats, passwords, personal details, API keys, tokens, proprietary client data or private memories. Git history retains prior versions even after removal. For sensitive memories, use private storage with explicit access controls, and keep it separate from this public repository.

The CLI has no semantic retrieval, remote automation, or connection to ChatGPT by itself. Git commit/push and retrieval through an authorized connector are separate operations.
