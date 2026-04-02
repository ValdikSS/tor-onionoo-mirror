#!/usr/bin/env python3

'''
This script strips alleged_family, effective_family and indirect_family
relay options due to large file size of the original, which is too big
for GitHub.
'''

import json

j = json.load(open("details-full.json", "r"))

for r in j["relays"]:
    if r.get("alleged_family"):
        r["alleged_family"] = []
    if r.get("effective_family"):
        r["effective_family"] = []
    if r.get("indirect_family"):
        r["indirect_family"] = []

json.dump(j, open("details-full.json", "w"), indent=0)
