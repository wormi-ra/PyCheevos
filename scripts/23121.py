from core.helpers import *
from core.constants import *
from core.condition import Condition
from models.achievement import Achievement
from models.set import AchievementSet

my_set = AchievementSet(game_id=23121, title="Imported Set")

# --- Pole Position ---
# Logic: 0xH00009e=1_d0xH00009e=0_0xH000032=0_0xH0007dd=13
ach_555894_logic = [
    (byte(0x00009e) == value(0x1)),
    (byte(0x00009e).delta() == value(0x0)),
    (byte(0x000032) == value(0x0)),
    (byte(0x0007dd) == value(0xd)),
]
ach_555894 = Achievement(
    title="""Pole Position""",
    description="""Achieve your first Pole Position in any circuit""",
    points=1,
    id=555894
)
ach_555894.add_core(ach_555894_logic)
my_set.add_achievement(ach_555894)

# --- Pole to Win ---
# Logic: 0xH000032=0_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_555895_logic = [
    (byte(0x000032) == value(0x0)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_555895 = Achievement(
    title="""Pole to Win""",
    description="""Win a race after starting from Pole Position""",
    points=2,
    id=555895
)
ach_555895.add_core(ach_555895_logic)
my_set.add_achievement(ach_555895)

# --- First Upgrade ---
# Logic: 0xH0007dd=17Sd0xH00059b=0_0xH00059b>0Sd0xH00059c=0_0xH00059c>0Sd0xH00059d=0_0xH00059d>0Sd0xH00059e=0_0xH00059e>0Sd0xH00059f=1_0xH00059f!=1Sd0xH0005a0=1_0xH0005a0!=1Sd0xH0005a1=1_0xH0005a1!=1Sd0xH0005a3=0_0xH0005a3>0
ach_555385_logic = [
    (byte(0x0007dd) == value(0x11)),
]
ach_555385_alt1 = [
    (byte(0x00059b).delta() == value(0x0)),
    (byte(0x00059b) > value(0x0)),
]
ach_555385_alt2 = [
    (byte(0x00059c).delta() == value(0x0)),
    (byte(0x00059c) > value(0x0)),
]
ach_555385_alt3 = [
    (byte(0x00059d).delta() == value(0x0)),
    (byte(0x00059d) > value(0x0)),
]
ach_555385_alt4 = [
    (byte(0x00059e).delta() == value(0x0)),
    (byte(0x00059e) > value(0x0)),
]
ach_555385_alt5 = [
    (byte(0x00059f).delta() == value(0x1)),
    (byte(0x00059f) != value(0x1)),
]
ach_555385_alt6 = [
    (byte(0x0005a0).delta() == value(0x1)),
    (byte(0x0005a0) != value(0x1)),
]
ach_555385_alt7 = [
    (byte(0x0005a1).delta() == value(0x1)),
    (byte(0x0005a1) != value(0x1)),
]
ach_555385_alt8 = [
    (byte(0x0005a3).delta() == value(0x0)),
    (byte(0x0005a3) > value(0x0)),
]
ach_555385 = Achievement(
    title="""First Upgrade""",
    description="""Buy your first car improvement""",
    points=1,
    id=555385
)
ach_555385.add_core(ach_555385_logic)
ach_555385.add_alt(ach_555385_alt1)
ach_555385.add_alt(ach_555385_alt2)
ach_555385.add_alt(ach_555385_alt3)
ach_555385.add_alt(ach_555385_alt4)
ach_555385.add_alt(ach_555385_alt5)
ach_555385.add_alt(ach_555385_alt6)
ach_555385.add_alt(ach_555385_alt7)
ach_555385.add_alt(ach_555385_alt8)
my_set.add_achievement(ach_555385)

# --- Tifosi's Hero ---
# Logic: 0xH0013de=0_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554324_logic = [
    (byte(0x0013de) == value(0x0)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554324 = Achievement(
    title="""Tifosi's Hero""",
    description="""Win a race at the Italian circuit""",
    points=1,
    id=554324
)
ach_554324.add_core(ach_554324_logic)
my_set.add_achievement(ach_554324)

# --- Silverstone Conqueror ---
# Logic: 0xH0013de=1_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554334_logic = [
    (byte(0x0013de) == value(0x1)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554334 = Achievement(
    title="""Silverstone Conqueror""",
    description="""Win a race at the Great Britain circuit""",
    points=1,
    id=554334
)
ach_554334.add_core(ach_554334_logic)
my_set.add_achievement(ach_554334)

# --- Autobahn Ace ---
# Logic: 0xH0013de=2_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554325_logic = [
    (byte(0x0013de) == value(0x2)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554325 = Achievement(
    title="""Autobahn Ace""",
    description="""Win a race at the German circuit""",
    points=1,
    id=554325
)
ach_554325.add_core(ach_554325_logic)
my_set.add_achievement(ach_554325)

# --- Samba Victory ---
# Logic: 0xH0013de=3_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554333_logic = [
    (byte(0x0013de) == value(0x3)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554333 = Achievement(
    title="""Samba Victory""",
    description="""Win a race at the Brazilian circuit""",
    points=2,
    id=554333
)
ach_554333.add_core(ach_554333_logic)
my_set.add_achievement(ach_554333)

# --- Imola Champion ---
# Logic: 0xH0013de=4_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554329_logic = [
    (byte(0x0013de) == value(0x4)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554329 = Achievement(
    title="""Imola Champion""",
    description="""Win a race at the San Marino circuit""",
    points=1,
    id=554329
)
ach_554329.add_core(ach_554329_logic)
my_set.add_achievement(ach_554329)

# --- The Matador ---
# Logic: 0xH0013de=5_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554337_logic = [
    (byte(0x0013de) == value(0x5)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554337 = Achievement(
    title="""The Matador""",
    description="""Win a race at the Spanish circuit""",
    points=2,
    id=554337
)
ach_554337.add_core(ach_554337_logic)
my_set.add_achievement(ach_554337)

# --- Estoril Excellence ---
# Logic: 0xH0013de=6_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554327_logic = [
    (byte(0x0013de) == value(0x6)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554327 = Achievement(
    title="""Estoril Excellence""",
    description="""Win a race at the Portuguese circuit""",
    points=1,
    id=554327
)
ach_554327.add_core(ach_554327_logic)
my_set.add_achievement(ach_554327)

# --- High-Altitude Hero ---
# Logic: 0xH0013de=7_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554328_logic = [
    (byte(0x0013de) == value(0x7)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554328 = Achievement(
    title="""High-Altitude Hero""",
    description="""Win a race at the Mexican circuit""",
    points=1,
    id=554328
)
ach_554328.add_core(ach_554328_logic)
my_set.add_achievement(ach_554328)

# --- King of the Hungaroring ---
# Logic: 0xH0013de=8_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554331_logic = [
    (byte(0x0013de) == value(0x8)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554331 = Achievement(
    title="""King of the Hungaroring""",
    description="""Win a race at the Hungarian circuit""",
    points=1,
    id=554331
)
ach_554331.add_core(ach_554331_logic)
my_set.add_achievement(ach_554331)

# --- Wall of Champions ---
# Logic: 0xH0013de=9_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554339_logic = [
    (byte(0x0013de) == value(0x9)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554339 = Achievement(
    title="""Wall of Champions""",
    description="""Win a race at the Canadian circuit""",
    points=2,
    id=554339
)
ach_554339.add_core(ach_554339_logic)
my_set.add_achievement(ach_554339)

# --- Vive La Victoire! ---
# Logic: 0xH0013de=10_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554338_logic = [
    (byte(0x0013de) == value(0xa)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554338 = Achievement(
    title="""Vive La Victoire!""",
    description="""Win a race at the French circuit""",
    points=2,
    id=554338
)
ach_554338.add_core(ach_554338_logic)
my_set.add_achievement(ach_554338)

# --- Master of Eau Rouge ---
# Logic: 0xH0013de=11_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554332_logic = [
    (byte(0x0013de) == value(0xb)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554332 = Achievement(
    title="""Master of Eau Rouge""",
    description="""Win a race at the Belgian circuit""",
    points=2,
    id=554332
)
ach_554332.add_core(ach_554332_logic)
my_set.add_achievement(ach_554332)

# --- Down Under Dominator ---
# Logic: 0xH0013de=12_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554326_logic = [
    (byte(0x0013de) == value(0xc)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554326 = Achievement(
    title="""Down Under Dominator""",
    description="""Win a race at the Australian circuit""",
    points=2,
    id=554326
)
ach_554326.add_core(ach_554326_logic)
my_set.add_achievement(ach_554326)

# --- The American Dream ---
# Logic: 0xH0013de=13_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554336_logic = [
    (byte(0x0013de) == value(0xd)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554336 = Achievement(
    title="""The American Dream""",
    description="""Win a race at the USA circuit""",
    points=1,
    id=554336
)
ach_554336.add_core(ach_554336_logic)
my_set.add_achievement(ach_554336)

# --- Jewel in the Crown ---
# Logic: 0xH0013de=14_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554330_logic = [
    (byte(0x0013de) == value(0xe)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554330 = Achievement(
    title="""Jewel in the Crown""",
    description="""Win a race at the Monaco circuit""",
    points=2,
    id=554330
)
ach_554330.add_core(ach_554330_logic)
my_set.add_achievement(ach_554330)

# --- Suzuka Samurai ---
# Logic: 0xH0013de=15_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554335_logic = [
    (byte(0x0013de) == value(0xf)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_554335 = Achievement(
    title="""Suzuka Samurai""",
    description="""Win a race at the Japanese circuit""",
    points=2,
    id=554335
)
ach_554335.add_core(ach_554335_logic)
my_set.add_achievement(ach_554335)

# --- Capital Injection ---
# Logic: 0x 0013e2=1000_d0x 0013e2<1000_0xH001468=0_d0xH0007dd=16
ach_555198_logic = [
    (word(0x0013e2) == value(0x3e8)),
    (word(0x0013e2).delta() < value(0x3e8)),
    (byte(0x001468) == value(0x0)),
    (byte(0x0007dd).delta() == value(0x10)),
]
ach_555198 = Achievement(
    title="""Capital Injection""",
    description="""Start the game with a $10,000 bonus""",
    points=1,
    id=555198
)
ach_555198.add_core(ach_555198_logic)
my_set.add_achievement(ach_555198)

# --- Chief Engineer: Chassis ---
# Logic: 0xH00059b=2_d0xH00059b<2_0xH0007dd=17
ach_555219_logic = [
    (byte(0x00059b) == value(0x2)),
    (byte(0x00059b).delta() < value(0x2)),
    (byte(0x0007dd) == value(0x11)),
]
ach_555219 = Achievement(
    title="""Chief Engineer: Chassis""",
    description="""Purchase the Type 3 chassis upgrade""",
    points=5,
    id=555219
)
ach_555219.add_core(ach_555219_logic)
my_set.add_achievement(ach_555219)

# --- Chief Engineer: Gearing ---
# Logic: 0xH00059c=3_d0xH00059c<3_0xH0007dd=17
ach_555218_logic = [
    (byte(0x00059c) == value(0x3)),
    (byte(0x00059c).delta() < value(0x3)),
    (byte(0x0007dd) == value(0x11)),
]
ach_555218 = Achievement(
    title="""Chief Engineer: Gearing""",
    description="""Purchase the 7Speed transmission upgrade""",
    points=2,
    id=555218
)
ach_555218.add_core(ach_555218_logic)
my_set.add_achievement(ach_555218)

# --- Chief Engineer: Brakes ---
# Logic: 0xH00059d=2_d0xH00059d<2_0xH0007dd=17
ach_555217_logic = [
    (byte(0x00059d) == value(0x2)),
    (byte(0x00059d).delta() < value(0x2)),
    (byte(0x0007dd) == value(0x11)),
]
ach_555217 = Achievement(
    title="""Chief Engineer: Brakes""",
    description="""Purchase the Antilock brake upgrade""",
    points=2,
    id=555217
)
ach_555217.add_core(ach_555217_logic)
my_set.add_achievement(ach_555217)

# --- Chief Engineer: Suspension ---
# Logic: 0xH00059e=2_d0xH00059e<2_0xH0007dd=17
ach_555216_logic = [
    (byte(0x00059e) == value(0x2)),
    (byte(0x00059e).delta() < value(0x2)),
    (byte(0x0007dd) == value(0x11)),
]
ach_555216 = Achievement(
    title="""Chief Engineer: Suspension""",
    description="""Purchase the Active suspension upgrade""",
    points=1,
    id=555216
)
ach_555216.add_core(ach_555216_logic)
my_set.add_achievement(ach_555216)

# --- Chief Engineer: Diffuser ---
# Logic: 0xH00059f=3_d0xH00059f<3_0xH0007dd=17
ach_555215_logic = [
    (byte(0x00059f) == value(0x3)),
    (byte(0x00059f).delta() < value(0x3)),
    (byte(0x0007dd) == value(0x11)),
]
ach_555215 = Achievement(
    title="""Chief Engineer: Diffuser""",
    description="""Purchase the Special Diffuser upgrade""",
    points=2,
    id=555215
)
ach_555215.add_core(ach_555215_logic)
my_set.add_achievement(ach_555215)

# --- Chief Engineer: Rear Wing ---
# Logic: 0xH0005a1=2_d0xH0005a1<2_0xH0007dd=17
ach_555213_logic = [
    (byte(0x0005a1) == value(0x2)),
    (byte(0x0005a1).delta() < value(0x2)),
    (byte(0x0007dd) == value(0x11)),
]
ach_555213 = Achievement(
    title="""Chief Engineer: Rear Wing""",
    description="""Purchase the HI D.F Rear Wing upgrade""",
    points=5,
    id=555213
)
ach_555213.add_core(ach_555213_logic)
my_set.add_achievement(ach_555213)

# --- Chief Engineer: Front Wing ---
# Logic: 0xH0007dd=17_0xH0005a0=4_d0xH0005a0<4
ach_555214_logic = [
    (byte(0x0007dd) == value(0x11)),
    (byte(0x0005a0) == value(0x4)),
    (byte(0x0005a0).delta() < value(0x4)),
]
ach_555214 = Achievement(
    title="""Chief Engineer: Front Wing""",
    description="""Purchase the SPECIAL.W Front Wing upgrade""",
    points=2,
    id=555214
)
ach_555214.add_core(ach_555214_logic)
my_set.add_achievement(ach_555214)

# --- Chief Engineer: Tires ---
# Logic: 0xH0007dd=17_0xH0005a2=4_d0xH0005a2<4
ach_555212_logic = [
    (byte(0x0007dd) == value(0x11)),
    (byte(0x0005a2) == value(0x4)),
    (byte(0x0005a2).delta() < value(0x4)),
]
ach_555212 = Achievement(
    title="""Chief Engineer: Tires""",
    description="""Purchase the Special Tires upgrade""",
    points=1,
    id=555212
)
ach_555212.add_core(ach_555212_logic)
my_set.add_achievement(ach_555212)

# --- Chief Engineer: Engine ---
# Logic: 0xH0007dd=17_0xH0005a3=5_d0xH0005a3<5
ach_555211_logic = [
    (byte(0x0007dd) == value(0x11)),
    (byte(0x0005a3) == value(0x5)),
    (byte(0x0005a3).delta() < value(0x5)),
]
ach_555211 = Achievement(
    title="""Chief Engineer: Engine""",
    description="""Purchase the Homda V12 engine upgrade""",
    points=5,
    id=555211
)
ach_555211.add_core(ach_555211_logic)
my_set.add_achievement(ach_555211)

# --- Back of the Pack ---
# Logic: 0xH000039=0_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_555909_logic = [
    (byte(0x000039) == value(0x0)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_555909 = Achievement(
    title="""Back of the Pack""",
    description="""Win a race after starting from 8th place""",
    points=10,
    id=555909
)
ach_555909.add_core(ach_555909_logic)
my_set.add_achievement(ach_555909)

# --- Interlagos Rain Master ---
# Logic: 0xH0013de=3_0xH0013e0>0_0xH0007d9=0_T:0xH0007dd=7_0xH0007dd!=14_d0xH0007dd=13
ach_556004_logic = [
    (byte(0x0013de) == value(0x3)),
    (byte(0x0013e0) > value(0x0)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)).with_flag(trigger),
    (byte(0x0007dd) != value(0xe)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_556004 = Achievement(
    title="""Interlagos Rain Master""",
    description="""Win a race in rainy conditions at the Brazilian circuit""",
    points=10,
    id=556004
)
ach_556004.add_core(ach_556004_logic)
my_set.add_achievement(ach_556004)

# --- Dancing in the Rain ---
# Logic: 0xH0007d9=0_0xH0005a2=1_0xH0013e0>0_T:0xH0007dd=7_0xH0007dd!=14_0xH0007dd!=17_d0xH0007dd=13
ach_555222_logic = [
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0005a2) == value(0x1)),
    (byte(0x0013e0) > value(0x0)),
    (byte(0x0007dd) == value(0x7)).with_flag(trigger),
    (byte(0x0007dd) != value(0xe)),
    (byte(0x0007dd) != value(0x11)),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_555222 = Achievement(
    title="""Dancing in the Rain""",
    description="""Win any race in wet conditions after equipping RAIN tires""",
    points=2,
    id=555222
)
ach_555222.add_core(ach_555222_logic)
my_set.add_achievement(ach_555222)

# --- Untouchable ---
# Logic: 0xH00009e=1.1._0xH0013de=14_0xH0007d9=0_T:0xH0007dd=7_d0xH0007dd=13SR:0xH000076>0
ach_555221_logic = [
    (byte(0x00009e) == value(0x1)).with_hits(1),
    (byte(0x0013de) == value(0xe)),
    (byte(0x0007d9) == value(0x0)),
    (byte(0x0007dd) == value(0x7)).with_flag(trigger),
    (byte(0x0007dd).delta() == value(0xd)),
]
ach_555221_alt1 = [
    (byte(0x000076) > value(0x0)).with_flag(reset_if),
]
ach_555221 = Achievement(
    title="""Untouchable""",
    description="""Win a race at the Monaco circuit with zero damage to your car""",
    points=25,
    id=555221
)
ach_555221.add_core(ach_555221_logic)
ach_555221.add_alt(ach_555221_alt1)
my_set.add_achievement(ach_555221)

# --- Monaco Jackpot ---
# Logic: 0xH0007dd=10_0xH0013e8=67_0xH0013e9=65_0xH0013ea=83_0xH0013eb=73_0xH0013ec=78_0xH0013ed=79_0xH0006d0=5_d0xH0007dd=10
ach_555203_logic = [
    (byte(0x0007dd) == value(0xa)),
    (byte(0x0013e8) == value(0x43)),
    (byte(0x0013e9) == value(0x41)),
    (byte(0x0013ea) == value(0x53)),
    (byte(0x0013eb) == value(0x49)),
    (byte(0x0013ec) == value(0x4e)),
    (byte(0x0013ed) == value(0x4f)),
    (byte(0x0006d0) == value(0x5)),
    (byte(0x0007dd).delta() == value(0xa)),
]
ach_555203 = Achievement(
    title="""Monaco Jackpot""",
    description="""Discover and play the secret slot machine minigame in Monaco""",
    points=1,
    id=555203
)
ach_555203.add_core(ach_555203_logic)
my_set.add_achievement(ach_555203)

# --- [VOID]Big Luck 777 ---
# Logic: 0xH0007dd=10_0xH001222=244_0xH001223=240_0xH001224=240_0xH001225=240_d0xH001222!=244
ach_563375_logic = [
    (byte(0x0007dd) == value(0xa)),
    (byte(0x001222) == value(0xf4)),
    (byte(0x001223) == value(0xf0)),
    (byte(0x001224) == value(0xf0)),
    (byte(0x001225) == value(0xf0)),
    (byte(0x001222).delta() != value(0xf4)),
]
ach_563375 = Achievement(
    title="""[VOID]Big Luck 777""",
    description="""Win the top prize Jackpot of 4000 on the slot machine in Monaco""",
    points=10,
    id=563375
)
ach_563375.add_core(ach_563375_logic)
my_set.add_achievement(ach_563375)

# --- The Perfect Machine ---
# Logic: 0xH0005a3=5_0xH0005a2=4_0xH0005a1=2_0xH0005a0=4_0xH00059f=3_0xH00059e=2_0xH00059d=2_0xH00059c=3_0xH00059b=2_d0xH0007dd=17SQ:0xH0007dd=17_R:0xH0007dd!=17_C:0xH0005a3=5.1._C:0xH0005a2=4.1._C:0xH0005a1=2.1._C:0xH0005a0=4.1._C:0xH00059f=3.1._C:0xH00059e=2.1._C:0xH00059d=2.1._C:0xH00059c=3.1._C:0xH00059b=2.1._M:0=1.9.
ach_555220_logic = [
    (byte(0x0005a3) == value(0x5)),
    (byte(0x0005a2) == value(0x4)),
    (byte(0x0005a1) == value(0x2)),
    (byte(0x0005a0) == value(0x4)),
    (byte(0x00059f) == value(0x3)),
    (byte(0x00059e) == value(0x2)),
    (byte(0x00059d) == value(0x2)),
    (byte(0x00059c) == value(0x3)),
    (byte(0x00059b) == value(0x2)),
    (byte(0x0007dd).delta() == value(0x11)),
]
ach_555220_alt1 = [
    (byte(0x0007dd) == value(0x11)).with_flag(measured_if),
    (byte(0x0007dd) != value(0x11)).with_flag(reset_if),
    (byte(0x0005a3) == value(0x5)).with_flag(add_hits).with_hits(1),
    (byte(0x0005a2) == value(0x4)).with_flag(add_hits).with_hits(1),
    (byte(0x0005a1) == value(0x2)).with_flag(add_hits).with_hits(1),
    (byte(0x0005a0) == value(0x4)).with_flag(add_hits).with_hits(1),
    (byte(0x00059f) == value(0x3)).with_flag(add_hits).with_hits(1),
    (byte(0x00059e) == value(0x2)).with_flag(add_hits).with_hits(1),
    (byte(0x00059d) == value(0x2)).with_flag(add_hits).with_hits(1),
    (byte(0x00059c) == value(0x3)).with_flag(add_hits).with_hits(1),
    (byte(0x00059b) == value(0x2)).with_flag(add_hits).with_hits(1),
    Condition(value(0x0), '==', value(0x1)).with_flag(measured).with_hits(9),
]
ach_555220 = Achievement(
    title="""The Perfect Machine""",
    description="""Purchase all available upgrades for an F1 car""",
    points=25,
    id=555220
)
ach_555220.add_core(ach_555220_logic)
ach_555220.add_alt(ach_555220_alt1)
my_set.add_achievement(ach_555220)

# --- The Dream Comes True ---
# Logic: 0xH0000a3=32_d0xH0000a3!=32_0xH0000a4=144_0xH0000a5=29_0xH0013de=15_0xH001390=0
ach_555915_logic = [
    (byte(0x0000a3) == value(0x20)),
    (byte(0x0000a3).delta() != value(0x20)),
    (byte(0x0000a4) == value(0x90)),
    (byte(0x0000a5) == value(0x1d)),
    (byte(0x0013de) == value(0xf)),
    (byte(0x001390) == value(0x0)),
]
ach_555915 = Achievement(
    title="""The Dream Comes True""",
    description="""Win the F1 World Championship for the first time""",
    points=25,
    id=555915
)
ach_555915.add_core(ach_555915_logic)
my_set.add_achievement(ach_555915)

# --- Perfect Season ---
# Logic: 0xH001468=160_0xH0000a3=237_0xH0000a4=231_0xH0000a5=31_d0xH0000a3!=237
ach_555384_logic = [
    (byte(0x001468) == value(0xa0)),
    (byte(0x0000a3) == value(0xed)),
    (byte(0x0000a4) == value(0xe7)),
    (byte(0x0000a5) == value(0x1f)),
    (byte(0x0000a3).delta() != value(0xed)),
]
ach_555384 = Achievement(
    title="""Perfect Season""",
    description="""Win every single race in a full F1 season""",
    points=50,
    id=555384
)
ach_555384.add_core(ach_555384_logic)
my_set.add_achievement(ach_555384)

# --- [VOID] Legend of the Asphalt ---
# Logic: 0xH0013e6=2
ach_555916_logic = [
    (byte(0x0013e6) == value(0x2)),
]
ach_555916 = Achievement(
    title="""[VOID] Legend of the Asphalt""",
    description="""Win back-to-back Formula 1 World Championships""",
    points=0,
    id=555916
)
ach_555916.add_core(ach_555916_logic)
my_set.add_achievement(ach_555916)
my_set.save()