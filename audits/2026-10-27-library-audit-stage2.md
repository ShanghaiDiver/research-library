# Research library quality audit — follow-up editorial and source control

**27 October 2026 | Stage 2, continuation of `audits/2026-10-27-library-audit.md`**

## Remit

Verify that all reports are accessible and the register, dates, currencies, statuses and surrounding commentary are intelligible. Correct **clear** contradictions. Preserve substantive reports and original valuations as historical work. Do **not** develop new investment models or confer new Buy/Avoid ratings to make the library cosmetically uniform.

## Checks completed

- **Coverage:** `companies.json` contains 21 unique securities; all 21 corresponding HTML files are accessible on the published `main` branch at the beginning of this audit stage.
- **Verdict coherence:** index contains 1 Buy (GOOGL), 19 Watch, 1 Avoid (FLNC). RELX and ADYEN earlier August Buy headers were explicitly labelled as historical in the prior audit.
- **Unrated values:** AMZN, ANTO, ADYEN, PZC and FLNC have null numerical fair values and entry/review bands in the current index. The index already supports missing values instead of calculating spurious price gaps.
- **Currency:** LSE securities predominantly store share quotations in GBp (`p`); the LSE Compass row is in USD following the April 2026 quotation currency change; IHG is also in USD, not GBp. NASDAQ/NYSE in USD; Amsterdam ADYEN in EUR. Currency handling was checked structurally against the index and the previous reports; this is **not** a market-by-market independent quote verification.
- **Current versus archived:** 15 reports retain prominent June or August headers ahead of newer October reassessments: RELX, AAPL, GOOGL, BRK.B, CPG, GAW, SPX, ADYEN, BA., ANTO, DGE, GLEN, IHG, LGEN and PG. Each now carries a clearly dated current index snapshot **above** its older masthead, explicitly warning that the older panel is archived material. This is a presentation correction, not a new valuation.
- **Neutral price-range nomenclature:** the homepage middle band column now says **Reference range**, not **Hold**. Together with the prior Entry/Review changes, this reduces the chance a price-zone crossing looks like an order.

## Company-by-company cross-reference

| Security | Verdict | Price currency | Report state / remaining issue |
|---|---|---|---|
| RELX | Watch | GBp | Date/context banner; archived Buy and valuation explicitly historical |
| MSFT | Watch | USD | October report; check next results and all accounting period tags in later source audit |
| AAPL | Watch | USD | Date/context banner; June hero historical |
| AMZN | Watch | USD | October report; value and thresholds correctly withheld; next earnings 29 Oct |
| GOOGL | Buy | USD | Date/context banner; August hero historical |
| BRK.B | Watch | USD | Date/context banner; June hero historical |
| CPG | Watch | USD | Date/context banner; **old June GBp header** explicitly contextualised; verify all archived p-to-USD figures if reusing them |
| GAW | Watch | GBp | Date/context banner; June hero historical |
| SPX | Watch | GBp | Date/context banner; August hero historical |
| ADYEN | Watch | EUR | Date/context banner; value quarantined; 26 Oct market close remains provisionally sourced |
| ZTF | Watch | GBp | New reconstructed report; original may later be recovered |
| BA. | Watch | GBp | Date/context banner; June hero historical |
| RR. | Watch | GBp | October report current |
| ANTO | Watch | GBp | Date/context banner; unsupported historical value withdrawn |
| DGE | Watch | GBp | Date/context banner; August hero historical |
| GLEN | Watch | GBp | Date/context banner; June hero historical |
| IHG | Watch | USD | Date/context banner; archived June USD quotation |
| LGEN | Watch | GBp | Date/context banner; June hero historical |
| PG | Watch | USD | Date/context banner; June hero historical |
| PZC | Watch | GBp | New reconstructed report; no numerical fair value |
| FLNC | Avoid | USD | New reconstructed report; no numerical fair value |

## Financial-source spot checks (not full certification)

- Amazon Q2 2026 official results: $200.6bn sales (+20%), $27.5bn operating profit (+43%), AWS growth +37%. [Amazon investor release](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx).
- Antofagasta Q3 2026 company report: 9M copper 436.9kt (−8.3%), pre-by-product-credit cost $2.81/lb (+19.6%). [Primary report](https://prod.antofagasta.co.uk/investors/news/2026/q3-2026-production-report/).
- Fluence's September FY26 reset: $2.4bn expected revenue and approximately $200m adjusted EBITDA loss. [Company statement](https://ir.fluenceenergy.com/news-releases/news-release-details/fluence-energy-announces-revised-guidance-fiscal-year-2026).

These source checks corroborate selected figures; **they do not validate every figure in all 21 reports or certify all links**.

## Further remediation, separate from new investment research

1. **One current summary standard:** eventually relocate old hero/valuation material into a dedicated historic appendix rather than relying on a warning above it. Preserve every prior thesis and source.
2. **Quote provenance:** add separately stored `priceAsOf`, quote source, listing currency, FX reference if a quote changed currency, and `valuationAsOf` / validation status. `lastUpdated` dates a report, not necessarily a quote.
3. **Source-to-claim register:** retain the precise company filing, financial period, statutory-versus-adjusted definition, consolidation basis, data units and links for key tables. Include a specific link checker and published assertions QA.
4. **Reviewer workflow:** distinguish deterministic QA (file references, available fields, date syntax, currency, basic math) from expert review (fair value, risk, verdict, client portfolio fit). Build scheduled update detection only after that separation is established.

**Conclusion:** This PR resolves the reproducible high-visibility presentation inconsistency across the 15 old-header reports. Financial line-by-line assurance and source-link verification remain separate audit work. No fair values or verdicts were changed.
