import re
from pathlib import Path

# Remove "<...- More -...>" within a single line (non-greedy; case-insensitive; does not cross EOL).
MORE_RE = re.compile(rb"<[^>\r\n]*-\s*More\s*-[^>\r\n]*>", re.IGNORECASE)

# Remove any segment on a line that starts with literal "^M", has any bytes (non-greedy), then another literal "^M".
CARET_M_SEGMENT_LINE_RE = re.compile(rb"\^M.*?\^M")

def clean_line(line: bytes) -> bytes:
    # Preserve newline if present.
    has_nl = line.endswith(b"\n")
    if has_nl:
        body = line[:-1]
    else:
        body = line

    # Remove carriage returns (0x0D).
    body = body.replace(b"\r", b"")

    # Delete "<...- More -...>" substrings (e.g., "<--- More --->" -> "").
    body = MORE_RE.sub(b"", body)

    # Replace any "^M ... ^M" segment with empty string.
    body = CARET_M_SEGMENT_LINE_RE.sub(b"", body)

    # Trim leading spaces that may remain after removals (to match the example expectation).
    body = body.lstrip(b" ")

    # Remove all non-printable ASCII (keep printable 0x20–0x7E only).
    body = bytes(b for b in body if 0x20 <= b <= 0x7E)

    return body + (b"\n" if has_nl else b"")

def main():
    in_path = input("Enter input file path: ").strip()
    if not in_path:
        print("No input file provided.")
        return
    src = Path(in_path)
    if not src.is_file():
        print(f"Input file not found: {src}")
        return

    out_path = input("Enter output file path (press Enter for default '<input>.clean'): ").strip()
    dst = Path(out_path) if out_path else Path(str(src) + ".clean")

    try:
        raw = src.read_bytes()
        cleaned = bytearray()
        for line in raw.splitlines(keepends=True):
            cleaned.extend(clean_line(line))
        dst.write_bytes(bytes(cleaned))
        print(f"Cleaned file written to: {dst}")
    except OSError as e:
        print(f"I/O error: {e}")

if __name__ == "__main__":
    main()
