# Changelog

### Fixed
- **Pip Installation:** Fixed `ModuleNotFoundError` when using the library installed via pip. Internal imports in `models` were converted to absolute paths (`from pycheevos.core...`) to ensure correct resolution.
- **Note Parser:** Fixed an issue where literal `\r\n` escape sequences in note files were not parsed correctly, causing malformed variable names and merged comments.
- **Wildcard Imports:** Removed unsafe wildcard imports (`import *`) from internal modules to improve code safety and linter compatibility.

### Changed
- **Variable Naming:** Improved conflict resolution in `import_notes`. Duplicate variable names now use a clean sequential counter (e.g., `health_2`) instead of appending raw memory addresses.

### Added
- **Documentation:** Added an `Installation` section to the README with specific instructions for `pip` and how to execute utility scripts using the `python -m` module flag.