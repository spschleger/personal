# YesMandarin Social Content Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local multi-agent pipeline that researches Sydney trends daily and produces actionable TikTok + Instagram Reels content briefs for a Mandarin language school.

**Architecture:** Shell script orchestrator dispatches 4 trend scout agents in parallel via `claude -p`, merges their JSON results with a cultural calendar, pipes through a relevance filter agent, then a brief generator agent. Final output is a Markdown file with 5-7 actionable briefs.

**Tech Stack:** Bash (orchestrator), Claude CLI (`claude -p` with `--model haiku` for scouts/filter, `--model sonnet` for brief generation), JSON (intermediate data), Markdown (output)

**Spec:** `docs/superpowers/specs/2026-04-11-social-content-pipeline-design.md`

---

## File Structure

```
content-pipeline/
├── run.sh                          # Main orchestrator — dispatches agents, chains results
├── prompts/
│   ├── scouts/
│   │   ├── tiktok-scout.md         # TikTok trend research prompt
│   │   ├── google-trends-scout.md  # Google Trends Sydney prompt
│   │   ├── sydney-local-scout.md   # Sydney events/restaurants/news prompt
│   │   └── reddit-scout.md         # Reddit r/sydney buzz prompt
│   ├── filter.md                   # Relevance filter + ranking prompt
│   └── brief-generator.md         # Brief generator prompt (produces final output)
├── data/
│   └── cultural-calendar.json     # Static Chinese cultural calendar dates
├── output/                        # Daily output files (gitignored)
├── tmp/                           # Temporary scout results (gitignored)
└── .gitignore
```

---

### Task 1: Project Scaffolding

**Files:**
- Create: `content-pipeline/.gitignore`

- [ ] **Step 1: Create directory structure**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
mkdir -p content-pipeline/{prompts/scouts,data,output,tmp}
```

- [ ] **Step 2: Create .gitignore**

Create `content-pipeline/.gitignore`:

```
output/
tmp/
```

- [ ] **Step 3: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/.gitignore
git commit -m "scaffold: create content pipeline directory structure"
```

---

### Task 2: Chinese Cultural Calendar

**Files:**
- Create: `content-pipeline/data/cultural-calendar.json`

- [ ] **Step 1: Create the calendar data file**

Create `content-pipeline/data/cultural-calendar.json`:

