#!/usr/bin/env python3
"""Mechanical checks for research-library data. No valuation opinions or remote URLs."""
import datetime as dt
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"ticker", "company", "exchange", "sector", "currency", "track",
            "verdict", "price", "fairValue", "buyBelow", "trimAbove",
            "lastUpdated", "file"}
CURRENCIES = {"p", "$", "€"}
VERDICTS = {"Buy", "Watch", "Avoid"}
errors, warnings = [], []

def issue(category, label, message):
    (errors if category == "error" else warnings).append(f"{label}: {message}")

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"a", "link", "script", "img"}:
            key = "href" if tag in {"a", "link"} else "src"
            if attrs.get(key):
                self.urls.append((tag, attrs[key]))

try:
    doc = json.loads((ROOT / "companies.json").read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as ex:
    sys.exit(f"ERROR: cannot parse companies.json: {ex}")
rows = doc.get("companies")
if not isinstance(rows, list):
    sys.exit("ERROR: companies must be an array")
if len(rows) != 21:
    issue("warning", "index", f"expected historical baseline of 21 securities, found {len(rows)}; update expected count if intentionally changed")
seen, filenames = set(), set()
for index, c in enumerate(rows, start=1):
    label = c.get("ticker", f"row #{index}")
    missing = REQUIRED - c.keys()
    if missing:
        issue("error", label, f"missing required keys: {sorted(missing)}")
        continue
    if label in seen:
        issue("error", label, "duplicate ticker")
    seen.add(label)
    if c["file"] in filenames:
        issue("error", label, f"duplicate report file {c['file']}")
    filenames.add(c["file"])
    if c["currency"] not in CURRENCIES:
        issue("error", label, f"unsupported currency {c['currency']!r}")
    if c["verdict"] not in VERDICTS:
        issue("error", label, f"unsupported verdict {c['verdict']!r}")
    try:
        dt.date.fromisoformat(c["lastUpdated"])
    except (TypeError, ValueError):
        issue("error", label, "lastUpdated must be ISO YYYY-MM-DD")
    if c.get("nextResults"):
        try:
            dt.date.fromisoformat(c["nextResults"])
        except (TypeError, ValueError):
            issue("error", label, "nextResults must be ISO YYYY-MM-DD")
    if not isinstance(c["price"], (float, int)) or isinstance(c["price"], bool) or c["price"] <= 0:
        issue("error", label, "price must be positive numeric")
    nums = [c[x] for x in ("fairValue", "buyBelow", "trimAbove")]
    if any(x is None for x in nums) and not all(x is None for x in nums):
        issue("error", label, "fairValue/buyBelow/trimAbove must all be null or all numeric")
    for key in ("fairValue", "buyBelow", "trimAbove"):
        val = c[key]
        if val is not None and (not isinstance(val, (float, int)) or isinstance(val, bool) or val <= 0):
            issue("error", label, f"{key} must be positive numeric or null")
    if c["verdict"] == "Avoid" and c["buyBelow"] is not None:
        issue("warning", label, "Avoid verdict has an entry threshold; verify this is intentionally historic")
    file_name = c["file"]
    if not isinstance(file_name, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+\.html", file_name):
        issue("error", label, f"invalid report filename: {file_name!r}")
        continue
    report = ROOT / file_name
    if not report.is_file():
        issue("error", label, f"missing report: {file_name}")
        continue
    html = report.read_text(encoding="utf-8")
    if "<html" not in html.lower() or "</html>" not in html.lower() or "<title" not in html.lower():
        issue("error", label, "report missing basic HTML document structure")
    parser = Links()
    parser.feed(html)
    if not parser.urls:
        issue("warning", label, "no linked sources or navigation found")
    sources = 0
    for tag, raw in parser.urls:
        url = raw.strip()
        if url.startswith(("https://", "http://")):
            if url.startswith("http://"):
                issue("warning", label, f"insecure external link: {url}")
            if "fonts.googleapis" not in url and "fonts.gstatic" not in url:
                sources += 1
            continue
        if url.startswith(("#", "mailto:", "tel:", "data:", "javascript:", "//")):
            if url.startswith("javascript:"):
                issue("warning", label, "javascript URI in link")
            continue
        path = unquote(urlsplit(url).path)
        if path and not (report.parent / path).is_file():
            issue("error", label, f"broken relative {tag} link: {url}")
    if not sources:
        issue("warning", label, "no external source link (may be intentional)")
for path in ("index.html", "methodology.html", "screening.html"):
    if not (ROOT / path).is_file():
        issue("error", "site", f"missing root navigation file: {path}")
try:
    dt.date.fromisoformat(doc.get("updated"))
except (TypeError, ValueError):
    issue("error", "index", "top-level updated must be ISO YYYY-MM-DD")
print(f"Checked {len(rows)} index entries; {len(errors)} errors, {len(warnings)} warnings.")
for m in errors:
    print("ERROR:", m)
for m in warnings:
    print("WARNING:", m)
sys.exit(1 if errors else 0)
