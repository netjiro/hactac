#!/usr/bin/python

import math
import random

import sys


#import pyparsing




# ------------- for regular quick roll selection, just change here -------------
#distribution = "standard_set"     # standard selection of chars, 18 dudes
distribution = "small_set"     # small but representative set of chars, 10 dudes
#distribution = "min_set"     # minimal set, 7 dudes
#distribution = "goblin_destiny"  # special set for goblin destiny campaign
#distribution = "goblinsonly"     # test selection for ap changes, test 2
#-------------------------------------------------------------------------------





#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80


# First have to declare which race, then choose from those available
# total 16 dudes are too many, will get too OP stats
if distribution == "standard_set" :
    humans =       3
    dwarves =      2
    elves =        2
    halflings =    3
    orcs =         2
    goblins =      4

# 10 total, reasonable representation if choosing from all races
if distribution == "small_set" :
    humans =       2
    dwarves =      1
    elves =        1
    halflings =    2
    orcs =         1
    goblins =      3

# 7 total, minimal set if choosing from all races
if distribution == "min_set" :
    humans =       1
    dwarves =      1
    elves =        1
    halflings =    1
    orcs =         1
    goblins =      2


# 13 total
if distribution == "goblin_destiny" :
    humans =       1
    dwarves =      0
    elves =        0
    halflings =    1
    orcs =         1
    goblins =      10
# 10 gobbos, choose two to play:
if distribution == "goblinsonly" :
    humans =       0
    dwarves =      0
    elves =        0
    halflings =    0
    orcs =         0
    goblins =     10
# should try 6 gobbos? 10 Gobbos seems to give too good results.




# make some dice functions
def die(n):
    return random.randint(1,n)
def d2():
    return die(2)
def d3():
    return die(3)
def d4():
    return die(4)
def d5():
    return die(5)
def d6():
    return die(6)
def d7():
    return die(7)
def d8():
    return die(8)
def d9():
    return die(9)
def d10():
    return die(10)
def d12():
    return die(12)
def d15():
    return die(15)
def d20():
    return die(20)
def d60():
    return die(60)
def d90():
    return die(90)
def d100():
    return die(100)

# NOPE!! can't overload functions in python just by argument

# true if rolled less than or equal value on a d100 [1,100]
def roll(chance):
    if d100() <= chance:
        return True
    else:
        return False

# true or false, 50/50
def flip():
    if random.randint(0,1) == 0:
        return False
    else:
        return True

def r2d3():
    return d3() + d3()
def r2d4():
    return d4() + d4()
def r2d5():
    return d5() + d5()
def r2d6():
    return d6() + d6()
def r2d7():
    return d7() + d7()
def r2d8():
    return d8() + d8()
def r2d10():
    return d10() + d10()
def r2d20():
    return d20() + d20()

def pad2(string):
    if len(string) > 1:
        return string
    else:
        return " " + string





#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
class Character:
    race = "unset"
    # basic character traits
    str = -1
    dex = -1
    con = -1
    int = -1
    psy = -1
    per = -1
    cha = -1
    # secondary character traits
    hp = -1
    m = -1
    w = -1
    r = -1
    d = -1
    stam = -1
    visRange = -1
    visArc = -1
    visMode = "unset"
    mana = -1
    ap = -1
    xp = -1
    # tertiary character traits
    bonuses = []
    money = "unset"
    extras = []
    # starting skills & attacks, maneuvers
    skills = {}
    maneuvers = []

    def __init__(self):
        self.bonuses = []
        self.extras = []
        self.skills.clear()
        self.maneuvers = []

    def printSheet(self, i):
        # create left column text
        pad20 = "                    "
        #nr = pad2(str(i))
        nr = str(i)
        str_hp =   "str " + pad2(str(self.str)) + pad20
        dex_move = "dex " + pad2(str(self.dex)) + pad20
        con_stam = "con " + pad2(str(self.con)) + pad20
        int_vis =  "int " + pad2(str(self.int)) + pad20
        psy_mana = "psy " + pad2(str(self.psy)) + pad20
        per_ap =   "per " + pad2(str(self.per)) + pad20
        cha_xp =   "cha " + pad2(str(self.cha)) + pad20
        # create right column text
        str_hp = str_hp + "hp " + str(self.hp) + " abs 0"
        dex_move = dex_move + "m" + str(self.m) + " w" + str(self.w) + " r" + str(self.r) + " d" + str(self.d)
        con_stam = con_stam + "stamina " + str(self.stam)
        int_vis = int_vis + "vision " + str(self.visRange) + " " + str(self.visMode) + " " + str(self.visArc)
        psy_mana = psy_mana + "mana " + str(self.mana)
        per_ap = per_ap + "action points " + str(self.ap)
        cha_xp = cha_xp + "xp " + str(self.xp)
        # start printing
        print("================== "+self.race+" "+nr+" ==================")
        print(str_hp)
        print(dex_move)
        print(con_stam)
        print(int_vis)
        print(psy_mana)
        print(per_ap)
        print(cha_xp)
        print("--------------------------------------------")
        for bonus in self.bonuses :
            print(bonus)
        print("--------------------------------------------")
        skillset = []
        for skill, lvl in self.skills.items() :
            skillset.append(skill +" "+ str(lvl))
        skillset.sort()
        for skill in skillset :
            print(skill)
        print("--------------------------------------------")
        for maneuver in self.maneuvers :
            print(maneuver)
        print("--------------------------------------------")
        print("money: " + str(self.money))
        for extra in self.extras:
                print(extra)