```json
[
  {
    "name": "Lunar New Year / Spring Festival (春节 chūn jié)",
    "date_rule": "varies — Chinese lunisolar calendar, typically late Jan to mid Feb",
    "2026": "2026-02-17",
    "2027": "2027-02-06",
    "content_angle": "New Year greetings, family vocabulary, food names, red envelope culture, zodiac animals",
    "lead_days": 14
  },
  {
    "name": "Lantern Festival (元宵节 yuán xiāo jié)",
    "date_rule": "15th day of 1st lunar month — 15 days after Lunar New Year",
    "2026": "2026-03-04",
    "2027": "2027-02-20",
    "content_angle": "Lantern vocabulary, riddle traditions, tangyuan (glutinous rice balls), family reunion phrases",
    "lead_days": 7
  },
  {
    "name": "Qingming Festival (清明节 qīng míng jié)",
    "date_rule": "April 4 or 5 each year",
    "2026": "2026-04-05",
    "2027": "2027-04-05",
    "content_angle": "Ancestor respect vocabulary, spring outing phrases, cultural sensitivity around death/remembrance",
    "lead_days": 7
  },
  {
    "name": "Dragon Boat Festival (端午节 duān wǔ jié)",
    "date_rule": "5th day of 5th lunar month — typically June",
    "2026": "2026-05-31",
    "2027": "2027-06-19",
    "content_angle": "Zongzi (rice dumpling) vocabulary, dragon boat racing terms, Qu Yuan story phrases",
    "lead_days": 10
  },
  {
    "name": "Chinese Valentine's Day / Qixi (七夕 qī xī)",
    "date_rule": "7th day of 7th lunar month — typically August",
    "2026": "2026-08-19",
    "2027": "2027-08-08",
    "content_angle": "Romance vocabulary, love phrases, Cowherd and Weaver Girl legend, date night Mandarin",
    "lead_days": 7
  },
  {
    "name": "Mid-Autumn Festival (中秋节 zhōng qiū jié)",
    "date_rule": "15th day of 8th lunar month — typically September or October",
    "2026": "2026-10-04",
    "2027": "2027-09-23",
    "content_angle": "Mooncake vocabulary and ordering, moon-gazing phrases, family gathering expressions, Chang'e legend",
    "lead_days": 14
  },
  {
    "name": "Chinese National Day / Golden Week (国庆节 guó qìng jié)",
    "date_rule": "October 1 every year",
    "2026": "2026-10-01",
    "2027": "2027-10-01",
    "content_angle": "China travel vocabulary, national pride phrases, Golden Week travel expressions",
    "lead_days": 7
  },
  {
    "name": "Double Eleven / Singles' Day (双十一 shuāng shí yī)",
    "date_rule": "November 11 every year",
    "2026": "2026-11-11",
    "2027": "2027-11-11",
    "content_angle": "Shopping vocabulary, bargaining phrases, number culture (1/11/11), online shopping Mandarin",
    "lead_days": 7
  },
  {
    "name": "Winter Solstice (冬至 dōng zhì)",
    "date_rule": "December 21 or 22 each year",
    "2026": "2026-12-22",
    "2027": "2027-12-22",
    "content_angle": "Dumpling vocabulary (northern tradition), tangyuan (southern tradition), seasonal food phrases",
    "lead_days": 7
  },
  {
    "name": "Sydney Lunar Festival (Lunar Lanes / Chinatown events)",
    "date_rule": "Aligns with Lunar New Year — check City of Sydney events",
    "2026": "2026-02-14",
    "2027": "varies",
    "content_angle": "On-location at Sydney Chinatown, street food vocabulary, event-specific Mandarin, order in Mandarin challenge",
    "lead_days": 10
  },
  {
    "name": "Vivid Sydney",
    "date_rule": "Late May to mid June each year — check vividsydney.com",
    "2026": "2026-05-22",
    "2027": "varies",
    "content_angle": "Light/art vocabulary in Mandarin, describing what you see, Sydney landmark names in Chinese, on-location content at Circular Quay",
    "lead_days": 10
  }
]
```

- [ ] **Step 2: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/data/cultural-calendar.json
git commit -m "feat: add Chinese cultural calendar with Sydney events"
```

---

### Task 3: TikTok Scout Prompt

**Files:**
- Create: `content-pipeline/prompts/scouts/tiktok-scout.md`

- [ ] **Step 1: Write the TikTok scout prompt**

Create `content-pipeline/prompts/scouts/tiktok-scout.md`:

````markdown
# TikTok Trend Scout — Sydney / Australia

You are a TikTok trend research agent. Your job is to find what's currently trending on TikTok in Australia, with a focus on content that a Mandarin language teacher in Sydney could adapt.

## Your Task

Search the web for current TikTok trends in Australia. Focus on:

1. **Trending sounds/audio** — what audio clips are creators using right now?
2. **Trending formats** — what video structures are getting high engagement? (e.g. "get ready with me", "things that just make sense", POV formats, stitch/duet chains)
3. **Trending hashtags** — what hashtags are surging in Australia, especially in education, food, culture, lifestyle, comedy?
4. **Trending topics** — what subjects are Australian TikTok creators making content about this week?

## Where to Search

- TikTok Creative Center (search for trending information from this platform)
- Search for "trending TikTok Australia this week" and similar queries
- Search for "trending TikTok sounds today" and "trending TikTok formats 2026"
- Search for "TikTok trends Sydney" or "Australian TikTok trends"
- Look for creator roundup posts that list current trends

## What Makes a Good Find

- Trends that are RISING, not already fading
- Formats that can be adapted to teach Mandarin (almost anything can — a restaurant trend becomes "how to order in Mandarin", a meme format becomes a language joke)
- Sydney or Australia-specific trends are gold
- Trending audio that a language teacher could use

## Output Format

Return ONLY a JSON array. No other text before or after. Each item:

```json
[
  {
    "topic": "Name or description of the trend",
    "source": "tiktok",
    "velocity": "rising | peaking | fading",
    "locality": "sydney | australia | global",
    "raw_context": "Details: what the trend is, how creators are using it, why it's popular, any example creators or videos you found, specific audio names if applicable",
    "location": null,
    "trending_audio": "Name of trending sound if applicable, otherwise null"
  }
]
```

Return 5-8 trends. Prioritise rising trends over peaking ones. Do not include fading trends.
````

- [ ] **Step 2: Test the scout in isolation**

```bash
cd ~/Documents/Web\ Projects/YesMandarin/content-pipeline
claude -p "$(cat prompts/scouts/tiktok-scout.md)" --model haiku > tmp/test-tiktok.json
cat tmp/test-tiktok.json
```

Verify: output is a valid JSON array with the expected fields. Adjust prompt if the output includes preamble text or is malformed.

- [ ] **Step 3: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/prompts/scouts/tiktok-scout.md
git commit -m "feat: add TikTok trend scout prompt"
```

