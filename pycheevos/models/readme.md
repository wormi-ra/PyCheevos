# @pycheevos/models

The **Models** module defines the structural components of a RetroAchievements set. While [`core`](https://github.com/CarlosNatanael/PyCheevos/tree/main/core) handles the logic (memory, conditions), `models` handles the containers that organize that logic into exportable files.

### Table of Contents
1. [AchievementSet](#1-achievementset)
    - [Initialization](#initialization)
    - [Methods](#methods)
2. [Achievement](#2-achievement)
    - [Initialization](#initialization-1)
    - [Achievement Types (Enum)](#achievement-types-enum)
    - [Logic Methods](#logic-methods)
3. [Leaderboard](#3-leaderboard)
    - [Initialization](#initialization-2)
    - [Logic Components](#logic-components)
    - [Examples (Time & Score)](#leaderboard-examples)
4. [Rich Presence](#4-rich-presence)
    - [Initialization](#initialization-3)
    - [Lookups & Displays](#lookups--displays)
    - [Complete Example](#rich-presence-example)
    - [Independent Save](#independent-save)
5. [Game Objects (OOP)](#5-game-objects-oop)
    - [Defining a Class](#defining-a-class)
    - [Static vs Dynamic](#usage-static-vs-dynamic)
6. [How it works](#6-under-the-hood-how-it-works)
    - [The Code](#the-code)

---

### 1. **AchievementSet**
The `AchievementSet` is the main container for your project. It holds all achievements, leaderboards, and the rich presence script, and is responsible for exporting them to text files.

#### **Initialization**
```python
from pycheevos.models.set import AchievementSet

game_set = AchievementSet(game_id=12345, title="My Awesome Game")
```

* **game_id**: The unique ID of the game on RetroAchievements.org.
* **title**: The name of the game (used for folder/file naming).

#### **Methods**

* `add_achievement(achievement)`: Registers an achievement object.
* `add_leaderboard(leaderboard)`: Registers a leaderboard object.
* `add_rich_presence(rp)`: Registers the Rich Presence object.
* `save(path=None)`: Exports `[ID]-User.txt` and `[ID]-Rich.txt`.
* If `path` is not provided, defaults to an `output/` folder next to the script file.

---

### 2. **Achievement**

Represents a single achievement. It manages the logic groups: Core (Required) and Alts (Alternative paths).

#### **Initialization**

```python
from pycheevos.models.achievement import Achievement
from pycheevos.core.constants import AchievementType

ach = Achievement(
    title="Master of Unlocking",
    description="Unlock 10 doors.",
    points=5,
    id=111000001,
    badge="12345",
    type=AchievementType.PROGRESSION
)
```

#### **Achievement Types (Enum)**

Always use the `AchievementType` enum to prevent typos.

* `AchievementType.STANDARD`: Default (empty string).
* `AchievementType.PROGRESSION`: Automatically unlocks as you play (progression markers).
* `AchievementType.WIN_CONDITION`: Triggers when beating the game.
* `AchievementType.MISSABLE`: Can be missed in a single playthrough.

#### **Logic Methods**

* `add_core(conditions)`: Adds conditions that **must always be true**. Supports lists or single conditions.
* `add_alt(conditions)`: Adds an **alternative group**. The achievement triggers if Core is True AND (Alt 1 is True OR Alt 2 is True...).
* `add_condition(condition)`: Helper to add a single condition to the Core group.

#### **Example: Logic with Alts**

```python
# Logic: Level 5 AND (Health > 0 OR Cheats = 0)
ach.add_core(mem_level == 5)

# Alt Group 1: Surviving
ach.add_alt(mem_health > 0)

# Alt Group 2: Hardcore (No Cheats)
ach.add_alt(mem_cheats == 0)
```

---

### 3. **Leaderboard**

Represents a leaderboard (Speedrun, High Score). It consists of four distinct logic sections.

#### **Initialization**

```python
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.core.constants import LeaderboardFormat

lb = Leaderboard(
    title="Green Hill Zone Act 1",
    description="Fastest time",
    id=111000002,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
```

#### **Logic Components**

You can set these using lists of conditions or single expressions.

* `set_start(conditions)`: **START**. When these conditions become true, the attempt begins.
* `set_cancel(conditions)`: **CANCEL**. If these become true during an attempt, it is invalidated.
* `set_submit(conditions)`: **SUBMIT**. When these become true, the current value is sent to the server.
* `set_value(conditions)`: **VALUE**. The memory expression that calculates the score/time.
* **Note:** The condition passed here usually needs the `measured()` helper if it's not a raw value.

#### **Leaderboard Examples**

**A. Speedrun (Lowest Time)**

```python
lb = Leaderboard(
    title="Speedrun - Stage 1",
    description="Finish Stage 1 as fast as possible",
    id=123,
    format=LeaderboardFormat.FRAMES, # Converts frames to MM:SS.mm
    lower_is_better=True
)

# Start: Entered Stage 1 (and wasn't there before)
lb.set_start((stage == 1) & (prior(stage) != 1))

# Cancel: Left stage, died (lives decreased), or went to menu
lb.set_cancel((stage != 1) | (lives < prior(lives)) | (menu_active == 1))

# Submit: Reached the goal (Game Clear flag)
lb.set_submit(level_complete == 1)

# Value: The in-game timer (measured in frames)
lb.set_value(mem_timer) 
```

**B. High Score (Highest Value)**

```python
lb_score = Leaderboard(
    title="High Score - Arcade Mode",
    description="Get the highest score",
    id=124,
    format=LeaderboardFormat.VALUE,
    lower_is_better=False
)

# Start: Game started (State changed from Title to In-Game) and Score is 0
lb_score.set_start((state == 2) & (prior(state) == 1) & (score == 0))

# Cancel: Player used a Continue (Credits dropped)
lb_score.set_cancel(credits < prior(credits))

# Submit: Game Over screen appears
lb_score.set_submit(state == 3) # 3 = Game Over

# Value: The raw score memory address
lb_score.set_value(score)
```

---

### 4. **Rich Presence**

Handles the dynamic status display (Rich Presence) seen on the website.

#### **Initialization**

```python
from pycheevos.models.rich_presence import RichPresence
rp = RichPresence()
```

#### **Lookups & Displays**

1. **Lookups**: Map integer values to text. You can now use **tuples** to map multiple IDs to the same string.
2. **Displays**: A list of conditions evaluated top-to-bottom.
* Use `None` as the condition for the default fallback.
* You can use **f-strings** with memory objects (`@VALUE({mem})`) for cleaner code.
* You can pass complex logic (using `&`, `|`) directly to `add_display`.



#### **Rich Presence Example**

```python
# 1. Define Lookups
rp.add_lookup("Characters", {
    0: "Sonic", 
    1: "Tails", 
    2: "Knuckles"
})

# New Feature: Grouping keys with tuples
rp.add_lookup("Stages", {
    (0, 1, 2): "Green Hill Zone", 
    (3, 4, 5): "Marble Zone",
    6: "Spring Yard"
})

# 2. Define Display Logic (Order matters!)

# Case 1: Title Screen (State == 0)
rp.add_display(
    mem_state == 0, 
    "In Title Screen"
)

# Case 2: Paused (Paused == 1)
# New Syntax: using f-strings for formatting
rp.add_display(
    mem_paused == 1, 
    f"Paused - @Stages({mem_stage}) [Time: @VALUE({mem_time})]"
)

# Case 3: In-Game (Default fallback)
# Use 'None' for the unconditional display
rp.add_display(
    None,
    f"Playing as @Characters({mem_char}) in @Stages({mem_stage}) (Lives: {mem_lives})"
)

# 3. Add to Set
game_set.add_rich_presence(rp)
```

#### **Independent Save**

You can save the Rich Presence script separately from the main set if you prefer modularity.

```python
# Generates 12345-Rich.txt in the output folder
rp.save(game_id=12345, title="My Game RP")
```

---

### 5. **Game Objects (OOP)**

You can create reusable classes for game entities (like Player, Enemy, Inventory) using the `GameObject` base class. This allows you to define memory offsets once and reuse them for both static memory addresses and dynamic pointers.

#### **Defining a Class**

Inherit from `GameObject` and use `self.offset()` to map memory relative to the object's base.

```python
from pycheevos.models.generic import GameObject
from pycheevos.core.helpers import byte, word

class Player(GameObject):
    def __init__(self, address):
        super().__init__(address)
        # Define properties: self.offset(distance, type)
        self.health = self.offset(0x00, byte)
        self.coins  = self.offset(0x04, word)
     
    def is_dead(self):
        return self.health == 0
```

#### **Usage (Static vs Dynamic)**

The logic handles both integers (Static RAM) and MemoryValues (Pointers) automatically.

```python
from pycheevos.core.helpers import dword

# Scenario A: Player is always at 0x1000
p1 = Player(0x1000)

# Scenario B: Player is at the address pointed to by 0x5000
pointer = dword(0x5000)
p2 = Player(pointer)

# Using properties
ach.add_core(p1.is_dead())
ach.add_core(p2.coins >= 50)
```

---

### 6. **Under the Hood: How it works**

Here is a complete example showing the Python code and the exact string PyCheevos generates for RetroAchievements.

**The Scenario: "Untouchable"**
**Goal**: Complete Stage 1 with 50+ coins without taking damage.

#### **The Code**

```python
from pycheevos.models.set import *
from pycheevos.models.achievement import *
from pycheevos.core.helpers import byte, trigger, reset_if
from pycheevos.core.constants import AchievementType

def damage_car():
    mem_damage = byte(0x000076)
    mem_event = byte(0x0007dd)
    mem_green = byte(0x00009e)
    mem_position = byte(0x0007d9)
    mem_circuit = byte(0x0013de)

    # 1. Start Condition: Green Light (0) for 1 frame
    cond_start = (mem_green == 0).with_hits(1)
    
    # 2. Track & Rank requirements
    circuit_monaco = (mem_circuit == 14)
    cond_first = (mem_position == 0)

    # 3. Trigger: Event changed to 7 (Victory)
    # New Syntax: using trigger() helper
    victory_cond = trigger(mem_event == 7)

    # 4. Delta Check: Event was 13 previously
    delta_circuit = (mem_event.delta() == 13)

    core = [
        cond_start,
        circuit_monaco,
        cond_first,
        victory_cond,
        delta_circuit
    ]

    # 5. Reset: If Damage > 0
    # Uses Logical Operator '~' (NOT) for demonstration
    # Logic: Reset if (Damage == 0) is FALSE
    cond_reset = reset_if(~(mem_damage == 0))

    alt_damage = [cond_reset]

    return core, alt_damage

# Setup
my_set = AchievementSet(game_id=23121, title="Racing game")

monaco_damageless = Achievement(
    title="Untouchable",
    description="Win a race at the Monaco circuit with zero damage to your car",
    points=25,
    badge="00000",
    type=AchievementType.PROGRESSION
)

l_core, l_alt1 = damage_car()

monaco_damageless.add_core(l_core)
monaco_damageless.add_alt(l_alt1) # Adds Reset logic as an Alternate Group

my_set.add_achievement(monaco_damageless)
# my_set.save()
```

#### **The Generated Output**

This is the string written to `23121-User.txt`:

```plaintext
111001:"0xH009e=0.1._0xH13de=14_0xH07d9=0_T:0xH07dd=7_d0xH07dd=13SR:0xH0076!=0":"Untouchable":"Win a race at the Monaco circuit with zero damage to your car":::progression:PyCheevos:25:::::00000
```

#### **Decoding the String**

| Python | Generated | Meaning |
| --- | --- | --- |
| `(mem_green == 0).with_hits(1)` | `0xH00009e=0.1.` | Addr 0x9e must be 0 (Hit Count: 1). |
| `mem_circuit == 14` | `0xH0013de=14` | Track ID must be 14 (Monaco). |
| `trigger(mem_event == 7)` | `T:0xH0007dd=7` | Trigger icon when Event is 7. |
| `mem_event.delta() == 13` | `d0xH0007dd=13` | Previous Event value must be 13. |
| `add_alt(...)` | `S` | Separator for Alternate Group. |
| `reset_if(~(mem_damage == 0))` | `R:0xH000076!=0` | Reset if Damage is NOT 0. |