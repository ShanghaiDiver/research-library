# Mechanical quality-assurance checks — 27 October 2026

The research library contains 21 indexed company theses. The preliminary manual audit established that all 21 indexed report paths return HTML, reports have a closing HTML tag, and extracted report source links are HTTPS or site-relative. This does **not** verify that every remote link still works or that every financial statement and valuation is correct.

This change introduces a small, dependency-free Python validator, `scripts/validate_library.py`, and GitHub Actions pull-request workflow `.github/workflows/research-library-qa.yml`.

## Checks performed automatically

- Parse companies.json and verify it contains an array of entries, each with required identifiers and fields.
- Reject duplicate tickers/report filenames; check that each linked local HTML report exists and has a basic HTML document structure.
- Check permitted verdict labels, recognised currencies, positive numeric quote, and ISO format for dates.
- Require valuation fields to be **all null** (unrated) or **all numeric** (reference values), preventing misleading partial price-band calculation in the existing index UI.
- Parse local links and flag missing targets.
- Warn about unsecured HTTP source links, links that execute JavaScript, missing source links and Avoid ratings that still have active entry bands.
- Check the site's index, methodology and screening pages exist.

The checks deliberately **do not** impose valuation multiples, price targets, live quote updates or a Buy/Sell conclusion.

## Limitations and next steps

- Remote sources: URL syntax and HTTPS are checked; a complete **external live-link HTTP audit has not been executed**. Automated website HEAD requests are often blocked or redirected; introduce controlled checks with timeout/retry and a human exception review before treating them as reliable CI failures.
- Financial accuracy: the validator cannot know whether “+7%” or “£1.2bn” is correct. Verification against original annual/interim results and chart/model formulas remains editorial QA and should be tracked in a claim/source register.
- Dates: valid ISO dates are checked, but a `lastUpdated` timestamp remains a **report date**, not a `priceAsOf` or `valuationAsOf`. Introduce distinct fields as a separate schema migration.
- The initial static check has not itself been executed on GitHub Actions until this draft PR is opened and CI runs; its pass/fail result should be reviewed prior to merge. This is a *proposed* QA gate, not a claim of all checks already passing.

Review the output in the PR's Checks tab. A failing report-link or malformed-data check should block merging until corrected.