---

### Task 4: Google Trends Scout Prompt

**Files:**
- Create: `content-pipeline/prompts/scouts/google-trends-scout.md`

- [ ] **Step 1: Write the Google Trends scout prompt**

Create `content-pipeline/prompts/scouts/google-trends-scout.md`:

````markdown
# Google Trends Scout — Sydney

You are a Google Trends research agent. Your job is to find what people in Sydney, Australia are searching for right now — breakout topics and rising searches that a Mandarin language teacher could create content about.

## Your Task

Search the web for current Google Trends data focused on Sydney, Australia. Look for:

1. **Breakout search terms** — queries that have spiked recently in Sydney
2. **Rising searches** — queries with significant growth in the past 7 days
3. **Trending topics in relevant categories** — food, restaurants, travel, culture, education, entertainment
4. **Sydney-specific searches** — anything people in Sydney are specifically looking up right now

## Where to Search

- Search for "Google Trends Australia today" and "trending searches Sydney"
- Search for "what's trending in Sydney this week"
- Search for "trending topics Australia April 2026" (use current date)
- Search for breakout topics on Google Trends Australia
- Look for any trending food, restaurant, or cultural searches in Sydney

## What Makes a Good Find

- Searches with sharp recent growth (breakout or 100%+ increase)
- Topics that are Sydney-specific or Australia-specific
- Any topic that could be tied to a Mandarin lesson (very broad — a trending restaurant means "learn to order in Mandarin", a trending travel destination means "travel phrases", a trending news topic means "discuss this in Mandarin")
- Seasonal or event-driven searches

## Output Format

Return ONLY a JSON array. No other text before or after. Each item:

```json
[
  {
    "topic": "The trending search term or topic",
    "source": "google_trends",
    "velocity": "rising | peaking | fading",
    "locality": "sydney | australia | global",
    "raw_context": "Details: search volume trend, why it might be spiking, any related queries, what category it falls into",
    "location": null,
    "trending_audio": null
  }
]
```

Return 5-8 trends. Focus on rising and breakout terms. Skip anything that's clearly declining.
````

- [ ] **Step 2: Test the scout in isolation**

```bash
cd ~/Documents/Web\ Projects/YesMandarin/content-pipeline
claude -p "$(cat prompts/scouts/google-trends-scout.md)" --model haiku > tmp/test-google.json
cat tmp/test-google.json
```

Verify: output is valid JSON array with expected fields.

