# Auren ⇄ Atlas Warehouse: Cross-chat retrieval and deposit

This is the operational entry point for using Atlas Warehouse as **external, persistent
project knowledge** with the connected GitHub integration. It is not a neural
upgrade, a private memory store, or an always-running AI process.

## Begin a new project chat

Ask: **"Auren, load Atlas Warehouse and continue [project/topic]."**

Auren can use connected GitHub tooling in ChatGPT to:

1. Read the exact file: warehouse/INDEX.json in nobleknights015-maker/Atlas-Warehouse.
2. Search the record titles, summaries and tags to select relevant shelves.
3. Fetch the exact record paths from the index for full context, evidence and notes.
4. Inspect open work orders and verify actual live project code/tests before making
   status claims. Warehouse records may be older than current project activity.
5. Use AUREN_HANDOFF.md as a compact orientation map.

The private Atlas Warehouse Bridge plugin provides this procedure across relevant
ChatGPT conversations **when it is enabled and invoked by the product**. Plugin
creation alone does not activate the plugin; it must be enabled by the account
owner. ChatGPT does not guarantee automatic GitHub retrieval in every chat.
If that does not occur, explicitly say "Load Atlas Warehouse".

## Store something learned

Use the public project record intake route on the [Atlas operations issue
#2](https://github.com/nobleknights015-maker/Atlas-Warehouse/issues/2):

    /atlas receive pixel-art | Sprite evaluation checklist | Check all articulated legs at native pixel resolution before accepting an animation base | pixel-art,validation | Founder art review

Atlas's VI processes owner-authored commands, commits the JSON record and updates
the index. New records begin **unverified**. Verified records should cite actual
test or review evidence:

    /atlas review RECORD_ID | tested | exact reproduction steps and passing test

The owner's connected GitHub tools can also post commands to the operations
issue. For programmatic intake, commands are recorded in a durable cursor
checkpoint, so a burst of messages can be drained by a later runner if GitHub
cancels some pending jobs. Acknowledgment is given only when the workflow
commits and posts the result. This is not a guarantee against all outages.

The raw project records remain source-of-truth. Generated INDEX.json and
AUREN_HANDOFF.md are deterministic lookup aids, rebuilt after VI operations.

## Current knowledge shelves

- pixel-art: training methods, geometry review, gait quality, character anatomy
- asset-standards: sheet constraints and engine runtime integration
- engine: release gates and validation constraints
- workflow: source verification, revision discipline and handoff requirements

More project-safe information can be added deliberately. **Do not bulk-copy
private chats, financial/personal information, sensitive files, or client data
into this public repository.** The automated filters only catch obvious
secret patterns; human review remains necessary.

## What the integration does not yet do

- ChatGPT does not automatically sync *every* past and future message.
- Atlas VI does not train its own neural model, browse arbitrary websites,
  or execute Bearframe engine or art work merely because a task is assigned.
- Scheduled ChatGPT study output is not automatically ingested into GitHub
  unless the study session or an authorized workflow explicitly deposits it.
- The skills-only plugin does not create a new backend service or give
  ChatGPT new credentials. It uses the already-connected GitHub tools.

## Owner controls

All repository content, records, issue comments, and audit ledger are public.
Only the repository owner may issue Atlas VI commands through issue #2.
Other commenters are ignored by the job. A private storage tier would require
separate repository permissions and data-handling review.
