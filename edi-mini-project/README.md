
# EDI Mini Project – Simple 850 & 856 Checker (Beginner Friendly)

This is a very simple **Python EDI project for beginners**.

It does two things:
1. Checks a basic EDI 850 Purchase Order file for required segments.
2. Checks a basic EDI 856 ASN file for required segments.

Both checks are intentionally simple so you can understand the flow and then improve it.

## Features

- Works on plain text EDI files (one segment per line or `~` separated).
- Verifies presence of important segments:
  - 850: ISA, GS, ST, BEG, PO1, CTT, SE, GE, IEA
  - 856: ISA, GS, ST, BSN, HL, LIN, CTT, SE, GE, IEA
- Prints a small error report in the terminal.

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.

### Check sample 850

```bash
python edi_checker.py samples/sample_850.edi 850
```

### Check sample 856

```bash
python edi_checker.py samples/sample_856.edi 856
```

## Example Output

```text
--- EDI Check Report ---
File: samples/sample_850.edi
Type: 850

Missing segments:
  - CTT

Tips:
- Make sure your 850 has a CTT segment with the line count.
```

## Ideas to Improve

If you want to grow this into a bigger project:

- Add more detailed validations (element-level checks).
- Add support for more transaction sets (810, 997, 855, etc.).
- Export the error report to a CSV or JSON file.
- Build a small CLI menu or even a web UI.

This project is perfect as a **first EDI-related GitHub repo**.
