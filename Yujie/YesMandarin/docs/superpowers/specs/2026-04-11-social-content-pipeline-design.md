# YesMandarin Social Content Pipeline — Design Spec

## Overview

An automated multi-agent pipeline that researches trending topics in Sydney, identifies opportunities relevant to Mandarin language learning, and produces actionable daily content briefs for Instagram Reels and TikTok. Felicity (the sole teacher and business owner) records all videos herself — the system is the strategy engine behind her.

## Goals

- Generate 5-7 content briefs per day, giving Felicity a menu to pick from
- Each brief has separate TikTok and Instagram Reels versions
- Briefs are action-oriented shot lists, not abstract ideas
- Mix of at-home (topic-driven) and on-location (place-driven) briefs
- Every brief ends with CTA: free trial class
- Run locally via CLI, manually triggered

## Target Audience

Two segments, both in Sydney:

1. **Local adults** — professionals, travellers, and hobbyists wanting to learn conversational Mandarin
2. **Australian-born Chinese (ABCs)** — reconnecting with heritage language, likely have some passive understanding, strong emotional/cultural identity angle

## Architecture

Three layers running in sequence, with parallelism within the first layer:

```
┌─────────────────────────────────────────────────┐
│              ORCHESTRATOR                        │
│  Run manually via CLI                            │
│  Dispatches scouts in parallel                   │
│  Chains results through filter → brief generator │
└──────────┬──────────────────────────┬────────────┘
           │                          │
     ┌─────▼─────┐            ┌──────▼───────┐
     │ LAYER 1   │            │              │
     │ Trend     │ x4 parallel│  All return   │
     │ Scouts    │────────────│  same schema  │
     └─────┬─────┘            └──────┬───────┘
           │ merged + deduplicated    │
     ┌─────▼──────────────────────────▼──┐
     │ LAYER 2: Relevance Filter          │
     │ Ranks by velocity + locality       │
     │ Light Mandarin angle check         │
     │ Outputs: Top 5-7 ranked trends     │
     └─────┬─────────────────────────────┘
           │
     ┌─────▼─────────────────────────────┐
     │ LAYER 3: Brief Generator           │
     │ Produces per trend:                │
     │  - TikTok brief                    │
     │  - Instagram Reels brief           │
     │ Action-oriented shot lists         │
     └───────────────────────────────────┘
```

**Output:** Markdown file per day saved to a local directory.

## Layer 1: Trend Scouts

Four scouts run in parallel, each specialised to one data source. All return a standardised schema so the filter layer can process them uniformly.

### Scout 1: TikTok Trends

- Source: TikTok Creative Center, web search for trending TikTok content in Australia
- Looks for: trending hashtags, sounds, video formats in education, food, culture, lifestyle, comedy
- Filters for Australia/Sydney geo where possible
- Returns: topic name, trend velocity, example content, trending audio names

### Scout 2: Google Trends — Sydney

- Source: Google Trends filtered to Sydney metro
- Looks for: rising search terms — breakout topics, anything that could be adapted to a Mandarin angle
- Not limited to language-related searches — any trending topic is fair game
- Returns: search terms, trend direction, relative volume

### Scout 3: Sydney Local — Events, News, Restaurants

- Sources: Web searches for Time Out Sydney, Broadsheet Sydney, Sydney Morning Herald lifestyle, upcoming Sydney events
- Looks for: new restaurant openings (especially Chinese/Asian), cultural events, festivals, trending spots, viral locations
- Returns: event/topic, date, location, address where applicable, why it's trending

### Scout 4: Reddit + Social Buzz

- Sources: r/sydney, r/australia, r/languagelearning
- Looks for: hot posts, local conversation topics, cultural discussions, anything with a language or China/Chinese culture angle
- Returns: topic, thread context, sentiment

### Standardised Scout Output Schema

Each scout returns an array of trend objects:

```
{
  topic: string           — what the trend is
  source: string          — which scout found it
  velocity: "rising" | "peaking" | "fading"
  locality: "sydney" | "australia" | "global"
  raw_context: string     — supporting detail, links, examples
  location?: {            — if it's a physical place
    name: string
    address: string
  }
  trending_audio?: string — if a specific sound is trending
}
```

## Layer 2: Relevance Filter

Takes all scout outputs and produces a ranked shortlist.

### Process

