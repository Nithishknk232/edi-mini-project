
import sys

REQUIRED_SEGMENTS_850 = ["ISA", "GS", "ST", "BEG", "PO1", "CTT", "SE", "GE", "IEA"]
REQUIRED_SEGMENTS_856 = ["ISA", "GS", "ST", "BSN", "HL", "LIN", "CTT", "SE", "GE", "IEA"]

def load_segments(file_path):
    """Load segments from an EDI file.
    Supports:
    - One segment per line, OR
    - All segments on one line separated by '~'
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read().strip()

    # If file uses '~' as segment terminator
    if "~" in data:
        raw_segments = [seg.strip() for seg in data.split("~") if seg.strip()]
    else:
        raw_segments = [line.strip() for line in data.splitlines() if line.strip()]

    segments = []
    for seg in raw_segments:
        segment_id = seg.split("*")[0].strip()
        if segment_id:
            segments.append(segment_id)

    return segments

def check_required_segments(segments, edi_type):
    if edi_type == "850":
        required = REQUIRED_SEGMENTS_850
    elif edi_type == "856":
        required = REQUIRED_SEGMENTS_856
    else:
        raise ValueError("Unsupported EDI type. Use '850' or '856'.")

    missing = [seg for seg in required if seg not in segments]
    return missing

def main():
    if len(sys.argv) != 3:
        print("Usage: python edi_checker.py <file_path> <850|856>")
        sys.exit(1)

    file_path = sys.argv[1]
    edi_type = sys.argv[2]

    try:
        segments = load_segments(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

    missing = check_required_segments(segments, edi_type)

    print("\n--- EDI Check Report ---")
    print(f"File: {file_path}")
    print(f"Type: {edi_type}\n")

    if not segments:
        print("No segments found in file. Check that the file is not empty.")
        sys.exit(0)

    if missing:
        print("Missing segments:")
        for seg in missing:
            print(f"  - {seg}")
    else:
        print("All basic required segments are present. (Simple check only)")

    print("\nTips:")
    if edi_type == "850":
        print("- Make sure your 850 has at least one PO1 line and a CTT with line count.")
    else:
        print("- Make sure your 856 HL structure and LIN segments match your trading partner guide.")

if __name__ == "__main__":
    main()
