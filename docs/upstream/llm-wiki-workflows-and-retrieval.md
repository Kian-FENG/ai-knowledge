# Knowledge workflows

## Ingest a source

1. Read the immutable source and search existing concepts/source summaries.
   Explain new takeaways, corroboration and contradictions to the user. Existing
   authorization to ingest is sufficient; do not invent an additional approval.
2. Scaffold a source summary (or paper) with `ingest.py draft --type source
   --slug example --domain agents`. Source templates are in `_templates/`.
3. Replace every scaffold marker. Write the synthesis in the wiki's voice;
   cite the raw path/URL and relevant page/section/version. Create or update
   concepts and entities; promote reusable methods to techniques and failure
   modes to patterns. Merge curated knowledge, preserving disagreements and sources.
4. For a transcript, conversation or blog, also write a synthesis under
   `research/<domain>/` when its substance warrants it. Keep a source summary
   for traceability. Avoid redundant summaries of already-covered supplements.
5. Add an inbound path-qualified link from a reachable existing page. Update
   `index.md`, append `log.md`, and mark the tracker entry if one exists.
6. Run `python3 scripts/ingest.py review PAGE --reviewer NAME`. This checks
   content completeness, reference resolution and schema, and records who reviewed plus a content fingerprint. Editing the page after
   review invalidates that fingerprint and requires another review.
7. Run `python3 scripts/ingest.py finalize PAGE [PAGE ...]`. This validates,
   builds all six indices in a temporary directory, checks navigation reachability,
   and publishes under a write lock. Generator errors block publication. File
   replacement failures roll back; an interrupted batch recovers at the next
   locked write. Readers do not acquire the lock, so concurrent readers can see
   a batch in progress. This is recovery, not an instantaneous multi-file snapshot.
8. Run relevant offline tests; use `bash tests/run.sh` before declaring the whole
   wiki healthy. Inspect the diff. Finalize does not make a Git commit.

When a source comes from the discovery queue, append
`--candidate CANONICAL_ID --state PATH_TO_SQLITE` to finalize. The default state
path is `.cache/source-watch/state.sqlite3`. Selected pages must belong to that
candidate's recorded drafts. The candidate becomes `ingested` only after every
recorded route is published. If queue reconciliation fails after file publication,
retry the same finalize command; it is idempotent and reports the partial outcome.
External routes may use an explicit `status: published` when their recorded
repository's page schema declares `status` rather than `lifecycle`. A missing
publication field remains pending, including legacy pages that default to visible
in their own repository; publish those pages explicitly before reconciliation.

`ingest.py commit PAGE` is a compatibility alias for finalize. Bare `commit`
validates and regenerates published indices; it does not publish drafts.

## Batch reads

Explore the source structure and track chapters/modules in `ingest-tracker.md`.
Group related submodules into one source page. For each chunk, read, synthesize,
update affected concepts and add source citations; mark supplements already covered
with a reason. Batch related activity into one log entry. Publish a coherent set
of reviewed pages together so their mutual references are resolvable.

## Verification and corrections

`reviewed_at` records publication review. `last_verified` records checking the
claim against evidence; neither `created` nor `updated` substitutes for it.
Before `ingest.py touch PAGE --verification-note DESCRIPTION`, record evidence:

```yaml
evidence_kind: reported
verification: unchecked
evidence:
  - source: source-example
    locator: 'Section 3, Table 2'
    version: 'v2 / sha256:...'
```

Read that source and confirm the claim and its scope, then touch the page with
its actual verification date. Independent replication must document the external
experiment and measured outcomes before setting `verification: replicated`.
Legacy backfill scripts only report missing data; they never manufacture review.

For conflicting evidence, state both claims and their dates/conditions before
resolving them. Update the existing concept page. Use `supersedes` for a replacement
page; deprecated pages are excluded from default search. Preserve raw versions and
record the correction in the activity log.

## Lint and weekly maintenance

Use `orphan_report.py` to inspect inbound links, navigation reachability, unresolved
references and ambiguous references separately. Review stale and unchecked worklists.
Look for contradictory claims and missing concepts/cross-references. Fix within
existing user authorization; otherwise report proposed content changes for review.

`weekly.sh` generates indices, a capability report, then runs offline tests.
Discovery stays in `refresh-sources.sh`; weekly maintenance does not fetch sources.
The optional pre-commit hook preserves the configured existing hook and its exit
code. Global or managed hook directories may require separate write permission;
no hook is installed merely by changing the installer in this repository.
# Retrieval schema and evidence

`data/schemas.yaml` defines required fields for the eight types: concept, source,
paper, entity, technique, pattern, note and comparison. `domain` contains 1–2
values from `tags/domains.yaml`; no domain receives a ranking bonus. IDs are unique
`<type>-<slug>`. Tags are advisory; aliases are folded by `tags/aliases.yaml`.
Chinese query phrases use `data/retrieval-aliases.yaml` plus character bigrams.

## Lifecycle

`draft → reviewed → published`; `deprecated` retains retired knowledge. Default
query, page, grep and generated indices include only published pages.
`--include-unpublished` opts into inspection. Templates never set verification dates.

`specializes` uses concept IDs. Reverse links are derived by readers and indices.
`sources`, `related`, `supersedes`, `applies_to` and body wikilinks use the shared
resolver: unique IDs, paths, titles, aliases and slugs. Ambiguous targets remain
unresolved; a broken explicit path does not fall back to a same-named file.

## Evidence and verification

These axes are independent, not a trust ladder:

| Field | Values | Meaning |
|---|---|---|
| evidence_kind | unknown, reported, derived, measured | How the claim originated |
| verification | unchecked, source-checked, replicated | What checking was performed |
| lifecycle | draft, reviewed, published, deprecated | Whether the page is ready for retrieval |

`confidence` remains a compatibility field. Existing labels were retained during
migration; all 680 pages were marked unchecked because metadata migration does not
verify their claims. Historical `last_verified` dates were preserved, not renewed.
A fresh date with unchecked evidence is not a verified claim.

Measured results (including legacy experimental confidence) require substantive
`## Evidence`. Checked/replicated claims also require `last_verified`,
`verification_note`, and `evidence: [{source, locator, version}]`. Sources must
resolve to another page, an existing raw snapshot or an HTTP(S) URL. These are
structural checks; reviewers must read the evidence and assess support. Link
existence alone does not demonstrate entailment or independent replication.

`--follow-sources` returns typed evidence references from frontmatter and body
Sources/Evidence sections, plus navigation references. It does not classify an
ordinary related link as evidence. Evidence may be absent or contradictory;
call that out rather than fill the gap from memory.

## Freshness and machine output

All readers/reports use today's date (or `--as-of` where supported), each page's
`last_verified`, and per-type thresholds in `data/refresh-cutoff.yaml`. Buckets
are fresh, stale, undated and invalid. Validation rejects malformed/future dates.
The historical cutoff date is never used as a default review date.

`query.py --json` returns success/empty/invalid-input. `get_page.py --json`
returns metadata, body and freshness, optionally typed references; missing or
unpublished pages return not-found. Empty `--paths-only` writes no lines.
