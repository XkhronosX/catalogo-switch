#!/usr/bin/env python3
"""
Genera catálogo completo de juegos NSP/XCI de discos D: y E:
"""

import json
import re
from pathlib import Path

# ============================================================
# LISTA COMPLETA DISCO D: (833 archivos)
# ============================================================
D_FILES = [
    "/d/(XCI) Resident Evil 5 (1.0.3).xci",
    "/d/0003 - ARMS (World) (En,Ja,Fr,De,Es,It,Nl,Ru).xci",
    "/d/6 DLC/Hot Wheels Unleashed 2 Turbocharged [DLC AcceleRacers All-Star Pack] [01001BE01908D006][v0].nsp",
    "/d/6 DLC/Hot Wheels Unleashed 2 Turbocharged [DLC Just a Scratch Pack] [01001BE01908D004][v0].nsp",
    "/d/6 DLC/Hot Wheels Unleashed 2 Turbocharged [DLC Rust and Fast Pack] [01001BE01908D001][v0].nsp",
    "/d/6 DLC/Hot Wheels Unleashed 2 Turbocharged [DLC Speed Kings Pack] [01001BE01908D003][v0].nsp",
    "/d/6 DLC/Hot Wheels Unleashed 2 Turbocharged [DLC Twin Mill Unleashed Edition] [01001BE01908D005][v0].nsp",
    "/d/6 DLC/Hot Wheels Unleashed 2 Turbocharged [DLC Unstoppables Pack] [01001BE01908D002][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Havik] [01006560184E7012][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Jean-Claude Van Damme Skin] [01006560184E700F][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Kameo Unlock Pack] [01006560184E7013][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Omni-Man] [01006560184E7004][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC One-Time Dragon Pack] [01006560184E7010][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Quan Chi and Khameleon Kameo] [01006560184E7005][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Shang Tsung] [01006560184E7001][v0].nsp",
    "/d/8 DLC/Mortal Kombat 1 [DLC Sub-Zero Day of the Dead Skin] [01006560184E7003][v0].nsp",
    "/d/ACA NEOGEO METAL SLUG 3 [UPD][0100ba8001dc6800][v131072].nsp",
    "/d/ACA NEOGEO METAL SLUG [UPD][0100ebe002b3e800][v65536].nsp",
    "/d/Aeterna Noctis (v1.1.005).nsp",
    "/d/Alan Wake Remastered 1.0.1.nsp",
    "/d/Arkanoid - Eternal Battle (1.1.14).nsp",
    "/d/Arkanoid vs Space Invaders (1.0.0).nsp",
    "/d/Assassin's Creed III Remastered [01007F600B134800][v1.0.3].nsp",
    "/d/Assassins Creed The Ezio Collection [DLC Embers] [v0].nsp",
    "/d/Assassins Creed The Ezio Collection [DLC Lineage] [v0].nsp",
    "/d/Assassins Creed The Ezio Collection [DLC Revelations] [v0].nsp",
    "/d/Assassins Creed The Ezio Collection [v0].nsp",
    "/d/Assassins Creed The Ezio Collection ][v131072].nsp",
    "/d/Assassins_Creed_III_Remastered_Update v131072.nsp",
    "/d/Assassins_Creed_III_Remastered__Additional_Playable_Missions_Pack_DLC.nsp",
    "/d/Assassins_Creed_The_Ezio_Collection_DLC_Brotherhood_v0_part1/Assassins Creed The Ezio Collection [DLC Brotherhood] [v0].nsp",
    "/d/Assassin's Creed The Rebel Collection (NSP)(Extra Content Pack)/Assassin's Creed The Rebel Collection [Assassin's Creed The Rebel Collection - Extra Content Pack] [v0].nsp",
    "/d/Assassin's Creed The Rebel Collection (NSP)(German Audio Pack)/Assassin's Creed The Rebel Collection [Assassin's Creed The Rebel Collection - German Audio Pack] [v0].nsp",
    "/d/Assassin's Creed The Rebel Collection [Assassin's Creed Rogue] [v0].nsp",
    "/d/Assassin's Creed The Rebel Collection[010044700DEB0000][US][v0].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Atelier Series Legacy BGM Pack][0100D1900EC8112C][US][v0].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Captain Tao][0100D1900EC810D1][US][v65536].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Cool Selenite][0100D1900EC810D3][US][v65536].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Costume Set Another Fashion][0100D1900EC810CC][US][v0].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Costume Set Summer Style][0100D1900EC810CD][US][v0].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Elegant Mermaid][0100D1900EC810CF][US][v65536].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Ever Summer Queen & the Secret Island][0100D1900EC811F6][US][v65536].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [Extra Large! Rebuild Gem Pack][0100D1900EC81191][US][v0].nsp",
    "/d/Atelier Ryza Ever Darkness & the Secret Hideout [GUST Extra BGM Pack][0100D1900EC8112D][US][v65536].nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Character_Blake_Belladonna.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Characters_Jubei,_Aegis.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Characters_Mai_Natsume.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Characters_Nine_the_Phantom.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Characters_Platinum,_Kanji.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Color_Set_1_0100B61008209001v0.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Color_Set_2_0100B61008209002v0.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Additional_Color_Set_3_0100B61008209003v0.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Naoto_Kurogane,_Teddie,_Seth,_Heart.nsp",
    "/d/BLAZBLUE_CROSS_TAG_BATTLE_DLC_Ver_2_0_Expansion_Pack_0100B6100820900Dv65536.nsp",
    "/d/Barony_Legends_&_Pariahs_DLC0100A4E00F671002USAv0.nsp",
    "/d/Barony_Myths_&_Outcasts_DLC0100A4E00F671001USAv0.nsp",
    "/d/Batman Arkham Asylum [0100E870163CA000][v0].nsp",
    "/d/BioShock Remastered.nsp",
    "/d/Blasphemous (1.0.8).nsp",
    "/d/Bluey The Videogame Update 1.0.1 [US].nsp",
    "/d/Bluey The Videogame [01008C2019598000][v0][US].xci",
    "/d/Bramble The Mountain King [v1.0.5].xci",
    "/d/BrowseNX.050032A5CF12E001.v0.nsp",
    "/d/Burnout Paradise Remastered (1.0.0).nsp",
    "/d/Burnout Paradise Remastered.xci",
    "/d/Bye Sweet Carole [0100D66024594000][v0].nsp",
    "/d/CONTRA_ROGUE_CORPS_DLC_Assassin_Pack_0100F2600D711006v0.nsp",
    "/d/CONTRA_ROGUE_CORPS_DLC_Hungry_Beast_2_T_shirts_0100F2600D711001v0.nsp",
    "/d/CONTRA_ROGUE_CORPS_DLC_Hungry_Beast_4_T_shirts_Pack_0100F2600D711002v0.nsp",
    "/d/CONTRA_ROGUE_CORPS_DLC_Retro_Bill_Pack_0100F2600D711004v0.nsp",
    "/d/CONTRA_ROGUE_CORPS_DLC_The_Gentleman_Beetle_Pack_0100F2600D711005v0.nsp",
    "/d/Cadence of Hyrule (1.5.0).nsp",
    "/d/Call of Juarez - Gunslinger (1.0.3).nsp",
    "/d/Call of Juarez Gunslinger [0100B4700BFC6000][v0].nsp",
    "/d/Capcom Beat 'Em Up Bundle[multi].xci",
    "/d/Castlevania Anniversary Collection (1.1.0).nsp",
    "/d/Castlevania Anniversary Collection [01001A800D6BC000][v0].nsp",
    "/d/Castlevania Anniversary Collection [01001A800D6BC800][v131072].nsp",
    "/d/Contra Anniversary Collection [0100DCA00DA7E000][v0].nsp",
    "/d/Contra Anniversary Collection [0100DCA00DA7E800][v65536].nsp",
    "/d/Contra Rogue Corps [0100F2600D710000][v0].nsp",
    "/d/Contra Rogue Corps [0100F2600D710800][v327680].nsp",
    "/d/Contra_Operation_Galuga_DLC_Early_Purchase_Bonus_0100CF401A98F001v0.nsp",
    "/d/Crash Bandicoot N. Sane Trilogy [0100D1B006744000][v0].nsp",
    "/d/Cruis n Blast (v1.0.7).nsp",
    "/d/Cry Babies Magic Tears The Big Game [0100A1201B82A000][v0].nsp",
    "/d/Crypt of the NecroDancer Nintendo Switch Edition (1.0.5).nsp",
    "/d/Cult of the Lamb [01002E7016C46000][v0][Base][Thanks to Bugely@Nxbrew.com].nsp",
    "/d/Cult of the Lamb [01002E7016C46800][v1048576] (1.22 GB).nsp",
    "/d/Cult of the Lamb [v1.4.6].xci",
    "/d/Cuphead [0100A5C00D162800][v655360][US].nsp",
    "/d/Cuphead [DLC The Delicious Last Course] [0100A5C00D163001][v0][US].nsp",
    "/d/Custom DLC Unlocker/Mortal Kombat 1 [DLC Custom Unlocker] [01006560184E7099][v0].nsp",
    "/d/DBI ACCESO DIRECTO.nsp",
    "/d/DBI.nsp",
    "/d/DOOM 1993 [010018900DD00000][v0].nsp",
    "/d/DOOM 2 [0100D4F00DD02800][v589824].nsp",
    "/d/DOOM 3 [010029D00E740000][v0].nsp",
    "/d/DOOM 64 [01005D700E742800][v131072].nsp",
    "/d/DOOM 64[01005D700E742000][US][v0].nsp",
    "/d/DOOM [010018900DD00800][v589824].nsp",
    "/d/DOOm.eter.v1.13+dlcs.xci",
    "/d/DRAGON BALL Sparking! ZERO [010035F022079004][v0][DLC 4].nsp",
    "/d/DRAGON BALL Sparking! ZERO [010035F022079005][v0][DLC 5].nsp",
    "/d/DRAGON BALL Sparking! ZERO [v2.0.74+8dlc].xci",
    "/d/DRAGON QUEST III HD-2D Remake [01003E601E324000][v0][US].nsp",
    "/d/DREDGE[v1.0.2].nsp",
    "/d/Darksiders II Deathinitive Edition.nsp",
    "/d/Darksiders III v1.0.1.xci",
    "/d/Darksiders Warmastered Edition (1.0.0).nsp",
    "/d/Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles 2 [0100AD80208A8000][v0].xci",
    "/d/DevMenu6.nsp",
    "/d/Diablo III: Eternal Collection [01001B300B9BE000][v0][Base].nsp",
    "/d/Disney Epic Mickey Rebrushed [0100DA201EBF8000][v0].nsp",
    "/d/Disney Epic Mickey Rebrushed [0100DA201EBF8800][v262144].nsp",
    "/d/Disney_Epic_Mickey_Rebrushed_DLC_Rebrushed_Costume_Pack_0100DA201EBF9001v0.nsp",
    "/d/Donkey Kong Country Returns HD [01009D901BC56000][v0][US].xci",
    "/d/Doraemon_Story_of_Seasons_Friends_of_the_Great_Kingdom_DLC_101008EE0177A9001v0.nsp",
    "/d/Doraemon_Story_of_Seasons_Friends_of_the_Great_Kingdom_Premium_Crops.nsp",
    "/d/Doraemon_Story_of_Seasons_Friends_of_the_Great_Kingdom_Seasonal.nsp",
    "/d/Double_Dragon_Gaiden_Rise_of_the_Dragons_01005D001AE48000v0.nsp",
    "/d/Double_Dragon_Gaiden_Rise_of_the_Dragons_01005D001AE48800v720896.nsp",
    "/d/Dying Light Platinum Edition [French Language Pack] [01008C8012921043][v0].nsp",
    "/d/Dying Light Platinum Edition [German Language Pack] [01008C8012921040][v0].nsp",
    "/d/Dying Light Platinum Edition [Italian Language Pack ] [01008C8012921044][v0].nsp",
    "/d/Dying Light Platinum Edition [Polish Language Pack] [01008C8012921041][v0].nsp",
    "/d/Dying Light Platinum Edition [Portuguese Language Pack] [01008C801292103F][v0].nsp",
    "/d/Dying Light Platinum Edition [Spanish Language Pack] [01008C8012921042][v0].nsp",
    "/d/Dying Light: Definitive Edition [01008C8012920000][v0][Base].nsp",
    "/d/Dying Light: Definitive Edition [01008C8012920800][v327680][1.0.5][UPD].nsp",
    "/d/EA SPORTS FC 25 [010054E01D878000][v0].nsp",
    "/d/EA Sports FC 26 Switch NSP Base Game/EA Sports FC 26.nsp",
    "/d/EA Sports FC 26 Switch NSP Update V1.0.1/EA Sports FC 26 v196608.nsp",
    "/d/Everybody 1-2-Switch! [01006F900BF8E800][v65536][US].nsp",
    "/d/FAIRY TAIL 2 [0100B9801F872000][v0][US].nsp",
    "/d/FIFA 18/FIFA 18 [0100f7b002340000][v0].nsp",
    "/d/FIFA 18/FIFA 18 [UPD][0100f7b002340800][v458752].nsp",
    "/d/FIFA 22 Nintendo Switch Legacy Edition [0100216014472000][v0][US].nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Bel_Dats.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Chelinkas.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Chimes_Crystal.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Enchanted.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Layles_Crystal.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Leos_Crystal.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Miras_Crystal.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Moogle_Weapon.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Relic_Weapon.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Sapphire.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Sherlottas.nsp",
    "/d/FINAL_FANTASY_CRYSTAL_CHRONICLES_Remastered_Edition_DLC_Yuris_Crystal.nsp",
    "/d/Fairy Tail [0100CF900FA3E000][v0].nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_additional_dungeon_fairy_tailrift_in_time_and_spacefairy_tail_dlc_0100cf900fa3f044.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_additional_friends_set_fairy_taillevyfairy_tail_dlc_0100cf900fa3f041.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_additional_friends_set_fairy_taillisanna_and_elfmanfairy_tail_dlc_0100cf900fa3f042.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_additional_friends_set_fairy_taillyonfairy_tail_dlc_0100cf900fa3f040.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_bonus_lacrima_handy_in_the_games_early_stages_x_5_dlc_0100cf900fa3f001.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_ddx_only_lucys_costume_gust_collaboration_ryza_and_limited_edition_growth_lacrima_x_5_dlc_0100cf900fa3f007.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_erzas_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f020.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_erzas_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f031.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_erzas_costume_fairy_tailfairy_tail_team_afairy_tail_dlc_0100cf900fa3f00b.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_erzas_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f00f.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_gajeels_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f024.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_gajeels_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f035.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_gajeels_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f013.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_gildartss_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f028.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_gildartss_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f039.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_gildartss_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f017.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_grays_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f021.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_grays_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f032.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_grays_costume_fairy_tailfairy_tail_team_afairy_tail_dlc_0100cf900fa3f00a.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_grays_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f010.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_ichiyas_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f02b.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_ichiyas_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f03c.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_ichiyas_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f01a.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_jellals_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f025.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_jellals_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f036.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_jellals_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f014.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_juvias_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f026.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_juvias_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f037.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_juvias_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f015.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_kaguras_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f02a.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_kaguras_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f03b.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_kaguras_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f019.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_laxuss_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f023.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_laxuss_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f034.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_laxuss_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f012.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_limited_edition_growth_lacrima_x_5_dlc_0100cf900fa3f045.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_lucys_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f01f.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_lucys_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f030.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_lucys_costume_fairy_tailfairy_tail_team_afairy_tail_dlc_0100cf900fa3f009.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_lucys_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f00e.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_mirajanes_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f027.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_mirajanes_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f038.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_mirajanes_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f016.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_natsus_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f01e.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_natsus_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f02f.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_natsus_costume_fairy_tailfairy_tail_team_afairy_tail_dlc_0100cf900fa3f008.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_natsus_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f00d.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_rogues_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f02d.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_rogues_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f03e.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_rogues_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f01c.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_sherrias_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f029.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_sherrias_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f03a.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_sherrias_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f018.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_special_erza_costume_miss_fairy_tail_dlc_0100cf900fa3f006.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_stings_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f02c.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_stings_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f03d.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_stings_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f01b.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_very_difficult_requests_set_dlc_0100cf900fa3f043.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_wendys_costume_fairy_tailanime_final_seasonfairy_tail_dlc_0100cf900fa3f022.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_wendys_costume_fairy_taildress_upfairy_tail_dlc_0100cf900fa3f033.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_wendys_costume_fairy_tailfairy_tail_team_afairy_tail_dlc_0100cf900fa3f00c.nsp",
    "/d/Fairy Tail [62 DLC Unlocker]NSP/sxs-fairy_tail_wendys_costume_fairy_tailspecial_swimsuitfairy_tail_dlc_0100cf900fa3f011.nsp",
    "/d/Fire Emblem Engage (1.3.0).nsp",
    "/d/Fire Emblem Engage [0100A6301214E000][v0][US].nsp",
    "/d/Fire Emblem Engage [0100A6301214E800][v327680][US].nsp",
    "/d/Fire Emblem Three Houses [6 DLC]/Fire Emblem Three Houses [Additional Quests][010055D009F79004][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [6 DLC]/Fire Emblem Three Houses [Additional Support Items][010055D009F79005][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [6 DLC]/Fire Emblem Three Houses [Auxiliary Battle Maps][010055D009F79003][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [6 DLC]/Fire Emblem Three Houses [New Attire][010055D009F79002][US][v262144].nsp",
    "/d/Fire Emblem Three Houses [6 DLC]/Fire Emblem Three Houses [Officers Academy Uniform Byleth][010055D009F79006][US][v262144].nsp",
    "/d/Fire Emblem Three Houses [6 DLC]/Fire Emblem Three Houses [Side Story Cindered Shadows][010055D009F79001][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [Additional Quests][010055D009F79004][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [Additional Support Items][010055D009F79005][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [Auxiliary Battle Maps][010055D009F79003][US][v196608].nsp",
    "/d/Fire Emblem Three Houses [New Attire][010055D009F79002][US][v262144].nsp",
    "/d/Fire Emblem Three Houses [Officers Academy Uniform Byleth][010055D009F79006][US][v262144].nsp",
    "/d/Fire Emblem Three Houses [Side Story Cindered Shadows][010055D009F79001][US][v196608].nsp",
    "/d/Fire Emblem Warriors Three Hopes [010071F0143EA000][v0][US].nsp",
    "/d/Fire Emblem Warriors Three Hopes [010071F0143EA800][v131072][US].nsp",
    "/d/Fire Emblem Warriors Three Hopes [Digital Purchase DLC][010071F0143EA000][v0][US].nsp",
    "/d/Five Nights at Freddy's 2 [01004EB00E43A000][v0].nsp",
    "/d/Five Nights at Freddy's 3 [010056100E43C000][v0].nsp",
    "/d/Five Nights at Freddy's 3 [010056100E43C800][v65536].nsp",
    "/d/Five Nights at Freddy's 4 [010083800E43E000][v0].nsp",
    "/d/Five Nights at Freddy's 4 [010083800E43E800][v131072].nsp",
    "/d/Five Nights at Freddy's Help Wanted [0100F7901118C000][v0].nsp",
    "/d/Five Nights at Freddy's [0100B6200D8D2000][v0].nsp",
    "/d/Five Nights at Freddys Security Breach.nsp",
    "/d/Five Nights at Freddys Sister Location [01003B200E440000][v0].nsp",
    "/d/Five Nights at Freddys Sister Location [01003B200E440800][v131072].nsp",
    "/d/Game Boy - NSO [0100C62011050000][v0].nsp",
    "/d/Game Boy Advance - Nintendo Switch Online [010012F017576000].nsp",
    "/d/Ghost Trick Phantom Detective [010029B018432000][v0][US].nsp",
    "/d/Ghosts n Goblins Resurrection.nsp",
    "/d/Gothic 2 [0100AB001A960000][v0] (9.29 GB).nsp",
    "/d/Gothic 2 [0100AB001A960800][v65536] (0.71 GB).nsp",
    "/d/Grace_of_Letoile_No_Encounters_DLC0100CAC01C3ED002USAv0.nsp",
    "/d/Grand Theft Auto 3 [0100C3C012718000][v0].nsp",
    "/d/Grand Theft Auto 3 [0100C3C012718800][v524288].nsp",
    "/d/Grand Theft Auto San Andreas [010065A014024000][v0].nsp",
    "/d/Grand Theft Auto San Andreas [010065A014024800][v524288].nsp",
    "/d/Grand Theft Auto Vice City [0100182014022000][v0].nsp",
    "/d/Grand Theft Auto Vice City [0100182014022800][v524288].nsp",
    "/d/Guacamelee STCE.nsp",
    "/d/Guns, Gore and Cannoli (1.0.0).nsp",
    "/d/Hades II [0100A00019DE0000].nsp",
    "/d/Hades II [0100A00019DE0800][v196608][1.0.131248].nsp",
    "/d/Hades [0100535012974800][v589824].nsp",
    "/d/Hades[0100535012974000][v0].nsp",
    "/d/Hogwarts Legacy [0100F7E00C70E000][v0][US](nsw2u.com).xci",
    "/d/Hogwarts Legacy [0100F7E00C70E800][v65536][US](nsw2u.com).nsp",
    "/d/Hunting Simulator [0100C460040EA000][v0].nsp",
    "/d/Hyrule Warriors Age of Calamity.nsp",
    "/d/It Takes Two [010092A0172E4000][v0][US].nsp",
    "/d/It Takes Two [010092A0172E4000][v131072][US].nsp",
    "/d/It Takes Two [DLC Full Game] [010092A0172E5001][v0][US].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Character Pack 10 Shoto Todoroki][0100183010F130D2][US][v0].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Character Pack 11][0100183010F130D3][US][v0].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Character Pack 12][0100183010F130D4][US][v0].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Character Pack 13][0100183010F130D5][US][v0].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Character Pack 14][0100183010F130D6][US][v0].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Early Purchase Bonus][0100183010F13065][US][v0].nsp",
    "/d/JUMP FORCE - Deluxe Edition [JUMP FORCE Early Purchase Bonus][0100183010F1306C][US][v0].nsp",
    "/d/JUMP FORCE Character Pack 10 Shoto Todoroki[0100183010F130D2][US][v0].nsp",
    "/d/JUMP FORCE Deluxe Edition [0100183010F12000][v0](US).nsp",
    "/d/Jujutsu Kaisen Cursed Clash [010085401A455001][v0][DLC 1].nsp",
    "/d/Jujutsu Kaisen Cursed Clash [010085401A45500B][v0][DLC 11].nsp",
    "/d/Jump Force Deluxe Edition.nsp",
    "/d/Jurassic_Park_Classic_Games_Collection_0100D4801BF26000v0USnsw2u.nsp",
    "/d/KILL la KILL - IF [010018600E03E000][v0][EU].nsp",
    "/d/KINGDOM HEARTS Melody of Memory [01005D2011EA8000][v0](US-EU).nsp",
    "/d/L0LLIP0P CHAINS@W RePOP.v1.1.xci",
    "/d/LEGO Star Wars The Skywalker Saga [010042D00D900000][v0].nsp",
    "/d/LEGO Star Wars The Skywalker Saga [010042D00D900800][v524288][US].nsp",
    "/d/LEGO Star Wars The Skywalker Saga [DLC Spanish Mexico Language Pack][010042D00D901013][v0].nsp",
    "/d/LEGO_Marvel_Super_Heroes_2_DLC_Agents_of_Atlas_Character_Pack_0.nsp",
    "/d/Little Friends: Dogs & Cats [010079A00D9E8000][v0][Base].nsp",
    "/d/Little Friends: Puppy Island [010023801A52A000][v0][Base].nsp",
    "/d/Little Nightmares III [010066101A55A000].xci",
    "/d/METAL GEAR SOLID - Master Collection Version [0100C1301A9C2800][v458752][UPD3.0.0][US].nsp",
    "/d/METAL GEAR SOLID 1 - Master Collection Version [0100C1301A9C2000][v0].nsp",
    "/d/Mario + Rabbids Sparks of Hope v1.6.2225577+7dlc.xci",
    "/d/Mario Kart 8 Deluxe (NSP)(Booster Course Wave 1 to 6)/Mario Kart 8 Deluxe [Booster Course][0100152000023001][v65536][US].nsp",
    "/d/Mario Kart 8 Deluxe [0100152000022800][v1376256][US](nsw2u.com).nsp",
    "/d/Mario Kart 8 Deluxe v3.0.5.nsp",
    "/d/Mario Party Superstars[01006FE013472000][US][v0].nsp",
    "/d/Mario Tennis Aces[0100BDE00862A000][US][v0].nsp",
    "/d/Mario Tennis Aces[0100BDE00862A800][US][v786432].nsp",
    "/d/Mario and Luigi Brothership [01006D0017F7A000][v0][US].nsp",
    "/d/Mario vs. Donkey Kong [0100B99019412000][v0].nsp",
    "/d/Mario vs. Donkey Kong [0100B99019412800][v65536].nsp",
    "/d/Mario_Kart_8_Deluxe_DLC_Booster_Course_Pass_0100152000023001v65536.nsp",
    "/d/Metroid Dread v2.1.0.xci",
    "/d/Metroid Prime 4 Beyond [v1.1.0].xci",
    "/d/Metroid Prime Remastered [010012101468C000].nsp",
    "/d/Miitopia [01003DA010E8A000][US][v0].nsp",
    "/d/Miitopia [01003DA010E8A800][v196608].nsp",
    "/d/Minecraft Dungeons [01006C100EC08000][v0].nsp",
    "/d/Minecraft Dungeons [01006C100EC08800][v1769472].nsp",
    "/d/Minecraft Legends [01007C6012CC8000][v0].nsp",
    "/d/Minecraft Legends [01007C6012CC8800][v720896].nsp",
    "/d/Minecraft Story Mode - Season Two [01003EF007ABA000][v0].nsp",
    "/d/Minecraft Story Mode - The Complete Adventure [010059C002AC2000][v0].nsp",
    "/d/Minecraft [0100D71004694800][v10420224][1.26.44][UPD].nsp",
    "/d/Monster High Skulltimate Secrets [010097F01C75A000][USA][v0][Base].xci",
    "/d/Monster High Skulltimate Secrets [010097F01C75A800][USA][v65536][Update].nsp",
    "/d/Mortal Kombat 1 [01006560184E6000][v0] (5.87 GB).nsp",
    "/d/Mortal Kombat 1 [01006560184E6800][v589824] (30.19 GB).nsp",
    "/d/My Little Puppy [01005EB0269DE000][v0][Base].nsp",
    "/d/NARUTO SHIPPUDEN Ultimate Ninja Storm Trilogy [0100EC800800C000][v0].nsp",
    "/d/NARUTO SHIPPUDEN Ultimate Ninja Storm Trilogy [0100EC800800C800][v65536].nsp",
    "/d/NARUTO X BORUTO ULTIMATE NINJA STORM CONNECTIONS [DLC pack 1][0100D2D0190A5007][v0][US](nsw2u.com).nsp",
    "/d/NARUTO X BORUTO ULTIMATE NINJA STORM CONNECTIONS [DLC pack 1][0100D2D0190A5007][v0][US].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS DLC Pack 2 DLC][0100D2D0190A5008][v0][US].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [0100D2D0190A4800][v262144][US].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [0100D2D0190A4800][v458752][US](nsw2u.com).nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [0100D2D0190A500C][v0][DLC 12].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [NBUNSC - Costume _ Accessory Pack] [0100D2D0190A5001][v0].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [NBUNSC - Kakashi Hatake Maskless] [0100D2D0190A5005][v0].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [NBUNSC - Naruto Uzumaki The Great Ninja War End] [0100D2D0190A5006][v0].nsp",
    "/d/NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS [NBUNSC - Pre-Order Pack] [0100D2D0190A5002][v0].nsp",
    "/d/NPS  [0100F4300BF2C800][v262144].nsp",
    "/d/Need For Speed Hot Pursuit Remastered[v0].nsp",
    "/d/NieR Automata The End of YoRHa Edition (1.0.2).nsp",
    "/d/Ninja Gaiden Sigma (v1.0.2).nsp",
    "/d/Ninja Gaiden Sigma 2 (v1.0.4).nsp",
    "/d/Nintendo 64 - Nintendo Switch Online [0100C9A00ECE6000][v0].nsp",
    "/d/Nintendo Entertainment System - Nintendo Switch Online [0100D870045B6000][v0].nsp",
    "/d/Nintendo NES Nintendo Switch Online [v6.8.0 -V1].xci",
    "/d/Nintendo Switch Sports v1.4.0.xci",
    "/d/No Man's Sky [v5.5.5].xci",
    "/d/OKAMI HD [0100276009872000][v0].nsp",
    "/d/Octopath Traveler 2.xci",
    "/d/Octopath Traveler [010057D006492000][v0].nsp",
    "/d/Octopath Traveler [010057D006492800][v262144].nsp",
    "/d/One Peace - Unlimited World Red.nsp",
    "/d/Ori and the Blind Forest Definitive Edition [010061D00DB74000][v0].nsp",
    "/d/Ori and the Blind Forest Definitive Edition [010061D00DB74800][v65536].nsp",
    "/d/Ori and the Blind Forest Definitive Edition.nsp",
    "/d/Ori and the Will of the Wisps[01008DD013200000][v0].nsp",
    "/d/Ori and the Will of the Wisps[01008DD013200800][Update 1.1.0].nsp",
    "/d/Outlast 2.nsp",
    "/d/Overcooked 2 [01006FD0080B2000][v0].nsp",
    "/d/Overcooked 2 [01006FD0080B2800][v983040].nsp",
    "/d/Overcooked Special Edition [01009B900401E000].nsp",
    "/d/Overcooked Special Edition [01009B900401E800][v262144].nsp",
    "/d/Overcooked! 2 [DLC Additional Content Third Course Carnival of Chaos] [01006FD0080B3005][v0].nsp",
    "/d/Overcooked! 2 [DLC Campfire Cook Off] [01006FD0080B3003][v0].nsp",
    "/d/Overcooked! 2 [DLC Night of the Hangry Horde][01006FD0080B3004][v0].nsp",
    "/d/Overcooked! 2 [DLC Surf and Turf] [01006FD0080B3002][v0].nsp",
    "/d/Overcooked! 2 [DLC Too Many Cooks Pack] [01006FD0080B3001][v0].nsp",
    "/d/PQ [01005D100807A000][v0] (2).nsp",
    "/d/PQ [01005D100807A000][v0].nsp",
    "/d/PQ [01005D100807A800][v65536] (2).nsp",
    "/d/PQ [01005D100807A800][v65536].nsp",
    "/d/PT DX [0100B3F000BE2000][v0].nsp",
    "/d/PT DX [0100B3F000BE2800][v458752].nsp",
    "/d/Pacman Championship Edition 2.nsp",
    "/d/Pang Adventures.nsp",
    "/d/Panzer Dragoon Remake.nsp",
    "/d/Paper Mario The Thousand Year Door.xci",
    "/d/Paw Patrol Grand Prix [0100360016800000][v0][US].xci",
    "/d/Persona 5 Royal v1.0.2.xci",
    "/d/Persona 5 Strikers [2dlc].xci",
    "/d/Pikmin 4 v1.0.2.xci",
    "/d/Plants vs Zombies Neighborville Complete Edition.nsp",
    "/d/Pokemon Brilliant Diamond [0100000011D90000][v0] (4.29 GB).nsp",
    "/d/Pokemon Cafe Mix [010072400E04A000][v0].nsp",
    "/d/Pokemon Cafe Mix [010072400E04A800][v786432].nsp",
    "/d/Pokemon Legends Arceus [01001F5010DFA800][v262144](nsw2u.xyz).nsp",
    "/d/Pokemon Quest [DLC Expedition Pack] [01005d100807b001][v0].nsp",
    "/d/Pokemon Quest [DLC Scattershot Stone] [01005D100807B005][v0] (2).nsp",
    "/d/Pokemon Quest [DLC Scattershot Stone] [01005D100807B005][v0].nsp",
    "/d/Pokemon Quest [DLC Sharing Stone] [01005D100807B00A][v0] (2).nsp",
    "/d/Pokemon Quest [DLC Sharing Stone] [01005D100807B00A][v0].nsp",
    "/d/Pokemon Quest [DLC Stay Strong Stone] [01005D100807B009][v0] (2).nsp",
    "/d/Pokemon Quest [DLC Stay Strong Stone] [01005D100807B009][v0].nsp",
    "/d/Pokemon Scarlet v4.0.0.nsp",
    "/d/Pokemon Shield [01008DB008C2C000][v0] (9.53 GB).nsp",
    "/d/Pokemon Shining Pearl [010018E011D92000][v0] (4.29 GB).nsp",
    "/d/Pokemon Sword [0100ABF008968000][v0] (9.53 GB).nsp",
    "/d/Pokemon_Brilliant_Diamond_0100000011D90800v393216_2_55_GB.nsp",
    "/d/Pokemon_Quest_DLC_Great_Expedition_Pack_01005d100807b002v0.nsp",
    "/d/Pokemon_Scarlet_DLC_The_Indigo_Disk,_The_Teal_Mask_+_New_Uniform.nsp",
    "/d/Pokemon_Violet_DLC_The_Indigo_Disk,_The_Teal_Mask_+_New_Uniform.nsp",
    "/d/Pokken_Tournament_DX_DLC_Battle_Pack_Wave_1_0100B3F000BE3001v65536.nsp",
    "/d/Pokken_Tournament_DX_DLC_Battle_Pack_Wave_2_0100B3F000BE3002v65536.nsp",
    "/d/Pokémon Legends Z-A.nsp",
    "/d/Pokémon Scarlet [0100A3D008C5C800][v720896].nsp",
    "/d/Poppy Playtime Chapter 4 [v1.1].xci",
    "/d/Poppy Playtime Triple Pack [0100C3801C786000].xci",
    "/d/PowerWash Simulator [0100926016012000][v0][US].nsp",
    "/d/Prince of Persia The Lost Crown [0100210019428000][v0] (5.98 GB).nsp",
    "/d/Prince of Persia The Lost Crown [0100210019428800][v720896].nsp",
    "/d/Prince of Persia The Lost Crown.nsp",
    "/d/Prince_of_Persia_The_Lost_Crown_DLC_Dark_Prince_Skin_0100210019429005v0.nsp",
    "/d/Prince_of_Persia_The_Lost_Crown_DLC_Immortal_Outfit_0100210019429002v0.nsp",
    "/d/Prince_of_Persia_The_Lost_Crown_DLC_Mask_of_Darkness_0100210019429004v0.nsp",
    "/d/Prince_of_Persia_The_Lost_Crown_DLC_Pre_Order_Bonus_0100210019429001v0.nsp",
    "/d/Prince_of_Persia_The_Lost_Crown_DLC_Prosperity_Bird_Amulet_0100210019429003v0.nsp",
    "/d/Prince_of_Persia_The_Lost_Crown_DLC_Two_Thrones_Skin_0100210019429006v0.nsp",
    "/d/REYNATIS_Antispellant_x10_DLC010050F01DF9D00Ev0USnsw2u_com.nsp",
    "/d/REYNATIS_Chill_Grande_L_x10_DLC010050F01DF9D00Bv0USnsw2u_com.nsp",
    "/d/REYNATIS_Chill_Short_MAX_x10_DLC010050F01DF9D008v0USnsw2u_com.nsp",
    "/d/REYNATIS_Chill_Tall_MAX_x10_DLC010050F01DF9D009v0USnsw2u_com.nsp",
    "/d/REYNATIS_Chill_Venti_MAX_x10_DLC010050F01DF9D00Av0USnsw2u_com.nsp",
    "/d/REYNATIS_Clear_Bonus_Early_Unlock_DLC_DLC010050F01DF9D002v0USnsw2u.nsp",
    "/d/REYNATIS_Con_Elixir_L_x10_DLC010050F01DF9D00Dv0USnsw2u_com.nsp",
    "/d/REYNATIS_Death_Panacea_x10_DLC010050F01DF9D00Fv0USnsw2u_com.nsp",
    "/d/Red Dead Redemption [01007820196A6000][v0].nsp",
    "/d/Red Dead Redemption [01007820196A6800][v262144].nsp",
    "/d/Resident Evil 6 [01002A000CD48000][USA][v0](eShop).nsp",
    "/d/River City Girls Complete Edition [0100B740191E2000].xci",
    "/d/S+M+3D+All-S.by.farenheith v1.1.1.xci",
    "/d/SNK Heroines Tag Team Frenzy.nsp",
    "/d/Sega_Dreamcast[Reicast] SWITCH/Dreamcast_[Reicast].nsp",
    "/d/Shakedown Hawaii.nsp",
    "/d/Skul the Hero Slayer (v1.7.1).nsp",
    "/d/Sniper Elite 4 [010007B010FCC000][v0].nsp",
    "/d/Snoopy & The Great Mystery Club [v1.0.1+dlc].xci",
    "/d/Snow Bros. Wonderland v1.0.0[0100A1D0205E2000][v0][APP].nsp",
    "/d/Sonic Frontiers [01004AD014BF0000][v0][US].nsp",
    "/d/Sonic Frontiers [01004AD014BF0800][v458752][US].nsp",
    "/d/Sonic Racing CrossWorlds v1.00[01006E001823C000][v0][APP].nsp",
    "/d/Sonic x Shadow Generation [01005EA01C0FC000][v0] .nsp",
    "/d/Splatoon 2.nsp",
    "/d/Splatoon 3 [0100C2500FC20000][v65536].nsp",
    "/d/Story of Seasons Grand Bazaar [0100DAE01E4C8000].xci",
    "/d/Stray [010075101EF84000][v0][US].nsp",
    "/d/Stray [010075101EF84800][v131072][US].nsp",
    "/d/Subnautica (v1.21.71113).nsp",
    "/d/Subnautica Below Zero (v1.21.49397).nsp",
    "/d/Super Bomberman R [01007AD00013E800][v720896].nsp",
    "/d/Super Mario Galaxy 2 v1.0.0[0100FD8022DAA000][v0][APP].nsp",
    "/d/Super Mario Galaxy v1.0.0[010099C022B96000][v0][APP].nsp",
    "/d/Super Mario Maker 2 [01009B90006DC000][v0].nsp",
    "/d/Super Mega Baseball 3.nsp",
    "/d/Super Monkey Ball Banana Blitz HD.nsp",
    "/d/Super Nintendo Entertainment System - Nintendo Switch Online [01008D300C50C000][v0].nsp",
    "/d/Super Smash Bros Ultimate [01006A800016E000][v0] (13.63 GB).nsp",
    "/d/Super Smash Bros Ultimate [01006A800016E800][v1769472] (3.66 GB).nsp",
    "/d/Super Smash Bros Ultimate [DLC Aeriths Outfit] [01006A800016F045].nsp",
    "/d/Super Smash Bros Ultimate [DLC Akira Outfit and Wig] [01006A800016F031][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Altïar Outfit and Hood] [01006A800016F034][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Barrets Outfit] [01006A800016F043].nsp",
    "/d/Super Smash Bros Ultimate [DLC Bomberman] [01006A800016F041][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Callie Outfit and Wig] [01006A800016F039][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 10] [01006A800016F00B][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 11] [01006A800016F00C][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 1] [01006A800016F002][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 2] [01006A800016F003][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 3] [01006A800016F004][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 4] [01006A800016F005][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 5] [01006A800016F006][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 6] [01006A800016F007][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 8] [01006A800016F009][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC Challenger Pack 9] [01006A800016F00A][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Chocobo Hat] [01006A800016F046].nsp",
    "/d/Super Smash Bros Ultimate [DLC Costume Doom Slayers Armor and Helmet] [01006A800016F052][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Costume Judd Hat] [01006A800016F050][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Costume Octoling Wig] [01006A800016F051][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Creeper] [01006A800016F03D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Cuphead Outfit and Hat] [01006A800016F033][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Dante Costume] [01006A800016F04C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Diamond] [01006A800016F03F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Dragonborn Costume] [01006A800016F04E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Erdricks Armour and Helmet] [01006A800016F025][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Fighters Pass Bonus Mii Fighter Costume Ancient Soldier] [01006A800016F016][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Fighters Pass Bonus Mii Fighter Costume Rex] [01006A800016F015][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Geno Hat Outfit] [01006A800016F047].nsp",
    "/d/Super Smash Bros Ultimate [DLC Gils] [01006A800016F042][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Goemon Outfit and Wig] [01006A800016F02A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Heihachi Outfit and Wig] [01006A800016F03C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Iori Yagami Outfit and Wig] [01006A800016F030][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Jackys Outfit and Wig] [01006A800016F032][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Knuckles Outfit and Hat] [01006A800016F024][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Lloyd Costume] [01006A800016F04F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Marie Outfit and Wig] [01006A800016F03A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Martial Artist Gi and Wig] [01006A800016F026][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC MegaMan EXEs Armor and Helmet] [01006A800016F037][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Morgana Hat] [01006A800016F022][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC NSO Spirits Set 2 01] [01006A800016F085][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC NSO Spirits Set 2 02] [01006A800016F086][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Nakoruru Outfit and Wig] [01006A800016F02F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Ninjara Outfit and Wig] [01006A800016F038][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Persona 3 Protagonist Outfit and Wig] [01006A800016F01F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Persona 4 Protagonist] [01006A800016F020][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Pig] [01006A800016F03E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Piranha Plant Standalone Fighter] [01006A800016F001][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Proto Mans Armor and Helmet] [01006A800016F02C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Rabbids Hat] [01006A800016F035][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Ryo Sakazaki Outfit and Wig] [01006A800016F02E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Sans Outfit and Mask] [01006A800016F02B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Shantae Costume] [01006A800016F04D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Slime Hat] [01006A800016F028][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge Various Spirits] [01006A800016F065][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge Various Spirits] [01006A800016F066][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge Various Spirits] [01006A800016F067][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge various Spirits] [01006A800016F068][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F069][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 3 Bonus 5000 ingame Gold and 3 Classic Tickets] [01006A800016F06E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 3 Bonus 5000 ingame Gold and 3 Classic Tickets] [01006A800016F06F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F070][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F071][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F072][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F073][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target!] [01006A800016F077][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target!] [01006A800016F078][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target!] [01006A800016F079][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target] [01006A800016F07A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target] [01006A800016F07B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 1] [01006A800016F07E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 2] [01006A800016F07F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 3] [01006A800016F080][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 4] [01006A800016F081][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 5] [01006A800016F082][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Booster Bundle 2 Reaching Lv. Max 2] [01006A800016F088][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirit Booster Bundle 2 Reaching Lv. Max] [01006A800016F087][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Spirits Set 1 Legend Support and Ace Primary] [01006A800016F084][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Super Smash Bros Ultimate Challenger Pack 7] [01006A800016F008][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC Tails Outfit and Hat] [01006A800016F023][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Team Rocket Outfit and Hat] [01006A800016F029][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Teddie Hat] [01006A800016F021][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Tifas Outfit] [01006A800016F044].nsp",
    "/d/Super Smash Bros Ultimate [DLC Travis] [01006A800016F040][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Vault Boy Outfit and Mask] [01006A800016F03B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Vault Shopper Set 2 Classic Tickets and Gold for Music Mii Costumes and More] [01006A800016F07D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Veronicas Outfit and Hat] [01006A800016F027][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Xs Armor and Helmet] [01006A800016F036][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC Zeros Armor and Helmet] [01006A800016F02D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC-124] [01006A800016F07C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC-131] [01006A800016F083][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC-72] [01006A800016F048][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC-73] [01006A800016F049][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC-74] [01006A800016F04A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC-75] [01006A800016F04B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Aeriths Outfit] [01006A800016F045].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Akira Outfit and Wig] [01006A800016F031][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Altïar Outfit and Hood] [01006A800016F034][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Barrets Outfit] [01006A800016F043].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Bomberman] [01006A800016F041][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Callie Outfit and Wig] [01006A800016F039][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 10] [01006A800016F00B][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 11] [01006A800016F00C][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 1] [01006A800016F002][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 2] [01006A800016F003][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 3] [01006A800016F004][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 4] [01006A800016F005][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 5] [01006A800016F006][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 6] [01006A800016F007][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 8] [01006A800016F009][v131072].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Challenger Pack 9] [01006A800016F00A][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Chocobo Hat] [01006A800016F046].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Costume Doom Slayers Armor and Helmet] [01006A800016F052][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Costume Judd Hat] [01006A800016F050][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Costume Octoling Wig] [01006A800016F051][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Creeper] [01006A800016F03D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Cuphead Outfit and Hat] [01006A800016F033][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Dante Costume] [01006A800016F04C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Diamond] [01006A800016F03F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Dragonborn Costume] [01006A800016F04E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Erdricks Armour and Helmet] [01006A800016F025][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Fighters Pass Bonus Mii Fighter Costume Ancient Soldier] [01006A800016F016][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Fighters Pass Bonus Mii Fighter Costume Rex] [01006A800016F015][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Geno Hat Outfit] [01006A800016F047].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Gils] [01006A800016F042][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Goemon Outfit and Wig] [01006A800016F02A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Heihachi Outfit and Wig] [01006A800016F03C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Iori Yagami Outfit and Wig] [01006A800016F030][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Jackys Outfit and Wig] [01006A800016F032][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Knuckles Outfit and Hat] [01006A800016F024][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Lloyd Costume] [01006A800016F04F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Marie Outfit and Wig] [01006A800016F03A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Martial Artist Gi and Wig] [01006A800016F026][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC MegaMan EXEs Armor and Helmet] [01006A800016F037][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Morgana Hat] [01006A800016F022][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC NSO Spirits Set 2 01] [01006A800016F085][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC NSO Spirits Set 2 02] [01006A800016F086][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Nakoruru Outfit and Wig] [01006A800016F02F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Ninjara Outfit and Wig] [01006A800016F038][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Persona 3 Protagonist Outfit and Wig] [01006A800016F01F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Persona 4 Protagonist] [01006A800016F020][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Pig] [01006A800016F03E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Piranha Plant Standalone Fighter] [01006A800016F001][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Proto Mans Armor and Helmet] [01006A800016F02C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Rabbids Hat] [01006A800016F035][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Ryo Sakazaki Outfit and Wig] [01006A800016F02E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Sans Outfit and Mask] [01006A800016F02B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Shantae Costume] [01006A800016F04D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Slime Hat] [01006A800016F028][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge Various Spirits] [01006A800016F065][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge Various Spirits] [01006A800016F066][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge Various Spirits] [01006A800016F067][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 1 Challenge various Spirits] [01006A800016F068][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F069][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 2 Challenge Strong Enemies] [01006A800016F06D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 3 Bonus 5000 ingame Gold and 3 Classic Tickets] [01006A800016F06E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 3 Bonus 5000 ingame Gold and 3 Classic Tickets] [01006A800016F06F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F070][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F071][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F072][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 4 Bolster Your Spirits] [01006A800016F073][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target!] [01006A800016F077][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target!] [01006A800016F078][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target!] [01006A800016F079][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target] [01006A800016F07A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 5 Snipe your Target] [01006A800016F07B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 1] [01006A800016F07E][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 2] [01006A800016F07F][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 3] [01006A800016F080][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 4] [01006A800016F081][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Board Challenge Pack 7 - 5] [01006A800016F082][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Booster Bundle 2 Reaching Lv. Max 2] [01006A800016F088][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirit Booster Bundle 2 Reaching Lv. Max] [01006A800016F087][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Spirits Set 1 Legend Support and Ace Primary] [01006A800016F084][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Super Smash Bros Ultimate Challenger Pack 7] [01006A800016F008][v65536].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Tails Outfit and Hat] [01006A800016F023][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Team Rocket Outfit and Hat] [01006A800016F035][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Teddie Hat] [01006A800016F021][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Tifas Outfit] [01006A800016F044].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Travis] [01006A800016F040][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Vault Boy Outfit and Mask] [01006A800016F03B][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Vault Shopper Set 2 Classic Tickets and Gold for Music Mii Costumes and More] [01006A800016F07D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Veronicas Outfit and Hat] [01006A800016F027][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Xs Armor and Helmet] [01006A800016F036][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC Zeros Armor and Helmet] [01006A800016F02D][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC-124] [01006A800016F07C][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC-131] [01006A800016F083][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC-72] [01006A800016F048][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC-73] [01006A800016F049][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC-74] [01006A800016F04A][v0].nsp",
    "/d/Super Smash Bros Ultimate [DLC] [NSP] Switch/Super Smash Bros Ultimate [DLC-75] [01006A800016F04B][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Challenger Pack 11] [01006A800016F00C][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Aeriths Outfit] [01006A800016F045][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Akira Outfit and Wig] [01006A800016F031][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Altaïr Outfit and Hood] [01006A800016F034][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Arthurs Armor and Helm] [01006A800016F048][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Barrets Outfit] [01006A800016F043][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Bomberman Outfit and Mask] [01006A800016F041][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Callie Outfit and Wig] [01006A800016F039][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Chocobo Hat] [01006A800016F046][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Creeper Outfit and Mask] [01006A800016F03D][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Cuphead Outfit and Hat] [01006A800016F033][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Dante Outfit and Wig] [01006A800016F04C][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Diamond Armor and Helmet] [01006A800016F03F][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Doom Slayers Armor and Helmet][01006A800016F052].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Dragonborn Outfit and Helm] [01006A800016F04E][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Erdricks Armor and Helmet] [01006A800016F025][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Felyne Hat] [01006A800016F049][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Geno Hat + Outfit] [01006A800016F047][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Gils Armor and Helmet] [01006A800016F042][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Goemon Outfit and Wig] [01006A800016F02A][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Heihachi Outfit and Wig] [01006A800016F03C][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Hunters Mail and Helm] [01006A800016F04A][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Iori Yagami Outfit and Wig] [01006A800016F030][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Jackys Outfit and Wig] [01006A800016F032][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Judd Hat][01006A800016F050].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Knuckles Outfit and Hat] [01006A800016F024][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Lloyd Outfit and Wig] [01006A800016F04F][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Marie Outfit and Wig] [01006A800016F03A][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Martial Artist Gi and Wig] [01006A800016F026][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume MegaMan EXEs Armor and Helmet] [01006A800016F037][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Morgana Hat] [01006A800016F022][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Nakoruru Outfit and Wig] [01006A800016F02F][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Ninjara Outfit and Wig] [01006A800016F038][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Octoling Wig][01006A800016F051].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Persona 3 Protagonist Outfit and Wig] [01006A800016F01F][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Persona 4 Protagonist Outfit and Wig] [01006A800016F020][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Pig Outfit and Mask] [01006A800016F03E][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Proto Mans Armor and Helmet] [01006A800016F02C][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Rabbids Hat] [01006A800016F035][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Rathalos Mail and Helm] [01006A800016F04B][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Ryo Sakazaki Outfit and Wig] [01006A800016F02E][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Sans Outfit and Mask] [01006A800016F02B][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Shantae Outfit, Wig, and Song] [01006A800016F04D][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Slime Hat] [01006A800016F028][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Tails Outfit and Hat] [01006A800016F023][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Team Rocket Outfit and Hat] [01006A800016F029][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Teddie Hat] [01006A800016F021][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Tifas Outfit] [01006A800016F044][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Travis Outfit and Wig] [01006A800016F040][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Vault Boy Outfit and Mask] [01006A800016F03B][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Veronicas Outfit and Hat] [01006A800016F027][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Xs Armor and Helmet] [01006A800016F036][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Costume Zeros Armor and Helmet] [01006A800016F02D][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Fighters Pass Bonus Mii Fighter Costume Ancient Soldier] [01006A800016F016][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F065][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F066][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F067][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F068][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F069][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06A][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06B][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06C][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06D][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 3 -Bonus 5000 in-game Gold and 3 Classic Tickets -] [01006A800016F06E][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 3 -Bonus 5000 in-game Gold and 3 Classic Tickets -] [01006A800016F06F][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F070][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F071][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F072][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F073][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F077][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F078][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F079][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F07A][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F07B][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F07E][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F07F][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F080][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F081][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F082][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Booster Bundle 2 - Reaching Lv MAX] [01006A800016F087][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirit Booster Bundle 2 - Reaching Lv MAX] [01006A800016F088][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirits Set 1 - Legend Support and Ace Primary] [01006A800016F083][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirits Set 1 - Legend Support and Ace Primary] [01006A800016F084][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirits Set 2 - Legend-Class Primary  Ace-Class Support] [01006A800016F085][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Spirits Set 2 - Legend-Class Primary  Ace-Class Support] [01006A800016F086][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 10] [01006A800016F00B][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 1] [01006A800016F002][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 2] [01006A800016F003][v131072].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 3] [01006A800016F004][v131072].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 4] [01006A800016F005][v131072].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 5] [01006A800016F006][v131072].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 6] [01006A800016F007][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 7] [01006A800016F008][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 8] [01006A800016F009][v131072].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 9] [01006A800016F00A][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Fighters Pass Bonus Mii Fighter Costume Rex] [01006A800016F015][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Super Smash Bros Ultimate Piranha Plant Standalone Fighter] [01006A800016F001][v65536].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Vault Shopper Set 2 -Classic Tickets and Gold for Music, Mii Costumes, and More-] [01006A800016F07C][v0].nsp",
    "/d/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate(99 DLC) Incluidos outfit/Super Smash Bros Ultimate [Vault Shopper Set 2 -Classic Tickets and Gold for Music, Mii Costumes, and More-] [01006A800016F07D][v0].nsp",
    "/d/Super.Mario.Maker.2.01009B90006DC800.v458752.nsp",
    "/d/THE HOUSE OF THE DEAD Remake [v1.1.0].xci",
    "/d/TLoZ EoW Update 1.0.1 (v65536).nsp",
    "/d/TMNT Mutants Unleashed [010013001BD62000][v0].nsp",
    "/d/TMNT Mutants Unleashed [010013001BD62800][v196608].nsp",
    "/d/TMNT Shredders Revenge [0100FE701475A000][v0].nsp",
    "/d/TMNT Shredders Revenge [0100FE701475A800][v589824].nsp",
    "/d/TMNT Splintered Fate [01005CF01E784000][v0].nsp",
    "/d/TMNT Splintered Fate [01005CF01E784800][v655360].nsp",
    "/d/TMNT_Mutants_Unleashed_DLC_1984_Comic_Book_Pack_010013001BD63002v0.nsp",
    "/d/TMNT_Mutants_Unleashed_DLC_1987_Animated_Series_Pack_010013001BD63001v0.nsp",
    "/d/TMNT_Mutants_Unleashed_DLC_Fresh_Meat_Mission_Pack_010013001BD63004v0.nsp",
    "/d/TMNT_Mutants_Unleashed_DLC_Metalheads_Pack_010013001BD63003v0.nsp",
    "/d/TMNT_Shredders_Revenge_DLC_Dimension_Shellshock_0100FE701475B001v0.nsp",
    "/d/TMNT_Shredders_Revenge_DLC_Radical_Reptiles_0100FE701475B002v0.nsp",
    "/d/TMNT_Splintered_Fate_DLC_Casey_Jones_and_the_Junkyard_Jam_01005CF01E785001v0.nsp",
    "/d/Tales_of_Graces_f_Remastered_Super_Growth_Support_Herb_Set_DLC_.nsp",
    "/d/Tangle Tower [0100F7600F3B8000][v0].nsp",
    "/d/Team Sonic Racing [010092B0091D0800][v131072][US].nsp",
    "/d/Teenage Mutant Ninja Turtles The Cowabunga Collection [0100FDB0154E4000][v0].nsp",
    "/d/Teenage_Mutant_Ninja_Turtles_Arcade_Wrath_of_the_Mutants_0100C7.nsp",
    "/d/Teenage_Mutant_Ninja_Turtles_Arcade_Wrath_of_the_Mutants_0100C7601CDAC000v0.nsp",
    "/d/Teenage_Mutant_Ninja_Turtles_The_Cowabunga_Collection_0100FDB0154E4800v262144.nsp",
    "/d/Terraria [0100E46006708000][v0].nsp",
    "/d/Terraria [0100E46006708800][v1114112].nsp",
    "/d/The Elder Scrolls V Skyrim.nsp",
    "/d/The Legend of Zelda Breath of the Wild [01007EF00011E000][v0].nsp",
    "/d/The Legend of Zelda Breath of the Wild [01007EF00011E800][v786432].nsp",
    "/d/The Legend of Zelda Breath of the Wild [DLC Pack 1 The Master Trials] [01007EF00011F001][v196608].nsp",
    "/d/The Legend of Zelda Echoes of Wisdom [01008CF01BAAC0].nsp",
    "/d/The Legend of Zelda Links Awakening [01006BB00C6F0800][v65536].nsp",
    "/d/The Legend of Zelda Skyward Sword HD [01002DA013484000][v0] (7.07 GB).nsp",
    "/d/The Legend of Zelda Skyward Sword HD [01002DA013484800][v65536] (0.04 GB).nsp",
    "/d/The Legend of Zelda Tears of the Kingdom [0100F2C0115B6000][v0].nsp",
    "/d/The Witcher 3 Wild Hunt (EU) [01003D100E9C6000][v0] (28.01 GB).nsp",
    "/d/The Witcher 3 Wild Hunt (EU) [01003D100E9C6800][v458752] (11.12 GB).nsp",
    "/d/The_Legend_of_Zelda_Links_Awakening_1_0_0_NSP_RUS+ENG_Nintendo_Switch/The Legend of Zelda Links Awakening [01006BB00C6F0000][v0] (5.84 GB).nsp",
    "/d/Toki Remake.nsp",
    "/d/Tomodachi Life Living the Dream.nsp",
    "/d/Trine 2 Complete Story.nsp",
    "/d/Trine 4 - The Nightmare Prince.nsp",
    "/d/Turok 2.nsp",
    "/d/Turok 3 Shadow of Oblivion [010013D019CF4000][USA][v0].nsp",
    "/d/Turok 3 Shadow of Oblivion [010013D019CF4800][USA][v65536].nsp",
    "/d/Turok.nsp",
    "/d/Unravel TWO v1.0.1.xci",
    "/d/Vampire Crawlers [v1.4.0].xci",
    "/d/WARRIORS_Abyss_dynasty_warriors_costume_set_DLC01005AE0209A9001v0US.nsp",
    "/d/WarioWare Move It! [010045B018EC2000][USA][v0].nsp",
    "/d/Xenoblade Chronicles 3 [010074F013262800][v655360].nsp",
    "/d/Xenoblade Chronicles X Definitive Edition [0100453019AA8000][v0].nsp",
    "/d/Xenoblade_Chronicles_X_Definitive_Edition_0100453019AA8800v65536.nsp",
    "/d/Yu-Gi-Oh Early Days Collection [01000D001FF18000][v0].nsp",
    "/d/Yu-Gi-Oh Early Days Collection [01000D001FF18800][v65536].nsp",
    "/d/Yu-Gi-Oh! RUSH DUEL Dawn of the Battle Royale!! [0100261015BE2000][v0] (3.04 GB).nsp",
    "/d/Yu_Gi_Oh!_Legacy_of_the_Duelist_Link_Evolution_010022400BE5A000v0.nsp",
    "/d/Yu_Gi_Oh!_Legacy_of_the_Duelist_Link_Evolution_010022400BE5A800v65536.nsp",
    "/d/Yu_Gi_Oh!_RUSH_DUEL_Dawn_of_the_Battle_Royale!!_0100261015BE2800v262144.nsp",
    "/d/[NSW] AeternoBlade.nsp",
    "/d/[NSW] Agatha Knife.nsp",
    "/d/atmosphere/contents/0100000000000352/exefs.nsp",
    "/d/atmosphere/contents/010000000000bd00/exefs.nsp",
    "/d/atmosphere/contents/054e4f4558454000/exefs.nsp",
    "/d/atmosphere/contents/420000000000000B/exefs.nsp",
    "/d/atmosphere/contents/420000000007E51A/exefs.nsp",
    "/d/atmosphere/contents/690000000000000D/exefs.nsp",
    "/d/atmosphere/hbl.nsp",
    "/d/bbb-h-aab8a.xci",
    "/d/hbmenu.nsp",
    "/d/hbmenu_[0104444444440000].nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd005.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd006.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd007.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd008.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd009.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd00a.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd00b.nsp",
    "/d/sxs-sniper_elite_4_dlc_010007b010fcd00c.nsp",
    "/d/sxs-sniper_elite_4_multiplayer_maps_pack_dlc.nsp",
    "/d/v-astralchain.nsp",
    "/d/v-sniper_elite_4_deathstorm_part_1_inception_dlc.nsp",
    "/d/v-sniper_elite_4_deathstorm_part_2_infiltration_dlc.nsp",
    "/d/v-sniper_elite_4_deathstorm_part_3_obliteration_dlc.nsp",
    "/d/v-sniper_elite_4_target_fuhrer_dlc.nsp",
]

