# MRI lumbar spine + sacrum — 18 Aug 2026 (I-MED Chatswood)

Acc #77.60502003 · Se times 10:59–11:27 · Sag 4.0 mm/4.8 mm; Ax 3.0 mm/3.45 mm

**What these files are:** single-frame PNG screenshots exported from the I-MED patient viewer on 19 Aug 2026 — **one frame per series**, not the full DICOM stacks. Two download passes were byte-identical duplicates except where noted; duplicates removed. Read is in `../../mri-2026-08-18-read.md`.

**Still to obtain:** the full DICOM study — every stack below is 24–36 slices and only one is captured here; the second key image (Im 2/2) was not captured; the formal report (patient copy ~24 Aug; GP already has it).

**How to get DICOMs (established 19 Aug):** the web viewer is Intelerad **Enterprise Viewer** embedded in the **My I-MED** patient portal. Per the EV 2.12 User Guide (p.114 "Downloading Images") the viewer's only download is a **PNG snapshot of the selected viewport** — no DICOM/study export exists in the viewer. Per I-MED's My I-MED FAQ the patient portal is **view + share only** (share = sends a viewer link by SMS/email). So DICOMs come from the clinic, not the app:
1. **Ring/visit I-MED Chatswood** and ask for "a copy of the study on CD/USB" (Acc #77.60502003). Routine request; small fee or free; usually same/next day. She is entitled to it under APP 12 (Privacy Act) — they can charge a reasonable fee, not refuse.
2. **Ask I-MED to forward the study electronically to the neurosurgeon's rooms** when the appointment is booked — surgeons access it via I-MED Online / InteleViewer at full resolution.
3. Meanwhile, better screenshots: EV's PNG = the viewport at its on-screen size → **full-screen the browser, 1-viewport layout, hide nothing**, then Download Image on each slice you want (L5–S1 axials pre + post contrast; midline sagittals). `key-image-4.png` (454 px) vs `key-image-1.png` (322 px) shows the difference.

## Sequence timeline (from overlays) — why it matters

| Time | Series | Note |
|---|---|---|
| 10:59 | SAG T2 Dixon (water + in-phase) | routine |
| 11:00 | SAG T1 | routine — the radiologist's **key image** with measurements comes from this series (Se 18001, Im 1/2) |
| ~11:0x | COR STIR | routine |
| 11:0x–11:07 | AX T2 upper + lower L-spine (Se 21001/22001, 36 slices each) | routine |
| **11:09** | **AX T2_ (Se 23001, 34 slices, starts at L5)** | **added** — dedicated L5→sacrum stack |
| **11:10** | **AX T1 (Se 24001, 34 slices, starts at L5)** | **added** |
| ~11:1x | AX T1 FS (Se ~25001) | **added** |
| **11:27** | **AX T1 FS C+ (Se 28001) + SAG T1 Dixon C+** | **gadolinium given** — added |

Contrast + a T1/T1FS/T2 sacral stack after the routine sequences = the reporting radiologist saw a lesion at the lumbosacral junction and ran a characterisation protocol (tumour vs non-enhancing tissue). This is not what a normal disc study looks like.

## Files

### non-contrast/
- `sag-T1.png` — Se ?, far-lateral slice (through iliac wing/kidney) — non-diagnostic frame
- `sag-T2-dixon-water-a.png` — Se 17001, Im 12/24, paramedian (facets visible). Shows discs, sac contour, terminal sac
- `sag-T2-dixon-water-b.png` — far paramedian (facets/foramina) — limited
- `sag-T2-dixon-inphase-a.png`, `-b.png` — far-lateral frames — non-diagnostic
- `cor-STIR.png` — anterior coronal (bowel) — incidental only
- `ax-T2-upper-lspine.png` — Se 21001, T12 level — normal cord cross-section
- `ax-T2-lower-lspine.png` — Se 22001, Im 1/36, labelled **L3** — ovoid dark structure inside sac (cord? / flow void?) — see read
- `ax-T2.png` — **Se 23001, Im 1/34, L5 — KEY FRAME**: dorsal intradural soft-tissue structure filling ~half the sac
- `ax-T1.png` — **Se 24001, Im 1/34, L5 — KEY FRAME**: same structure, T1 iso (not fat)
- `ax-T1-FS.png` — lower sacral level, grainy — limited

### contrast/
- `ax-T1-FS-C+.png` — Se 28001, Im 1/34, labelled L4-5 (oblique) — no clear enhancing focus on this frame; not the lesion level
- `sag-T1-dixon-water-C+.png` — far-lateral frame — non-diagnostic

### key-images/
- `key-image-4.png` — same key frame captured at a larger viewport (454 px tall) — **use this one**
- `key-image-1.png` (2 and 3 are the same frame re-downloaded) — **SAG T1 midline with radiologist's measurements**: line 1 = 12.12 cm (posterior sac at L4/5 → skin at coccyx level, along the dorsal sacrum), line 2 = 1.96 cm (perpendicular at L5/S1, sac tip → dorsal line), ratio 6.17. Im 1/2 — **Im 2/2 not captured**.

### scout/
- `scout-composite-sag.png` — whole-spine localiser — non-diagnostic