#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollHuman():
    char = Character()
    char.race = "human"
    # primary
    char.str = r2d5()                     #  2 - 10   6
    char.dex = r2d5()                     #  2 - 10   6
    char.con = r2d5()                     #  2 - 10   6
    char.int = r2d5()                     #  2 - 10   6
    char.psy = r2d5()                     #  2 - 10   6
    char.per = r2d5()                     #  2 - 10   6
    char.cha = r2d5()                     #  2 - 10   6                 1 1
    # secondary                                       1,2,3,4,5,6,7,8,9,0,1
    char.hp = 8 + r2d6()                  # 10 - 20  15
    char.m = 1 + int(d10() / 10)          #  1 -  2   9,1
    char.w = 2 + int(d10() / 4)           #  2 -  4     3,4,3
    char.r = 5 + int(d10() / 4)           #  5 -  7           3,4,3
    char.d = 8 + int(d10() / 3)           #  8 - 11                 2,3,3,2
    char.stam = 3 + d7()                  #  4 - 10   7
    char.visRange = 15 + d10()            # 16 - 25  20
    char.visArc = 180 + d90()             # 181-270 225
    char.visMode = "day"
    char.mana = r2d10()                   #  2 - 20  11
    char.ap = 3 + int(d10() / 8)          #  3 -  4   7,3
    char.xp = 100 + d20()                 # 101-120 110
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.bonuses.append("yield bonus " + str(2 + int(d10() / 4)))
    char.money = str(d4())+" gold, "+str(d8())+" silver, "+str(d20())+" copper"
    # skills
    char.skills['Common'] = int(char.int / 2) + d6()
    char.skills['avoid'] = int(char.dex / 4) + d2()
    char.skills['throw'] = int(char.dex / 4) + d2()
    # maneuvers
    char.maneuvers.append('yield')
    char.maneuvers.append('off balance')
    char.maneuvers.append('strength bonus')
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollDwarf():
    char = Character()
    char.race = "dwarf"
    # primary
    char.str = r2d5() +2                  #  4 - 12   8
    char.dex = r2d4()                     #  2 -  8   5
    char.con = r2d5() +2                  #  4 - 12   8
    char.int = r2d5()                     #  2 - 10   6
    char.psy = r2d4() +3                  #  5 - 11   8
    char.per = r2d5()                     #  2 - 10   6
    char.cha = r2d5() -1                  #  1 -  9   5
    # secondary                                       1,2,3,4,5,6,7
    char.hp = 10 + r2d6()                 # 12 - 22  17
    char.m = 1 + int(d10() / 8)           #  1 -  2   7,3
    char.w = 2 + int(d10() / 6)           #  2 -  3     5,5
    char.r = 3 + int(d10() / 4)           #  3 -  5       3,4,3
    char.d = 5 + int(d10() / 4)           #  5 -  7           3,4,3
    char.stam = 5 + r2d5()                #  7 - 15  11
    char.visRange = 15 + d5()             # 16 - 20  18
    char.visArc = 120 + d90()             # 121-210 165
    char.visMode = "infra/dusk"
    char.mana = r2d10()                   #  2 - 20  11
    char.ap = 3 + int(d10() / 8)          #  3 -  4   7,3
    char.xp = 105 + d20()                 # 106-125 115
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.bonuses.append("yield bonus " + str(2 + int(d10() / 4)))
    char.bonuses.append("haggle bonus +" + str(d3()))
    dungeoneeringbonus = 0
    if roll(25):
        dungeoneeringbonus = d3()
        char.bonuses.append("dungeoneering bonus +" + str(dungeoneeringbonus))
    char.money = str(d10())+" gold, "+str(d20())+" silver, "+str(d20())+" copper" + ", and a gemstone worth " + str(5+d6()) + " gold"
    char.extras.append("con bonus +3 against poisons")
    char.extras.append("haggle bonus +3")
    char.extras.append("tackle and block mod+"+str(d3()))
    char.extras.append("Dwarves without any gems, and/or with less than 5 gold total \n" \
                       +"coin suffer psy-1 mod until wealthy again.")
    char.extras.append("Dwarves with 50+ gold in coins and gems gain psy+1 mod while wealthy.")
    # skills
    char.skills['Dwarvish'] = int(char.int/2) + 2 + d4()
    char.skills['Common'] = int(char.int / 3) + d3()
    char.skills['avoid'] = int(char.dex / 4) + d2()
    char.skills['find'] = int(char.per / 4) + d2()
    char.skills['dungeoneering (incl bonus)'] = max(dungeoneeringbonus, d4())
    # maneuvers
    char.maneuvers.append('yield')
    char.maneuvers.append('off balance')
    char.maneuvers.append('strength bonus')
    if roll(50): char.maneuvers.append('synchronised')
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollElf():
    char = Character()
    char.race = "elf"
    # primary
    char.str = r2d4()                     #  2 -  8   5
    char.dex = r2d5() +1                  #  3 - 11   7
    char.con = r2d5()                     #  2 - 10   6
    char.int = r2d4() +3                  #  5 - 11   8
    char.psy = r2d4() +2                  #  4 - 10   7
    char.per = r2d5() +1                  #  3 - 11   7
    char.cha = r2d5() +2                  #  4 - 12   8                 1 1 1 1
    # secondary                                       1,2,3,4,5,6,7,8,9,0,1,2,3
    char.hp = 6 + r2d6()                  #  8 - 18  13
    char.m = 2 + int(d10() / 8)           #  2 -  3     7,3
    char.w = 3 + int(d10() / 4)           #  3 -  5       3,4,3
    char.r = 7 + int(d10() / 4)           #  7 -  9               3,4,3
    char.d = 11 + int(d10() / 4)          # 11 - 13                       3,4,3
    char.stam = 7 + d5()                  #  8 - 12  10
    char.visRange = 20 + d10()            # 21 - 30  25
    char.visArc = 220 + d90()             # 221-310 265
    char.visMode = "night"
    char.mana = r2d10() +4                #  6 - 24  15
    char.ap = 3 + int(d10() / 5)          #  3 -  5   4,5,1
    char.xp = 110 + d20()                 # 111-130 120
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.bonuses.append("yield bonus " + str(2 + int(d10() / 3)))
    char.bonuses.append("haggle bonus -" + str(d3()))
    char.money = str(d4())+" gold, "+str(d8())+" silver, "+str(d20())+" copper"
    char.money = "What for? Well I have "+ str(d5()) + " silver and " + str(d10()) + " copper somewhere here"
    char.extras.append("immune to poisons")
    char.extras.append("Elves who are staying in a city or cave without access to nature \n"+
                       "suffer psy-1 mod per week to max -3.")
    char.extras.append("This is immediately restored to mod-0 when returning to nature.")
    # skills
    char.skills['Elvish'] = int(char.int/2) + 3 + d3()
    char.skills['Common'] = int(char.int/3) + d3()
    char.skills['avoid'] = int(char.dex/3) + d2()
    # maneuvers
    char.maneuvers.append('yield')
    char.maneuvers.append('off balance')
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollHalfling():
    char = Character()
    char.race = "halfling"
    # primary
    char.str = r2d4() -1                  #  1 -  7   4
    char.dex = r2d5() +2                  #  4 - 12   7
    char.con = r2d5() -1                  #  1 -  9   5
    char.int = r2d5()                     #  2 - 10   6
    char.psy = r2d5()                     #  2 - 10   6
    char.per = r2d5() +2                  #  4 - 12   8
    char.cha = r2d5() +1                  #  3 - 11   7
    # secondary                                       1,2,3,4,5,6,7,8,9
    char.hp = 6 + r2d5()                  #  8 - 16  12
    char.m = 2 + int(d10() / 10)          #  2 -  3     9,1
    char.w = 2 + int(d10() / 4)           #  2 -  4     3,4,3
    char.r = 4 + int(d10() / 3)           #  4 -  7         2,3,3,2
    char.d = 6 + int(d10() / 3)           #  6 -  9             2,3,3,2
    char.stam = 2 + d5()                  #  4 -  7   5
    char.visRange = 15 + d10()            # 16 - 25  20
    char.visArc = 270 + d90()             # 271-360 315
    char.visMode = "day"
    char.mana = r2d10()                   #  2 - 20  11
    char.ap = 3 + int(d10() / 4)          #  3 -  5   3,4,3
    char.xp = 100 + d20()                 # 101-120 110
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.bonuses.append("yield bonus " + str(2 + int(d10() / 3)))
    sneakbonus = d3()
    char.bonuses.append("sneak bonus +" + str(sneakbonus))
    findbonus = d3()
    char.bonuses.append("find bonus +" + str(findbonus))
    gossipbonus = 0
    if roll(50):
        gossipbonus = d3()
        char.bonuses.append("gossip bonus +" + str(gossipbonus))
    char.yieldBonus = 2 + int(d10() / 3)
    char.money = str(d4())+" gold, "+str(d8())+" silver, "+str(d20())+" copper"
    char.extras.append("Halflings have psy mod-1 unless they eat good food (2x price)")
    # skills
    char.skills['Common'] = int(char.int / 2) + d6()
    char.skills['avoid'] = int(char.dex / 3) + d3()
    char.skills['sneak (incl bonus)'] = max(sneakbonus, int(char.dex / 4) + d2())
    char.skills['find (incl bonus)'] = max(findbonus, int(char.per / 4) + d2())
    if gossipbonus > 0:
        char.skills['gossip (incl bonus)'] = max(gossipbonus, d4())
    # maneuvers
    char.maneuvers.append('yield')
    char.maneuvers.append('off balance')
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollOrc():
    char = Character()
    char.race = "orc"
    # primary
    char.str = r2d6() +1                  #  3 - 13   8
    char.dex = r2d5()                     #  2 - 10   6
    char.con = r2d6() +1                  #  3 - 13   8
    char.int = r2d5() -2                  #  0 -  8   3
    char.psy = r2d5() -2                  #  0 -  8   3
    char.per = r2d5()                     #  2 - 10   6
    char.cha = r2d5() -3                  # -1 -  7   3
    # secondary                                       1,2,3,4,5,6,7,8,9
    char.hp = 7 + r2d10()                 #  9 - 25  18
    char.m = 1 + int(d10() / 4)           #  1 -  3   3,4,3
    char.w = 3 + int(d10() / 4)           #  3 -  5       3,4,3
    char.r = 5 + int(d10() / 4)           #  5 -  7           3,4,3
    char.d = 6 + int(d10() / 3)           #  6 -  9             2,3,3,2
    char.stam = 5 + r2d5()                #  7 - 15  11
    char.visRange = 10 + d10()            # 11 - 20  15
    char.visArc = 120 + d60()             # 121-180 150
    char.visMode = "dusk"
    char.mana = r2d10() -5                # -3 - 15   6
    char.ap = 3 + int(d10() / 9)          #  3 -  4   8,2
    char.xp = 90 + d20()                  # 91 -110 100
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.yieldBonus = 2 + int(d10() / 4)
    char.bonuses.append("yield bonus " + str(char.yieldBonus))
    veteranbonus = d3()
    char.bonuses.append("veteran bonus +" + str(veteranbonus))
    brawlbonus = d3()
    char.bonuses.append("brawl bonus +" + str(brawlbonus))
    char.money = str(d6())+" silver, "+str(d10())+" copper" + ", and " + str(d4()) + " large teeth/claws"
    # skills
    char.skills['Svartlingo'] = int(char.int / 2) + d5()
    char.skills['Common'] = int(char.int / 3) + d3()
    char.skills['veteran (incl bonus)'] = max(veteranbonus, d3())
    brawlskill = max(brawlbonus, int(char.str / 4) + d3())
    char.skills['brawl (incl bonus)'] = brawlskill
    biteskill = d4()
    char.skills['bite'] = biteskill
    # maneuvers
    char.maneuvers.append('strength bonus')
    # yield or perhaps intercept ?
    if roll(50):
        char.maneuvers.append('yield')
    else:
        char.maneuvers.append('! this orc does not start with yield')
        if roll(50):
            char.maneuvers.append('intercept')
        elif roll(50):
            char.maneuvers.append('opportunity')
    char.maneuvers.append('off balance')
    char.maneuvers.append('opportunity')
    # extras
    char.extras.append("double con against poisons")
    char.extras.append("Orcs without any war trophies suffer psy-1 mod, until honour reclaimed.")
    char.extras.append("bite "+str(biteskill)+" dam " + str(int(char.str/6)+d3()) + " slow-1 scf 0.5")
    char.extras.append("brawl fist "+str(brawlskill)+" dam "+str(int(char.str/3)) + " fast+1")
    char.extras.append("brawl kick "+str(brawlskill)+" dam "+str(int(char.str/3)+2))
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollGoblin():
    char = Character()
    char.race = "goblin"
    # primary
    char.str = r2d4() -2                  #  0 -  6   3
    char.dex = r2d5() +2                  #  4 - 12   8
    char.con = r2d4()                     #  2 -  8   5
    char.int = r2d5() -2                  #  0 -  8   4
    char.psy = r2d5() -2                  #  0 -  8   4
    char.per = r2d5()                     #  2 - 10   6
    char.cha = r2d4() -2                  #  0 -  8   3
    # secondary                                       1,2,3,4,5,6,7,8
    char.hp = 6 + r2d4()                  #  8 - 14  11
    char.m = 1 + int(d10() / 10)          #  1 -  2   9,1
    char.w = 2 + int(d10() / 4)           #  2 -  4     3,4,3
    char.r = 3 + int(d10() / 3)           #  3 -  6       2,3,3,2
    char.d = 5 + int(d10() / 3)           #  5 -  8           2,3,3,2
    char.stam = 2+d5()                    #  4 -  7   5
    char.visRange = 15 + d10()            # 16 - 25  20
    char.visArc = 180 + d90()             # 181-270 225
    char.visMode = "dusk"
    char.mana = r2d8()-4                  # -2 - 12   5
    char.ap = 4 + int(d10() / 4)          #  4 -  6   3,4,3
    char.xp = 80 + d20()                  # 81 -100  90
    # fixup
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.bonuses.append("yield bonus " + str(2 + int(d10() / 3)))
    sneakbonus = d3()
    char.bonuses.append("sneak bonus +" + str(sneakbonus))
    if roll(66):
        disengagebonus = d3()
        char.bonuses.append("disengage bonus +" + str(d3()))
    else:
        disengagebonus = 0
    char.yieldBonus = 2 + int(d10() / 3)
    if char.mana < 0 and roll(50):
        char.mana = -9
        char.bonuses.append("Nullskull")
    # skills
    char.skills['Svartlingo'] = int(char.int / 2) + d3()
    char.skills['Common'] = int(char.int / 3) + d3()
    char.skills['brawl'] = int(max(char.dex,char.str) / 4) + d3()
    char.skills['avoid'] = int(char.dex / 4) + d3()
    char.skills['sneak (incl bonus)'] = max(sneakbonus, int(char.per / 4) + d2())
    if disengagebonus > 0:
        char.skills['disengage (incl bonus)'] = max(disengagebonus, int(char.dex / 4) + d2())
    else:
        char.skills['disengage'] = int(char.dex / 4) + d2()
    char.skills['throw'] = int(char.dex / 4) +d2()
    bitedam = 1+int(d10()/3)                             # 1-4 (2,3,3,2)
    scratchdam = int(1+d10()/10)                       # 1-2 (9,1)
    # maneuvers
    char.maneuvers.append('yield')
    char.maneuvers.append('off balance')
    # extras
    char.extras.append("goblins can live on half rations, and can eat spoiled food")
    char.extras.append("brawl bite: dam "+str(bitedam)+" 3ap (2ap if both hands free)")
    char.extras.append("brawl scratch: dam "+str(scratchdam)+" 2ap (1ap if both hands free) every third attack costs 1 stamina")
    if roll(33):
        clawbonus = 1
        if roll(33):
            clawbonus = 2
        char.extras.append("brawl claw: dam(fist)+"+str(clawbonus)+" fast+1 first two attacks don't require stamina")
    char.money = str(int(d10()/4))+" silver, "+str(d12())+" copper" +", "+ str(d4())+" teeth, " \
                 + str(d3())+ " stones, "+ str(d2())+ " feathers, "+ str(d3())+" glass beads"
    # done
    return char


#roll humans
for i in range(0, humans):
    rollHuman().printSheet(i)
    print("\n\n\n")
print("\n\n\n")


#roll dwarves
for i in range(0,dwarves):
    rollDwarf().printSheet(i)
    print("\n\n\n")
print("\n\n\n")


#roll elves
for i in range(0,elves):
    rollElf().printSheet(i)
    print("\n\n\n")
print("\n\n\n")


#roll halflings
for i in range(0,halflings):
    rollHalfling().printSheet(i)
    print("\n\n\n")
print("\n\n\n")


#roll orcs
for i in range(0,orcs):
    rollOrc().printSheet(i)
    print("\n\n\n")
print("\n\n\n")


#roll goblins
for i in range(0,goblins):
    rollGoblin().printSheet(i)
    print("\n\n\n")
print("\n\n\n")







# exit here for the new roll stuff, the old comes below
sys.exit(0)
