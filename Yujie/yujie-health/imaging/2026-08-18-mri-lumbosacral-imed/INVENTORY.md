# MRI lumbar spine — I-MED Chatswood, 18 Aug 2026 — DICOM inventory

Source: I-MED patient DVD-R (volume `CAO_YUJIE`, InteleViewer disc, burned 27 Aug 2026), copied byte-identical to this folder on 28 Aug 2026.
Report: `../../records/2026-08-18-mri-lumbosacral-report-imed.pdf`

| Field | Value |
|---|---|
| Study | MRI NR SPINE LUMBAR, 18 Aug 2026 10:50 |
| Accession | 77.60502003 |
| Site / scanner | I-MED Radiology Chatswood — Siemens MAGNETOM Altea 1.5 T |
| Referrer | Dr Ling Guan |
| Format | DICOM Part 10, Explicit VR Little Endian (uncompressed — opens in anything) |
| Files | 342 DICOM (330 images + 12 presentation states) + 12 Siemens `SeriesHeader.zip` sidecars; matches DICOMDIR index exactly |

## Series (14)

| # | Plane | Imgs | Matrix | Slice | Description |
|---|---|---|---|---|---|
| 15001 | SAG | 15 | 510×111 | 1.7 | Scout / MPR |
| 16001 | SAG | 24 | 456×384 | 4.0 | SAG T2 DIXON in-phase |
| 17001 | SAG | 24 | 456×384 | 4.0 | SAG T2 DIXON water (fat-sat) |
| 18001 | SAG | 24 | 608×512 | 4.0 | SAG T1 |
| 19001 | COR | 24 | 460×384 | 4.0 | COR STIR |
| 21001 | AX | 30 | 364×448 | 3.0 | AX T2 upper lumbar |
| 22001 | AX | 36 | 364×448 | 3.0 | AX T2 lower lumbar |
| 23001 | AX | 34 | 392×480 | 3.0 | AX T2 |
| 24001 | AX | 34 | 416×512 | 3.0 | AX T1 |
| 25001 | AX | 36 | 392×480 | 3.0 | AX T1 fat-sat |
| 27001 | SAG | 15 | 500×416 | 4.0 | SAG T1 DIXON post-contrast water |
| 28001 | AX | 34 | 416×416 | 3.0 | AX T1 fat-sat post-contrast |
| 28002 | — | 2 | — | — | Key images (radiologist-flagged) |
| 28003 | — | 10 | — | — | Presentation states (radiologist annotations) |

Contrast was given (series 27001/28001 C+). Sagittal T1 (18001) and T1 DIXON (17001/27001) are the ones that show the lipoma/tethering; axial T1 FS (25001/28001) for the dermal sinus and root involvement.

## Files here (raw data git-ignored; only this inventory is tracked)

- `DICOMDIR`, `DICOM/` — the study; drag the folder into Horos / 3D Slicer / Weasis
- `Viewer/` — Windows-only InteleViewer from the disc; not needed
- `../2026-08-18-mri-lumbosacral-imed-dicom.zip` — DICOMDIR + DICOM only, for sending to surgeons / hospital PACS import
