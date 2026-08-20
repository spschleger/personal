#!/usr/bin/env python3
"""Ryerson Index searches for the Johnstone family (Frederick Jason "Toby" line).
POSTs to https://ryersonindex.org/search.php. Long delays; backs off hard on 429."""
import requests, time, sys, os, re
from bs4 import BeautifulSoup

D = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
S = requests.Session()
S.headers.update({"User-Agent": UA, "Referer": "https://ryersonindex.org/search.php",
                  "Origin": "https://ryersonindex.org",
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                  "Accept-Language": "en-AU,en;q=0.9"})

QUERIES = [
    # (label, POST fields)
    ("gn-Mafalda-any-surname",      {"search_gn": "Mafalda"}),
    ("JOHNSTONE-Mafalda",           {"search_sn": "JOHNSTONE", "search_gn": "Mafalda", "search_sx": "1"}),
    ("JOHNSTONE-Jacqueline",        {"search_sn": "JOHNSTONE", "search_gn": "Jacqueline", "search_sx": "1"}),
    ("JOHNSTONE-Jacquiline",        {"search_sn": "JOHNSTONE", "search_gn": "Jacquiline", "search_sx": "1"}),
    ("JOHNSTONE-Yola",              {"search_sn": "JOHNSTONE", "search_gn": "Yola", "search_sx": "1"}),
    ("JOHNSTONE-Frederick",         {"search_sn": "JOHNSTONE", "search_gn": "Frederick", "search_sx": "1"}),
    ("JOHNSTONE-Rose",              {"search_sn": "JOHNSTONE", "search_gn": "Rose", "search_sx": "1"}),
    ("JOHNSTONE-Gilbert",           {"search_sn": "JOHNSTONE", "search_gn": "Gilbert", "search_sx": "1"}),
    ("JOHNSTONE-Desmond",           {"search_sn": "JOHNSTONE", "search_gn": "Desmond", "search_sx": "1"}),
    ("JOHNSTONE-Elsie",             {"search_sn": "JOHNSTONE", "search_gn": "Elsie", "search_sx": "1"}),
    ("JOHNSTONE-Elsie-Daisy-loc",   {"search_sn": "JOHNSTONE", "search_gn": "Daisy", "search_sx": "1"}),
    ("STREHLAU-any",                {"search_sn": "STREHLAU", "search_sx": "1"}),
    ("JOSEFSKI-any",                {"search_sn": "JOSEFSKI", "search_sx": "1"}),
    ("JOHNSTONE-Rockhampton-loc",   {"search_sn": "JOHNSTONE", "search_lo": "Rockhampton"}),
]

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for tr in soup.find_all("tr"):
        tds = [td.get_text(" ", strip=True) for td in tr.find_all(["td", "th"])]
        if len(tds) >= 4:
            rows.append(" | ".join(tds))
    txt = re.sub(r"\n\s*\n+", "\n", soup.get_text("\n")).strip()
    return rows, txt

def run(label, fields):
    fn = os.path.join(D, f"ryerson_{label}.txt")
    if os.path.exists(fn) and os.path.getsize(fn) > 200:
        print(f"SKIP (have) {label}", flush=True); return True
    delay = 0
    for attempt in range(5):
        if delay: 
            print(f"  backoff {delay}s", flush=True); time.sleep(delay)
        try:
            data = dict(fields); data["search"] = "Search Ryerson"
            r = S.post("https://ryersonindex.org/search.php", data=data, timeout=60)
        except Exception as e:
            print(f"  ERR {label}: {e}", flush=True); delay = 120; continue
        if r.status_code == 429:
            print(f"  429 on {label}", flush=True); delay = 300 * (attempt + 1); continue
        if r.status_code != 200:
            print(f"  HTTP {r.status_code} on {label}", flush=True); delay = 120; continue
        rows, txt = parse(r.text)
        with open(fn, "w") as f:
            f.write(f"# Ryerson Index search  https://ryersonindex.org/search.php (POST)\n")
            f.write(f"# query: {fields}\n# accessed: {time.strftime('%Y-%m-%d %H:%M %Z')}\n")
            f.write(f"# HTTP {r.status_code}, {len(r.text)} bytes\n\n")
            f.write("## table rows\n")
            for x in rows: f.write(x + "\n")
            f.write("\n## page text\n" + txt + "\n")
        print(f"OK {label}: {len(rows)} table rows, {len(r.text)}b", flush=True)
        for x in rows[:40]:
            print("    " + x[:200], flush=True)
        return True
    print(f"FAIL {label}", flush=True)
    return False

if __name__ == "__main__":
    for i, (label, fields) in enumerate(QUERIES):
        run(label, fields)
        if i < len(QUERIES) - 1:
            time.sleep(45)
