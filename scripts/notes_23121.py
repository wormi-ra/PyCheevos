# Code Notes for Game ID 23121
# Source: Smart Importer Sync

from pycheevos.core.helpers import *

# 0x000032: [USA] [EU] [JP] [8-bit] Qualifying Grid Position Block
qualifying_grid_position_block = byte(0x000032)
#Stores the starting grid order after qualifying. Address represents Grid Position (in reverse order), and the Value is the Driver ID starting there.
#Value holds ID of Driver starting in 1st Place

# 0x000033: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 2nd Place
value_holds_id_of_driver_starting_in_2nd_place = byte(0x000033)

# 0x000034: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 3rd Place
value_holds_id_of_driver_starting_in_3rd_place = byte(0x000034)

# 0x000035: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 4th Place
value_holds_id_of_driver_starting_in_4th_place = byte(0x000035)

# 0x000036: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 5th Place
value_holds_id_of_driver_starting_in_5th_place = byte(0x000036)

# 0x000037: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 6th Place
value_holds_id_of_driver_starting_in_6th_place = byte(0x000037)

# 0x000038: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 7th Place
value_holds_id_of_driver_starting_in_7th_place = byte(0x000038)

# 0x000039: [USA] [EU] [JP] [8-bit] Value holds ID of Driver starting in 8th Place
value_holds_id_of_driver_starting_in_8th_place = byte(0x000039)

# 0x000048: [USA] [EU] [JP] [8-bit] [Bitmask] Player Input (Controls)
player_input = byte(0x000048)
#This tracks the player's controller input.
#0x80 = Nitro

# 0x000049: [USA] [EU] [JP] [8-bit] [Bitmask] Player Input (Controls)
player_input_2 = byte(0x000049)
#This tracks the player's controller input.
#0x01 = Right
#0x02 = Left
#0x40 = Brake
#0x80 = Accelerate
#0x20 = Select
#0x10 = Pause

# 0x00006f: [USA] [EU] [JP] [8-bit] Shop Menu Cursor (X-Axis) (Partial)
shop_menu_cursor = byte(0x00006f)
#This tracks the horizontal cursor, but only for the first 4 items (values 0x00 to 0x03). For items 5 and 6, this address locks at 0x03. This address must be used WITH 0x000075

# 0x000073: [USA] [EU] [JP] [8-bit] Shop Menu Cursor (Y-Axis)
shop_menu_cursor_2 = byte(0x000073)
#0x00 = Chassis
#0x01 = Mission (Gearbox)
#0x02 = Brake
#0x03 = Suspension
#0x04 = Diffuser
#0x05 = Front Wing
#0x06 = Rear Wing
#0x07 = Tire
#0x08 = Engine
#0x09 = Nitro
#0x0a = Exit

# 0x000075: [USA] [EU] [JP] [8-bit] [Bitmask] Shop Menu Page (X-Axis)
shop_menu_page = byte(0x000075)
#This tracks the "page" or "scroll" of the shop menu. It works with 0x00006f to get the true item.
#0x00 = Page 1 (Items 1-4)
#0x40 = Page 2 (Item 5)
#0x80 = Page 3 (Item 6)

# 0x000076: [USA] [EU] [JP] [8-bit] Car Damage
car_damage = byte(0x000076)
#- This tracks car damage. Any value > 0x00 means the car is damaged.

# 0x00009e: [USA] [EU] [JP] [8-bit] Starting Grid Semaphore / Cutscene
starting_grid_semaphore___cutscene = byte(0x00009e)
#Tracks the status of the race start countdown lights.
#0x00 = Cutscene Active (Grid is being set up)
#0x01 = Green Light / Race Start

# 0x0000a3: [USA] [EU] [JP] [8-bit] Game Cutscene/Event ID Block
game_cutscene_event_id_block = byte(0x0000a3)
#These 3 bytes work together to identify the current fullscreen cutscene/event.
#0x20, 0x90, 0x1d = Victory Lane (End of Championship - Champion Only)
#0xed, 0xe7, 0x1f = End of Season Points Tally (End of Championship)
#0xb7, 0xd3, 0x1f = Next Season Transition (End of Championship)
#0x77, 0xda, 0x12 = Prize Money Screen (Post-Race)
#0x3b, 0xaa, 0x1c = Rank Driver Screen (Post-Race)