# ============================================================
# LISTA COMPLETA DISCO E: (557 archivos)
# ============================================================
E_FILES = [
    "/e/0003 - ARMS (World) (En,Ja,Fr,De,Es,It,Nl,Ru).xci",
    "/e/2 DLC/AVICII Invector [DLC Magma Track Pack] [010064600F983002][v0].nsp",
    "/e/2 DLC/AVICII Invector [DLC TIM Track Pack] [010064600F983001][v0].nsp",
    "/e/A Hat in Time [DLC Nyakuza Metro][v0].nsp",
    "/e/A Hat in Time [DLC Seal the Deal][v0].nsp",
    "/e/ACA NEOGEO Money Puzzle Exchanger [010038f00afa0000][v0].nsp",
    "/e/ACA NEOGEO NEO TURF MASTERS/ACA NEOGEO NEO TURF MASTERS [01002e70032e8000][v0].nsp",
    "/e/ACA NEOGEO NEO TURF MASTERS/ACA NEOGEO NEO TURF MASTERS [UPD][01002e70032e8800][v65536].nsp",
    "/e/ACA NEOGEO OVER TOP [01003a5001dba000][v0].nsp",
    "/e/ACA NEOGEO SAMURAI SHODOWN IV [010047f001dbc000][v0].nsp",
    "/e/ACA NEOGEO SAMURAI SHODOWN [01005c9002b42000][v0].nsp",
    "/e/ACA NEOGEO SENGOKU 2 [01009b300872a000][v0].nsp",
    "/e/ACA NEOGEO SHOCK TROOPERS/ACA NEOGEO SHOCK TROOPERS [01008a9001dc2000][v0].nsp",
    "/e/ACA NEOGEO SHOCK TROOPERS/ACA NEOGEO SHOCK TROOPERS [UPD][01008a9001dc2800][v65536].nsp",
    "/e/ACA NEOGEO SPIN MASTER [01007d1004dba000][v0].nsp",
    "/e/ACA NEOGEO SUPER SIDEKICKS 2/ACA NEOGEO SUPER SIDEKICKS 2 [010055a00a300000][v0].nsp",
    "/e/ACA NEOGEO SUPER SIDEKICKS 2/ACA NEOGEO SUPER SIDEKICKS 2 [UPD][010055a00a300800][v65536].nsp",
    "/e/ACA NEOGEO SUPER SIDEKICKS 3  THE NEXT GLORY/ACA NEOGEO SUPER SIDEKICKS 3  THE NEXT GLORY [0100a4d00a308000][v0].nsp",
    "/e/ACA NEOGEO SUPER SIDEKICKS 3  THE NEXT GLORY/ACA NEOGEO SUPER SIDEKICKS 3  THE NEXT GLORY [UPD][0100a4d00a308800][v65536].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '94 [0100eb2001dcc000][v0].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '95/ACA NEOGEO THE KING OF FIGHTERS '95 [01009dc001db6000][v0].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '95/ACA NEOGEO THE KING OF FIGHTERS '95 [UPD][01009dc001db6800][v65536].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '96 [01006f0004fb4000][v0].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '97 [0100170008728000][v0].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '98/ACA NEOGEO THE KING OF FIGHTERS '98 [0100b42001db4000][v0].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '98/ACA NEOGEO THE KING OF FIGHTERS '98 [UPD][0100b42001db4800][v65536].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS '99 [0100583001dca000][v0].nsp",
    "/e/ACA NEOGEO THE KING OF FIGHTERS 2000 [0100b97002b44000][v0].nsp",
    "/e/ACA NEOGEO THE LAST BLADE 2 [0100699008792000][v0].nsp",
    "/e/ACA NEOGEO THE SUPER SPY [0100f7f00afa2000][v0].nsp",
    "/e/ACA NEOGEO WAKU WAKU 7/ACA NEOGEO WAKU WAKU 7 [0100cef001dc0000][v0].nsp",
    "/e/ACA NEOGEO WAKU WAKU 7/ACA NEOGEO WAKU WAKU 7 [UPD][0100cef001dc0800][v131072].nsp",
    "/e/ACA NEOGEO WORLD HEROES PERFECT/ACA NEOGEO WORLD HEROES PERFECT [01009d4001dc4000][v0].nsp",
    "/e/ACA NEOGEO WORLD HEROES PERFECT/ACA NEOGEO WORLD HEROES PERFECT [UPD][01009d4001dc4800][v65536].nsp",
    "/e/APLICACIONES PARA NINTENDO SWITCH MAGICA/nsp/DBI.nsp",
    "/e/APLICACIONES PARA NINTENDO SWITCH MAGICA/nsp/HBL INSTALADOR.nsp",
    "/e/APLICACIONES PARA NINTENDO SWITCH MAGICA/nsp/USB File Transfer.nsp",
    "/e/APLICACIONES PARA NINTENDO SWITCH MAGICA/nsp/YouTube v2.0.0 Patched [05003A400C3DA000][v262144].nsp",
    "/e/ARK Survival Evolved [0100D4A00B284800][v851968][US].nsp",
    "/e/ARK Survival Evolved [ARK Aberration] [0100D4A00B285002][v131072][US].nsp",
    "/e/ARK Survival Evolved [ARK Ragnarok] [0100D4A00B285004][v65536][US].nsp",
    "/e/ARK Survival Evolved [ARK Scorched Earth] [0100D4A00B285001][v262144][US].nsp",
    "/e/ARK Survival Evolved [ARK Survival Evolved Aberrant Skins Pack] [0100D4A00B28500C][v131072][US].nsp",
    "/e/ARK Survival Evolved [ARK Survival Evolved HLN-A Cosmetic Pet] [0100D4A00B28500D][v262144][US].nsp",
    "/e/A_Space_for_the_Unbound_01006BF01923E000v0USnsw2u_com.xci",
    "/e/A_Space_for_the_Unbound_01006BF01923E800v196608USnsw2u_com.nsp",
    "/e/Arcade Archives 10-Yard Fight/Arcade Archives 10-Yard Fight [0100be80097fa000][v0].nsp",
    "/e/Arcade Archives 10-Yard Fight/Arcade Archives 10-Yard Fight [UPD][0100be80097fa800][v65536].nsp",
    "/e/Arcade Archives CRAZY CLIMBER [0100bb1001dd6000][v0].nsp",
    "/e/Arcade Archives City Connection/Arcade Archives City Connection [010007a00980c000][v0].nsp",
    "/e/Arcade Archives City Connection/Arcade Archives City Connection [UPD][010007a00980c800][v65536].nsp",
    "/e/Arcade Archives DONKEY KONG [0100e9e00b052000][v0].nsp",
    "/e/Arcade Archives DOUBLE DRAGON [0100f25001dd0000][v0].nsp",
    "/e/Arcade Archives HEROIC EPISODE US [01009A4008A30000][v0].nsp",
    "/e/Arcade Archives Ikki US [01000DB00980A000][v0].nsp",
    "/e/Arcade Archives Kid Niki Radical Ninja US [010010B008A36000][v0].nsp",
    "/e/Arcade Archives Kid's Horehore Daisakusen US [0100E7C001DE0000][v0].nsp",
    "/e/Arcade Archives MOON PATROL/Arcade Archives MOON PATROL [01003000097fe000][v0].nsp",
    "/e/Arcade Archives MOON PATROL/Arcade Archives MOON PATROL [UPD][01003000097fe800][v65536].nsp",
    "/e/Arcade Archives Mario Bros/Arcade Archives Mario Bros. [0100755004608000][v0].nsp",
    "/e/Arcade Archives Mario Bros/Arcade Archives Mario Bros. [UPD][0100755004608800][v65536].nsp",
    "/e/Arcade Archives Ninja-Kid US [0100369001DDC000][v0].nsp",
    "/e/Arcade Archives OMEGA FIGHTER [01004a200bb48000][v0].nsp",
    "/e/Arcade Archives PUNCH-OUT!!/Arcade Archives PUNCH-OUT!! [01001530097f8000][v0].nsp",
    "/e/Arcade Archives PUNCH-OUT!!/Arcade Archives PUNCH-OUT!! [UPD][01001530097f8800][v65536].nsp",
    "/e/Arcade Archives Renegade [010081e001dd2000][v0].nsp",
    "/e/Arcade Archives STAR FORCE [010069f008a38000][v0].nsp",
    "/e/Arcade Archives Sky Skipper [010008f00b054000][v0].nsp",
    "/e/Arcade Archives TERRA CRESTA/Arcade Archives TERRA CRESTA US [0100422001DDA000][v0].nsp",
    "/e/Arcade Archives TERRA CRESTA/Arcade Archives TERRA CRESTA US [UPD][0100422001DDA800][v65536].nsp",
    "/e/Arcade Archives TERRA CRESTA/Expeditions A MudRunner Game [Expeditions A MudRunner Game - Cotco Canyon DLC][01002C101C1AB003][v0][US].nsp",
    "/e/Arcade Archives TERRA CRESTA/Expeditions A MudRunner Game [Expeditions A MudRunner Game - Pioneer Pack DLC][01002C101C1AB002][v0][US].nsp",
    "/e/Arcade Archives TERRA CRESTA/Expeditions A MudRunner Game [Expeditions A MudRunner Game - Season 1 DLC][01002C101C1AB004][v0][US].nsp",
    "/e/Arcade Archives TERRA CRESTA/Expeditions A MudRunner Game [Expeditions A MudRunner Game - The Great Don 71 DLC][01002C101C1AB001][v0][US].nsp",
    "/e/Arcade Archives Traverse/Arcade Archives Traverse USA [010029d006ed8000][v0].nsp",
    "/e/Arcade Archives Traverse/Arcade Archives Traverse USA [UPD][010029d006ed8800][v65536].nsp",
    "/e/Arcade Archives VS. SUPER MARIO BROS/Arcade Archives VS. SUPER MARIO BROS. [010021d00812a000][v0].nsp",
    "/e/Arcade Archives VS. SUPER MARIO BROS/Arcade Archives VS. SUPER MARIO BROS. [UPD][010021d00812a800][v131072].nsp",
    "/e/Batman Arkham City [01003F00163CE000][v0][US].nsp",
    "/e/Bayonetta 3 (World) (En,Ja,Fr,De,Es,It,Zh-Hant,Zh-Hans,Ko,Ru)/Bayonetta 3 (World) (En,Ja,Fr,De,Es,It,Zh-Hant,Zh-Hans,Ko,Ru).xci",
    "/e/Bayonetta 3 [01004A4010FEA800][v1.1.0].nsp",
    "/e/Bayonetta Origins Cereza and the Lost Demon [0100CF5010FEC000][v0][US].nsp",
    "/e/Boomerang Fu [DLC Fresh Flavors Pack] [010081A00EE63001][v720896].nsp",
    "/e/Boomerang Fu [DLC Just Desserts] [010081A00EE63002][v0].nsp",
    "/e/Capcom Beat 'Em Up Bundle[multi].xci",
    "/e/Captain Toad Treasure Tracker [01009bf0072d4000][v0].nsp",
    "/e/Castlevania Anniversary Collection [01001A800D6BC000][v0].nsp",
    "/e/Castlevania Anniversary Collection [01001A800D6BC800][v131072].nsp",
    "/e/Chef_Life_A_Restaurant_Simulator_DLC_Al_Forno_Pack_0100F24014281002v0.nsp",
    "/e/Chef_Life_A_Restaurant_Simulator_DLC_Bon_Appetit_Pack_0100F24014281001v0.nsp",
    "/e/Contra Operation Galuga [0100CF401A98E000][v0][US].nsp",
    "/e/Contra Operation Galuga [0100CF401A98E800][USA][v131072].nsp",
    "/e/Crash Team Racing.xci",
    "/e/Cult of the Lamb [01002E7016C46000][v0][US].nsp",
    "/e/Cult of the Lamb [01002E7016C46800][v1179648][US].nsp",
    "/e/Cult of the Lamb[01002E7016C47001][0][2.1.0][DLC].nsp",
    "/e/Cult of the Lamb[01002E7016C47002][0][2.1.0][DLC].nsp",
    "/e/Cult of the Lamb[01002E7016C47003][0][2.8.0][DLC].nsp",
    "/e/Cult of the Lamb[01002E7016C47004].nsp",
    "/e/Cuphead [0100A5C00D162000] + (v131072 UPD) (eshop).xci",
    "/e/CyberR [DLC Green Line] [0100DF9022E0F001][v0].nsp",
    "/e/CyberR [DLC Orange Line] [0100DF9022E0F002][v0].nsp",
    "/e/CyberR [DLC Red Line] [0100DF9022E0F003][v0].nsp",
    "/e/DARK SOULS REMASTERED [01004AB00A260000][v0].nsp",
    "/e/DARK SOULS REMASTERED [01004AB00A260800][v196608].nsp",
    "/e/DLC/Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles [0100309016E7B005][v0].nsp",
    "/e/DLC/Demon Slayer The Hinokami Chronicles [DLC Character Unlock Nezuko Kamado, Zenitsu Agatsuma, Inosuke Hashibira] [0100309016E7B002][v0].nsp",
    "/e/DLC/Demon Slayer The Hinokami Chronicles [DLC Character Unlock Tanjiro Kamado] [0100309016E7B001][v0].nsp",
    "/e/DLC/Sonic Origins [Sonic Origins Classic Music Pack] [01009FB016287003][v0][US].nsp",
    "/e/DLC/Sonic Origins [Sonic Origins Premium Fun Pack] [01009FB016287002][v0][US].nsp",
    "/e/DLC/Sonic Origins [Sonic Origins Start Dash Pack] [01009FB016287001][v0][US].nsp",
    "/e/DOOM Eternal [DLC Campaign] [0100B1A00D8CF003][v0].nsp",
    "/e/DOOM Eternal [DLC Rip and Tear Pack] [0100B1A00D8CF001][v0].nsp",
    "/e/DOOM Eternal [DLC The Ancient Gods - Part Two] [0100B1A00D8CF005][v0].nsp",
    "/e/DOOM Eternal [DLC The Ancient Gods] [0100B1A00D8CF004][v0].nsp",
    "/e/DOOM Eternal [Deluxe Edition Content] [0100B1A00D8CF002][v0].nsp",
    "/e/DOOM/DOOM [0100416004c00000][v0].nsp",
    "/e/DOOM/DOOM [UPD][0100416004c00800][v131072].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Android 17][0100A250097F100D][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Android 21 Unlock][0100A250097F1002][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Anime Music Pack][0100A250097F1005][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Bardock][0100A250097F1007][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Broly][0100A250097F1008][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Character Pack 14][0100A250097F1019][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Commentator Voice Pack 2][0100A250097F101A][US][v65536].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Commentator Voice Pack 3][0100A250097F101B][US][v65536].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Commentator Voice Pack 4][0100A250097F101C][US][v65536].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Commentator Voice Pack][0100A250097F1006][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Cooler][0100A250097F100E][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Exclusive SS Goku Lobby Avatar][0100A250097F100F][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - FighterZ Pack 16][0100A250097F101E][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - FighterZ Pack 17][0100A250097F101F][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - FighterZ Pack 18][0100A250097F1020][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - FighterZ Pack 19][0100A250097F1021][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Gogeta SSGSS][0100A250097F1018][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Goku GT][0100A250097F1016][US][v65536].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Goku][0100A250097F100B][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Janemba][0100A250097F1017][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Jiren][0100A250097F1014][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Kefla][0100A250097F101D][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - SSGSS Goku and SSGSS Vegeta Unlock][0100A250097F1001][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - SSGSS Lobby Avatars][0100A250097F1003][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Stamps Girls Pack][0100A250097F1004][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Vegeta][0100A250097F100C][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Vegito SSGSS][0100A250097F100A][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Videl][0100A250097F1015][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ - Zamasu Fused][0100A250097F1009][US][v0].nsp",
    "/e/DRAGON BALL FIGHTERZ [DRAGON BALL FIGHTERZ – Anime Music Pack 2][0100A250097F1013][US][v0].nsp",
    "/e/DRAGON BALL FighterZ [0100A250097F0800][v851968].nsp",
    "/e/DRAGON_BALL_FIGHTER Z v0.nsp",
    "/e/DREDGE 1.4.2 [01008CD0172D6800][v524288][UPD].nsp",
    "/e/DREDGE [01008CD0172D6000][v0][US].nsp",
    "/e/DREDGE [Blackstone Key DLC][01008CD0172D7002][v0][US].nsp",
    "/e/DREDGE [Custom Rod DLC][01008CD0172D7001][v0][US].nsp",
    "/e/DREDGE [DLC 3] [01008CD0172D7003][v0].nsp",
    "/e/Death's Gambit Afterlife [Ashes of Vados DLC][01006A0015813001][v0][US].nsp",
    "/e/Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles [0100309016E7A800][v1.30].nsp",
    "/e/Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles [0100309016E7B005][v0].nsp",
    "/e/Demon Slayer The Hinokami Chronicles [DLC Character Unlock Nezuko Kamado, Zenitsu Agatsuma, Inosuke Hashibira] [0100309016E7B002][v0].nsp",
    "/e/Demon Slayer The Hinokami Chronicles [DLC Character Unlock Tanjiro Kamado] [0100309016E7B001][v0].nsp",
    "/e/Disney Dreamlight Valley [A Rift In Time DLC][0100D39012C1B002][v0][US].nsp",
    "/e/Donkey Kong Country - Tropical Freeze[multi][xcib].xci",
    "/e/DreadOut 2 [010032B01C6F2000][v0][US](nsw2u.com).nsp",
    "/e/DreadOut 2 [010032B01C6F2800][v131072][US](nsw2u.com).nsp",
    "/e/ENDER LILIES Quietus of the Knights [0100CCF012E9A000].nsp",
    "/e/ENDER LILIES Quietus of the Knights [0100CCF012E9A800][US][131072].nsp",
    "/e/Expeditions A MudRunner Game [Expeditions A MudRunner Game - Cotco Canyon DLC][01002C101C1AB003][v0][US].nsp",
    "/e/Expeditions A MudRunner Game [Expeditions A MudRunner Game - Pioneer Pack DLC][01002C101C1AB002][v0][US].nsp",
    "/e/Expeditions A MudRunner Game [Expeditions A MudRunner Game - Season 1 DLC][01002C101C1AB004][v0][US].nsp",
    "/e/Expeditions A MudRunner Game [Expeditions A MudRunner Game - The Great Don 71 DLC][01002C101C1AB001][v0][US].nsp",
    "/e/FIFA 18/FIFA 18 [0100f7b002340000][v0].nsp",
    "/e/FIFA 18/FIFA 18 [UPD][0100f7b002340800][v458752].nsp",
    "/e/FINAL FANTASY IX.nsp",
    "/e/FateEXTELLA [010053e002ea2000][v0].nsp",
    "/e/Fire Emblem Three Houses [Additional Quests][010055D009F79004][US][v196608].nsp",
    "/e/Fire Emblem Three Houses [Additional Support Items][010055D009F79005][US][v196608].nsp",
    "/e/Fire Emblem Three Houses [Auxiliary Battle Maps][010055D009F79003][US][v196608].nsp",
    "/e/Fire Emblem Three Houses [New Attire][010055D009F79002][US][v262144].nsp",
    "/e/Fire Emblem Three Houses [Officers Academy Uniform Byleth][010055D009F79006][US][v262144].nsp",
    "/e/Fire Emblem Three Houses [Side Story Cindered Shadows][010055D009F79001][US][v196608].nsp",
    "/e/Fire Emblem Three Houses[010055D009F78800][v1.2.0][v327680].nsp",
    "/e/Fire Emblem Warriors Three Hopes [Digital Purchase DLC][010071F0143EA000][v0][US].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors  [Fire Emblem Awakening DLC Pack] [DLC][0100f15003e65004][v65536].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors  [Fire Emblem Fates DLC Pack] [DLC][0100f15003e65002][v131072].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors  [Fire Emblem Shadow Dragon DLC Pack] [DLC][0100f15003e65003][v65536].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors  [Japanese-Voice Pack] [DLC][0100f15003e65005][v0].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors  [Lucina's Bridal Costume] [DLC][0100f15003e65001][v0].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors [0100f15003e64000][v0].nsp",
    "/e/Fire Emblem Warriors/Fire Emblem Warriors [UPD][0100f15003e64800][v327680].nsp",
    "/e/Fizeau Hechizos MOd/atmosphere/contents/0100000000000F12/exefs.nsp",
    "/e/Fran Bow [010061701A53E000][v0][US] .nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1001].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1002].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1003].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1004].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1005].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1006].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1007].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1008].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1009].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff100a].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff100b].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff100c].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff100d].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff100e].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff100f].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1010].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1011].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1012].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1013].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1014].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1015].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1016].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1017].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1018].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1019].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff101a].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff101b].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff101c].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff101d].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff101e].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff101f].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1020].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1021].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1022].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1023].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1024].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1025].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1026].nsp",
    "/e/Gear.Club Unlimited 2[DLC][10072900aff1027].nsp",
    "/e/Gear.Club Unlimited [DLC Limited Edition Cars Pack 1 BMW M2 Coupe Sanguine][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Limited Edition Cars Pack 1][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Limited Edition Cars Pack 2 Alpha Romeo 4C Italian Pike][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Limited Edition Cars Pack 2][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Mclaren 570S GT4 Orange][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Mclaren 570S GT4 Pack][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Mclaren 570S GT4 White][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Premium Car Chevrolet Camaro 50th Anniversary][v0].nsp",
    "/e/Gear.Club Unlimited [DLC Premium Car Nissan 370z Nismo][v0].nsp",
    "/e/Gear.Club Unlimited [DLC Super Car Mazzanti Evantra][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Super Car Pagani Zonda Cinque][v65536].nsp",
    "/e/Gear.Club Unlimited [DLC Super Car W Motors Lykan Hypersport][v65536].nsp",
    "/e/Grace of Letoile [Damage x2 - Grace of Letoile] [0100CAC01C3ED003][v0][US].nsp",
    "/e/Grace of Letoile [Experience x3 - Grace of Letoile] [0100CAC01C3ED001][v0][US].nsp",
    "/e/Grace of Letoile [No Encounters - Grace of Letoile] [0100CAC01C3ED002][v0][US].nsp",
    "/e/Guacamelee STCE [0100bae00b470000][v0].nsp",
    "/e/Guacamelee! 2 DLC [01007E100456D001].nsp",
    "/e/Guacamelee! 2 DLC [01007E100456D002].nsp",
    "/e/Guacamelee! 2 [01007E100456C000].nsp",
    "/e/Guacamelee! 2 [01007E100456C800][v196608].nsp",
    "/e/Hellblade Senua's Sacrifice [Update v1.0.1].nsp",
    "/e/Hero of Fate [Western Horizon Adventures DLC][010082501DAF3001][v0][US].nsp",
    "/e/Hollow Knight/Hollow Knight [0100633007d48000][v0].nsp",
    "/e/Hollow Knight/Hollow Knight [UPD][0100633007d48800][v131072].nsp",
    "/e/Hungry Shark World/Hungry Shark World [0100e1a00af40000][v0].nsp",
    "/e/Hungry Shark World/Hungry Shark World [UPD][0100e1a00af40800][v65536].nsp",
    "/e/Hyrule Warriors Definitive Edition [v65536].nsp",
    "/e/Hyrule Warriors Definitive Edition/Hyrule Warriors Definitive Edition [0100ae00096ea000][v0].nsp",
    "/e/Hyrule Warriors Definitive Edition/Hyrule Warriors Definitive Edition [UPD][0100ae00096ea800][v65536].nsp",
    "/e/ICEY [0100be9007e7e000][v0].nsp",
    "/e/Indivisible [01001D3003FDE000][v0].nsp",
    "/e/Jujutsu Kaisen Cursed Clash [010085401A454800][v65536][EU].nsp",
    "/e/Jujutsu Kaisen Cursed Clash [Jujutsu High First-Years Outfit Set DLC][010085401A455001][v0][EU].nsp",
    "/e/Jurassic_Park_Classic_Games_Collection_0100D4801BF26000v0USnsw2u.nsp",
    "/e/KDB.nsp",
    "/e/KF2.nsp",
    "/e/KONOSUBA - God's blessing on this wonderful world! Love for these clothes of desire! v1.0.0 [01001F501A9AA000][v0][APP].nsp",
    "/e/KSA Update[v327680].nsp",
    "/e/KSA.nsp",
    "/e/Kirby Star Allies/Kirby Star Allies [01007e3006dda000][v0].nsp",
    "/e/Kirby Star Allies/Kirby Star Allies [UPD][01007e3006dda800][v262144].nsp",
    "/e/Kirby and the Forgotten Land [01004D300C5AE000][v0].nsp",
    "/e/Kirby's Return to Dream Land Deluxe [01006B601380E000][v0].nsp",
    "/e/LEGO Horizon Adventures [NSP]/LEGO Horizon Adventures [010073C01AF34000][v0].nsp",
    "/e/LEGO Horizon Adventures [NSP]/LEGO Horizon Adventures [010073C01AF34800][v262144].nsp",
    "/e/LEGO Horizon Adventures [NSP]/LEGO Horizon Adventures [DLC Digital Deluxe Edition Content] [010073C01AF35001].nsp",
    "/e/LEGO Horizon Adventures [NSP]/LEGO Horizon Adventures [DLC Pre-order Content] [010073C01AF35002].nsp",
    "/e/LEGO Worlds/LEGO Worlds [0100838002aea000][v0].nsp",
    "/e/LEGO Worlds/LEGO(r) Worlds [Classic Space Pack] [DLC][0100838002aeb003][v0].nsp",
    "/e/LEGO Worlds/LEGO(r) Worlds [DLC][0100838002aeb00a][v0].nsp",
    "/e/LEGO Worlds/LEGO(r) Worlds [Monsters Pack] [DLC][0100838002aeb007][v65536].nsp",
    "/e/LEGO Worlds/LEGO(r) Worlds [UPD][0100838002aea800][v393216].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Agents of Atlas Character Pack] [DLC][01007690040a1003][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Champions Character Pack] [DLC][01007690040a1005][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Classic Guardians of the Galaxy Character Pack ] [DLC][01007690040a1001][v0].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Cloak And Dagger Character and Level Pack] [DLC][01007690040a1007][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Marvel's Ant-Man and the Wasp Character and Level Pack] [DLC][01007690040a100a][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Marvel's Avengers Infinity War Movie Level Pack] [DLC][01007690040a1009][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Marvel's Black Panther Movie Character and Level Pack] [DLC][01007690040a1006][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Marvel's Guardians of the Galaxy Vol. 2 Movie Level Pack] [DLC][01007690040a1004][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Out of Time Character Pack] [DLC][01007690040a1002][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [Runaways Level and Character Pack] [DLC][01007690040a1008][v65536].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO(r) Marvel Super Heroes 2 [UPD][01007690040a0800][v393216].nsp",
    "/e/LEGO® MARVEL Super Heroes 2 (EU)/LEGO® MARVEL Super Heroes 2 (EU) [01007690040a0000][v0].nsp",
    "/e/Life is Strange Double Exposure [0100B2301F4A8800][v65536].nsp",
    "/e/Little Misfortune [0100E7000E826000][v0].nsp",
    "/e/Little Nightmares Complete Edition/Little Nightmares Complete Edition [UPD][01002fc00412c800][v65536].nsp",
    "/e/Little Nightmares Complete Edition/Little Nightmares [01002fc00412c000][v0].nsp",
    "/e/Little Nightmares Complete Edition/Little Nightmares [DLC][01002fc00412d001][v0].nsp",
    "/e/Little Nightmares Complete Edition/Little Nightmares [DLC][01002fc00412d002][v0].nsp",
    "/e/Luigis Mansion 2 HD[010048701995E000][1.0.0][0][17.0.1].nsp",
    "/e/Luigis Mansion 3.nsp",
    "/e/MARVELvsCAPCOM Fighting Collection Arcade Classics.nsp",
    "/e/MEGA MAN BATTLE & FIGHTERS [01003DF018D5A000][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [Edition Upgrade (Deluxe) DLC][01003EB01C2F1009][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [Musashi Wired Purchase Bonus DLC][01003EB01C2F1031][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire arshem captains uniform DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire arshem dress DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire arshem yukata DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire masamune casual DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire momoka yukata DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire victor yukata DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire yamato student uniform DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [attire yamato yukata DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [fashionable pack vol 1 DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [fashionable pack vol 2 DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [fashionable pack vol 3 DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [fashionable pack vol 4 DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [musashi wired purchase bonus DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [riding board color set DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [riding board effect set 1 DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [riding board effect set 2 DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue arthur riser dragon green DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue bloody zelle DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue brahms knight night black DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue cybane tamahagane silver DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue kaiser castle snow DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue mad bison demon bordeaux DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue musashi samurai red DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [rogue sparkman wave zeus white DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [v navigator dragon DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [v navigator jibanyan DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [v navigator korone inugami DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose badass DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose bodybuilder DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose boxing DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose drums DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose fist pump DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose hero DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose hoodlum DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose kabuki DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose karate DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose mystery DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose robot dance DLC][v0][US].nsp",
    "/e/MEGATON MUSASHI W WIRED Standard Edition [victory pose squad pose DLC][v0][US].nsp",
    "/e/MONSTER HUNTER RISE [0100B04011742000][US][v0].nsp",
    "/e/Mario Kart 8 Deluxe/Mario Kart 8 Deluxe [0100152000022000][v0].nsp",
    "/e/Mario Kart 8 Deluxe/Mario Kart 8 Deluxe [UPD][0100152000022800][v458752].nsp",
    "/e/Mario Kart 8 Deluxe/Stardew Valley/Stardew Valley [0100e65002bb8000][v0].nsp",
    "/e/Mario Kart 8 Deluxe/Stardew Valley/Stardew Valley [UPD][0100e65002bb8800][v131072].nsp",
    "/e/Mario Strikers Battle League [010019401051C000][v0].nsp",
    "/e/Mario_Kart_8_Deluxe_DLC_Booster_Course_Pass_0100152000023001v65536.nsp",
    "/e/Mario_and_Sonic_at_the_Olympic_Games_Tokyo_2020_V1.0.1_Eur_SuperXCi_switch-xci.com.xci",
    "/e/Mega Man Legacy Collection 2 [0100842008ec4000][v0].nsp",
    "/e/Mega Man Legacy Collection [01002d4007ae0000][v0].nsp",
    "/e/Mega Man X Legacy Collection 2 [01005250086c4000][v0].nsp",
    "/e/Mega Man X Legacy Collection [01005c60086be000][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Akiha Tohno Round Announcements] [01001E30126A1007][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Arcueid Round Announcements] [01001E30126A1005][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Character Aozaki Aoko] [01001E30126A1014][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Character Noel the Dead Apostle] [01001E30126A1013][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Ciel Round Announcements] [01001E30126A1006][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Hisui Round Announcements] [01001E30126A1008][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Kohaku Round Announcements] [01001E30126A1009][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Kouma Kishima Round Announcements] [01001E30126A100B][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Miyako Arima Round Announcements] [01001E30126A100F][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Noel Round Announcements] [01001E30126A100C][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Red Arcueid Round Announcements] [01001E30126A1010][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Roa Round Announcements] [01001E30126A100E][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Round Announcements - 13 Character Set] [01001E30126A1012][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Saber Round Announcements] [01001E30126A1011][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Shiki Tohno Round Announcements] [01001E30126A100A][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Vlov Round Announcements] [01001E30126A100D][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Voice Aozaki Aoko] [01001E30126A1016][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC Voice Noel the Dead Apostle] [01001E30126A1015][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC-23] [01001E30126A1017][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC-24] [01001E30126A1018][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC-25] [01001E30126A1019][v0].nsp",
    "/e/Melty Blood Type Lumina [DLC-26] [01001E30126A101A][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [01006bd001e06000][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [1st Birthday Skin Pack] [DLC][01006bd001e07021][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [2nd Birthday Skin Pack] [DLC][01006bd001e07033][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Biome Settlers Skin Pack 1] [DLC][01006bd001e07011][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Candy Texture Pack] [DLC][01006bd001e0700d][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Cartoon Texture Pack] [DLC][01006bd001e0700e][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Greek Mythology Mash-up Pack] [DLC][01006bd001e0700a][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Pattern Texture Pack] [DLC][01006bd001e07010][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Plastic Texture Pack] [DLC][01006bd001e0700c][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [Skin Pack 1] [DLC][01006bd001e07036][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/Minecraft Nintendo Switch Edition [UPD][01006bd001e06800][v1114112].nsp",
    "/e/Minecraft Nintendo Switch Edition/[DLC] Minecraft Nintendo Switch Edition [01006bd001e0700b][v0].nsp",
    "/e/Minecraft Nintendo Switch Edition/[DLC] Minecraft Nintendo Switch Edition [01006bd001e07032][v0].nsp",
    "/e/Minecraft Story Mode - The Complete Adventure [010059c002ac2000][v0].nsp",
    "/e/Minecraft/Minecraft [0100d71004694000][v0].nsp",
    "/e/Minecraft/Minecraft [UPD][0100d71004694800][v524288].nsp",
    "/e/Mortal Kombat 1 [01006560184E6000][v0].nsp",
    "/e/MvC FCAC Update[v65536].nsp",
    "/e/N64 NSO update 2.16 v12.0.nsp",
    "/e/N64 V0 NSO.nsp",
    "/e/Neva [v1.1.2].xci",
    "/e/New Joe & Mac Caveman Ninja [01003A9013DEE800][v131072][US].nsp",
    "/e/New Joe and Mac Caveman Ninja [01003A9013DEE000][v0][US].nsp",
    "/e/New Super Mario Bros. U Deluxe (1.0.0).nsp",
    "/e/New Super Mario Bros. U Deluxe [v0][0100EA80032EA000].nsp",
    "/e/Nintendo 64 Nintendo Switch Online v4.0.0.nsp",
    "/e/Nintendo 64 - Nintendo Switch Online MATURE 17+ [0100E0601C632000][v0][US](nsw2u.com).nsp",
    "/e/Nintendo 64 - Nintendo Switch Online MATURE 17+ [0100E0601C632800][v131072][US](nsw2u.com).nsp",
    "/e/No More Heroes 2 Desperate Struggle [010071400F204000][v0].nsp",
    "/e/No More Heroes 2 Desperate Struggle [010071400F204800][v196608].nsp",
    "/e/No More Heroes 3 [01007C600EB42800][v262144][US].nsp",
    "/e/No More Heroes 3 [Special CAT overseas ver T-shirt] [01007C600EB43006][v0].nsp",
    "/e/No More Heroes 3 [Special INSERT COIN overseas ver T-shirt] [01007C600EB43008][v0].nsp",
    "/e/No More Heroes [0100F0400F202000]+[v1.1.1].xci",
    "/e/No More Heroes [0100F0400F202800][v196608].nsp",
    "/e/No-M-H-3 By Jeiner YT[01007C600EB42000][v65536]/No More Heroes 3 [01007C600EB42000][v65536].nsp",
    "/e/OMORI [010014E017B14000][v0][US](nsw2u.xyz).nsp",
    "/e/Outer Wilds [Outer Wilds Echoes of the Eye DLC][01003DC0144B7001][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e2 DLC][0100D7B01AE59001][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e3 DLC][0100D7B01AE59002][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e4 DLC][0100D7B01AE59003][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e5 DLC][0100D7B01AE59004][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e6 DLC][0100D7B01AE59005][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e7 DLC][0100D7B01AE59006][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e8 DLC][0100D7B01AE59007][v0][US].nsp",
    "/e/PICROSS S+ [DLC Picross e9 DLC][0100D7B01AE59008][v0][US].nsp",
    "/e/Pokemon Legends Arceus [01001F5010DFA000][v0](Download From nsw2u.xyz).nsp",
    "/e/Pokemon Legends Arceus [01001F5010DFA800][v262144](nsw2u.xyz).nsp",
    "/e/Pokemon Scarlet [0100A3D008C5C000][v0][US](nsw2u.com).nsp",
    "/e/Pokemon Violet [01008F6008C5E000][v0].nsp",
    "/e/Pokemon_Scarlet_DLC_The_Indigo_Disk,_The_Teal_Mask_+_New_Uniform.nsp",
    "/e/Pokken Tournament DX.nsp",
    "/e/Pokémon Lets Go, Eevee! (1.0.2).nsp",
    "/e/Pokémon Lets Go, Pikachu! (1.0.2).nsp",
    "/e/Pokémon Scarlet [0100A3D008C5C800][v720896].nsp",
    "/e/Portal [01007BB017812000][v0].nsp",
    "/e/Princess Peach Showtime [01007A3009184000][v0].nsp",
    "/e/Rayman Legends Definitive Edition 1.2.nsp",
    "/e/Resident Evil 4 (ESP) NSP/Resident Evil 4 [010099A00BC1E000][v0].nsp",
    "/e/Resident Evil 4 [010099A00BC1E800][v131072][US].nsp",
    "/e/Root [DLC The Clockwork Expansion] [01000AF01518B001][v0].nsp",
    "/e/Root [DLC The Riverfolk Expansion] [01000AF01518B002][v0].nsp",
    "/e/SAMURAI_SHODOWN_NEOGEO_COLLECTION_0100F6800F48E800v196608.nsp",
    "/e/SMPJ [0100965017338800][v65536].nsp",
    "/e/SONIC SUPERSTARS [Shadow Costume DLC].nsp",
    "/e/SWORD ART ONLINE Alicization Lycoris [SWORD ART ONLINE Alicization Lycoris Premium Pass Bonus Costume] [010034501225D001][v0][EU].nsp",
    "/e/Sea of Stars [01008C0016544000][v0][US](nsw2u.com).nsp",
    "/e/Sega_Dreamcast[Reicast] SWITCH/Dreamcast_[Reicast].nsp",
    "/e/Shantae Half-Genie Hero Ultimate Edition [01006A200936C000][v0].nsp",
    "/e/Shantae Half-Genie Hero Ultimate Edition [01006A200936C800][v65536].nsp",
    "/e/Shantae Riskys Revenge - Directors Cut [0100ADA012370000][v0].nsp",
    "/e/Shantae Riskys Revenge Directors Cut [0100ADA012370800][v65536].nsp",
    "/e/Shantae [0100430013120000][v0][US].nsp",
    "/e/Shantae and the Seven Sirens [0100EB901040A000][v0].nsp",
    "/e/Shantae and the Seven Sirens [0100EB901040A800][v131072].nsp",
    "/e/Shovel Knight - Dig (1.0.0).nsp",
    "/e/Shovel Knight - Shovel of Hope (1.0.0).nsp",
    "/e/Sonic Colors Ultimate [Exclusive Player Icons] [010040E0116B9001][v65536].nsp",
    "/e/Sonic Colors Ultimate [Sonic Colors Ultimate - Music Pack] [010040E0116B9005][v65536].nsp",
    "/e/Sonic Colors Ultimate [Sonic Colors Ultimate - Ultimate Cosmetic Pack] [010040E0116B9006][v65536].nsp",
    "/e/Sonic Colors Ultimate [v196608].nsp",
    "/e/Sonic Origins [01009FB016286000][v0].nsp",
    "/e/Sonic Origins [01009FB016286800][v65536].nsp",
    "/e/Sonic Superstars [01008F701C074000][v0].nsp",
    "/e/Splatoon 3 [0100C2500FC20800][v1703936][US].nsp",
    "/e/Super Kirby Clash update[v65536].nsp",
    "/e/Super Kirby Clash.nsp",
    "/e/Super Mario 3D World Bowsers Fury [010028600EBDA000][v0].nsp",
    "/e/Super Mario Odyssey[multi][xcib].xci",
    "/e/Super Mario Party Jamboree [0100965017338000][v0].nsp",
    "/e/Super Mario Party [010036b0034e4000][v0].nsp",
    "/e/Super Mario RPG [0100BC0018138000][v0][US](nsw2u.com).nsp",
    "/e/Super Monkey Ball Banana Mania [Golden Banana Mode] v0][US].nsp",
    "/e/Super Monkey Ball Banana Mania [v0].nsp",
    "/e/Super Monkey Ball Banana Mania [v196608].nsp",
    "/e/Super_Mario_3D_World_+_Bowsers_Fury_010028600EBDA800v65536.nsp",
    "/e/Super_Mario_Bros_Wonder_010015100B514000v0USDumped_xci/Super Mario Bros. Wonder [010015100B514000][v0][US](nsw2u.com).xci",
    "/e/Superliminal [010075701153A000][USA][v0].nsp",
    "/e/THE KING OF FIGHTERS XIII GLOBAL MATCH [0100DC701A388000][v0][US](nsw2u.com).nsp",
    "/e/THE KING OF FIGHTERS XIII GLOBAL MATCH [0100DC701A388800][v65536][US](nsw2u.com).nsp",
    "/e/TLoZ EoW Update 1.0.1 (v65536).nsp",
    "/e/TMNT Mutants Unleashed [010013001BD62000][v0].nsp",
    "/e/TMNT Mutants Unleashed [010013001BD62800][v196608].nsp",
    "/e/TMNT Shredders Revenge [0100FE701475A000][v0].nsp",
    "/e/TMNT Shredders Revenge [0100FE701475A800][v589824].nsp",
    "/e/TMNT Splintered Fate [01005CF01E784000][v0].nsp",
    "/e/TMNT Splintered Fate [01005CF01E784800][v655360].nsp",
    "/e/TMNT_Mutants_Unleashed_DLC_1984_Comic_Book_Pack_010013001BD63002v0.nsp",
    "/e/TMNT_Mutants_Unleashed_DLC_1987_Animated_Series_Pack_010013001BD63001v0.nsp",
    "/e/TMNT_Mutants_Unleashed_DLC_Fresh_Meat_Mission_Pack_010013001BD63004v0.nsp",
    "/e/TMNT_Mutants_Unleashed_DLC_Metalheads_Pack_010013001BD63003v0.nsp",
    "/e/TMNT_Shredders_Revenge_DLC_Dimension_Shellshock_0100FE701475B001v0.nsp",
    "/e/TMNT_Shredders_Revenge_DLC_Radical_Reptiles_0100FE701475B002v0.nsp",
    "/e/TMNT_Splintered_Fate_DLC_Casey_Jones_and_the_Junkyard_Jam_01005CF01E785001v0.nsp",
    "/e/Taiko no Tatsujin Drum n Fun [01002C000B552000][v0].nsp",
    "/e/Taiko no Tatsujin Rhythm Festival [01006B0016AD6000][v0][US].nsp",
    "/e/Team Sonic Racing [v65536]UPDATE[romstorage.com].nsp",
    "/e/Teenage Mutant Ninja Turtles Arcade Wrath of the Mutants [0100C7601CDAC000][v0][US].xci",
    "/e/Teenage Mutant Ninja Turtles Arcade Wrath of the Mutants [0100C7601CDAC800][v65536][US].nsp",
    "/e/Teenage_Mutant_Ninja_Turtles_The_Cowabunga_Collection_0100FDB0154E4800v262144.nsp",
    "/e/The LEGO Movie 2 Videogame [0100A4400BE74000][v0].nsp",
    "/e/The Legend of Zelda Breath of the Wild [DLC Pack 1 The Master Trials] [01007EF00011F001][v196608].nsp",
    "/e/The Legend of Zelda Breath of the Wild [DLC Pack 2 The Champions Ballad] [01007EF00011F002][v196608].nsp",
    "/e/Tinfoil 20 [050000BADDAD0000][20.0][v1].nsp",
    "/e/Tinfoil [050000BADDAD0000][20.0][v1].nsp",
    "/e/Toki [0100F3400A432000][v0].nsp",
    "/e/Toki [0100F3400A432800][v65536].nsp",
    "/e/Trinity Trigger [01004950197B2000][v0][US].nsp",
    "/e/Trinity Trigger [azure dragon sword_cyan DLC][01004950197B30CB][v0][US].nsp",
    "/e/Trinity Trigger [crimson lotus bow_elise DLC][01004950197B30CB][v0][US].nsp",
    "/e/Trinity Trigger [extra episode cyan DLC][01004950197B30CB][v0][US].nsp",
    "/e/Trinity Trigger [extra episode elise DLC][01004950197B30CB][v0][US].nsp",
    "/e/Trinity Trigger [extra episode violet DLC][01004950197B30CB][v0][US].nsp",
    "/e/Trinity Trigger [extra episode zantis DLC][01004950197B30CB][v0][US].nsp",
    "/e/Trinity Trigger [white tiger axe zantis DLC][01004950197B30CB][v0][US].nsp",
    "/e/UNDER NIGHT IN-BIRTH II SysCeles [UNI2 - Season Pass DLC][0100BD401D18B003][v0][US].nsp",
    "/e/Urban Flow [Urban Flow - Expansion Pack] [0100B110109F9001][v0][US].nsp",
    "/e/Urban Flow [Urban Flow - London Rules] [0100B110109F9003][v0][US].nsp",
    "/e/Urban Flow [Urban Flow - Winter Expansion Pack] [0100B110109F9002][v0][US].nsp",
    "/e/Wargroove [DLC Double Trouble] [01000F0002BB7001][v589824].nsp",
    "/e/Wingspan [DLC][0100E05011351001][v0][US].nsp",
    "/e/Wingspan [DLC][0100E0501135100A][v0][US].nsp",
    "/e/Yoshi's Crafted World [01006000040C2800][v65536].nsp",
    "/e/Yoshi's Crafted World [01006000040c2000][v0]/Yoshi's Crafted World [01006000040c2000][v0].nsp",
    "/e/[3DLC]/Sonic Colors Ultimate [Exclusive Player Icons] [010040E0116B9001][v65536].nsp",
    "/e/[3DLC]/Sonic Colors Ultimate [Sonic Colors Ultimate - Music Pack] [010040E0116B9005][v65536].nsp",
    "/e/[3DLC]/Sonic Colors Ultimate [Sonic Colors Ultimate - Ultimate Cosmetic Pack] [010040E0116B9006][v65536].nsp",
    "/e/[NSW] ACA NEOGEO METAL SLUG 2.nsp",
    "/e/[NSW] ACA NEOGEO METAL SLUG 3.nsp",
    "/e/[NSW] ACA NEOGEO METAL SLUG 4.nsp",
    "/e/[NSW] ACA NEOGEO METAL SLUG 5.nsp",
    "/e/[NSW] ACA NEOGEO METAL SLUG X.nsp",
    "/e/[NSW] ACA NEOGEO METAL SLUG.nsp",
    "/e/[NSW] ACA NEOGEO THE KING OF FIGHTERS 2002.nsp",
    "/e/[NSW] ACA NEOGEO THE KING OF FIGHTERS 2003.nsp",
    "/e/[NSW] ACA NEOGEO THE LAST BLADE 2.nsp",
    "/e/[NSW] ACA NEOGEO THE LAST BLADE.nsp",
    "/e/[NSW] ACA NEOGEO THE SUPER SPY.nsp",
    "/e/[NSW] ACA NEOGEO THE ULTIMATE 11 SNK FOOTBALL CHAMPIONSHIP.nsp",
    "/e/[NSW] ACA NEOGEO THRASH RALLY.nsp",
    "/e/[NSW] ACA NEOGEO TOP HUNTER RODDY & CATHY.nsp",
    "/e/[NSW] ACA NEOGEO TOP PLAYER'S GOLF.nsp",
    "/e/[NSW] ACA NEOGEO TWINKLE STAR SPRITES.nsp",
    "/e/[NSW] ACA NEOGEO WAKU WAKU 7.nsp",
    "/e/[NSW] ACA NEOGEO WORLD HEROES 2 JET.nsp",
    "/e/[NSW] ACA NEOGEO WORLD HEROES 2.nsp",
    "/e/[NSW] ACA NEOGEO WORLD HEROES PERFECT.nsp",
    "/e/[NSW] ACA NEOGEO WORLD HEROES.nsp",
    "/e/[NSW] ACA NEOGEO ZED BLADE.nsp",
    "/e/[NSW] ACA NEOGEO ZUPAPA!.nsp",
    "/e/[NSW] Animal Crossing New Horizons.nsp",
    "/e/atmosphere/contents/010000000000bd00/exefs.nsp",
    "/e/mario+rabitsutsu kingudamubatoru/mario+rabitsutsu kingudamubatoru [0100e46003042000][v0].nsp",
    "/e/mario+rabitsutsu kingudamubatoru/mario+rabitsutsu kingudamubatoru [UPD][0100e46003042800][v65536].nsp",
    "/e/mario+rabitsutsu kingudamubatoru/mario+rabitsutsu kingudamubatoru [Xin sutoriZhui Jia ] [DLC][0100e46003043004][v65536].nsp",
    "/e/mario+rabitsutsu kingudamubatoru/mario+rabitsutsu kingudamubatoru [Zhui Jia Wu Qi patsuku(pikuseruFeng )] [DLC][0100e46003043001][v0].nsp",
    "/e/mario+rabitsutsu kingudamubatoru/mario+rabitsutsu kingudamubatoru [Zhui Jia Wu Qi patsuku(suchimupankuFeng )] [DLC][0100e46003043002][v0].nsp",
    "/e/mario+rabitsutsu kingudamubatoru/mario+rabitsutsu kingudamubatoru [chiyarenzimatsupuZhui Jia ] [DLC][0100e46003043003][v0].nsp",
]


