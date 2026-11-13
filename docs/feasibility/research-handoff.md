# Research handoff — F-04

Audit date: 13 November 2026 (Asia/Tehran). Status: **in progress; ownership and source recovery remain open**.

The implementation repository starts clean. The research package remains separately at `halle_docs/halle/` in the owner's Downloads folder. Paths below are relative to that research root, not files copied into this repository. This audit inspected file metadata, documentation, source configuration structure, and record counts. It did not execute research scripts, open the session database, authenticate to accounts, download content, or change the research package.

## Private material and account behavior

| Location | Observed issue | Handoff rule |
|---|---|---|
| `tools/halle_corpus/halle.session` | Telethon session file is present. Its validity and account identity were not inspected. | Keep private and outside source control; do not copy it into the implementation repository or use it for bot authentication. |
| `tools/harvest_inventory.py:47–49` | `TG_API_ID`, `TG_API_HASH`, and `TG_PHONE` have nonempty built-in defaults. Values are deliberately omitted here. | Do not import this script unchanged. Any future authorized offline reuse must remove personal defaults and require explicit local configuration. |
| `tools/harvest_inventory.py` | Can authenticate as a personal Telegram account, read messages, download media, and forward to a mirror. | Treat execution as a separate account action; do not run it as part of application setup or CI. |
| `tools/peek_saved.py`, `tools/peek_caption.py` | Instantiate a Telegram client and read account messages using the research setup. | Keep outside production and automated checks. |
| `tools/halle_corpus/inventory*.csv` | Contains source-chat/message references, filenames and dates; current and new inventories also contain captions. | Keep the raw inventories private pending ownership, permissions, and data review. Publish aggregate counts only. |
| `tools/venv/`, `__pycache__/` | Copied environment and generated caches are present. | Do not import or commit; recreate dependencies for any separately approved offline tooling. |
| `tools/halle_experiments/README.md` | Describes another project's server, Docker network, proxy and tunnel setup. | Do not run these commands, reuse that infrastructure, or assume network reachability establishes provider eligibility. |

No account identifiers or credential values have been reproduced. Nothing was deleted, rotated, or submitted externally. The presence of defaults/session files does not establish that they are active, exposed publicly, or owned by the current operator. Their owner must decide any subsequent handling.

## Available assets

The package contains **115 files** excluding virtual environments, Python caches and Git internals: 33 HTML, 19 Python, 41 JSONL, 5 CSV, 3 JSON, 3 Markdown, 8 PNG, 1 TXT, 1 session file and 1 extensionless file. Counts describe this local snapshot, not verified production content.

| Asset | Observed count | What it establishes |
|---|---:|---|
| `tools/halle_corpus/inventory.csv` | 11,525 CSV data rows | Discovery metadata; not downloaded or permitted questions. |
| `tools/halle_corpus/inventory.bak.csv` | 11,525 data rows | Older inventory variant; caption column absent. |
| `tools/halle_corpus/inventory_new.csv` | 15,494 data rows | Different inventory variant; authoritative version and overlap are unresolved. |
| `tools/halle_experiments/golden_set*.jsonl` | 7 files, 46 records total | Small research fixtures, potentially overlapping; not 46 distinct, reviewed question families. |
| Experiment result JSONL files | 13 files, 120 records total | Historical runs; no new experiment was executed and no quality claim was inferred. |
| `tools/halle_experiments/book_brains/` | 13 JSONL files, 163 records | Derived text/brain variants, not original source PDFs or permission records. |
| `tools/halle_experiments/book_brains_v2/` | 1 JSONL file, 1 record | Additional experimental extraction. |
| `tools/halle_experiments/book_embeddings/` | 6 JSONL files, 1,054 records | Existing vectors; model/version/source compatibility must be verified before any reuse. |
| `tools/halle_experiments/corpus.zist12.jsonl` | 6 records | Experimental corpus, not a reviewed curriculum registry. |
| `tools/halle_experiments/imgs_q/` | 8 PNGs | Research question images; provenance, permissions and real phone-photo coverage still need review. |
| Source PDFs | **0** | No textbook or question-paper PDFs were found anywhere in the package. |

Record totals are nonempty JSONL lines or CSV rows excluding headers. They are not deduplicated content counts. The old research README describes some material as safe to ship; this audit does not adopt that assertion as permission evidence.

## Missing sources and portability problems

1. `tools/halle_experiments/build_embeddings.py:20–25` references six PDFs using absolute paths from another machine: `C110216.pdf`, `C111216.pdf`, `C112216.pdf`, `C110210.pdf`, `C111210.pdf`, and `C112210.pdf`. None exists at its referenced path or in this package. Recover the selected official edition with its provenance and hash before ingestion; filenames alone do not prove edition or authenticity.
2. `tools/halle_experiments/build_v5_and_test.py:13` references another missing PDF, `@Frmol20.pdf`, at an absolute machine-specific path. Its source, ownership and permitted use are unconfirmed.
3. `golden_set.example.jsonl` has six image references; all six are missing relative to the experiments directory and its `imgs/` directory. The eight PNGs in `imgs_q/` do not by themselves repair these references.
4. `tools/halle_corpus/files/` exists, but no source PDF files were found. Inventory rows must not be treated as proof that a corresponding file is available.
5. The research implementation plan's final evidence links point to a different absolute Downloads layout. Repository documentation should use relative links for copied, reviewed documents and describe external research paths separately.
6. The experiment README contains `/opt/` and `/tmp/` deployment assumptions and references another project's network. Future offline tools need explicit input/output paths and their own reproducible environment.

## Import and ownership decisions

Keep original research in place. Copy only selected, reviewed documentation into the implementation repository. Keep raw content, account sessions, credentials, inventories, generated results, embeddings and environments outside Git by default. If a later task needs a fixture, create a minimal sanitized fixture with recorded provenance and permission rather than copying the research directory wholesale.

The owner still needs to confirm:

- Who owns and may use the personal Telegram account/session and the research source code.
- Which inventory is authoritative, and whether the listed source files can be recovered legitimately.
- The chosen textbook chapter/edition and permitted question/answer sources, with evidence of allowed uses.
- Who owns the implementation repository and future platform, provider, hosting and merchant accounts.
- Whether any research material was previously published; no remote repository or account audit was performed here.

**Completion condition:** F-04 can close after the clean repository's exclusions are verified, the owner records ownership/handling decisions, and this missing-source inventory is accepted. Source recovery and content permission review continue through F-05/K-01. This audit alone does not complete F-04.