# 0x0000a4: [USA] [EU] [JP] [8-bit] Game Cutscene/Event ID Block
game_cutscene_event_id_block_2 = byte(0x0000a4)
#These 3 bytes work together to identify the current fullscreen cutscene/event.

# 0x0000a5: [USA] [EU] [JP] [8-bit] Game Cutscene/Event ID Block
game_cutscene_event_id_block_3 = byte(0x0000a5)
#These 3 bytes work together to identify the current fullscreen cutscene/event.

# 0x0000a9: [USA] [EU] [JP] [8-bit] Lap Counter / Race Status Flag
lap_counter___race_status_flag = byte(0x0000a9)
#Tracks lap progression and race end state. Value increments after crossing the start/finish line.
#0x01 = Race Start / During Lap 1
#0x02 = Lap 1 Completed / During Lap 2
#0x03 = Lap 2 Completed / During Lap 3
#0x04 = Final Lap Completed (Race Finished Flag)

# 0x0000ad: [USA] [EU] [JP] [8-bit] [BCD] Total Race Timer
total_race_timer = byte(0x0000ad)
#- Minutes (e.g., 0x02)

# 0x0000ae: [USA] [EU] [JP] [8-bit] [BCD] Total Race Timer
total_race_timer_2 = byte(0x0000ae)
#- Seconds (e.g., 0x28)

# 0x0000b0: [USA] [EU] [JP] [JP] [8-bit] [BCD] Total Race Timer
total_race_timer_3 = byte(0x0000b0)
#Centiseconds/Milliseconds (e.g., 0x78)

# 0x00059b: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Chassis)
player_car_upgrade_levels_block = byte(0x00059b)
#Tracks the current purchased level for each upgrade part.
#0x00 = TYPE 1
#0x01 = TYPE 2
#0x02 = TYPE 3

# 0x00059c: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Transmission/Gearbox Level)
player_car_upgrade_levels_block_2 = byte(0x00059c)
#Tracks the current purchased level for each upgrade part.
#0x00 = 4SPEED
#0x01 = 5SPEED
#0x02 = 6SPEED
#0x03 = 7SPEED

# 0x00059d: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Brake Level)
player_car_upgrade_levels_block_3 = byte(0x00059d)
#Tracks the current purchased level for each upgrade part.
#0x00 = NORNAL
#0x01 = CARBON
#0x02 = ANTILOCK

# 0x00059e: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Suspension Level)
player_car_upgrade_levels_block_4 = byte(0x00059e)
#Tracks the current purchased level for each upgrade part.
#0x00 = SOFT
#0x01 = HARD
#0x02 = ACTIVE

# 0x00059f: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Diffuser Level)
player_car_upgrade_levels_block_5 = byte(0x00059f)
#Tracks the current purchased level for each upgrade part.
#0x00 = SMALL
#0x01 = NORMAL
#0x02 = LARGE
#0x03 = SPECIAL

# 0x0005a0: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Front Wing Level)
player_car_upgrade_levels_block_6 = byte(0x0005a0)
#Tracks the current purchased level for each upgrade part.
#0x00 = LOW D.F
#0x01 = NORMAL
#0x02 = HI D.F
#0x03 = SPECIAL.L
#0x04 = SPECIAL.W

# 0x0005a1: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Rear Wing Level)
player_car_upgrade_levels_block_7 = byte(0x0005a1)
#Tracks the current purchased level for each upgrade part.
#0x00 = LOW D.F
#0x01 = NORMAL
#0x02 = HI D.F

# 0x0005a2: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Tire Level)
player_car_upgrade_levels_block_8 = byte(0x0005a2)
#Tracks the current purchased level for each upgrade part.
#0x00 = SPARE
#0x01 = RAIN
#0x02 = NORMAL
#0x03 = HIGRIP
#0x04 = SPECIAL

