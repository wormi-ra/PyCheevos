from pycheevos.core.helpers import *
from pycheevos.core.constants import *
from pycheevos.core.condition import Condition
from pycheevos.models.achievement import Achievement
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet
from notes_23121 import *

my_set = AchievementSet(game_id=23121, title="Imported Set")

# --- Pole Position ---
# Logic: 0xH00009e=1_d0xH00009e=0_0xH000032=0_0xH0007dd=13
ach_555894_logic = [
    (starting_grid_semaphore___cutscene == 0x01),
    (starting_grid_semaphore___cutscene.delta() == 0x00),
    (qualifying_grid_position_block == 0x00),
    (game_state___current_screen == 0x0d),
]
ach_555894 = Achievement(
    title="""Pole Position""",
    description="""Achieve your first Pole Position in any circuit""",
    points=1, type=AchievementType.PROGRESSION,
    id=555894, badge="640254"
)
ach_555894.add_core(ach_555894_logic)
my_set.add_achievement(ach_555894)

# --- Pole to Win ---
# Logic: 0xH000032=0_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_555895_logic = [
    (qualifying_grid_position_block == 0x00),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_555895 = Achievement(
    title="""Pole to Win""",
    description="""Win a race after starting from Pole Position""",
    points=2, type=AchievementType.PROGRESSION,
    id=555895, badge="640435"
)
ach_555895.add_core(ach_555895_logic)
my_set.add_achievement(ach_555895)

