from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet

my_set = AchievementSet(game_id=23121, title="Imported Leaderboards")

# --- LB: Fastest Race - Italy ---
lb_144627_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(0)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_144627_cancel = [
    (value(0) == value(1)),
]
lb_144627_submit = [
    (value(1) == value(1)),
]
lb_144627_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_144627 = Leaderboard(
    title="""Fastest Race - Italy""",
    description="""Best total race time on the Italian circuit.""",
    id=144627,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_144627.set_start(lb_144627_start)
lb_144627.set_cancel(lb_144627_cancel)
lb_144627.set_submit(lb_144627_submit)
lb_144627.set_value(lb_144627_value)
my_set.add_leaderboard(lb_144627)

# --- LB: Fastest Race - Great Britain ---
lb_145005_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(1)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145005_cancel = [
    (value(0) == value(1)),
]
lb_145005_submit = [
    (value(1) == value(1)),
]
lb_145005_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145005 = Leaderboard(
    title="""Fastest Race - Great Britain""",
    description="""Best total race time on the Great Britain circuit.""",
    id=145005,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145005.set_start(lb_145005_start)
lb_145005.set_cancel(lb_145005_cancel)
lb_145005.set_submit(lb_145005_submit)
lb_145005.set_value(lb_145005_value)
my_set.add_leaderboard(lb_145005)

# --- LB: Fastest Race - Germany ---
lb_145007_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(2)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145007_cancel = [
    (value(0) == value(1)),
]
lb_145007_submit = [
    (value(1) == value(1)),
]
lb_145007_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145007 = Leaderboard(
    title="""Fastest Race - Germany""",
    description="""Best total race time on the German circuit.""",
    id=145007,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145007.set_start(lb_145007_start)
lb_145007.set_cancel(lb_145007_cancel)
lb_145007.set_submit(lb_145007_submit)
lb_145007.set_value(lb_145007_value)
my_set.add_leaderboard(lb_145007)

# --- LB: Fastest Race - Brazil ---
lb_145006_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(3)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145006_cancel = [
    (value(0) == value(1)),
]
lb_145006_submit = [
    (value(1) == value(1)),
]
lb_145006_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145006 = Leaderboard(
    title="""Fastest Race - Brazil""",
    description="""Best total race time on the Brazilian circuit.""",
    id=145006,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145006.set_start(lb_145006_start)
lb_145006.set_cancel(lb_145006_cancel)
lb_145006.set_submit(lb_145006_submit)
lb_145006.set_value(lb_145006_value)
my_set.add_leaderboard(lb_145006)

# --- LB: Fastest Race - San Marino ---
lb_145008_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(4)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145008_cancel = [
    (value(0) == value(1)),
]
lb_145008_submit = [
    (value(1) == value(1)),
]
lb_145008_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145008 = Leaderboard(
    title="""Fastest Race - San Marino""",
    description="""Best total race time on the San Marino circuit.""",
    id=145008,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145008.set_start(lb_145008_start)
lb_145008.set_cancel(lb_145008_cancel)
lb_145008.set_submit(lb_145008_submit)
lb_145008.set_value(lb_145008_value)
my_set.add_leaderboard(lb_145008)

# --- LB: Fastest Race - Spain ---
lb_145009_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(5)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145009_cancel = [
    (value(0) == value(1)),
]
lb_145009_submit = [
    (value(1) == value(1)),
]
lb_145009_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145009 = Leaderboard(
    title="""Fastest Race - Spain""",
    description="""Best total race time on the Spanish circuit.""",
    id=145009,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145009.set_start(lb_145009_start)
lb_145009.set_cancel(lb_145009_cancel)
lb_145009.set_submit(lb_145009_submit)
lb_145009.set_value(lb_145009_value)
my_set.add_leaderboard(lb_145009)

# --- LB: Fastest Race - Portugal ---
lb_145010_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(6)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145010_cancel = [
    (value(0) == value(1)),
]
lb_145010_submit = [
    (value(1) == value(1)),
]
lb_145010_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145010 = Leaderboard(
    title="""Fastest Race - Portugal""",
    description="""Best total race time on the Portuguese circuit.""",
    id=145010,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145010.set_start(lb_145010_start)
lb_145010.set_cancel(lb_145010_cancel)
lb_145010.set_submit(lb_145010_submit)
lb_145010.set_value(lb_145010_value)
my_set.add_leaderboard(lb_145010)

# --- LB: Fastest Race - Mexico ---
lb_145011_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(7)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145011_cancel = [
    (value(0) == value(1)),
]
lb_145011_submit = [
    (value(1) == value(1)),
]
lb_145011_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145011 = Leaderboard(
    title="""Fastest Race - Mexico""",
    description="""Best total race time on the Mexican circuit.""",
    id=145011,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145011.set_start(lb_145011_start)
lb_145011.set_cancel(lb_145011_cancel)
lb_145011.set_submit(lb_145011_submit)
lb_145011.set_value(lb_145011_value)
my_set.add_leaderboard(lb_145011)

# --- LB: Fastest Race - Hungary ---
lb_145012_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(8)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145012_cancel = [
    (value(0) == value(1)),
]
lb_145012_submit = [
    (value(1) == value(1)),
]
lb_145012_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145012 = Leaderboard(
    title="""Fastest Race - Hungary""",
    description="""Best total race time on the Hungarian circuit.""",
    id=145012,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145012.set_start(lb_145012_start)
lb_145012.set_cancel(lb_145012_cancel)
lb_145012.set_submit(lb_145012_submit)
lb_145012.set_value(lb_145012_value)
my_set.add_leaderboard(lb_145012)

# --- LB: Fastest Race - Canada ---
lb_145013_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(9)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145013_cancel = [
    (value(0) == value(1)),
]
lb_145013_submit = [
    (value(1) == value(1)),
]
lb_145013_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145013 = Leaderboard(
    title="""Fastest Race - Canada""",
    description="""Best total race time on the Canadian circuit.""",
    id=145013,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145013.set_start(lb_145013_start)
lb_145013.set_cancel(lb_145013_cancel)
lb_145013.set_submit(lb_145013_submit)
lb_145013.set_value(lb_145013_value)
my_set.add_leaderboard(lb_145013)

# --- LB: Fastest Race - France ---
lb_145014_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(10)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145014_cancel = [
    (value(0) == value(1)),
]
lb_145014_submit = [
    (value(1) == value(1)),
]
lb_145014_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145014 = Leaderboard(
    title="""Fastest Race - France""",
    description="""Best total race time on the French circuit.""",
    id=145014,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145014.set_start(lb_145014_start)
lb_145014.set_cancel(lb_145014_cancel)
lb_145014.set_submit(lb_145014_submit)
lb_145014.set_value(lb_145014_value)
my_set.add_leaderboard(lb_145014)

# --- LB: Fastest Race - Belgium ---
lb_145015_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(11)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145015_cancel = [
    (value(0) == value(1)),
]
lb_145015_submit = [
    (value(1) == value(1)),
]
lb_145015_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145015 = Leaderboard(
    title="""Fastest Race - Belgium""",
    description="""Best total race time on the Belgian circuit.""",
    id=145015,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145015.set_start(lb_145015_start)
lb_145015.set_cancel(lb_145015_cancel)
lb_145015.set_submit(lb_145015_submit)
lb_145015.set_value(lb_145015_value)
my_set.add_leaderboard(lb_145015)

# --- LB: Fastest Race - Australia ---
lb_145016_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(12)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145016_cancel = [
    (value(0) == value(1)),
]
lb_145016_submit = [
    (value(1) == value(1)),
]
lb_145016_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145016 = Leaderboard(
    title="""Fastest Race - Australia""",
    description="""Best total race time on the Australian circuit.""",
    id=145016,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145016.set_start(lb_145016_start)
lb_145016.set_cancel(lb_145016_cancel)
lb_145016.set_submit(lb_145016_submit)
lb_145016.set_value(lb_145016_value)
my_set.add_leaderboard(lb_145016)

# --- LB: Fastest Race - USA ---
lb_145017_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(13)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145017_cancel = [
    (value(0) == value(1)),
]
lb_145017_submit = [
    (value(1) == value(1)),
]
lb_145017_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145017 = Leaderboard(
    title="""Fastest Race - USA""",
    description="""Best total race time on the USA circuit.""",
    id=145017,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145017.set_start(lb_145017_start)
lb_145017.set_cancel(lb_145017_cancel)
lb_145017.set_submit(lb_145017_submit)
lb_145017.set_value(lb_145017_value)
my_set.add_leaderboard(lb_145017)

# --- LB: Fastest Race - Monaco ---
lb_145018_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(14)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145018_cancel = [
    (value(0) == value(1)),
]
lb_145018_submit = [
    (value(1) == value(1)),
]
lb_145018_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145018 = Leaderboard(
    title="""Fastest Race - Monaco""",
    description="""Best total race time on the Monaco circuit.""",
    id=145018,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145018.set_start(lb_145018_start)
lb_145018.set_cancel(lb_145018_cancel)
lb_145018.set_submit(lb_145018_submit)
lb_145018.set_value(lb_145018_value)
my_set.add_leaderboard(lb_145018)

# --- LB: Fastest Race - Japan ---
lb_145019_start = [
    (byte(0x0007dd) == value(13)),
    (byte(0x0013de) == value(15)),
    (byte(0x0000a9) == value(4)),
    (byte(0x0000a9).delta() == value(3)),
]
lb_145019_cancel = [
    (value(0) == value(1)),
]
lb_145019_submit = [
    (value(1) == value(1)),
]
lb_145019_value = [
    add_source(byte(0x0000ad).bcd()),
    add_source(byte(0x0000ae).bcd()),
    measured(byte(0x0000b0).bcd()),
]
lb_145019 = Leaderboard(
    title="""Fastest Race - Japan""",
    description="""Best total race time on the Japanese circuit.""",
    id=145019,
    format=LeaderboardFormat.MILLISECS,
    lower_is_better=True
)
lb_145019.set_start(lb_145019_start)
lb_145019.set_cancel(lb_145019_cancel)
lb_145019.set_submit(lb_145019_submit)
lb_145019.set_value(lb_145019_value)
my_set.add_leaderboard(lb_145019)

my_set.save()