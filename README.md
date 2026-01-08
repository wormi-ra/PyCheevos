# PyCheevos

**PyCheevos** is a set of tools to generate [RetroAchievements](https://retroachievements.org/) achievement sets programmatically using Python.

Inspired by **RATools** and **Cruncheevos**, it allows you to leverage the full power of the Python ecosystem (loops, functions, classes) to build complex achievement logic with clean, readable code.

- **[Core](https://github.com/CarlosNatanael/PyCheevos/blob/main/core)**: Handles condition parsing, memory addresses, and arithmetic logic (`byte`, `word`, `value`, `delta`, `prior`). Now supports logical operators (`&`, `|`, `~`) for condition chaining.

- **[Models](https://github.com/CarlosNatanael/PyCheevos/blob/main/models)**: Provides the structure for Sets, Achievements, Leaderboards, and Rich Presence.

- **[Utils](https://github.com/CarlosNatanael/PyCheevos/blob/main/utils)**: Contains hybrid importers (`import_notes`, `import_achievements`) that can fetch data from local files or directly from the RetroAchievements server.

### Usage
Using this library assumes familiarity with the [RetroAchievements](https://docs.retroachievements.org) workflow and memory inspection.

### Get Started
Create a new .py file and import the library modules (`models` and `core`).  

Run your .py file, it should generate to a folder called `output` in the same directory as your .py file.  
You can change this output location by defining a path in the `.save()` function of `AchievementSet`.  

- To import achievements, run `python utils/import_achievements.py`. It supports local files and server download.
- To import notes, run `python utils/import_notes.py`. It automatically detects pointer hierarchies and fetches notes from the server if needed.

#### Small Demo
```python
from models.set import AchievementSet
from models.achievement import Achievement
from core.helpers import byte, prior, value

# Initialize the set
game_set = AchievementSet(game_id=1, title="Sonic the Hedgehog")

# Define Memory Addresses
mem_rings = byte(0xFE20)
mem_zone  = byte(0xFE10)

# Reusable Logic Function
def got_rings(amount):
    """Triggers when ring count increases to or past 'amount'."""
    # New Syntax: Use '&' for AND, '|' for OR, '~' for NOT
    # Use value() to wrap constant numbers safely
    return (mem_rings >= value(amount)) & (prior(mem_rings) < value(amount))

# Create Achievement
ach = Achievement(
    title="Super Ring Collector", 
    description="Collect 1000 rings", 
    points=50, 
    id=111001
)

# Apply Logic
# You can chain logic directly using operators
ach.add_core(
    got_rings(1000) & (mem_zone == value(0)) # Must be in Green Hill
)

game_set.add_achievement(ach)

# Generate the user file (1-User.txt)
game_set.save()

```

### Contributing

You are welcome to ***report issues***. If you run into errors generating the script, please include your Python version and the traceback.

You are welcome to ***request features***. When doing so, please show how you would use the feature (pseudo-code) and what logic problem it solves.

The core library aims to be minimal. Complex logic specific to a single game should ideally be implemented in your own script using Python's flexibility, rather than hardcoded into the library core.

***Pull Requests*** are welcome, especially for documentation improvements or type hinting fixes.