1. **Deduplicate** — same topic surfaced by multiple scouts gets merged. Cross-source signal boosts the trend's rank (if TikTok AND Google Trends AND Reddit are all talking about it, it's hot).
2. **Score** each trend on:
   - **Trend velocity** (primary signal) — is it rising fast? Peaking trends are OK, fading trends are dropped.
   - **Sydney locality** (primary signal) — Sydney-specific beats Australia-wide beats global.
   - **Mandarin angle** (light check) — almost any topic can be adapted, so this is a sanity check not a hard filter. The connection just can't be completely forced.
   - **Content feasibility** — can this realistically be filmed as a short-form video?
3. **Rank and return top 5-7 trends** with a one-line rationale for each.

### Content Type Classification

Each trend is classified as one of:

- **On-location** — a specific trending place, restaurant, or event. Brief will include address and location-specific filming notes.
- **At-home / topic-driven** — a trending topic, format, or cultural moment. Can be filmed as talking head, green screen, or stitch/duet.

The daily output should include a mix of both types so Felicity can choose based on her schedule and energy.

## Layer 3: Brief Generator

For each top trend, produces two platform-specific briefs using proven engagement frameworks.

### Engagement Frameworks

The brief generator draws from these frameworks, selecting the best fit per trend:

- **Hook-Value-CTA** — grab attention in first 2 seconds, deliver value, close with free trial CTA
- **Pattern interrupt** — open with something unexpected ("Don't say nihao to a Chinese person")
- **Teach-in-context** — film at a location/event, teach vocabulary naturally within that setting
- **Us vs them / myth-busting** — "What Australians think X means vs what it actually means"
- **Identity content** — for ABCs specifically ("Things your Chinese parents say but you never understood")

### Brief Structure

Each brief contains:

```
Trend:           What it is, where it's trending, velocity
Type:            On-location (with address) or At-home
Audience Angle:  Which segment this targets (adults, ABCs, or both)
                 with specific framing for each

--- TikTok Version ---
Hook:            Opening 2 seconds — the line that stops the scroll
Talking Points:  2-4 structured points / Mandarin phrases to teach
Filming Notes:   Format (talking head, on-location, green screen, stitch/duet),
                 duration target, specific location if applicable
Audio:           Trending audio suggestion if relevant
Hashtags:        Trend-heavy, discovery-focused
CTA:             Free trial class — link in bio

--- Instagram Reels Version ---
Hook:            Adapted for Reels audience (can be slightly different pacing)
Key Differences: How this version differs from TikTok
                 (pacing, tone, edit style, bonus carousel option)
Hashtags:        Niche + local, community-focused
CTA:             Free trial class — DM me or link in bio
```

### Platform Differentiation

| Dimension | TikTok | Instagram Reels |
|---|---|---|
| Tone | Raw, fast, personality-driven | Slightly more polished, educational |
| Pacing | Quick cuts, high energy | Can breathe a bit more |
| Hook style | Provocative, pattern interrupt | Curiosity-driven, aspirational |
| Hashtags | Trend-heavy, discovery-focused | Niche + local, community-focused |
| CTA | "Link in bio" | "DM me or link in bio" |
| Bonus format | Stitch/duet if relevant | Could also be a carousel post |

## Static Additions

### Chinese Cultural Calendar

A baked-in calendar of predictable high-relevance content moments. Not trend-scouted — these are known dates:

- Lunar New Year
- Mid-Autumn Festival
- Dragon Boat Festival
- Qingming Festival
- Chinese National Day
- Other culturally significant dates

When one of these is approaching (within 1-2 weeks), the system automatically includes it as a brief topic regardless of whether it's "trending" — these are guaranteed engagement moments for a Mandarin teacher.

## Output Format

Daily output is a single Markdown file saved to:

```
~/Documents/Web Projects/YesMandarin/content-pipeline/output/YYYY-MM-DD-content-briefs.md
```

Contains:
- Date and summary of trend landscape
- 5-7 briefs, each with TikTok and Reels versions
- Mix of on-location and at-home content types
- Each brief is self-contained and actionable

## Invocation

Run manually from the command line via a shell script that orchestrates the full pipeline:

```bash
~/Documents/Web Projects/YesMandarin/content-pipeline/run.sh
```

The script dispatches scout agents in parallel, pipes results through the filter, generates briefs, and saves the output file.

## Future Evolution (v2)

Not in scope for initial build, but designed to be addable:

- **Performance feedback loop** — feed back engagement data from Instagram Graph API and TikTok analytics. System learns which types of content, hooks, and frameworks perform best for her audience. Requires 30-60 days of content history.
- **Competitor monitoring scout** — track what other language teachers/schools are posting. Currently not active enough in Sydney to be useful.
- **Content calendar view** — a simple web UI showing upcoming briefs, cultural calendar, and past performance.
- **Automated scheduling** — move from manual CLI trigger to scheduled remote agent (Claude Code triggers or cron).
