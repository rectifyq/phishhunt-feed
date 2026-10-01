#!/usr/bin/env python3
"""Refang PhishHunt feed rows. Use on an isolated host. You are responsible for what you do with live URLs."""
import csv, sys
def refang(s): return s.replace("[.]", ".").replace("[@]", "@").replace("hxxp", "http", 1)
r = csv.DictReader(sys.stdin); w = csv.DictWriter(sys.stdout, fieldnames=r.fieldnames); w.writeheader()
for row in r:
    row["url_defanged"] = refang(row["url_defanged"]); row["registrable_domain_defanged"] = refang(row["registrable_domain_defanged"]); w.writerow(row)