def parse_game(path, drive):
    """Extrae información del archivo"""
    filename = Path(path).name

    # Determinar tipo
    is_xci = filename.lower().endswith('.xci')
    file_type = 'xci' if is_xci else 'nsp'

    # Limpiar nombre para mostrar
    name = filename
    if name.endswith('.nsp') or name.endswith('.xci'):
        name = name[:-4]

    # Detectar categoría
    path_lower = path.lower()
    name_lower = name.lower()

    category = 'base'
    if any(x in path_lower for x in ['/dlc', '/dlc/', '[dlc', ' dlc ', ' costume ', ' outfit ', ' skin ', ' pack ', ' unlock', ' character ', ' avatar ', ' bgm ', ' music ', ' voice ']):
        category = 'dlc'
    elif any(x in name_lower for x in ['dlc', 'pack', 'unlock', 'costume', 'outfit', 'skin', 'character', 'avatar', 'bgm', 'music', 'voice']):
        category = 'dlc'
    elif any(x in path_lower for x in ['/upd', '[upd]', ' update ', ' v65536', ' v131072', ' v262144', ' v327680', ' v589824', ' v720896', ' v786432', ' v983040', ' v1179648', ' v1376256', ' v1703936', ' v1769472', ' v393216', ' v458752', ' v524288', ' v851968', ' v1048576', ' v10420224']):
        category = 'update'
    elif any(x in name_lower for x in ['update', 'upd', 'v65536', 'v131072', 'v262144', 'v327680', 'v589824', 'v720896', 'v786432', 'v983040', 'v1179648', 'v1376256', 'v1703936', 'v1769472', 'v393216', 'v458752', 'v524288', 'v851968', 'v1048576', 'v10420224']):
        category = 'update'

    # Nombre limpio para mostrar (quitar IDs y versiones)
    display_name = name
    # Remover [ID] patterns
    display_name = re.sub(r'\[0100[A-F0-9]{12}\]', '', display_name)
    display_name = re.sub(r'\[v\d+\]', '', display_name)
    display_name = re.sub(r'\(v[\d.]+\)', '', display_name)
    display_name = display_name.strip()
    # Tomar primera parte antes de múltiples espacios o corchetes
    if '  ' in display_name:
        display_name = display_name.split('  ')[0]
    display_name = display_name.strip()
    if not display_name:
        display_name = name[:80]

    return {
        'name': display_name,
        'filename': filename,
        'type': file_type,
        'category': category,
        'drive': drive,
        'path': path
    }


