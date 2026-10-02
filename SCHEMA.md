# Feed schema

| Column | Meaning |
|---|---|
| case_id | PH-YYYY-NNNNN |
| url_defanged | canonical URL, defanged |
| url_sha256 | sha256(host[:port] + path + ?query) — scheme-less |
| registrable_domain_defanged | eTLD+1 |
| first_seen / last_seen | epoch seconds UTC |
| state | validated · enriched · reported · acknowledged · down |
| target_alias | colour + sector noun, stable, never recycled |
| target_sector | banking · ewallet · courier · gov · telco · crypto · marketplace · airline · insurer · other |
| vector | sms · whatsapp · telegram · email · ads · search · qr · other |
| kit_family | fixed `kit:` tag |
| registrar / asn / country | from uncontradicted enrichments |
| taken_down_at / hours_to_takedown | Pendeta-confirmed |
| tags_fixed | space-separated fixed-vocabulary tags |
| tlp | always tlp:clear here |
