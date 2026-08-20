# html2pdf — WebKit HTML→PDF (single continuous page)

Why: on the M5 (rebuilt Aug 2026) headless Chrome `--print-to-pdf` produces PDFs with no text (font/sandbox issue), and `NSPrintOperation` hangs headless. `WKWebView.createPDF` works.

Build: `swiftc -O html2pdf.swift -o html2pdf`
Use:   `./html2pdf in.html out.pdf`   (run **outside** the CC sandbox — needs WindowServer)
Output: one page, 560 pt wide, height = content. Good for phone reading; not paginated A4.
Used for: ~/personal/Yujie/partner-health/summary-for-*.pdf (Aug 2026).
