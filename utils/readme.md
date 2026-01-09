# @pycheevos/utils

The **Utils** module provides powerful migration tools to convert existing RetroAchievements data (Code Notes and Achievements) into modern PyCheevos Python scripts.

These tools are **Hybrid**:
1.  **Local First**: They scan your emulator directory for existing work (`User.txt`, `.json`).
2.  **Cloud Fallback**: If nothing is found, they offer to download the latest data from the RetroAchievements server.

### Table of Contents
1. [First Run & Setup](#1-first-run--setup)
2. [Import Strategy](#2-import-strategy)
3. [Import Notes](#3-import-notes)
4. [Import Achievements](#4-import-achievements)

#

### 1. **First Run & Setup**
The scripts need to know where your emulator (RALibretro, RAIntegration, etc.) is located to find your local files.

**How it asks for the folder:**
1.  **Automatic Cache**: It first checks for a hidden file `RACache`. If it exists, it loads the path silently.
2.  **Selection Window**: If no cache is found, it attempts to open a system folder selection window (via `tkinter`).
3.  **Manual Input**: If the window cannot be opened, it falls back to asking you to type/paste the path in the terminal.

> [!NOTE] 
> The path is saved locally in `RACache` so you only need to do this once.

#

### 2. **Import Strategy**
When you provide a Game ID, the tool performs a smart scan of your emulator directory:

1.  **Recursive Scan**: It looks through the root folder and subfolders.
2.  **File Priority**:
    * **High Priority**: `[ID]-User.txt`. This file contains your local, unsaved edits. The tool prefers this so you don't lose work-in-progress.
    * **Medium Priority**: `[ID]-Notes.json` or `[ID].json`. These usually contain the last saved state from the server.
3.  **Parsing**: It reads the file line-by-line (for TXT) or parses the object structure (for JSON) to extract memory addresses and logic strings.

**Server Download (Fallback)**
If no local files are found, the script prompts for your RA credentials. It connects securely to fetch the latest game data directly from the database, ensuring you always have a starting point even on a fresh install.

#

### 3. **Import Notes**
**Script:** `utils/import_notes.py`

Reads code notes and generates a python file defining them as `byte()`, `word()`, `dword()`, etc. It handles naming conflicts and sanitizes strings to be valid Python identifiers.

**Usage:**
```bash
python utils/import_notes.py
# Follow the prompts to enter the Game ID
```

#### **Pointer Detection**

The importer recognizes the RetroAchievements pointer hierarchy convention (`+`, `++`) and automatically generates the corresponding pointer logic (`>>`).

**Input (Code Note):**

```r
[32-bit] Base Pointer
+0x44
++0x10
+++0x30 = [8-bit] Current Health
```

**Output (Generated Python):**

```python
base_pointer = dword(0x123456)

# Automatically chains offsets using right-shift (AddAddress)
current_health = (base_pointer >> dword(0x44) >> dword(0x10) >> byte(0x30))
```

### 4. **Import Achievements**

**Script:** `utils/import_achievements.py`

Lê um set de conquistas existente e gera um script Python completo (`scripts/imported_[ID].py`) com toda a lógica traduzida e pronta para compilar.

**Usage:**

```bash
python utils/import_achievements.py
```

#### **Logic Translation Capabilities**

The parser handles complex RetroAchievements logic features automatically:

* **Bitmasks**: Automatically identifies masked addresses (e.g., `0x00A0 & 0xFF`) and converts them to `(mem & value(0xFF))`.
* **Type Safety**: Wraps raw numbers in `value()` to ensure Python handles them as logic objects, preventing math errors.
* **Floats**: Correctly identifies and converts floating-point values.
* **Flags**: Translates all logic flags (`R:`, `P:`, `M:`, `A:`, etc.) into `.with_flag(...)`.

**Example Conversion:**

* **Original MemString**:
`0xH1234=1_R:0xH5678!=0`
* **Generated Python**:
```python
logic = [
    # Condition
    byte(0x1234) == value(1),

    # Reset Flag
    (byte(0x5678) != value(0)).with_flag(reset_if)
]
```