def main():
    all_games = []

    # Procesar D:
    for f in D_FILES:
        all_games.append(parse_game(f, 'd'))

    # Procesar E:
    for f in E_FILES:
        all_games.append(parse_game(f, 'e'))

    # Estadísticas
    total = len(all_games)
    d_count = sum(1 for g in all_games if g['drive'] == 'd')
    e_count = sum(1 for g in all_games if g['drive'] == 'e')
    nsp_count = sum(1 for g in all_games if g['type'] == 'nsp')
    xci_count = sum(1 for g in all_games if g['type'] == 'xci')
    base_count = sum(1 for g in all_games if g['category'] == 'base')
    dlc_count = sum(1 for g in all_games if g['category'] == 'dlc')
    update_count = sum(1 for g in all_games if g['category'] == 'update')

    print(f"Total: {total}")
    print(f"  Disco D: {d_count}")
    print(f"  Disco E: {e_count}")
    print(f"  NSP: {nsp_count}")
    print(f"  XCI: {xci_count}")
    print(f"  Base: {base_count}")
    print(f"  DLC: {dlc_count}")
    print(f"  Update: {update_count}")

    # Guardar JSON completo
    output = {
        'metadata': {
            'generated': '2026-11-08',
            'totalGames': total,
            'driveD': d_count,
            'driveE': e_count,
            'byFormat': {'NSP': nsp_count, 'XCI': xci_count},
            'byCategory': {'base': base_count, 'dlc': dlc_count, 'update': update_count}
        },
        'games': all_games
    }

    with open('catalogo-juegos-switch-completo.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("\n✅ JSON guardado: catalogo-juegos-switch-completo.json")

    # Generar HTML completo
    total_str = f"{total:,}"
    generate_html(all_games, total, d_count, e_count, nsp_count, xci_count, base_count, dlc_count, update_count, total_str)


def generate_html(games, total, d_count, e_count, nsp_count, xci_count, base_count, dlc_count, update_count, total_str):
    """Genera el HTML completo con todos los juegos"""

    # Ordenar: base primero, luego DLC, luego updates
    cat_order = {'base': 0, 'dlc': 1, 'update': 2}
    games_sorted = sorted(games, key=lambda g: (cat_order[g['category']], g['name'].lower()))

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo Completo Nintendo Switch - {total} juegos</title>
    <style>
        :root {{
            --bg-primary: #0d1117;
            --bg-secondary: #161b22;
            --bg-tertiary: #21262d;
            --fg-primary: #e6edf3;
            --fg-secondary: #8b949e;
            --accent: #58a6ff;
            --accent-hover: #79b8ff;
            --border: #30363d;
            --success: #3fb950;
            --warning: #d29922;
            --danger: #f85149;
            --card-bg: #161b22;
            --input-bg: #0d1117;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            background: var(--bg-primary);
            color: var(--fg-primary);
            line-height: 1.6;
            min-height: 100vh;
        }}
        .container {{ max-width: 1500px; margin: 0 auto; padding: 24px; }}
        header {{
            text-align: center;
            padding: 32px 0;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
        }}
        h1 {{
            font-size: 2.5rem;
            font-weight: 600;
            background: linear-gradient(135deg, var(--accent), #a371f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .stats {{ display: flex; justify-content: center; gap: 16px; margin-top: 16px; flex-wrap: wrap; }}
        .stat {{ background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 8px; padding: 12px 20px; text-align: center; min-width: 100px; }}
        .stat-value {{ font-size: 1.75rem; font-weight: 700; color: var(--accent); }}
        .stat-label {{ font-size: 0.75rem; color: var(--fg-secondary); text-transform: uppercase; letter-spacing: 0.5px; }}
        .controls {{ display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; align-items: center; }}
        .search-box {{ flex: 1; min-width: 280px; position: relative; }}
        .search-box input {{ width: 100%; padding: 10px 14px 10px 40px; background: var(--input-bg); border: 1px solid var(--border); border-radius: 8px; color: var(--fg-primary); font-size: 0.95rem; transition: border-color 0.2s, box-shadow 0.2s; }}
        .search-box input:focus {{ outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15); }}
        .search-box svg {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--fg-secondary); width: 18px; height: 18px; }}
        .filters {{ display: flex; gap: 8px; flex-wrap: wrap; }}
        .filter-btn {{ padding: 6px 12px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 6px; color: var(--fg-secondary); font-size: 0.8rem; cursor: pointer; transition: all 0.2s; white-space: nowrap; }}
        .filter-btn:hover {{ border-color: var(--accent); color: var(--fg-primary); }}
        .filter-btn.active {{ background: var(--accent); border-color: var(--accent); color: var(--bg-primary); }}
        .view-toggle {{ display: flex; border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }}
        .view-btn {{ padding: 6px 10px; background: transparent; border: none; color: var(--fg-secondary); cursor: pointer; transition: all 0.2s; }}
        .view-btn:hover {{ background: var(--bg-tertiary); color: var(--fg-primary); }}
        .view-btn.active {{ background: var(--accent); color: var(--bg-primary); }}
        .results-info {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding: 10px 14px; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 8px; font-size: 0.8rem; color: var(--fg-secondary); flex-wrap: wrap; gap: 8px; }}
        .game-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }}
        .game-grid.list-view {{ grid-template-columns: 1fr; }}
        .game-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s; }}
        .game-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.3); border-color: var(--accent); }}
        .game-card.list-view {{ display: flex; align-items: center; padding: 12px; }}
        .game-header {{ padding: 12px; border-bottom: 1px solid var(--border); display: flex; align-items: flex-start; gap: 10px; }}
        .game-icon {{ width: 40px; height: 40px; border-radius: 6px; background: linear-gradient(135deg, var(--accent), #a371f7); display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0; }}
        .game-icon.xci {{ background: linear-gradient(135deg, #f78166, #f78166); }}
        .game-icon.dlc {{ background: linear-gradient(135deg, var(--warning), #e3b341); }}
        .game-icon.update {{ background: linear-gradient(135deg, var(--success), #56d364); }}
        .game-title {{ flex: 1; min-width: 0; }}
        .game-title h3 {{ font-size: 0.9rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        .game-title .game-type {{ font-size: 0.65rem; color: var(--fg-secondary); text-transform: uppercase; letter-spacing: 0.5px; }}
        .game-info {{ padding: 12px; }}
        .game-path {{ font-size: 0.65rem; color: var(--fg-secondary); font-family: monospace; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 6px; }}
        .game-meta {{ display: flex; flex-wrap: wrap; gap: 6px; }}
        .meta-tag {{ display: inline-flex; align-items: center; gap: 3px; padding: 3px 7px; background: var(--bg-primary); border: 1px solid var(--border); border-radius: 3px; font-size: 0.6rem; color: var(--fg-secondary); }}
        .meta-tag.drive-d {{ border-color: #58a6ff; color: #58a6ff; }}
        .meta-tag.drive-e {{ border-color: #a371f7; color: #a371f7; }}
        .meta-tag.type-nsp {{ border-color: var(--success); color: var(--success); }}
        .meta-tag.type-xci {{ border-color: #f78166; color: #f78166; }}
        .meta-tag.type-dlc {{ border-color: var(--warning); color: var(--warning); }}
        .meta-tag.type-update {{ border-color: #a371f7; color: #a371f7; }}
        .meta-tag.type-base {{ border-color: var(--success); color: var(--success); }}
        .no-results {{ text-align: center; padding: 64px 24px; color: var(--fg-secondary); }}
        .no-results svg {{ width: 64px; height: 64px; margin-bottom: 16px; opacity: 0.5; }}
        @media (max-width: 768px) {{
            .container {{ padding: 16px; }}
            h1 {{ font-size: 1.75rem; }}
            .controls {{ flex-direction: column; align-items: stretch; }}
            .search-box {{ min-width: 0; }}
            .filters {{ justify-content: center; }}
            .game-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎮 Catálogo Completo Nintendo Switch</h1>
            <p style="color: var(--fg-secondary); margin-top: 8px;">{total} archivos NSP/XCI · Discos D: ({d_count}) + E: ({e_count})</p>
            <div class="stats">
                <div class="stat"><div class="stat-value">{total:,}</div><div class="stat-label">Total</div></div>
                <div class="stat"><div class="stat-value">{d_count:,}</div><div class="stat-label">Disco D:</div></div>
                <div class="stat"><div class="stat-value">{e_count:,}</div><div class="stat-label">Disco E:</div></div>
                <div class="stat"><div class="stat-value">{nsp_count:,}</div><div class="stat-label">NSP</div></div>
                <div class="stat"><div class="stat-value">{xci_count:,}</div><div class="stat-label">XCI</div></div>
                <div class="stat"><div class="stat-value">{base_count:,}</div><div class="stat-label">Base</div></div>
                <div class="stat"><div class="stat-value">{dlc_count:,}</div><div class="stat-label">DLCs</div></div>
                <div class="stat"><div class="stat-value">{update_count:,}</div><div class="stat-label">Updates</div></div>
            </div>
        </header>

        <div class="controls">
            <div class="search-box">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <input type="text" id="search-input" placeholder="Buscar juegos, DLCs, actualizaciones..." autocomplete="off">
            </div>
            <div class="filters" id="filters">
                <button class="filter-btn active" data-filter="all">Todos ({total:,})</button>
                <button class="filter-btn" data-filter="base">Juegos Base ({base_count:,})</button>
                <button class="filter-btn" data-filter="dlc">DLCs ({dlc_count:,})</button>
                <button class="filter-btn" data-filter="update">Actualizaciones ({update_count:,})</button>
                <button class="filter-btn" data-filter="nsp">NSP ({nsp_count:,})</button>
                <button class="filter-btn" data-filter="xci">XCI ({xci_count:,})</button>
                <button class="filter-btn" data-filter="drive-d">Disco D: ({d_count:,})</button>
                <button class="filter-btn" data-filter="drive-e">Disco E: ({e_count:,})</button>
            </div>
            <div class="view-toggle">
                <button class="view-btn active" data-view="grid" title="Vista cuadrícula"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg></button>
                <button class="view-btn" data-view="list" title="Vista lista"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
            </div>
        </div>

        <div class="results-info">
            <span id="results-count">Mostrando {total:,} de {total:,} juegos</span>
            <span id="active-filters"></span>
        </div>

        <div class="game-grid" id="game-grid">
'''

    # Renderizar todas las cartas
    for game in games_sorted:
        cat = game['category']
        icon = '💾' if game['type'] == 'xci' else ('🧩' if cat == 'dlc' else ('⬆️' if cat == 'update' else '🎮'))
        icon_class = 'xci' if game['type'] == 'xci' else ('dlc' if cat == 'dlc' else ('update' if cat == 'update' else ''))
        drive_label = 'D:' if game['drive'] == 'd' else 'E:'
        drive_class = 'drive-d' if game['drive'] == 'd' else 'drive-e'
        type_class = 'type-nsp' if game['type'] == 'nsp' else 'type-xci'
        cat_class = 'type-dlc' if cat == 'dlc' else ('type-update' if cat == 'update' else 'type-base')
        cat_label = 'Base' if cat == 'base' else ('DLC' if cat == 'dlc' else 'Update')

        # Escape HTML
        name_escaped = game['name'].replace('&', '&').replace('<', '<').replace('>', '>').replace('"', '"')
        path_escaped = game['path'].replace('&', '&').replace('<', '<').replace('>', '>')

        html += f'''            <article class="game-card" data-name="{name_escaped.lower()}" data-category="{cat}" data-type="{game['type']}" data-drive="{game['drive']}">
                <div class="game-header">
                    <div class="game-icon {icon_class}">{icon}</div>
                    <div class="game-title">
                        <h3 title="{name_escaped}">{name_escaped}</h3>
                        <span class="game-type">{cat_label}</span>
                    </div>
                </div>
                <div class="game-info">
                    <div class="game-path">{path_escaped}</div>
                    <div class="game-meta">
                        <span class="meta-tag {drive_class}">{drive_label}</span>
                        <span class="meta-tag {type_class}">{game['type'].upper()}</span>
                        <span class="meta-tag {cat_class}">{cat_label}</span>
                    </div>
                </div>
            </article>
'''

    html += f'''        </div>

        <div class="no-results" id="no-results" style="display: none;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="8" x2="14" y2="14"></line><line x1="14" y1="8" x2="8" y2="14"></line></svg>
            <h3>No se encontraron resultados</h3>
            <p>Intenta cambiar los filtros o la búsqueda</p>
        </div>
    </div>

    <script>
        const allGames = document.querySelectorAll('.game-card');
        const searchInput = document.getElementById('search-input');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const viewBtns = document.querySelectorAll('.view-btn');
        const grid = document.getElementById('game-grid');
        const resultsCount = document.getElementById('results-count');
        const activeFiltersEl = document.getElementById('active-filters');
        const noResults = document.getElementById('no-results');

        let currentView = 'grid';
        let activeFilter = 'all';
        let searchTerm = '';

        function getCategory(el) {{ return el.dataset.category; }}
        function getType(el) {{ return el.dataset.type; }}
        function getDrive(el) {{ return el.dataset.drive; }}
        function getName(el) {{ return el.dataset.name; }}

        function filterGames() {{
            let visible = 0;
            allGames.forEach(el => {{
                const nameMatch = getName(el).includes(searchTerm.toLowerCase());
                let filterMatch = true;
                const cat = getCategory(el);
                const type = getType(el);
                const drive = getDrive(el);

                if (activeFilter === 'base') filterMatch = cat === 'base';
                else if (activeFilter === 'dlc') filterMatch = cat === 'dlc';
                else if (activeFilter === 'update') filterMatch = cat === 'update';
                else if (activeFilter === 'nsp') filterMatch = type === 'nsp';
                else if (activeFilter === 'xci') filterMatch = type === 'xci';
                else if (activeFilter === 'drive-d') filterMatch = drive === 'd';
                else if (activeFilter === 'drive-e') filterMatch = drive === 'e';

                if (nameMatch && filterMatch) {{
                    el.style.display = '';
                    visible++;
                }} else {{
                    el.style.display = 'none';
                }}
            }});

            if (visible === 0) {{
                grid.style.display = 'none';
                noResults.style.display = 'block';
            }} else {{
                grid.style.display = currentView === 'list' ? 'grid' : 'grid';
                noResults.style.display = 'none';
            }}

            resultsCount.textContent = `Mostrando $${{visible.toLocaleString()}} de {total_str} juegos`;
            updateActiveFilters();
        }}

        function updateActiveFilters() {{
            const labels = {{ 'all': 'Todos', 'base': 'Juegos Base', 'dlc': 'DLCs', 'update': 'Actualizaciones', 'nsp': 'NSP', 'xci': 'XCI', 'drive-d': 'Disco D:', 'drive-e': 'Disco E:' }};
            let activeLabels = [];
            if (activeFilter !== 'all') activeLabels.push(labels[activeFilter]);
            if (searchTerm) activeLabels.push(`Búsqueda: "${{searchTerm}}"`);
            activeFiltersEl.textContent = activeLabels.length ? `Filtros: ${{activeLabels.join(' • ')}}` : '';
        }}

        searchInput.addEventListener('input', (e) => {{ searchTerm = e.target.value; filterGames(); }});

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeFilter = btn.dataset.filter;
                filterGames();
            }});
        }});

        viewBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                viewBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentView = btn.dataset.view;
                grid.classList.toggle('list-view', currentView === 'list');
            }});
        }});

        document.addEventListener('keydown', (e) => {{
            if (e.target === searchInput) return;
            if (e.key === '/') {{ e.preventDefault(); searchInput.focus(); }}
            if (e.key === 'Escape') {{ searchInput.value = ''; searchTerm = ''; searchInput.blur(); filterGames(); }}
        }});

        filterGames();
    </script>
</body>
</html>'''

    with open('catalogo-juegos-switch-completo.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("✅ HTML guardado: catalogo-juegos-switch-completo.html")


if __name__ == '__main__':
    main()