- [ ] **Step 3: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/prompts/scouts/google-trends-scout.md
git commit -m "feat: add Google Trends Sydney scout prompt"
```

---

### Task 5: Sydney Local Scout Prompt

**Files:**
- Create: `content-pipeline/prompts/scouts/sydney-local-scout.md`

- [ ] **Step 1: Write the Sydney local scout prompt**

Create `content-pipeline/prompts/scouts/sydney-local-scout.md`:

````markdown
# Sydney Local Scout — Events, Restaurants, News

You are a Sydney local events and culture research agent. Your job is to find what's happening in Sydney right now — trending restaurants, new openings, upcoming events, cultural moments, and viral locations that a Mandarin language teacher could visit and create content at.

## Your Task

Search the web for what's happening in Sydney right now. Focus on:

1. **Trending restaurants** — new openings, viral spots, restaurants getting social media buzz (especially Chinese, Asian, or any cuisine where Mandarin would be relevant for ordering)
2. **Events coming up** — festivals, markets, cultural events, food events, anything happening in the next 1-2 weeks in Sydney
3. **Viral Sydney locations** — spots that are getting social media attention right now
4. **Local news with cultural angle** — anything in Sydney news that touches on Chinese culture, language, food, trade, travel, immigration, or multiculturalism

## Where to Search

- Search Time Out Sydney for latest restaurant news and events
- Search Broadsheet Sydney for new openings and trending spots
- Search "Sydney events this week" and "Sydney events this weekend"
- Search "new restaurant Sydney 2026" and "best new restaurants Sydney"
- Search "Sydney food festival" or "Sydney cultural events"
- Search Sydney Morning Herald Good Food section
- Search "viral Sydney restaurant" or "trending Sydney spots"

## What Makes a Good Find

- A specific place Felicity could physically go to and film content
- New or buzzy enough that location-tagging it would catch algorithmic attention
- Chinese/Asian restaurants are ideal but any trending spot works (she teaches you how to describe anything in Mandarin)
- Events where on-location filming would feel natural
- Include the address when you can find it

## Output Format

Return ONLY a JSON array. No other text before or after. Each item:

```json
[
  {
    "topic": "Name of the restaurant, event, or location",
    "source": "sydney_local",
    "velocity": "rising | peaking | fading",
    "locality": "sydney",
    "raw_context": "Details: what it is, why it's trending, what kind of content could be filmed there, when the event is (if applicable), any social media buzz around it",
    "location": {
      "name": "Venue or location name",
      "address": "Street address, suburb, Sydney"
    },
    "trending_audio": null
  }
]
```

Return 5-8 items. Prioritise places/events that are genuinely buzzy right now over evergreen recommendations.
````

- [ ] **Step 2: Test the scout in isolation**

```bash
cd ~/Documents/Web\ Projects/YesMandarin/content-pipeline
claude -p "$(cat prompts/scouts/sydney-local-scout.md)" --model haiku > tmp/test-local.json
cat tmp/test-local.json
```

Verify: output is valid JSON array. Location fields should be populated for most items.

- [ ] **Step 3: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/prompts/scouts/sydney-local-scout.md
git commit -m "feat: add Sydney local events/restaurants scout prompt"
```

---

### Task 6: Reddit Scout Prompt

**Files:**
- Create: `content-pipeline/prompts/scouts/reddit-scout.md`

- [ ] **Step 1: Write the Reddit scout prompt**

Create `content-pipeline/prompts/scouts/reddit-scout.md`:

````markdown
# Reddit Scout — Sydney Social Buzz

You are a Reddit and social buzz research agent. Your job is to find what Sydneysiders are talking about right now — hot discussion topics, viral local conversations, and cultural moments from Reddit and social media that a Mandarin language teacher could create content about.

## Your Task

Search the web for current hot topics on Sydney-related Reddit communities and broader social buzz. Focus on:

1. **r/sydney hot posts** — what are the top discussions in r/sydney right now?
2. **r/australia trending topics** — national conversations that have a Sydney angle
3. **r/languagelearning** — any hot posts about Mandarin, Chinese, or language learning in general
4. **Sydney social buzz** — viral local stories, memes, or conversations happening on social media about Sydney

## Where to Search

- Search "reddit sydney hot posts this week"
- Search "site:reddit.com/r/sydney" for recent popular posts
- Search "site:reddit.com/r/australia" for trending discussions
- Search "reddit language learning mandarin" for recent posts
- Search "Sydney viral" or "Sydney trending" for broader social buzz
- Search "Sydney meme" or "things about Sydney" for culturally resonant content

## What Makes a Good Find

- Topics that Sydneysiders are actively discussing and have strong opinions about
- Cultural observations about Sydney life that could be tied to a Mandarin lesson
- Food/restaurant discussions (very common on r/sydney)
- Any discussions about Chinese culture, language, or the Chinese-Australian experience
- Relatable Sydney moments that could become "how to say X in Mandarin" content
- Avoid: political controversies, sensitive racial topics, anything that could backfire for a small business

## Output Format

Return ONLY a JSON array. No other text before or after. Each item:

```json
[
  {
    "topic": "The discussion topic or viral moment",
    "source": "reddit",
    "velocity": "rising | peaking | fading",
    "locality": "sydney | australia | global",
    "raw_context": "Details: what people are saying, why it's resonating, the sentiment (positive/negative/funny), specific threads or posts if found, how it could be adapted to Mandarin content",
    "location": null,
    "trending_audio": null
  }
]
```