# 0x0005a3: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Engine Level)
player_car_upgrade_levels_block_9 = byte(0x0005a3)
#Tracks the current purchased level for each upgrade part.
#0x00 = JADD V8
#0x01 = FORO V8
#0x02 = ILMOA V10
#0x03 = REMARTY V10
#0x04 = FERARI V12
#0x05 = HOMDA V12

# 0x0005a4: [USA] [EU] [JP] [8-bit] Player Car Upgrade Levels Block (Nitro Level ('Nitro'))
player_car_upgrade_levels_block_10 = byte(0x0005a4)
#Tracks the current purchased level for each upgrade part.

# 0x0005c7: [USA] [EU] [JP] [8-bit] Nitro Fuel Level
nitro_fuel_level = byte(0x0005c7)
#Tracks the current amount of Nitro fuel available.
#0x04 = Full (100%)
#0x03 = ~70%
#0x02 = ~50%
#0x00 = Empty

# 0x0006d0: [USA] [EU] [8-bit] Casino Minigame - Roulette Selector
casino_minigame___roulette_selector = byte(0x0006d0)
#Tracks the cursor position on the Casino roulette wheel.
#0x00 = No selection / Spinning
#0x01 = Selector 1
#0x02 = Selector 2
#0x03 = Selector 3
#0x04 = Selector 4
#0x05 = Selector 5

# 0x000731: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start = byte(0x000731)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 1 (Minutes)

# 0x000732: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_2 = byte(0x000732)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 1 (Seconds)

# 0x000733: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_3 = byte(0x000733)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 1 (Centiseconds/Miliseconds)

# 0x000735: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_4 = byte(0x000735)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 2 (Minutes)

# 0x000736: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_5 = byte(0x000736)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 2 (Seconds)

# 0x000737: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_6 = byte(0x000737)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 2 (Centiseconds/Miliseconds)

# 0x000739: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_7 = byte(0x000739)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 3 (Minutes)

# 0x00073a: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_8 = byte(0x00073a)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 3 (Seconds)

# 0x00073b: [USA] [EU] [JP] [8-bit BCD per segment] Player Lap Times Block - Start
player_lap_times_block___start_9 = byte(0x00073b)
#Stores the player's completed lap times. Appears to be BCD format.
#Lap 3 (Centiseconds/Miliseconds)

# 0x000741: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start = byte(0x000741)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x000741) / (0x00074b). Seems active during Race mode.

# 0x000751: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start_2 = byte(0x000751)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x000751) / (0x00075b). Seems active during Race mode.

# 0x000761: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start_3 = byte(0x000761)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x000761) / (0x00076b). Seems active during Race mode.

# 0x000771: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start_4 = byte(0x000771)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x000771) / (0x00077b). Seems active during Race mode.

# 0x000781: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start_5 = byte(0x000781)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x000781) /  (0x00078b). Seems active during Race mode.

# 0x000791: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start_6 = byte(0x000791)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x000791) /  (0x00079b). Seems active during Race mode.

# 0x0007a1: [USA] [EU] [JP] [8-bit BCD per segment] AI Opponent Lap Times Block - Start
ai_opponent_lap_times_block___start_7 = byte(0x0007a1)
#Appears to store completed lap times for AI opponents, structured similarly to the player block (0x0007a1) / (0x0007ab) . Seems active during Race mode.

# 0x0007b1: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block = byte(0x0007b1)
#- Position for FER (T. PHILIPS)

# 0x0007b2: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block_2 = byte(0x0007b2)
#- Position for LEY (M. OWEM)

# 0x0007b3: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block_3 = byte(0x0007b3)
#- Position for MCL (A. SETA)

# 0x0007b4: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block_4 = byte(0x0007b4)
#- Position for WIL (N.J. MYDEN)

# 0x0007b5: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block_5 = byte(0x0007b5)
#- Position for TYR (J. SPOHN)

