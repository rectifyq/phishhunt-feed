# Rectifyq PhishHunt — public feed

Defanged phishing indicators observed by the Malaysian PhishHunt community. Every URL is defanged (`hxxps://`, `[.]`);
`url_sha256` is the hash of the scheme-less canonical form so you can deduplicate without ever refanging.

Cases in corpus: **7** · regenerated 2026-10-06T18:00:23.000Z · TLP:CLEAR

| File | Content |
|---|---|
| `feeds/latest.csv` / `.json` | last 30 days |
| `feeds/all.csv` | full corpus |
| `feeds/by-month/YYYY-MM.csv` | monthly slices |
| `feeds/by-sector/<sector>.csv` | sector slices |
| `tools/refang.py` | refang locally, on your own responsibility |
| `SCHEMA.md` | column definitions |

MISP and STIX exports cannot be defanged and remain functional; they live on `feeds.rectifyq.com`.

## Featured analyses

_None yet._

## Editorial

A claim is a claim. Target organisations appear as stable colour+sector aliases ("Yellow Bank"). Free-form tags and attribution notes never appear here.
Corrections are published in place and dated. Contact: rectifyq.com.