Return 5-8 topics. Skip anything politically charged or that could be reputationally risky for a small business owner.
````

- [ ] **Step 2: Test the scout in isolation**

```bash
cd ~/Documents/Web\ Projects/YesMandarin/content-pipeline
claude -p "$(cat prompts/scouts/reddit-scout.md)" --model haiku > tmp/test-reddit.json
cat tmp/test-reddit.json
```

Verify: output is valid JSON array with expected fields.

- [ ] **Step 3: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/prompts/scouts/reddit-scout.md
git commit -m "feat: add Reddit/social buzz scout prompt"
```

---

### Task 7: Relevance Filter Prompt

**Files:**
- Create: `content-pipeline/prompts/filter.md`

- [ ] **Step 1: Write the relevance filter prompt**

Create `content-pipeline/prompts/filter.md`:

````markdown
# Relevance Filter — YesMandarin Content Pipeline

You are a content strategist for YesMandarin, a Mandarin language school in Sydney run by Felicity Cao. Your job is to take raw trend data from multiple sources and produce a ranked shortlist of the best content opportunities for today.

## Context

- **Business:** YesMandarin — in-person Mandarin classes in Sydney
- **Teacher:** Felicity Cao — sole teacher, records all videos herself
- **Audience:** (1) Local Sydney adults learning Mandarin (2) Australian-born Chinese (ABCs) reconnecting with heritage language
- **Platforms:** TikTok and Instagram Reels (separate content for each)
- **CTA:** Free trial class
- **Content style:** Felicity piggybacks on trending topics to teach Mandarin. She films at-home (talking head, topic-driven) and on-location (at trending restaurants, events, spots in Sydney)

## Your Task

You will receive a JSON array of trend objects from four research scouts (TikTok, Google Trends, Sydney local, Reddit). Your job:

1. **Deduplicate** — merge trends that are about the same topic from different sources. Cross-source trends (found by multiple scouts) should be ranked higher.

2. **Score and rank** each trend on:
   - **Trend velocity** (primary) — rising beats peaking. Drop anything fading.
   - **Sydney locality** (primary) — Sydney-specific > Australia-wide > global.
   - **Content type** — classify as "on-location" (a specific place to go) or "at-home" (a topic to discuss from home).
   - **Mandarin angle** (light check) — almost any topic can be adapted to teach Mandarin. Only filter out trends where the connection would feel completely forced or nonsensical.
   - **Content feasibility** — can this realistically be filmed as a 30-60 second vertical video?

3. **Select top 5-7 trends** ensuring a mix of on-location and at-home content types.

4. **Check cultural calendar** — if any cultural events from the CULTURAL_CALENDAR section below are approaching within the next 14 days, include them as additional trend items regardless of scouted data.

## Output Format

Return ONLY a JSON array. No other text before or after. Each item:

```json
[
  {
    "rank": 1,
    "topic": "Merged/cleaned topic name",
    "type": "on-location | at-home",
    "sources": ["tiktok", "google_trends"],
    "velocity": "rising | peaking",
    "locality": "sydney | australia | global",
    "rationale": "One sentence: why this is a good content opportunity today",
    "audience": "adults | abcs | both",
    "raw_context": "Merged context from all sources that found this trend",
    "location": {
      "name": "Venue name if on-location",
      "address": "Address if known"
    },
    "trending_audio": "Audio name if applicable",
    "cultural_event": false
  }
]
```

## CULTURAL_CALENDAR

{{CULTURAL_CALENDAR}}

## Trend Data

{{SCOUT_DATA}}
````

- [ ] **Step 2: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/prompts/filter.md
git commit -m "feat: add relevance filter prompt with cultural calendar injection"
```

---

### Task 8: Brief Generator Prompt

**Files:**
- Create: `content-pipeline/prompts/brief-generator.md`

- [ ] **Step 1: Write the brief generator prompt**

Create `content-pipeline/prompts/brief-generator.md`:

````markdown
# Content Brief Generator — YesMandarin

You are a social media content strategist specialising in short-form video for language education. You create actionable content briefs for Felicity Cao, a Mandarin teacher in Sydney who runs YesMandarin.

## Context