# 0x0007b6: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block_6 = byte(0x0007b6)
#- Position for BEN (R. PALUKA)

# 0x0007b7: [USA] [EU] [JP] [8-bit] AI Race Position Block (WRAM)
ai_race_position_block_7 = byte(0x0007b7)
#- Position for JOR (M. FLAERTY)

# 0x0007d9: [USA] [EU] [JP] [8-bit] Player Race Position (0-Based)
player_race_position = byte(0x0007d9)
#- it is updated only at the end of each completed lap (when crossing the start/finish line). It holds the value 0x00 during the first lap until the first crossing.
#0x00 = 1st Place
#0x01 = 2nd Place
#0x02 = 3rd Place
#0x03 = 4th Place
#0x04 = 5th Place
#0x05 = 6th Place
#0x06 = 7th Place
#0x07 = 8th Place

# 0x0007dd: [USA] [EU] [JP] [8-bit] Game State / Current Screen
game_state___current_screen = byte(0x0007dd)
#Tracks the current screen or game mode.
#0x0d = Race Session
#0x0e = Qualifying Session
#0x11 = Car Setup Screen
#0x10 = Initial Menus
#0x0a = Casino Minigame
#0x0b = Save Data Screen
#0x0c = Next Track Intro Screen
#0x05 = Post-Qualifying Results Screen
#0x07 = Overall Classification Results Screen (Victory - 1st Place)
#0x08 = Post-Race Results Screen (Finished 2nd or 3rd Place)
#0x04 = Post-Race Results Screen (Finished 4th, 5th, or 6th Place)
#0x03 = Post-Race Results Screen (Finished 7th or 8th Place)
#0x06 = Overall Classification Results Screen (Final results screen when finishing 4th-8th)

# 0x0011a2: [EU] [8-bit] Casino Win Display - Thousands
eu_casino_win_display___thousands = byte(0x0011a2)
#Note: Controls the thousands digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x0011a3: [EU] [8-bit] Casino Win Display - Hundreds
eu_casino_win_display___hundreds = byte(0x0011a3)
#Note: Controls the hundreds digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x0011a4: [EU] [8-bit] Casino Win Display - Tens
eu_casino_win_display___tens = byte(0x0011a4)
#Note: Controls the tens digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x0011a5: [EU] [8-bit] Casino Win Display - Units
eu_casino_win_display___units = byte(0x0011a5)
#Note: Controls the units digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x001222: [USA] [8-bit] Casino Win Display - Thousands
casino_win_display___thousands = byte(0x001222)
#Note: Controls the thousands digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x001223: [USA] [8-bit] Casino Win Display - Hundreds
casino_win_display___hundreds = byte(0x001223)
#Note: Controls the hundreds digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x001224: [USA] [8-bit] Casino Win Display - Tens
casino_win_display___tens = byte(0x001224)
#Note: Controls the tens digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x001225: [USA] [8-bit] Casino Win Display - Units
casino_win_display___units = byte(0x001225)
#Note: Controls the units digit shown in the "WIN" box on the slot machine.
#Values:
#0x3f = Empty/Space
#0xF0 = 0
#0xF1 = 1
#0xF2 = 2
#0xF3 = 3
#0xF4 = 4
#0xF5 = 5
#...

# 0x001310: [EU] [JP] [8-bit] Overall Championship Standings Block
eu_overall_championship_standings_block = byte(0x001310)
#This block stores the current championship ranking. The logic is inverted: Address represents the Rank, and the Value is the Driver ID holding that rank.
#0x00 = Player
#0x01 = A. PROTEUS (FER)
#0x02 = I. CAPYS (LEY)
#0x03 = A. SETH (MCL)
#0x04 = N. MANSON (WIL)
#0x05 = S. NAKADA (TYR)
#0x06 = N. PIOUS (BEN)
#0x07 = A. CHESTER (JOR)
#Value holds ID of Driver in 1st Place