# --- First Upgrade ---
# Logic: 0xH0007dd=17Sd0xH00059b=0_0xH00059b>0Sd0xH00059c=0_0xH00059c>0Sd0xH00059d=0_0xH00059d>0Sd0xH00059e=0_0xH00059e>0Sd0xH00059f=1_0xH00059f!=1Sd0xH0005a0=1_0xH0005a0!=1Sd0xH0005a1=1_0xH0005a1!=1Sd0xH0005a3=0_0xH0005a3>0
ach_555385_logic = [
    (game_state___current_screen == 0x11),
]
ach_555385_alt1 = [
    (player_car_upgrade_levels_block.delta() == 0x00),
    (player_car_upgrade_levels_block > 0x00),
]
ach_555385_alt2 = [
    (player_car_upgrade_levels_block_2.delta() == 0x00),
    (player_car_upgrade_levels_block_2 > 0x00),
]
ach_555385_alt3 = [
    (player_car_upgrade_levels_block_3.delta() == 0x00),
    (player_car_upgrade_levels_block_3 > 0x00),
]
ach_555385_alt4 = [
    (player_car_upgrade_levels_block_4.delta() == 0x00),
    (player_car_upgrade_levels_block_4 > 0x00),
]
ach_555385_alt5 = [
    (player_car_upgrade_levels_block_5.delta() == 0x01),
    (player_car_upgrade_levels_block_5 != 0x01),
]
ach_555385_alt6 = [
    (player_car_upgrade_levels_block_6.delta() == 0x01),
    (player_car_upgrade_levels_block_6 != 0x01),
]
ach_555385_alt7 = [
    (player_car_upgrade_levels_block_7.delta() == 0x01),
    (player_car_upgrade_levels_block_7 != 0x01),
]
ach_555385_alt8 = [
    (player_car_upgrade_levels_block_9.delta() == 0x00),
    (player_car_upgrade_levels_block_9 > 0x00),
]
ach_555385 = Achievement(
    title="""First Upgrade""",
    description="""Buy your first car improvement""",
    points=1,
    id=555385, badge="640396"
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
    (current_circuit == 0x00),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554324 = Achievement(
    title="""Tifosi's Hero""",
    description="""Win a race at the Italian circuit""",
    points=1,
    id=554324, badge="640397"
)
ach_554324.add_core(ach_554324_logic)
my_set.add_achievement(ach_554324)

# --- Silverstone Conqueror ---
# Logic: 0xH0013de=1_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554334_logic = [
    (current_circuit == 0x01),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554334 = Achievement(
    title="""Silverstone Conqueror""",
    description="""Win a race at the Great Britain circuit""",
    points=1,
    id=554334, badge="640398"
)
ach_554334.add_core(ach_554334_logic)
my_set.add_achievement(ach_554334)

# --- Autobahn Ace ---
# Logic: 0xH0013de=2_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554325_logic = [
    (current_circuit == 0x02),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554325 = Achievement(
    title="""Autobahn Ace""",
    description="""Win a race at the German circuit""",
    points=1,
    id=554325, badge="640399"
)
ach_554325.add_core(ach_554325_logic)
my_set.add_achievement(ach_554325)

# --- Samba Victory ---
# Logic: 0xH0013de=3_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554333_logic = [
    (current_circuit == 0x03),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554333 = Achievement(
    title="""Samba Victory""",
    description="""Win a race at the Brazilian circuit""",
    points=2,
    id=554333, badge="640400"
)
ach_554333.add_core(ach_554333_logic)
my_set.add_achievement(ach_554333)

# --- Imola Champion ---
# Logic: 0xH0013de=4_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554329_logic = [
    (current_circuit == 0x04),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554329 = Achievement(
    title="""Imola Champion""",
    description="""Win a race at the San Marino circuit""",
    points=1,
    id=554329, badge="640401"
)
ach_554329.add_core(ach_554329_logic)
my_set.add_achievement(ach_554329)

# --- The Matador ---
# Logic: 0xH0013de=5_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554337_logic = [
    (current_circuit == 0x05),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554337 = Achievement(
    title="""The Matador""",
    description="""Win a race at the Spanish circuit""",
    points=2,
    id=554337, badge="640402"
)
ach_554337.add_core(ach_554337_logic)
my_set.add_achievement(ach_554337)

# --- Estoril Excellence ---
# Logic: 0xH0013de=6_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554327_logic = [
    (current_circuit == 0x06),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554327 = Achievement(
    title="""Estoril Excellence""",
    description="""Win a race at the Portuguese circuit""",
    points=1,
    id=554327, badge="640403"
)
ach_554327.add_core(ach_554327_logic)
my_set.add_achievement(ach_554327)

# --- High-Altitude Hero ---
# Logic: 0xH0013de=7_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554328_logic = [
    (current_circuit == 0x07),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554328 = Achievement(
    title="""High-Altitude Hero""",
    description="""Win a race at the Mexican circuit""",
    points=1,
    id=554328, badge="640404"
)
ach_554328.add_core(ach_554328_logic)
my_set.add_achievement(ach_554328)

# --- King of the Hungaroring ---
# Logic: 0xH0013de=8_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554331_logic = [
    (current_circuit == 0x08),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554331 = Achievement(
    title="""King of the Hungaroring""",
    description="""Win a race at the Hungarian circuit""",
    points=1,
    id=554331, badge="640405"
)
ach_554331.add_core(ach_554331_logic)
my_set.add_achievement(ach_554331)

# --- Wall of Champions ---
# Logic: 0xH0013de=9_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554339_logic = [
    (current_circuit == 0x09),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554339 = Achievement(
    title="""Wall of Champions""",
    description="""Win a race at the Canadian circuit""",
    points=2,
    id=554339, badge="640406"
)
ach_554339.add_core(ach_554339_logic)
my_set.add_achievement(ach_554339)

# --- Vive La Victoire! ---
# Logic: 0xH0013de=10_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554338_logic = [
    (current_circuit == 0x0a),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554338 = Achievement(
    title="""Vive La Victoire!""",
    description="""Win a race at the French circuit""",
    points=2,
    id=554338, badge="640407"
)
ach_554338.add_core(ach_554338_logic)
my_set.add_achievement(ach_554338)

# --- Master of Eau Rouge ---
# Logic: 0xH0013de=11_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554332_logic = [
    (current_circuit == 0x0b),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554332 = Achievement(
    title="""Master of Eau Rouge""",
    description="""Win a race at the Belgian circuit""",
    points=2,
    id=554332, badge="640408"
)
ach_554332.add_core(ach_554332_logic)
my_set.add_achievement(ach_554332)

# --- Down Under Dominator ---
# Logic: 0xH0013de=12_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554326_logic = [
    (current_circuit == 0x0c),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554326 = Achievement(
    title="""Down Under Dominator""",
    description="""Win a race at the Australian circuit""",
    points=2,
    id=554326, badge="640409"
)
ach_554326.add_core(ach_554326_logic)
my_set.add_achievement(ach_554326)

# --- The American Dream ---
# Logic: 0xH0013de=13_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554336_logic = [
    (current_circuit == 0x0d),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554336 = Achievement(
    title="""The American Dream""",
    description="""Win a race at the USA circuit""",
    points=1,
    id=554336, badge="640410"
)
ach_554336.add_core(ach_554336_logic)
my_set.add_achievement(ach_554336)

# --- Jewel in the Crown ---
# Logic: 0xH0013de=14_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554330_logic = [
    (current_circuit == 0x0e),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554330 = Achievement(
    title="""Jewel in the Crown""",
    description="""Win a race at the Monaco circuit""",
    points=2,
    id=554330, badge="640411"
)
ach_554330.add_core(ach_554330_logic)
my_set.add_achievement(ach_554330)

# --- Suzuka Samurai ---
# Logic: 0xH0013de=15_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_554335_logic = [
    (current_circuit == 0x0f),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_554335 = Achievement(
    title="""Suzuka Samurai""",
    description="""Win a race at the Japanese circuit""",
    points=2,
    id=554335, badge="640412"
)
ach_554335.add_core(ach_554335_logic)
my_set.add_achievement(ach_554335)

# --- Capital Injection ---
# Logic: 0x 0013e2=1000_d0x 0013e2<1000_0xH001468=0_d0xH0007dd=16
ach_555198_logic = [
    (total_player_money == 0x3e8),
    (total_player_money.delta() < 0x3e8),
    (championship_points == 0x00),
    (game_state___current_screen.delta() == 0x10),
]
ach_555198 = Achievement(
    title="""Capital Injection""",
    description="""Start the game with a $10,000 bonus""",
    points=1, type=AchievementType.MISSABLE,
    id=555198, badge="640413"
)
ach_555198.add_core(ach_555198_logic)
my_set.add_achievement(ach_555198)

# --- Chief Engineer: Chassis ---
# Logic: 0xH00059b=2_d0xH00059b<2_0xH0007dd=17
ach_555219_logic = [
    (player_car_upgrade_levels_block == 0x02),
    (player_car_upgrade_levels_block.delta() < 0x02),
    (game_state___current_screen == 0x11),
]
ach_555219 = Achievement(
    title="""Chief Engineer: Chassis""",
    description="""Purchase the Type 3 chassis upgrade""",
    points=5,
    id=555219, badge="640414"
)
ach_555219.add_core(ach_555219_logic)
my_set.add_achievement(ach_555219)

# --- Chief Engineer: Gearing ---
# Logic: 0xH00059c=3_d0xH00059c<3_0xH0007dd=17
ach_555218_logic = [
    (player_car_upgrade_levels_block_2 == 0x03),
    (player_car_upgrade_levels_block_2.delta() < 0x03),
    (game_state___current_screen == 0x11),
]
ach_555218 = Achievement(
    title="""Chief Engineer: Gearing""",
    description="""Purchase the 7Speed transmission upgrade""",
    points=2,
    id=555218, badge="640415"
)
ach_555218.add_core(ach_555218_logic)
my_set.add_achievement(ach_555218)

# --- Chief Engineer: Brakes ---
# Logic: 0xH00059d=2_d0xH00059d<2_0xH0007dd=17
ach_555217_logic = [
    (player_car_upgrade_levels_block_3 == 0x02),
    (player_car_upgrade_levels_block_3.delta() < 0x02),
    (game_state___current_screen == 0x11),
]
ach_555217 = Achievement(
    title="""Chief Engineer: Brakes""",
    description="""Purchase the Antilock brake upgrade""",
    points=2,
    id=555217, badge="640416"
)
ach_555217.add_core(ach_555217_logic)
my_set.add_achievement(ach_555217)

# --- Chief Engineer: Suspension ---
# Logic: 0xH00059e=2_d0xH00059e<2_0xH0007dd=17
ach_555216_logic = [
    (player_car_upgrade_levels_block_4 == 0x02),
    (player_car_upgrade_levels_block_4.delta() < 0x02),
    (game_state___current_screen == 0x11),
]
ach_555216 = Achievement(
    title="""Chief Engineer: Suspension""",
    description="""Purchase the Active suspension upgrade""",
    points=1,
    id=555216, badge="640417"
)
ach_555216.add_core(ach_555216_logic)
my_set.add_achievement(ach_555216)

# --- Chief Engineer: Diffuser ---
# Logic: 0xH00059f=3_d0xH00059f<3_0xH0007dd=17
ach_555215_logic = [
    (player_car_upgrade_levels_block_5 == 0x03),
    (player_car_upgrade_levels_block_5.delta() < 0x03),
    (game_state___current_screen == 0x11),
]
ach_555215 = Achievement(
    title="""Chief Engineer: Diffuser""",
    description="""Purchase the Special Diffuser upgrade""",
    points=2,
    id=555215, badge="640418"
)
ach_555215.add_core(ach_555215_logic)
my_set.add_achievement(ach_555215)

# --- Chief Engineer: Rear Wing ---
# Logic: 0xH0005a1=2_d0xH0005a1<2_0xH0007dd=17
ach_555213_logic = [
    (player_car_upgrade_levels_block_7 == 0x02),
    (player_car_upgrade_levels_block_7.delta() < 0x02),
    (game_state___current_screen == 0x11),
]
ach_555213 = Achievement(
    title="""Chief Engineer: Rear Wing""",
    description="""Purchase the HI D.F Rear Wing upgrade""",
    points=5,
    id=555213, badge="640419"
)
ach_555213.add_core(ach_555213_logic)
my_set.add_achievement(ach_555213)

# --- Chief Engineer: Front Wing ---
# Logic: 0xH0007dd=17_0xH0005a0=4_d0xH0005a0<4
ach_555214_logic = [
    (game_state___current_screen == 0x11),
    (player_car_upgrade_levels_block_6 == 0x04),
    (player_car_upgrade_levels_block_6.delta() < 0x04),
]
ach_555214 = Achievement(
    title="""Chief Engineer: Front Wing""",
    description="""Purchase the SPECIAL.W Front Wing upgrade""",
    points=2,
    id=555214, badge="640420"
)
ach_555214.add_core(ach_555214_logic)
my_set.add_achievement(ach_555214)

# --- Chief Engineer: Tires ---
# Logic: 0xH0007dd=17_0xH0005a2=4_d0xH0005a2<4
ach_555212_logic = [
    (game_state___current_screen == 0x11),
    (player_car_upgrade_levels_block_8 == 0x04),
    (player_car_upgrade_levels_block_8.delta() < 0x04),
]
ach_555212 = Achievement(
    title="""Chief Engineer: Tires""",
    description="""Purchase the Special Tires upgrade""",
    points=1,
    id=555212, badge="640421"
)
ach_555212.add_core(ach_555212_logic)
my_set.add_achievement(ach_555212)

# --- Chief Engineer: Engine ---
# Logic: 0xH0007dd=17_0xH0005a3=5_d0xH0005a3<5
ach_555211_logic = [
    (game_state___current_screen == 0x11),
    (player_car_upgrade_levels_block_9 == 0x05),
    (player_car_upgrade_levels_block_9.delta() < 0x05),
]
ach_555211 = Achievement(
    title="""Chief Engineer: Engine""",
    description="""Purchase the Homda V12 engine upgrade""",
    points=5,
    id=555211, badge="640422"
)
ach_555211.add_core(ach_555211_logic)
my_set.add_achievement(ach_555211)

# --- Back of the Pack ---
# Logic: 0xH000039=0_0xH0007d9=0_0xH0007dd=7_d0xH0007dd=13
ach_555909_logic = [
    (value_holds_id_of_driver_starting_in_8th_place == 0x00),
    (player_race_position == 0x00),
    (game_state___current_screen == 0x07),
    (game_state___current_screen.delta() == 0x0d),
]
ach_555909 = Achievement(
    title="""Back of the Pack""",
    description="""Win a race after starting from 8th place""",
    points=10,
    id=555909, badge="640423"
)
ach_555909.add_core(ach_555909_logic)
my_set.add_achievement(ach_555909)

# --- Interlagos Rain Master ---
# Logic: 0xH0013de=3_0xH0013e0>0_0xH0007d9=0_T:0xH0007dd=7_0xH0007dd!=14_d0xH0007dd=13
ach_556004_logic = [
    (current_circuit == 0x03),
    (current_weather_condition > 0x00),
    (player_race_position == 0x00),
    trigger((game_state___current_screen == 0x07)),
    (game_state___current_screen != 0x0e),
    (game_state___current_screen.delta() == 0x0d),
]
ach_556004 = Achievement(
    title="""Interlagos Rain Master""",
    description="""Win a race in rainy conditions at the Brazilian circuit""",
    points=10,
    id=556004, badge="640424"
)
ach_556004.add_core(ach_556004_logic)
my_set.add_achievement(ach_556004)

# --- Dancing in the Rain ---
# Logic: 0xH0007d9=0_0xH0005a2=1_0xH0013e0>0_T:0xH0007dd=7_0xH0007dd!=14_0xH0007dd!=17_d0xH0007dd=13
ach_555222_logic = [
    (player_race_position == 0x00),
    (player_car_upgrade_levels_block_8 == 0x01),
    (current_weather_condition > 0x00),
    trigger((game_state___current_screen == 0x07)),
    (game_state___current_screen != 0x0e),
    (game_state___current_screen != 0x11),
    (game_state___current_screen.delta() == 0x0d),
]
ach_555222 = Achievement(
    title="""Dancing in the Rain""",
    description="""Win any race in wet conditions after equipping RAIN tires""",
    points=2,
    id=555222, badge="640425"
)
ach_555222.add_core(ach_555222_logic)
my_set.add_achievement(ach_555222)

# --- Untouchable ---
# Logic: 0xH00009e=1.1._0xH0013de=14_0xH0007d9=0_T:0xH0007dd=7_d0xH0007dd=13SR:0xH000076>0
ach_555221_logic = [
    (starting_grid_semaphore___cutscene == 0x01).with_hits(1),
    (current_circuit == 0x0e),
    (player_race_position == 0x00),
    trigger((game_state___current_screen == 0x07)),
    (game_state___current_screen.delta() == 0x0d),
]
ach_555221_alt1 = [
    reset_if((car_damage > 0x00)),
]
ach_555221 = Achievement(
    title="""Untouchable""",
    description="""Win a race at the Monaco circuit with zero damage to your car""",
    points=25,
    id=555221, badge="640426"
)
ach_555221.add_core(ach_555221_logic)
ach_555221.add_alt(ach_555221_alt1)
my_set.add_achievement(ach_555221)

# --- Monaco Jackpot ---
# Logic: 0xH0007dd=10_0xH0013e8=67_0xH0013e9=65_0xH0013ea=83_0xH0013eb=73_0xH0013ec=78_0xH0013ed=79_0xH0006d0=5_d0xH0007dd=10
ach_555203_logic = [
    (game_state___current_screen == 0x0a),
    (active_player_name___char_1 == 0x43),
    (active_player_name___char_2 == 0x41),
    (active_player_name___char_3 == 0x53),
    (active_player_name___char_4 == 0x49),
    (active_player_name___char_5 == 0x4e),
    (active_player_name___char_6 == 0x4f),
    (casino_minigame___roulette_selector == 0x05),
    (game_state___current_screen.delta() == 0x0a),
]
ach_555203 = Achievement(
    title="""Monaco Jackpot""",
    description="""Discover and play the secret slot machine minigame in Monaco""",
    points=1, type=AchievementType.MISSABLE,
    id=555203, badge="640427"
)
ach_555203.add_core(ach_555203_logic)
my_set.add_achievement(ach_555203)

# --- [VOID]Big Luck 777 ---
# Logic: 0xH0007dd=10_0xH001222=244_0xH001223=240_0xH001224=240_0xH001225=240_d0xH001222!=244
ach_563375_logic = [
    (game_state___current_screen == 0x0a),
    (casino_win_display___thousands == 0xf4),
    (casino_win_display___hundreds == 0xf0),
    (casino_win_display___tens == 0xf0),
    (casino_win_display___units == 0xf0),
    (casino_win_display___thousands.delta() != 0xf4),
]
ach_563375 = Achievement(
    title="""[VOID]Big Luck 777""",
    description="""Win the top prize Jackpot of 4000 on the slot machine in Monaco""",
    points=10,
    id=563375, badge="640431"
)
ach_563375.add_core(ach_563375_logic)
my_set.add_achievement(ach_563375)

# --- The Perfect Machine ---
# Logic: 0xH0005a3=5_0xH0005a2=4_0xH0005a1=2_0xH0005a0=4_0xH00059f=3_0xH00059e=2_0xH00059d=2_0xH00059c=3_0xH00059b=2_d0xH0007dd=17SQ:0xH0007dd=17_R:0xH0007dd!=17_C:0xH0005a3=5.1._C:0xH0005a2=4.1._C:0xH0005a1=2.1._C:0xH0005a0=4.1._C:0xH00059f=3.1._C:0xH00059e=2.1._C:0xH00059d=2.1._C:0xH00059c=3.1._C:0xH00059b=2.1._M:0=1.9.
ach_555220_logic = [
    (player_car_upgrade_levels_block_9 == 0x05),
    (player_car_upgrade_levels_block_8 == 0x04),
    (player_car_upgrade_levels_block_7 == 0x02),
    (player_car_upgrade_levels_block_6 == 0x04),
    (player_car_upgrade_levels_block_5 == 0x03),
    (player_car_upgrade_levels_block_4 == 0x02),
    (player_car_upgrade_levels_block_3 == 0x02),
    (player_car_upgrade_levels_block_2 == 0x03),
    (player_car_upgrade_levels_block == 0x02),
    (game_state___current_screen.delta() == 0x11),
]
ach_555220_alt1 = [
    measured_if((game_state___current_screen == 0x11)),
    reset_if((game_state___current_screen != 0x11)),
    add_hits((player_car_upgrade_levels_block_9 == 0x05).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_8 == 0x04).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_7 == 0x02).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_6 == 0x04).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_5 == 0x03).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_4 == 0x02).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_3 == 0x02).with_hits(1)),
    add_hits((player_car_upgrade_levels_block_2 == 0x03).with_hits(1)),
    add_hits((player_car_upgrade_levels_block == 0x02).with_hits(1)),
    measured((value(0x00) == 0x01).with_hits(9)),
]
ach_555220 = Achievement(
    title="""The Perfect Machine""",
    description="""Purchase all available upgrades for an F1 car""",
    points=25,
    id=555220, badge="640428"
)
ach_555220.add_core(ach_555220_logic)
ach_555220.add_alt(ach_555220_alt1)
my_set.add_achievement(ach_555220)

