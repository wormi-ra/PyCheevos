# Changelog

All notable changes to this project will be documented in this file.

## [0.0.3] - 2023-10-27

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