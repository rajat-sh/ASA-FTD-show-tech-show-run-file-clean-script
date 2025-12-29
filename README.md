# Cisco CLI Log Cleaner

This Python utility is designed to sanitize and "clean" raw log files captured from Cisco ASA, FTD, or IOS terminal sessions. It specifically targets common terminal artifacts—such as pagination prompts and carriage returns—that often clutter configuration backups or diagnostic outputs.

---

## 🔍 Overview

When capturing output from a Cisco device, the session often includes interactive elements like the `"-- More --"` prompt or control characters (e.g., `^M`). This script automates the removal of these artifacts, leaving behind only the clean, printable configuration or command output.

### Key Cleaning Actions:

* **Pagination Removal:** Deletes segments containing `<...- More -...>` (e.g., `<--- More --->`).
* **Control Character Stripping:** Removes carriage returns (`\r`) and specific `^M` segments.
* **ASCII Filtering:** Filters out all non-printable ASCII characters, preserving only the standard printable range (–).
* **Whitespace Normalization:** Trims leading spaces that often remain after removing terminal prompts.

---

## 🛠 Prerequisites

* **Python 3.6+**
* No external libraries are required; the script uses standard Python modules (`re`, `pathlib`).

---

## 🚀 Usage

1. **Run the script:**
python clean_files.py




2. **Enter Input Path:** Provide the path to your raw log or text file (e.g., `session_capture.txt`).
3. **Enter Output Path:**
* Provide a specific filename for the cleaned output.
* **OR** Press **Enter** to automatically save the file with a `.clean` extension (e.g., `session_capture.txt.clean`).



---

## 📖 How It Works

The script processes the file line-by-line using byte manipulation to ensure no data is lost during encoding conversions:

1. **`MORE_RE`**: A regular expression that identifies case-insensitive "More" prompts within a single line.
2. **`CARET_M_SEGMENT_LINE_RE`**: Targets literal `^M` markers often found in console captures.
3. **Byte Filtering**: The script creates a new byte array, only including bytes that fall within the valid printable ASCII range, ensuring the output is safe for standard text editors.

---

## ⚠️ Disclaimer

This script is intended for text-based terminal logs. Ensure you have a backup of your original data before processing, as this script permanently filters out non-printable characters.