# 0x001311: [EU] [JP] [8-bit] Value holds ID of Driver in 2nd Place
eu_value_holds_id_of_driver_in_2nd_place = byte(0x001311)

# 0x001312: [EU] [JP] [8-bit] Value holds ID of Driver in 3rd Place
eu_value_holds_id_of_driver_in_3rd_place = byte(0x001312)

# 0x001313: [EU] [JP] [8-bit] Value holds ID of Driver in 4th Place
eu_value_holds_id_of_driver_in_4th_place = byte(0x001313)

# 0x001314: [EU] [JP] [8-bit] Value holds ID of Driver in 5th Place
eu_value_holds_id_of_driver_in_5th_place = byte(0x001314)

# 0x001315: [EU] [JP] [8-bit] Value holds ID of Driver in 6th Place
eu_value_holds_id_of_driver_in_6th_place = byte(0x001315)

# 0x001316: [EU] [JP] [8-bit] Value holds ID of Driver in 7th Place
eu_value_holds_id_of_driver_in_7th_place = byte(0x001316)

# 0x001317: [EU] [JP] [8-bit] Value holds ID of Driver in 8th Place
eu_value_holds_id_of_driver_in_8th_place = byte(0x001317)

# 0x001318: [EU] [JP] [8-bit] Championship Points (Player)
eu_championship_points = byte(0x001318)
#This stores the points awarded when you finish a championship race.
#0x0A = 1st Place (10 pts)
#0x06 = 2nd Place (6 pts)
#0x04 = 3rd Place (4 pts)
#0x03 = 4th Place (3 pts)
#0x02 = 5th Place (2 pts)
#0x01 = 6th Place (1 pt)

# 0x001319: [EU] [JP] [8-bit] Championship Points IA (A. PROTEUS)
eu_championship_points_ia = byte(0x001319)

# 0x00131a: [EU] [JP] [8-bit] Championship Points IA (I. CAPYS)
eu_championship_points_ia_2 = byte(0x00131a)

# 0x00131b: [EU] [JP] [8-bit] Championship Points IA (A. SETH)
eu_championship_points_ia_3 = byte(0x00131b)

# 0x00131c: [EU] [JP] [8-bit] Championship Points IA (N. MANSON)
eu_championship_points_ia_4 = byte(0x00131c)

# 0x00131d: [EU] [JP] [8-bit] Championship Points IA (S. NAKADA)
eu_championship_points_ia_5 = byte(0x00131d)

# 0x00131e: [EU] [JP] [8-bit] Championship Points IA (N. PIOUS)
eu_championship_points_ia_6 = byte(0x00131e)

# 0x00131f: [EU] [JP] [8-bit] Championship Points IA (A. CHESTER)
eu_championship_points_ia_7 = byte(0x00131f)

# 0x001334: [EU] [JP] [8-bit] Driver Name Edit Selector
eu_driver_name_edit_selector = byte(0x001334)
#Note: Active on the Name Entry screen. Press Down on Controller 2 to activate hidden AI renaming.
#Values:
#0x00 = Player
#0x10 = T. PHILIPS (FER)
#0x20 = M. OWEM (LEY)
#0x30 = A. SETA (MCL)
#0x40 = N.J. MYDEN (WIL)
#0x50 = J. SPOHN (TYR)
#0x60 = R. PALUKA (BEN)
#0x70 = M. FIAERTY (JOR)

# 0x00135e: [EU] [JP] [8-bit] Current Circuit
eu_current_circuit = byte(0x00135e)
#0x00 = Italy
#0x01 = Great Britain
#0x02 = Germany
#0x03 = Brazil
#0x04 = San Marino
#0x05 = Spain
#0x06 = Portugal
#0x07 = Mexico
#0x08 = Hungary
#0x09 = Canada
#0x0a = France
#0x0b = Belgium
#0x0c = Australia
#0x0d = U.S.A
#0x0e = Monaco
#0x0f = Japan

# 0x001360: [EU] [JP] [8-bit] Current Weather Condition
eu_current_weather_condition = byte(0x001360)
#Tracks the weather for the current race/session.
#0x00 = Sunny Day
#0x01 = Light Rain
#0x02 = Heavy Rain