- **Who is Felicity:** Sole teacher at YesMandarin, a Mandarin language school in Sydney. She records all videos herself and is the face of the brand. She's warm, knowledgeable, and willing to go to trending locations around Sydney to film.
- **Audience segment 1 — Local adults:** Sydney professionals, travellers, hobbyists wanting conversational Mandarin. Motivated by practical skills (ordering food, travelling, impressing friends/colleagues).
- **Audience segment 2 — ABCs (Australian-born Chinese):** Reconnecting with heritage language. Often have passive understanding from parents/grandparents but want conversational fluency. Strong emotional/identity angle.
- **Goal:** Every video drives viewers to book a free trial class.
- **Platforms:** TikTok and Instagram Reels — each gets its own version of the brief.

## Engagement Frameworks

Select the best framework for each trend. You may combine frameworks.

### Hook-Value-CTA
Grab attention in 2 seconds → deliver value → close with CTA.
Best for: straightforward teaching content.

### Pattern Interrupt
Open with something unexpected or counterintuitive.
Examples: "Don't say nihao to a Chinese person", "This is NOT how you say thank you in Chinese"
Best for: myth-busting, common mistakes.

### Teach-in-Context
Film at a location and teach vocabulary naturally within that setting.
Examples: At a restaurant teaching ordering phrases, at a market teaching food names.
Best for: on-location content.

### Us vs Them / Myth-Busting
Contrast what Australians think vs reality.
Examples: "What Australians think this Chinese dish is called vs what it's actually called"
Best for: cultural content, food content.

### Identity Content
Specifically targets ABCs with emotionally resonant content about cultural identity.
Examples: "Things your Chinese parents say but you never understood", "Phrases you heard growing up but never knew the meaning of"
Best for: ABC audience, heritage reconnection.

## Your Task

You will receive a ranked JSON array of filtered trends. For each trend, produce a complete content brief with separate TikTok and Instagram Reels versions.

## Output Format

Output in Markdown. Use this exact structure for each brief:

---

For each trend, output:

```
## Brief N: [Trend Topic]

**Trend:** [What it is and why it's hot right now]
**Type:** 📍 On-location — [Venue, Address] OR 🏠 At-home
**Audience:** [Adults / ABCs / Both] — [specific angle for the target segment]
**Framework:** [Which engagement framework(s) to use]

### TikTok Version

**Hook (first 2 sec):** "[The exact opening line that stops the scroll]"

**Talking Points:**
1. [First point / Mandarin phrase to teach — include pinyin and meaning]
2. [Second point / phrase]
3. [Third point / phrase]

**Filming Notes:**
- Format: [talking head / on-location / green screen / stitch / duet]
- Duration: [target seconds]
- Location: [specific location if on-location, or "home studio"]
- Visual notes: [any specific visual suggestions — text overlays, props, etc.]

**Audio:** [Trending audio to use, or "original audio" if talking head]
**Hashtags:** [6-10 trend-heavy, discovery-focused hashtags]
**CTA:** "Want to learn more? Free trial class — link in bio 👆"

### Instagram Reels Version

**Hook:** "[Opening line — can be slightly adapted for Reels audience]"

**Key Differences from TikTok:**
- [Pacing adjustment]
- [Tone adjustment]
- [Any format difference — e.g. could also work as a carousel]

**Hashtags:** [6-10 niche + local, community-focused hashtags]
**CTA:** "Free trial class — DM me 'LEARN' or tap the link in bio"

---
```

## Important Guidelines

- **Hooks must be specific and punchy.** Not "Learn some Mandarin" but "Stop saying xiè xie wrong — here's how Chinese people actually say thank you"
- **Include actual Mandarin** in every brief — pinyin + characters + meaning. This is a language teaching account, every video teaches something.
- **Location briefs must be actionable** — specific venue name, address, what to film there.
- **Vary the frameworks** across briefs — don't use the same one for all 5-7.
- **ABC content should feel personal** — speak to the emotional experience of reconnecting with language and culture.
- **The CTA is always the same** — free trial class. Work it in naturally, don't make it jarring.

## Today's Date

{{TODAY}}

## Filtered Trends

{{FILTERED_TRENDS}}
````

