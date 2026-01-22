# @pycheevos/utils

The **Utils** module provides powerful migration tools to convert existing RetroAchievements data (Code Notes, Achievements, and Leaderboards) into modern PyCheevos Python scripts.

You can access these tools via the command line interface:

```bash
pycheevos-import
```

These tools are **Hybrid**:

1. **Local First**: They scan your emulator directory for existing work (`User.txt`, `.json`).
2. **Cloud Fallback**: If nothing is found, they offer to download the latest data from the RetroAchievements server.

### Table of Contents

1. [First Run & Setup](https://www.google.com/search?q=%231-first-run--setup)
2. [Import Strategy](https://www.google.com/search?q=%232-import-strategy)
3. [The Smart Importer (Unified)](https://www.google.com/search?q=%233-the-smart-importer-unified)
4. [Legacy/Individual Importers](https://www.google.com/search?q=%234-legacyindividual-importers)

### 1. **First Run & Setup**

The scripts need to know where your emulator (RALibretro, RAIntegration, etc.) is located to find your local files.

**How it asks for the folder:**

1. **Automatic Cache**: It first checks for a hidden file `.racache_path`. If it exists, it loads the path silently.
2. **Selection Window**: If no cache is found, it attempts to open a system folder selection window (via `tkinter`).
3. **Manual Input**: If the window cannot be opened, it falls back to asking you to type/paste the path in the terminal.

> [!NOTE]
> The path is saved locally so you only need to do this once.

### 2. **Import Strategy**

When you provide a Game ID, the tool performs a smart scan of your emulator directory:

1. **Recursive Scan**: It looks through the root folder and subfolders.
2. **File Priority**:
* **High Priority**: `[ID]-User.txt`. This file contains your local, unsaved edits. The tool prefers this so you don't lose work-in-progress.
* **Medium Priority**: `[ID]-Notes.json` or `[ID].json`. These usually contain the last saved state from the server.


3. **Parsing**: It reads the file line-by-line (for TXT) or parses the object structure (for JSON) to extract memory addresses, logic strings, and badge IDs.

**Server Download (Fallback)**
If no local files are found, the script prompts for your RA credentials. It connects securely to fetch the latest game data directly from the database, ensuring you always have a starting point even on a fresh install.

### 3. **The Smart Importer (Unified)**

**Menu Option:** `4` (Recommended)

This is the most powerful tool in the kit. It combines Note processing, Achievement generation, and Leaderboard generation to produce human-readable code.

**Key Features:**

1. **Generates Notes**: Downloads Code Notes and creates a `notes_[ID].py` file, defining variables like `health = byte(0x1234)`.
2. **Maps Variables**: It builds a dictionary of addresses -> variable names.
3. **Smart Generation**: It parses existing achievements and leaderboards, replacing raw addresses (`byte(0x1234)`) with variable names (`health`) in the generated code.
4. **Preserves Badges**: Automatically extracts the `BadgeName` (icon ID) to ensure your badges are not reset to "00000" upon saving.
5. **Smart Reconciliation**: If you have local Achievements but are missing local Leaderboards, it will automatically fetch the missing data from the server to generate a complete set.

**Comparison:**

* **Raw Import:**
```python
(byte(0x1234) == value(10))
```


* **Smart Import:**
```python
(health == 0x0a)
```



### 4. **Legacy/Individual Importers**

If you only need to generate one specific type of file, you can use the individual options.

#### **Import Notes**

**Menu Option:** `1`

Reads code notes and generates a python file defining them as `byte()`, `word()`, `dword()`, etc. It handles naming conflicts and sanitizes strings to be valid Python identifiers.

**Pointer Detection:**
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

#### **Import Achievements**

**Menu Option:** `2`

Reads an existing achievement set and generates a complete Python script (`scripts/achievement_[ID].py`) with all logic translated. Supports extracting Badge IDs.

> [!TIP]
> Use **Option 4 (Unified)** instead to get variable names in your logic. Option 2 produces "Raw" logic with memory addresses.

**Logic Translation Capabilities:**
The parser handles complex RetroAchievements logic features automatically:

* **Bitmasks**: Automatically identifies masked addresses (e.g., `0x00A0 & 0xFF`) and converts them to `(mem & 0xFF)`.
* **Hex Formatting**: Constants are formatted as Hexadecimal (`0x0f`) for readability.
* **Clean Syntax**: Smartly omits `value()` wrappers when comparing against memory objects.
* **Floats**: Correctly identifies and converts floating-point values.
* **Flags**: Translates all logic flags (`R:`, `P:`, `M:`, `A:`, etc.) into wrapper functions like `reset_if(...)`.

#### **Import Leaderboards**

**Menu Option:** `3`

Reads existing leaderboards and generates a Python script (`scripts/leaderboard_[ID].py`) containing the Start, Cancel, Submit, and Value logic.

* **Logic Parsing**: Splits the standard Leaderboard string (`STA:..::CAN:..::SUB:..::VAL:..`) into readable Python lists.
* **Raw Import**: Like Option 2, this generates logic using raw memory addresses. For variable mapping, use Option 4.
