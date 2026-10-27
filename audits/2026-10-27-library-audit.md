# Research library — quality audit (stage 1)

Audit date: 27 October 2026. Scope: all 21 companies.json rows, their 21 linked HTML files, the index UI, and primary-source spot checks. **Structural/editorial audit complete; detailed financial/source certification not complete.**

## Critical findings

| Priority | Finding | Status |
|---|---|---|
| P0 | Index used Buy / Trim labelling for stored levels, despite investment agreement that these are valuation checkpoints, not automatic trading orders | Fixed in this PR: Entry / Review with explanatory text |
| P0 | RELX and Adyen old page mastheads said Buy while index and October assessment said Watch | Fixed in this PR: explicitly historic August Buy, current Watch |
| P1 | Older hero panels before October updates show historical price, value and/or contradictory context | Open: harmonise a current front-page summary across reports; archive old panels |
| P1 | Many October index numerical values are retained from June/August and have not been freshly underwritten | Open: add valuation status, model timestamp, methodology and confidence to index |
| P1 | Antofagasta 3,174p October quote against 1,965p August value is especially unsuitable as a live trading signal | Open: recalculate mid-cycle mine NAV |
| P1 | Adyen October €926 close was marked provisional due to inconsistent sources | Open: exchange-price verification, source and timestamp |
| P1 | ZTF, PZC and FLNC reports were reconstructed when linked original HTML files were missing | Clearly identified; reconcile if originals subsequently found |
| P1 | Amazon preliminary enterprise-value-per-share proxies were not reconciled to full equity bridge | Already handled: null fair value and entry/review levels |
| P2 | Price observations are dated snapshots, but homepage called them 'today’s price' | Copy improved in this PR; future quoteAsOf and source fields needed |
| P2 | Index colours and Hold label may still appear to prescribe action | Open: separate prices from qualitative verdicts |
| P2 | Full 21-company primary-statement reconciliation, live URL checks and model arithmetical checks not yet performed | Open: staged financial assurance |

## Coverage

All **21/21** index report paths returned HTML on GitHub main when checked. 
RELX Watch; MSFT Watch; AAPL Watch; AMZN Watch; GOOGL Buy; BRK.B Watch; CPG Watch; GAW Watch; SPX Watch; ADYEN Watch; ZTF Watch; BA. Watch; RR. Watch; ANTO Watch; DGE Watch; GLEN Watch; IHG Watch; LGEN Watch; PG Watch; PZC Watch; FLNC Avoid.

Archived headings and panels observed across RELX, AAPL, GOOGL, BRK.B, CPG, GAW, SPX, ADYEN, BA., ANTO, DGE, GLEN, IHG, LGEN and PG; these must be labelled as historical rather than treated as October spot values.

## Primary-source spot checks

- Amazon official Q2 report confirms sales $200.6bn (+20%), operating profit $27.5bn (+43%), AWS growth +37%. https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
- Antofagasta 15 October production report confirms 436.9kt copper output YTD (−8.3%) and $2.81/lb pre-credit cash costs (+19.6%). https://www.antofagasta.co.uk/investors/news/2026/q3-2026-production-report/
- Fluence 16 September release confirms FY26 revenue ~$2.4bn and adjusted EBITDA loss ~$200m. https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-announces-revised-guidance-fiscal-year-2026

These are representative verification checks, **not proof that every value across every report is accurate**.

## Remediation priorities

1. Adopt a typed data schema separating price observation date/source/currency, valuation vintage and method, verdict, evidence date, and review thresholds. Do not infer a Buy from price automatically.
2. Give each report one current masthead and dated current valuation block; retain original analysis in clearly archived sections below.
3. Re-underwrite the most assumption-sensitive cases: ANTO mid-cycle copper NAV; Adyen acquisition/capex-inclusive cash; Glencore normalised trading; RELX AI business moat; Amazon AWS owner earnings/lease bridge.
4. Run a full assertions register: every meaningful financial claim mapped to primary result page, period, accounting definition, currency/unit and reviewed formula. Independently verify quotations and URL status.
5. Once accuracy is established, add automated CI validations for report/index existence, allowed verdicts, valuation timestamp/status and non-null price metadata, followed by scheduled earnings monitoring under human approval. Live share-price charting is a separate later workstream.

**Publication note:** This first PR fixes verified consistency faults and preserves historical analysis. It does not certify all company valuations, links, accounts, or models.
