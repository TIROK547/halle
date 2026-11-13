# F-06 / F-05 — Textbook recovery

Checked 13 November 2026 (Asia/Tehran). **Recovered candidate source; not yet approved for production or chosen as the release edition.**

## Publisher evidence

The [publisher listing](http://chap.sch.ir/books/14364), reached through its grade-12 science category, identifies Biology 3, code **112216**, school year **1405–1406**, and links the [complete PDF](http://chap.sch.ir/sites/default/files/lbooks/1405-1406/712/C112216.pdf). Its posted date is 1405/05/25. The downloaded PDF's imprint identifies the ninth printing, 1405. The file has 136 PDF pages and 6,587,991 bytes.

The PDF and a listing snapshot are stored locally under ignored `data/sources/biology12-1405/`. The [source manifest](../sources/biology12-1405.json) records their hashes, provenance, edition observations, page mapping and unresolved approvals. Original research files were not changed.

HTTPS requests to both chap.sch.ir and www.chap.sch.ir failed hostname certificate verification in this environment. Retrieval succeeded over the publisher's HTTP links. TLS verification was not disabled. The recorded SHA-256 identifies this downloaded copy; it is not a publisher-authenticated checksum. Obtain an independently trusted copy/checksum or reviewer comparison before accepting authenticity for production.

## Selected chapter boundaries

| Chapter | Title | Printed pages, inclusive | PDF pages, one-based, inclusive |
| --- | --- | --- | --- |
| 1 | مولکول‌های اطلاعاتی | 1–20 | 9–28 |
| 2 | جریان اطلاعات در یاخته | 21–36 | 29–44 |

PDF page = printed page + 8 within this selected range. The contents starts chapter 3 at printed page 37; extracted text locates its heading on PDF page 45. Keep printed and PDF page numbers separate in future source citations. These boundaries are structural observations, not a completed review of every concept, diagram or page.

## Permission and content review still required

PDF page 4 attributes rights to the Organization for Educational Research and Planning and states a permission requirement for uses including electronic presentation, adaptation and reproduction. This is a recorded publisher notice, not a full legal determination. Public download does not establish our intended commercial extraction, embedding, quotation or redistribution permissions. No permission has been obtained; production ingestion remains disabled in the manifest.

Owner/reviewer next actions:

1. Confirm this edition is appropriate for the selected cohort; no official exam timetable or cohort decision has been completed.
2. Verify the recovered copy against a trusted copy and review chapter boundaries, diagrams and supported input formats.
3. Record applicable permission evidence for the intended uses, or an approved alternative content source. Keep private correspondence outside Git.
4. Agree the reviewed question/key and practice sources separately; recovering a textbook does not supply the required question bank or holdout.

## Checks actually performed

- Retrieved the publisher listing and its linked PDF; recorded byte count and SHA-256.
- `pdfinfo`: 136 pages, unencrypted, no JavaScript reported.
- Extracted text with `pdftotext` to locate chapter starts and distinguish PDF/printed pagination.
- Rendered front pages with `pdftoppm`; visually checked imprint (PDF 2), rights notice (PDF 4) and contents (PDF 5).
- Kept the PDF, HTML snapshot, rendered images and extracted text out of Git. Only source metadata and findings enter the repository.

F-05, F-06 and K-01 remain open. This completes the initial recovery substep, not rights clearance, educational review or reproducible ingestion.