# --- The Dream Comes True ---
# Logic: 0xH0000a3=32_d0xH0000a3!=32_0xH0000a4=144_0xH0000a5=29_0xH0013de=15_0xH001390=0
ach_555915_logic = [
    (game_cutscene_event_id_block == 0x20),
    (game_cutscene_event_id_block.delta() != 0x20),
    (game_cutscene_event_id_block_2 == 0x90),
    (game_cutscene_event_id_block_3 == 0x1d),
    (current_circuit == 0x0f),
    (overall_championship_standings_block == 0x00),
]
ach_555915 = Achievement(
    title="""The Dream Comes True""",
    description="""Win the F1 World Championship for the first time""",
    points=25, type=AchievementType.WIN_CONDITION,
    id=555915, badge="640429"
)
ach_555915.add_core(ach_555915_logic)
my_set.add_achievement(ach_555915)

# --- Perfect Season ---
# Logic: 0xH001468=160_0xH0000a3=237_0xH0000a4=231_0xH0000a5=31_d0xH0000a3!=237
ach_555384_logic = [
    (championship_points == 0xa0),
    (game_cutscene_event_id_block == 0xed),
    (game_cutscene_event_id_block_2 == 0xe7),
    (game_cutscene_event_id_block_3 == 0x1f),
    (game_cutscene_event_id_block.delta() != 0xed),
]
ach_555384 = Achievement(
    title="""Perfect Season""",
    description="""Win every single race in a full F1 season""",
    points=50,
    id=555384, badge="640430"
)
ach_555384.add_core(ach_555384_logic)
my_set.add_achievement(ach_555384)

# --- [VOID] Legend of the Asphalt ---
# Logic: 0xH0013e6=2
ach_555916_logic = [
    (current_f1_season_id == 0x02),
]
ach_555916 = Achievement(
    title="""[VOID] Legend of the Asphalt""",
    description="""Win back-to-back Formula 1 World Championships""",
    points=0,
    id=555916, badge="640432"
)
ach_555916.add_core(ach_555916_logic)
my_set.add_achievement(ach_555916)

my_set.save()