# 0x001362: [EU] [JP] [16-bit] Total Player Money (Wallet)
eu_total_player_money = word(0x001362)
#- This is the main "wallet" address. The value is stored divided by 10.
#Example 1: 0x03e8 (1000) = $10,000 on screen.
#Example 2: 0x0032 (50) = $500 on screen.

# 0x001366: [EU] [JP] [8-bit] Current F1 Season ID
eu_current_f1_season_id = byte(0x001366)
#Tracks the player's current F1 season
#0x01 = F1 Season 1
#0x02 = F1 Season 2

# 0x001368: [EU] [JP] [8-bit ASCII] Active Player Name - Char 1
eu_active_player_name___char_1 = byte(0x001368)

# 0x001369: [EU] [JP] [8-bit ASCII] Active Player Name - Char 2
eu_active_player_name___char_2 = byte(0x001369)

# 0x00136a: [EU] [JP] [8-bit ASCII] Active Player Name - Char 3
eu_active_player_name___char_3 = byte(0x00136a)

# 0x00136b: [EU] [JP] [8-bit ASCII] Active Player Name - Char 4
eu_active_player_name___char_4 = byte(0x00136b)

# 0x00136c: [EU] [JP] [8-bit ASCII] Active Player Name - Char 5
eu_active_player_name___char_5 = byte(0x00136c)

# 0x00136d: [EU] [JP] [8-bit ASCII] Active Player Name - Char 6
eu_active_player_name___char_6 = byte(0x00136d)

# 0x00136e: [EU] [JP] [8-bit ASCII] Active Player Name - Char 7
eu_active_player_name___char_7 = byte(0x00136e)

# 0x00136f: [EU] [JP] [8-bit ASCII] Active Player Name - Char 8
eu_active_player_name___char_8 = byte(0x00136f)

# 0x001370: [EU] [JP] [8-bit ASCII] Active Player Name - Char 9
eu_active_player_name___char_9 = byte(0x001370)

# 0x001378: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9 = byte(0x001378)
#0x001378 - 0x001380 = A.PROTEUS

# 0x001388: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9_2 = byte(0x001388)
#0x001388 - 0x001390 = I. CAPYS

# 0x001390: [USA] [8-bit] Overall Championship Standings Block
overall_championship_standings_block = byte(0x001390)
#This block stores the current championship ranking. The logic is inverted: Address represents the Rank, and the Value is the Driver ID holding that rank.
#0x00 = Player
#0x01 = T. PHILIPS (FER)
#0x02 = M. OWEM (LEY)
#0x03 = A. SETA (MCL)
#0x04 = N.J. MYDEN (WIL)
#0x05 = J. SPOHN (TYR)
#0x06 = R. PALUKA (BEN)
#0x07 = M. FIAERTY (JOR)
#Value holds ID of Driver in 1st Place

# 0x001391: [USA] [8-bit] Value holds ID of Driver in 2nd Place
value_holds_id_of_driver_in_2nd_place = byte(0x001391)

# 0x001392: [USA] [8-bit] Value holds ID of Driver in 3rd Place
value_holds_id_of_driver_in_3rd_place = byte(0x001392)

# 0x001393: [USA] [8-bit] Value holds ID of Driver in 4th Place
value_holds_id_of_driver_in_4th_place = byte(0x001393)

# 0x001394: [USA] [8-bit] Value holds ID of Driver in 5th Place
value_holds_id_of_driver_in_5th_place = byte(0x001394)

# 0x001395: [USA] [8-bit] Value holds ID of Driver in 6th Place
value_holds_id_of_driver_in_6th_place = byte(0x001395)

# 0x001396: [USA] [8-bit] Value holds ID of Driver in 7th Place
value_holds_id_of_driver_in_7th_place = byte(0x001396)

# 0x001397: [USA] [8-bit] Value holds ID of Driver in 8th Place
value_holds_id_of_driver_in_8th_place = byte(0x001397)

