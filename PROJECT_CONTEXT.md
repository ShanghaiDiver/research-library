# Research Library — Project Context and Handover

**Updated:** 27 October 2026  
**Repository:** https://github.com/ShanghaiDiver/research-library  
**Published library:** https://shanghaidiver.github.io/research-library/  
**Purpose:** A durable starting point for future conversations, collaborators and research sessions. Read the live repository and audit trail before relying on these dated notes.

## 1. What we are building

A living, evidence-based investment research library for identifying, understanding and monitoring potential long-term holdings. It is **not** a trading system, an automatically executed portfolio, or a collection of permanently valid target prices.

The initial library has **21 indexed company reports**. The current company register is `companies.json`; the public-facing directory is `index.html`; individual investment theses are linked from the register. The repository and merged pull requests are the **record of what was actually published**; conversation recollections are useful context, not the authority for current facts.

## 2. Investment philosophy

- Seek outstanding businesses with enduring competitive advantages, high-quality management, sensible capital allocation, and the ability to compound **per-share owner cash flows** for many years.
- Do not confuse a high-quality business with an attractive purchase price, or a low share price with a margin of safety. An exceptional compounder can justify a premium, but the premium must be supported by realistic long-term returns.
- Focus on **what creates and retains the economic value**, including reinvestment, return on incremental capital, maintenance versus growth capex, working capital, cash taxes, debt, leases and dilution. Reported EPS, adjusted metrics and analyst targets are evidence, not substitutes for owner economics.
- Analyse both the strongest bull and bear cases; make the disconfirming evidence explicit. Compare opportunity cost against alternative holdings.
- Be open to **staged entries** when a great business sells off on a plausible but unproved threat: waiting for certainty may remove the discount. Stage sizing must still reflect downside and evidence.
- Apply special scrutiny to cyclical businesses: spot prices, peak margins and exceptional trading profits must not be treated as normalised perpetuities.
- Explicitly differentiate a **valuation-review threshold** from an automatic instruction to trim or sell. Concentration, position sizing and competing opportunities matter.
- Use UK English and direct, commercially grounded writing. Avoid generic promotional claims or false precision.

## 3. Three decision levels — do not conflate them

1. **Library research:** Understand franchise economics, moat, management, growth, risks, available financial evidence, historic valuations, and what would change the thesis. Verdicts (`Buy`, `Watch`, `Avoid`) are research classifications, not orders.
2. **Investment review (when a transaction becomes interesting):** Revisit current primary disclosures; challenge assumptions; rebuild a sufficiently detailed, auditable valuation if justified; test five-to-ten-year prospective per-share owner returns and downside. **Do not** build elaborate copper-price scenarios or company-wide DCFs just to complete a library quality audit.
3. **Portfolio decision:** Assess the user's actual holdings, weights, concentration, correlations, liquidity, tax/FX where relevant, and opportunity cost before buying, adding, holding or reducing. The portfolio-level sell/trim discipline has **not yet been finalised** and should not be invented from individual company price bands.

## 4. Evidence and editorial standards

- Prioritise **primary evidence**: company results, annual reports, trading updates, audited statements and appropriate exchange/regulatory filings. Date every claim and source; distinguish reported versus constant-currency, organic, adjusted and statutory figures.
- Separate **source-verified facts**, model assumptions, market consensus/sentiment, inference, and judgement. Never call an unverified share price 'live'.
- Cite source pages and reconcile units, periods and listing currency: notably **GBp versus GBP, USD and EUR**. The Compass (CPG) London index quotation and IHG quotation have been recorded in USD; do not assume every LSE-listed company is priced in pence. Check current exchange convention rather than carrying forward an old assumption.
- A model scenario, EV/share proxy, dated fair value or analyst price target is **not automatically an auditable current equity intrinsic value**. Where the bridge cannot be defended, use `null` for `fairValue`, `buyBelow` and `trimAbove` together and explain why in the report.
- Preserve substantive earlier research and valuation history, but label previous prices, verdicts and assumptions **historical**. Give readers a single clear current assessment. Do not silently 'improve' a model by forcing it toward market price.
- For every report update, inspect and reconcile `companies.json`; ensure dates, prices, verdicts, currencies and notes do not contradict the HTML. Do not present a stock quote or an old threshold as a trading instruction.
- Treat the first 21-company structural and editorial audit as **completed**, not the financial certification of every table, URL and model. Outstanding checks must be stated openly.

