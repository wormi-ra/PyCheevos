# Changelog

# [0.0.4] - 12/01/2026
### Fixed
- **Pip Installation:** Fixed `ModuleNotFoundError` when using the library installed via pip. Internal imports in `models` were converted to absolute paths (`from pycheevos.core...`) to ensure correct resolution.
- **Note Parser:** Fixed an issue where literal `\r\n` escape sequences in note files were not parsed correctly, causing malformed variable names and merged comments.
- **Wildcard Imports:** Removed unsafe wildcard imports (`import *`) from internal modules to improve code safety and linter compatibility.

### Changed
- **Variable Naming:** Improved conflict resolution in `import_notes`. Duplicate variable names now use a clean sequential counter (e.g., `health_2`) instead of appending raw memory addresses.

### Added
- **Documentation:** Added an `Installation` section to the README with specific instructions for `pip` and how to execute utility scripts using the `python -m` module flag.

---

## [0.0.3] - 11/01/2026

### Added
- **Helper Functions:** Added functional helpers for flags in `core.helpers` (e.g., `reset_if()`, `measured()`, `pause_if()`) for cleaner syntax.
- **AchievementType:** Added `AchievementType` Enum in `core.constants` (`PROGRESSION`, `WIN_CONDITION`, `MISSABLE`) to support achievement classification.
- **Logical Operators:** Added explicit support for `and_next()` and `or_next()` helpers, alongside pythonic `&` and `|` operators.

### Fixed
- **Emulator Parsing Error:** Fixed `User.txt` generation where titles containing colons (`:`) would break the parser. Titles and descriptions are now quoted.
- **Memory Formatting:** - Fixed extra space in Word addresses (`0x 1234` -> `0x1234`).
    - Fixed invalid `0x` prefix appearing on Float (`fF`) and Bitcount (`K`) memory types.
- **Recall Logic:** Fixed `RecallValue` rendering `{recall}` string instead of `0`, which caused emulator syntax errors.

### Changed
- **Breaking Change:** Removed lowercase flag constants (e.g., `reset_if`) from `core.constants` to avoid naming conflicts with the new helper functions. Please use the new functions or the uppercase constants (`Flag.RESET_IF`).