# 0x001398: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9_3 = byte(0x001398)
#0x001398 - 0x0013a0 = A. SETH

# 0x0013a8: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9_4 = byte(0x0013a8)
#0x0013a8 - 0x0013b0 = N. MANSON

# 0x0013b4: [USA] [8-bit] Driver Name Edit Selector
driver_name_edit_selector = byte(0x0013b4)
#Note: Active on the Name Entry screen. Press Down on Controller 2 to activate hidden AI renaming.
#Values:
#0x00 = Player
#0x10 = T. PHILIPS (FER)
#0x20 = M. OWEM (LEY)
#0x30 = A. SETA (MCL)
#0x40 = N.J. MYDEN (WIL)
#0x50 = J. SPOHN (TYR)
#0x60 = R. PALUKA (BEN)
#0x70 = M. FIAERTY (JOR)

# 0x0013b8: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9_5 = byte(0x0013b8)
#0x0013b8 - 0x0013c0 = S. NAKADA

# 0x0013c8: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9_6 = byte(0x0013c8)
#0x0013c8 - 0x0013d0 = N.PIOUS

# 0x0013d8: [EU] [JP] [8-bit ASCII] Name IA opponents Char 1-9
eu_name_ia_opponents_char_1_9_7 = byte(0x0013d8)
#0x0013d8 - 0x0013e0 = A. CHESTE

# 0x0013de: [USA] [8-bit] Current Circuit
current_circuit = byte(0x0013de)
#0x00 = Italy
#0x01 = Great Britain
#0x02 = Germany
#0x03 = Brazil
#0x04 = San Marino
#0x05 = Spain
#0x06 = Portugal
#0x07 = Mexico
#0x08 = Hungary
#0x09 = Canada
#0x0a = France
#0x0b = Belgium
#0x0c = Australia
#0x0d = U.S.A
#0x0e = Monaco
#0x0f = Japan

# 0x0013e0: [USA] [8-bit] Current Weather Condition
current_weather_condition = byte(0x0013e0)
#Tracks the weather for the current race/session.
#0x00 = Sunny Day
#0x01 = Light Rain
#0x02 = Heavy Rain

# 0x0013e2: [USA] [16-bit] Total Player Money (Wallet)
total_player_money = word(0x0013e2)
#- This is the main "wallet" address. The value is stored divided by 10.
#Example 1: 0x03e8 (1000) = $10,000 on screen.
#Example 2: 0x0032 (50) = $500 on screen.

# 0x0013e6: [USA] [8-bit] Current F1 Season ID
current_f1_season_id = byte(0x0013e6)
#Tracks the player's current F1 season
#0x01 = F1 Season 1
#0x02 = F1 Season 2

# 0x0013e8: [USA] [8-bit ASCII] Active Player Name - Char 1
active_player_name___char_1 = byte(0x0013e8)

# 0x0013e9: [USA] [8-bit ASCII] Active Player Name - Char 2
active_player_name___char_2 = byte(0x0013e9)

# 0x0013ea: [USA] [8-bit ASCII] Active Player Name - Char 3
active_player_name___char_3 = byte(0x0013ea)

# 0x0013eb: [USA] [8-bit ASCII] Active Player Name - Char 4
active_player_name___char_4 = byte(0x0013eb)

# 0x0013ec: [USA] [8-bit ASCII] Active Player Name - Char 5
active_player_name___char_5 = byte(0x0013ec)

# 0x0013ed: [USA] [8-bit ASCII] Active Player Name - Char 6
active_player_name___char_6 = byte(0x0013ed)

# 0x0013ee: [USA] [8-bit ASCII] Active Player Name - Char 7
active_player_name___char_7 = byte(0x0013ee)

# 0x0013ef: [USA] [8-bit ASCII] Active Player Name - Char 8
active_player_name___char_8 = byte(0x0013ef)

# 0x0013f0: [USA] [8-bit ASCII] Active Player Name - Char 9
active_player_name___char_9 = byte(0x0013f0)