## 5. GitHub workflow and approval

- The normal working pattern is **one or two companies per batch**, or a tightly scoped library infrastructure/audit change.
- Fetch the **current `main` branch** and relevant prior reports before editing. Preserve original analysis where appropriate; do not replace historical research with an unexplained short appendix.
- Work on a **new branch**, make logically grouped commits, and open a **draft pull request** with the evidence, changed files, conclusions, qualifications and explicit outstanding work.
- **Never merge a PR or publish changes without the user's explicit approval.** The user generally merges/reviews in GitHub; verify PR status before saying a change is live.
- GitHub commits and merged PRs are the persistent evidence trail. PR descriptions and `audits/` notes document *why* decisions were made.
- When a report is referenced in the index but missing on GitHub, search for an existing original before rebuilding; if recovery fails, label any new report as **reconstructed**. Zotefoams (ZTF), PZ Cussons (PZC) and Fluence Energy (FLNC) were reconstructed because their earlier HTML sources were not located. The user may recover originals later.

## 6. Current position as of this document

- The 21-company review and initial structural/editorial/mechanical QA work has been merged through **PR #16**, including a preliminary Python validator (`scripts/validate_library.py`) and GitHub Actions workflow (`.github/workflows/research-library-qa.yml`). Check Actions status rather than assuming CI has successfully run merely because the PR merged.
- Two financial-valuation reference sets — Antofagasta and Adyen — have been **withdrawn** from the current numerical index until a trade-specific deeper investigation warrants a defensible re-underwriting. Similarly Amazon, PZ Cussons and Fluence Energy have no current numerical house fair value. Historical references remain in their reports.
- A number of older report mastheads/hero panels have been preserved as archived historical context; dated current-index banners were added in PR #15. A unified current-first page design remains a possible later presentation improvement, not an invitation to rewrite all investment theses.
- One company is currently classed Buy, nineteen Watch, one Avoid (as at 27 October 2026); always check `companies.json` because classifications and prices can change.
- **Amazon Q3 2026 results are expected 29 October 2026**, after the date of this handover. Treat that as a forthcoming monitoring event, not an already observed result.
- A reported position of **27 Amazon shares** and its cost basis appear in the previously drafted Amazon report; **do not assume this is a complete or up-to-date portfolio**. Ask for the current holdings when beginning the portfolio-stage work.

## 7. Agreed roadmap

1. **Research-library audit:** structure, consistency and presentation substantially done; continue proportional source/financial-assertion assurance without rebuilding investment models simply for the audit.
2. **Portfolio framework:** obtain current holdings; examine concentration, correlations, role of each security and opportunity cost.
3. **Investment decision rules:** agree staged entry, long-run return hurdles and evidence-led holding/add/reduction decisions; no automatic trim from stored price bands.
4. **Research automation:** monitor company announcements and financial reports; identify material changes and stale claims; produce proposed, cited refreshes with a **human approval gate**. Separate deterministic QA from analytical judgement.
5. **Live share-price history charts:** investigate Google's actual embeddable data/chart options, licensing and technical limits; add suitable time-series charts only after a reliable method is verified. Google Finance is a preference, not an assumption that a supported public API/embed exists.

## 8. Starting a new conversation

Use a handover such as:

> Continue work on my investment research library at `ShanghaiDiver/research-library`. First read `PROJECT_CONTEXT.md`, then check current `companies.json`, recent relevant merged/draft pull requests and audit documents. Respect the staged library → investment review → portfolio decision process. Preserve original reports, use primary sources for new claims, and never merge or publish without my approval. Tell me which roadmap item you are advancing.

**Caution:** This file is a snapshot of the agreed working approach. If it conflicts with later explicit instructions, current company filings, the live repository or newer audit notes, confirm and use the newer authoritative evidence.