- [ ] **Step 2: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/prompts/brief-generator.md
git commit -m "feat: add brief generator prompt with engagement frameworks"
```

---

### Task 9: Orchestrator Script

**Files:**
- Create: `content-pipeline/run.sh`

- [ ] **Step 1: Write the orchestrator script**

Create `content-pipeline/run.sh`:

```bash
#!/bin/bash
set -euo pipefail

# YesMandarin Content Pipeline — Orchestrator
# Dispatches trend scouts in parallel, filters results, generates briefs.

PIPELINE_DIR="$(cd "$(dirname "$0")" && pwd)"
TODAY=$(date +%Y-%m-%d)
TMP_DIR="$PIPELINE_DIR/tmp/$TODAY"
OUTPUT_DIR="$PIPELINE_DIR/output"
OUTPUT_FILE="$OUTPUT_DIR/$TODAY-content-briefs.md"

# Model selection — scouts and filter use haiku for speed, brief generator uses sonnet for quality
SCOUT_MODEL="haiku"
FILTER_MODEL="sonnet"
BRIEF_MODEL="sonnet"

echo "=== YesMandarin Content Pipeline ==="
echo "Date: $TODAY"
echo ""

# Create today's tmp directory
mkdir -p "$TMP_DIR"
mkdir -p "$OUTPUT_DIR"

# --- LAYER 1: Trend Scouts (parallel) ---
echo "🔍 Layer 1: Dispatching trend scouts in parallel..."

claude -p "$(cat "$PIPELINE_DIR/prompts/scouts/tiktok-scout.md")" \
  --model "$SCOUT_MODEL" > "$TMP_DIR/tiktok.json" 2>/dev/null &
PID_TIKTOK=$!

claude -p "$(cat "$PIPELINE_DIR/prompts/scouts/google-trends-scout.md")" \
  --model "$SCOUT_MODEL" > "$TMP_DIR/google-trends.json" 2>/dev/null &
PID_GOOGLE=$!

claude -p "$(cat "$PIPELINE_DIR/prompts/scouts/sydney-local-scout.md")" \
  --model "$SCOUT_MODEL" > "$TMP_DIR/sydney-local.json" 2>/dev/null &
PID_LOCAL=$!

claude -p "$(cat "$PIPELINE_DIR/prompts/scouts/reddit-scout.md")" \
  --model "$SCOUT_MODEL" > "$TMP_DIR/reddit.json" 2>/dev/null &
PID_REDDIT=$!

# Wait for all scouts
echo "  Waiting for scouts to complete..."
FAILED=0

wait $PID_TIKTOK || { echo "  ⚠️  TikTok scout failed"; FAILED=$((FAILED+1)); }
echo "  ✓ TikTok scout complete"

wait $PID_GOOGLE || { echo "  ⚠️  Google Trends scout failed"; FAILED=$((FAILED+1)); }
echo "  ✓ Google Trends scout complete"

wait $PID_LOCAL || { echo "  ⚠️  Sydney local scout failed"; FAILED=$((FAILED+1)); }
echo "  ✓ Sydney local scout complete"

wait $PID_REDDIT || { echo "  ⚠️  Reddit scout failed"; FAILED=$((FAILED+1)); }
echo "  ✓ Reddit scout complete"

if [ "$FAILED" -eq 4 ]; then
  echo "❌ All scouts failed. Aborting."
  exit 1
fi

echo ""

# --- Merge scout outputs ---
echo "📋 Merging scout results..."

# Combine all scout JSON arrays into one. Handle missing/empty files gracefully.
MERGED="["
FIRST=true
for f in "$TMP_DIR"/tiktok.json "$TMP_DIR"/google-trends.json "$TMP_DIR"/sydney-local.json "$TMP_DIR"/reddit.json; do
  if [ -f "$f" ] && [ -s "$f" ]; then
    # Extract the array contents (strip outer brackets) and append
    CONTENT=$(cat "$f" | sed 's/^[[:space:]]*\[//' | sed 's/\][[:space:]]*$//')
    if [ -n "$CONTENT" ]; then
      if [ "$FIRST" = true ]; then
        MERGED="$MERGED$CONTENT"
        FIRST=false
      else
        MERGED="$MERGED,$CONTENT"
      fi
    fi
  fi
done
MERGED="$MERGED]"