# 0x0013f8: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9 = byte(0x0013f8)
#0x0013f8 - 0x001400 = T.PHILIPS

# 0x001408: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9_2 = byte(0x001408)
#0x001408 - 0x001410 = M.OWEM

# 0x001418: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9_3 = byte(0x001418)
#0x001418 - 0x001421 = A.SETA

# 0x001428: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9_4 = byte(0x001428)
#0x001428 - 0x001430 = N.J.MYDEN

# 0x001438: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9_5 = byte(0x001438)
#0x001438 - 0x001440 = J.SPOHN

# 0x001448: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9_6 = byte(0x001448)
#0x001448 - 0x001450 = R.PALUKA

# 0x001458: [USA] [8-bit ASCII] Name IA opponents Char 1-9
name_ia_opponents_char_1_9_7 = byte(0x001458)
#0x001458 - 0x001460 = M.FLAERTY

# 0x001468: [USA] [8-bit] Championship Points (Player)
championship_points = byte(0x001468)
#This stores the points awarded when you finish a championship race.
#0x0a = 1st Place (10 pts)
#0x06 = 2nd Place (6 pts)
#0x04 = 3rd Place (4 pts)
#0x03 = 4th Place (3 pts)
#0x02 = 5th Place (2 pts)
#0x01 = 6th Place (1 pt)

# 0x001469: [USA] [8-bit] Championship Points IA (T. PHILIPS)
championship_points_ia = byte(0x001469)

# 0x00146a: [USA] [8-bit] Championship Points IA (M. OWEM)
championship_points_ia_2 = byte(0x00146a)

# 0x00146b: [USA] [8-bit] Championship Points IA (A. SETA)
championship_points_ia_3 = byte(0x00146b)

# 0x00146c: [USA] [8-bit] Championship Points IA (N.J. MYDEN)
championship_points_ia_4 = byte(0x00146c)

# 0x00146d: [USA] [8-bit] Championship Points IA (J. SPOHN)
championship_points_ia_5 = byte(0x00146d)

# 0x00146e: [USA] [8-bit] Championship Points IA (R. PALUKA)
championship_points_ia_6 = byte(0x00146e)

# 0x00146f: [USA] [8-bit] Championship Points IA (M. FLAERTY)
championship_points_ia_7 = byte(0x00146f)

# 0x001471: [EU] [JP] [8-bit ASCII] Recycled ASCII Display Buffer - Start (approx. 7 bytes: 0x14f1-0x14f7)
eu_recycled_ascii_display_buffer___start = byte(0x001471)
#This buffer is recycled by the game.
#STATE 1 (In-Race/End): Displays the player's "Best Lap Time" as an ASCII string (e.g., "0:42.27").
#STATE 2 (Prize Screen): Displays the "Prize Money" earned as an ASCII string (e.g., " 4000").
#(This is the prize display, not the total money address.)

# 0x0014bf: [EU] [JP] [8-bit] Select Player Cursor
eu_select_player_cursor = byte(0x0014bf)
#- 0x00 = Name1
#- 0x01 = Name2
#- 0x02 = Name3
#- 0x03 = Name4
#- 0x04 = New
#- 0x05 = NameChange

# 0x0014f1: [USA] [8-bit ASCII] Recycled ASCII Display Buffer - Start (approx. 7 bytes: 0x14f1-0x14f7)
recycled_ascii_display_buffer___start = byte(0x0014f1)
#This buffer is recycled by the game.
#STATE 1 (In-Race/End): Displays the player's "Best Lap Time" as an ASCII string (e.g., "0:42.27").
#STATE 2 (Prize Screen): Displays the "Prize Money" earned as an ASCII string (e.g., " 4000").
#(This is the prize display, not the total money address.)

# 0x00153f: [USA] [8-bit] Select Player Cursor
select_player_cursor = byte(0x00153f)
#- 0x00 = Name1
#- 0x01 = Name2
#- 0x02 = Name3
#- 0x03 = Name4
#- 0x04 = New
#- 0x05 = NameChange
