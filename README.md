# Atlas Warehouse

**Atlas VI is running on GitHub Actions — no dedicated paid server required.**

The retired FreeFrame repository has become Bearframe Labs' Atlas Warehouse: a public,
version-controlled project-knowledge inventory, work-order system, audit trail and
deterministic Virtual Intelligence (VI) operated by Atlas.

Atlas has his canonical practical, dryly funny Warehouse Director personality in a
dedicated configuration. He is Auren's younger brother in the Bearframe team dynamic;
he works with Vera on quality and with Sentinel's independent Watchtower department
when appropriate. He responds in his own consistent voice. **He does not have a
separately hosted language model, neural sentience, or open-ended conversational
reasoning.**

## Talk to Atlas

Open **[Atlas's Operations Console](https://github.com/nobleknights015-maker/Atlas-Warehouse/issues/2)**
and comment:

    /atlas status

Atlas's GitHub worker will reply in the same issue. The repository owner can use
other commands to add records, assign tasks, validate evidence and produce handoffs.
The worker commits inventory changes to GitHub before replying. Other people's
issue comments cannot trigger the VI.

[**All commands, operations, and examples →**](warehouse/ATLAS_VI.md)

## Department capabilities

- **Knowledge inventory:** receive, classify, search, inspect, review, and archive.
- **Persistent memory:** source-backed public project knowledge and version history.
- **Work orders:** assign owners/priorities, start, block, complete and reopen tasks.
- **Quality control:** review labels and evidence; inspections flag invalid,
  duplicate, unverified or stale stock.
- **Daily inspections:** a scheduled GitHub Actions job checks the warehouse.
- **Audit ledger:** actor- and time-stamped mutation records.
- **Auren handoffs:** compact source-aware briefings retrieved on demand.
- **Personality:** rules, phrasing and relationships live in atlas_persona.json.

The worker uses Python 3.11 standard-library code and GitHub's existing runners.
No permanent server, paid API or model weights are required for this VI. GitHub
Actions worker queues, usage policies and capacity limits still apply.

## Run locally

    python warehouse/atlas_vi.py "hello"
    python warehouse/atlas_vi.py "status"
    python warehouse/atlas_vi.py "handoff pixel-art"
    python -m unittest discover -s warehouse/tests -v
    python warehouse/atlas_warehouse.py validate

Key files:

- [VI department engine](warehouse/atlas_vi.py)
- [Atlas's canonical personality](warehouse/atlas_persona.json)
- [GitHub command bridge](warehouse/github_runner.py)
- [VI command reference](warehouse/ATLAS_VI.md)
- [Warehouse record specification](warehouse/SCHEMA.md)
- [Unit tests](warehouse/tests)

## Security and honest limitations

**This repository and its issue comments are PUBLIC.** Never place passwords,
API keys, private chat transcripts, personal secrets, client data or private
memories here. Historical Git revisions and issue comments can remain accessible.

Atlas's VI runs defined operations; it does not perform arbitrary autonomous
work outside these operations or retrain a language model. Storing knowledge
here does not automatically load it into ChatGPT in every chat; Auren must
retrieve relevant records through the linked GitHub tools. Work orders track
assignments; they do not silently complete outside work.

## Retired FreeFrame source

FreeFrame is discontinued as an active product. Its source remains for archival
purposes. The [original README](legacy/README-FreeFrame.md) and the original
LICENSE, NOTICE and THIRD_PARTY_NOTICES.md are preserved. Any third-party
components remain subject to their original licensing terms.
