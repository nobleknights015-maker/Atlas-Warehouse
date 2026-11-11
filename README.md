# Atlas Warehouse

**Status:** early working prototype — no paid server required.

Atlas Warehouse repurposes the retired FreeFrame project into a persistent, version-controlled knowledge inventory for Bearframe Labs. Atlas's fictional role remains warehouse and production management. In software, the first implemented component is a local JSON record system with search, validation and Git history.

This is NOT a second neural network, independent AI personality runtime, live ChatGPT memory connector, or continuously running server. Those integrations would require additional work and should only be described as operational after testing.

## What works

- Add records with titles, categories, tags, sources, and evidence labels.
- Search existing records by keywords, inspect them by ID, and validate their format.
- Keep all records as human-readable JSON that can be committed to Git.
- Run Python unit tests and GitHub Actions validation without a paid hosted AI service.
- Keep the retired FreeFrame app source and its license/third-party notices for preservation.

## Warehouse commands

Requires Python 3.11+; no third-party packages.

    python warehouse/atlas_warehouse.py put --kind pixel-art --title "Sprite anatomy checks" --summary "Check limbs, silhouette, and native-scale readability." --tags "sprite,quality" --source "documented visual review" --confidence reviewed

    python warehouse/atlas_warehouse.py search "sprite"
    python warehouse/atlas_warehouse.py validate
    python -m unittest discover -s warehouse/tests -v

Adding a record writes a local JSON file. To preserve it across machines and chats, an authorized tool or operator must commit and push it to GitHub. ChatGPT can consult a repository through the GitHub connector where available, but retrieval is not yet automatic at the beginning of every conversation.

Confidence labels:
- unverified: collected or proposed, without validation
- tested: repeatable verification demonstrated
- reviewed: manually reviewed

## Initial inventory

- warehouse/atlas_warehouse.py — inventory command-line tool
- warehouse/records/ — public, non-sensitive records
- warehouse/SCHEMA.md — record contract and privacy requirements
- warehouse/tests/ — automated tests

## Data protection

**This GitHub repository is public.** Never store sensitive personal memories, private conversation transcripts, client secrets, credentials, or API keys here. Use private storage with access controls for sensitive information. A public Git commit can remain in history even if the file is subsequently removed.

## Retired FreeFrame

FreeFrame Mobile is discontinued as an active product. Its source remains present for historical preservation and possible lawful code reuse, not as part of a working Atlas Warehouse deployment. The original project README was preserved at legacy/README-FreeFrame.md. Existing LICENSE, NOTICE and THIRD_PARTY_NOTICES.md remain applicable to the original components.

**GitHub repository name:** at this transition stage the URL still uses Freeframe-mobile. Renaming the repository itself to atlas-warehouse is a separate GitHub Settings action.