echo "$MERGED" > "$TMP_DIR/merged-scouts.json"
echo "  ✓ Merged $(echo "$MERGED" | grep -o '"topic"' | wc -l | tr -d ' ') trends from scouts"
echo ""

# --- Load cultural calendar ---
CULTURAL_CAL=$(cat "$PIPELINE_DIR/data/cultural-calendar.json")

# --- LAYER 2: Relevance Filter ---
echo "🎯 Layer 2: Running relevance filter..."

# Build the filter prompt with injected data
FILTER_PROMPT=$(cat "$PIPELINE_DIR/prompts/filter.md")
FILTER_PROMPT="${FILTER_PROMPT//\{\{CULTURAL_CALENDAR\}\}/$CULTURAL_CAL}"
FILTER_PROMPT="${FILTER_PROMPT//\{\{SCOUT_DATA\}\}/$MERGED}"

echo "$FILTER_PROMPT" | claude -p - --model "$FILTER_MODEL" > "$TMP_DIR/filtered.json" 2>/dev/null

echo "  ✓ Filter complete — $(cat "$TMP_DIR/filtered.json" | grep -o '"rank"' | wc -l | tr -d ' ') trends selected"
echo ""

# --- LAYER 3: Brief Generator ---
echo "✍️  Layer 3: Generating content briefs..."

FILTERED=$(cat "$TMP_DIR/filtered.json")

BRIEF_PROMPT=$(cat "$PIPELINE_DIR/prompts/brief-generator.md")
BRIEF_PROMPT="${BRIEF_PROMPT//\{\{TODAY\}\}/$TODAY}"
BRIEF_PROMPT="${BRIEF_PROMPT//\{\{FILTERED_TRENDS\}\}/$FILTERED}"

# Generate briefs and save directly to output
BRIEFS=$(echo "$BRIEF_PROMPT" | claude -p - --model "$BRIEF_MODEL" 2>/dev/null)

# Write output file with header
cat > "$OUTPUT_FILE" << HEADER
# YesMandarin Content Briefs — $TODAY

> Generated by the YesMandarin Content Pipeline
> Trends sourced from: TikTok, Google Trends (Sydney), Sydney local media, Reddit

---

HEADER

echo "$BRIEFS" >> "$OUTPUT_FILE"

echo "  ✓ Briefs generated"
echo ""
echo "=== Pipeline Complete ==="
echo "📄 Output: $OUTPUT_FILE"
echo ""
echo "Briefs ready for review!"
```

- [ ] **Step 2: Make the script executable**

```bash
chmod +x ~/Documents/Web\ Projects/YesMandarin/content-pipeline/run.sh
```

- [ ] **Step 3: Commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add content-pipeline/run.sh
git commit -m "feat: add orchestrator script — parallel scouts, filter, brief generation"
```

---

### Task 10: End-to-End Test Run

**Files:**
- No new files — this is a validation task

- [ ] **Step 1: Run the full pipeline**

```bash
cd ~/Documents/Web\ Projects/YesMandarin/content-pipeline
./run.sh
```

Watch for:
- All 4 scouts complete (some may warn but at least 1 must succeed)
- Merged JSON is valid
- Filter produces a ranked JSON array of 5-7 items
- Brief generator produces formatted Markdown briefs
- Output file is created at `output/YYYY-MM-DD-content-briefs.md`

- [ ] **Step 2: Review the output**

Open the output file and check:
- 5-7 briefs present
- Each brief has both TikTok and Reels versions
- Mix of on-location and at-home types
- Hooks are specific and punchy (not generic)
- Actual Mandarin phrases included (pinyin + meaning)
- CTAs present on every brief
- Hashtags are platform-appropriate

- [ ] **Step 3: Fix any issues**

If scout output includes preamble text before the JSON, add `--output-format json` flag or adjust the prompt to emphasise "Return ONLY a JSON array."

If the filter or brief generator is producing malformed output, adjust the respective prompt.

- [ ] **Step 4: Run a second time to verify consistency**

```bash
./run.sh
```

Check that a second run produces different content (not cached/repeated) and the output file for today is overwritten with fresh results.

- [ ] **Step 5: Final commit**

```bash
cd ~/Documents/Web\ Projects/YesMandarin
git add -A content-pipeline/
git commit -m "feat: YesMandarin content pipeline v1 — complete and tested"
```
