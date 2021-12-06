#!/usr/bin/python

import math
import random

import sys

#import pyparsing




# ------------- for regular quick roll selection, just change here -------------
#distribution = "standard_set"      # standard selection: 17 dudes, too heroic
distribution = "small_set"         # small set, any race: 10 dudes, still heroic
#distribution = "tiny_set"          # small set, any race: 8 dudes, still strong
#distribution = "min_set"           # minimal set, 6 dudes, one of each race
#-------------------------------------------------------------------------------




#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80

# clean zero set:
humans = dwarves = elves = halflings = orcs = goblins = 0


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
# still give too high chance of OP characters in each set.
if distribution == "small_set" :
    humans =       2
    dwarves =      1
    elves =        1
    halflings =    2
    orcs =         1
    goblins =      3

# 8 total, reasonable representation if choosing from all races
# still give high chance of OP characters in each set.
if distribution == "tiny_set" :
    humans =       2
    dwarves =      1
    elves =        1
    halflings =    1
    orcs =         1
    goblins =      2

# 6 total, minimal set if choosing from all races
# but distribution will make less interesting race spread
if distribution == "min_set" :
    humans =       1
    dwarves =      1
    elves =        1
    halflings =    1
    orcs =         1
    goblins =      1




#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80

# check command line arguments, will override any set value

if len(sys.argv) != 1 :
    if len(sys.argv) == 3 :
        humans = dwarves = elves = halflings = orcs = goblins = 0   # clear set
        locals()[sys.argv[1]] = int(sys.argv[2])                    # race,number
    else :
        print ("USAGE: rollchars.py [race number]")
        print ("  e.g: rollchars.py orcs 3")
        print ("       note race plural form")
        exit(1)




#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80

def die(n):
    return random.randint(1,n)

# create more dice functions on the form: dN()
for n in {2,3,4,5,6,7,8,9,10,12,15,20,30,40,50,60,90,100}:
    exec("def d"+str(n)+"(): return die("+str(n)+")")

# create more dice functions on the form: r2dN()
for n in {3,4,5,6,7,8,9,10,20}:
    exec("def r2d"+str(n)+"(): return d"+str(n)+"() + d"+str(n)+"()")


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

def flat(min,max):
    return min + random.randint(0,(max-min))

def bell2(min,max):
    if (max-min)%2 != 0:
        raise NameError("bell2("+str(min)+","+str(max)+") has range "
                +str(max-min+1)+", which is not evenly divisible by 2.")
    dx = (max-min)/2 +1
    return min-2 + die(dx) + die(dx)

def bell3(min,max):
    if (max-min)%3 != 0:
        raise NameError("bell3("+str(min)+","+str(max)+") has range "
                +str(max-min+1) +", which is not evenly divisible by 3.")
    dx = (max-min)/3 +1
    return min-3 + die(dx) + die(dx) + die(dx)


def pad2(string):
    if len(string) >= 2:
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
    extras = []
    # starting skills & attacks, maneuvers
    skills = []
    money = "unset"

    def __init__(self):
        self.bonuses = []
        self.extras = []
        self.skills.clear()
        self.maneuvers = []

    def printSheet(self, i):
        # create left column text, 26 cols
        pad20 = " " * 20
        str_hp =   "str " + pad2(str(self.str)) + pad20
        dex_move = "dex " + pad2(str(self.dex)) + pad20
        con_stam = "con " + pad2(str(self.con)) + pad20
        int_vis =  "int " + pad2(str(self.int)) + pad20
        psy_mana = "psy " + pad2(str(self.psy)) + pad20
        per_ap =   "per " + pad2(str(self.per)) + pad20
        cha_xp =   "cha " + pad2(str(self.cha)) + pad20
        # create right column text
        str_hp = str_hp + "hp " + str(self.hp) + " abs 0"
        dex_move = (dex_move + "m" + str(self.m) + " w" + str(self.w)
                + " r" + str(self.r) + " d" + str(self.d))
        con_stam = con_stam + "stamina " + str(self.stam)
        int_vis = (int_vis + "vision " + str(self.visRange) + " "
                + str(self.visMode) + " " + str(self.visArc))
        psy_mana = psy_mana + "mana " + str(self.mana)
        per_ap = per_ap + "action points " + str(self.ap)
        cha_xp = cha_xp + "xp " + str(self.xp)
        # start printing
        #print("================== "+self.race+" "+nr+" ==================")
        linelength = 44
        sepline = "-" * linelength
        title = " " + self.race + " " + str(i+1) + " "
        pre = "=" * int((linelength - len(title)) / 2)
        post = "=" * (linelength - len(pre) - len(title))
        header = pre + title + post
        print(header)
        # stat lines
        print(str_hp)
        print(dex_move)
        print(con_stam)
        print(int_vis)
        print(psy_mana)
        print(per_ap)
        print(cha_xp)
        # extras, bonuses, skills, etc
        if len(self.bonuses) > 0:
            print(sepline)
            for bonus in self.bonuses :
                print(bonus)
        if len(self.skills) > 0:
            print(sepline)
            for skill in self.skills :
                print(skill)
        if len(self.extras) > 0:
            print(sepline)
            for extra in self.extras:
                print(extra)
        print(sepline)
        print("money: " + str(self.money))


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80





# There are some strange dice combinations in here. If you feel uncertain about
# the various distributions check out something like: https://anydice.com/
# which can give you a better grasp on how the rolls spread.
#
# Here are some distributions, scores and percentages
#
#  2d6:               2d5:               2d4:          2d3:
#   2    2.78          2    4.00          2    6.25     2   11.11
#   3    5.56          3    8.00          3   12.50     3   22.22
#   4    8.33          4   12.00          4   18.75     4   33.33
#   5   11.11          5   16.00          5   25.00     5   22.22
#   6   13.89          6   20.00          6   18.75     6   11.11
#   7   16.67          7   16.00          7   12.50
#   8   13.89          8   12.00          8    6.25
#   9   11.11          9    8.00
#  10    8.33         10    4.00
#  11    5.56
#  12    2.78


# I've generally included the range and division spreads as comments for quick
# comparisons. Here is a summary.
#
# asymmetric distributions: 5,7-10
#                 d10/10 1-9                 10     0,1  9,1
#                 d10/9  1-8               9-10     0,1  8,2
#                 d10/8  1-7               8-10     0,1  7,3
#                 d10/7  1-6               7-10     0,1  6,4
#                 d10/5  1-4      5-9        10     0-2  4,5,1
#
# symmetric distributions: 2-4,6
#                 d10/6  1-5               6-10     0,1  5-5
#                 d10/4  1-3      4-7      8-10     0-2  3-4-3
#                 d10/3  1-2   3-5   6-8   9-10     0-3  2-3-3-2
#                 d10/2  1  2-3 4-5 6-7 8-9  10     0-5  1-2-2-2-2-1




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
    # fixup movement speeds
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    char.money = str(d4())+" gold, "+str(d8())+" silver, "+str(d20())+" copper"
    # skills
    char.skills.append("Common " + str(flat(3,4+int(char.int/3))))
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
    char.int = r2d4() +2                  #  4 - 10   7
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
    char.visArc = 150 + d60()             # 151-210 180
    char.visMode = "infra+dusk"
    char.mana = r2d10()                   #  2 - 20  11
    char.ap = 3 + int(d10() / 9)          #  3 -  4   8,2
    char.xp = 105 + d20()                 # 106-125 115
    # fixup movement speeds
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    hagglebonus = flat(1,3)
    blockbonus = flat(1,3)
    dungeoneeringbonus = 0
    if roll(25):
        dungeoneeringbonus = flat(1,3)
    char.bonuses.append("haggle bonus +" + str(hagglebonus))
    char.bonuses.append("block bonus +"+str(blockbonus))
    dungeoneeringbonus = 0
    if dungeoneeringbonus > 0:
        char.bonuses.append("dungeoneering bonus +" + str(dungeoneeringbonus))
    char.money = (str(d10())+" gold, "+str(d20())+" silver, "+str(d20())+" "
            +" copper" + ", and a gemstone worth " + str(5+d6()) + " gold")
    char.extras.append("con bonus +3 against poisons")
    char.extras.append("Dwarves without any gems, and/or with less than "
            +"5 gold \n"+"total coin suffer psy-1 mod until wealthy again.")
    char.extras.append("Dwarves with 50+ gold in coins and gems gain psy+1 "
            +"mod while wealthy.")
    # skills
    char.skills.append("Dwarvish " + str(flat(4,5+int(char.int/3))))
    char.skills.append("Common " + str(flat(3,4+int(char.int/3))))
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
    char.hp = 8 + r2d5()                  # 10 - 18  14
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
    # fixup movement speeds
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    hagglebonus = -flat(1,3)
    avoidbonus = flat(0,2)
    char.bonuses.append("haggle bonus " + str(hagglebonus))
    if avoidbonus > 0:
        char.bonuses.append("avoid bonus +" + str(avoidbonus))
    char.money = ("What for? Well I have "+ str(d5()) + " silver and "
            + str(d10()) + " copper somewhere here")
    char.extras.append("immune to poisons")
    char.extras.append("Elves who are staying in a city or cave without "
            +"access to nature \n"+"suffer psy-1 mod per week to max -3.")
    char.extras.append("This is immediately restored to mod-0 when "
            +"returning to nature.")
    # skills
    char.skills.append("Elvish " + str(flat(5,6+int(char.int/3))))
    char.skills.append("Common " + str(flat(2,4)))
    #char.skills["avoid"] = flat(1,3)
    # maneuvers
    #char.maneuvers.append("yield +" + str(2 + int(d10() / 3)))   # 2-5 (2,3,3,2)
    char.maneuvers.append("off balance")
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollHalfling():
    char = Character()
    char.race = "halfling"
    # primary
    char.str = r2d4() -1                  #  1 -  7   4
    char.dex = r2d5() +2                  #  4 - 12   8
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
    char.stam = 3 + d7()                  #  4 - 10   7
    char.visRange = 15 + d10()            # 16 - 25  20
    char.visArc = 270 + d90()             # 271-360 315
    char.visMode = "day"
    char.mana = r2d10()                   #  2 - 20  11
    char.ap = 3 + int(d10() / 4)          #  3 -  5   3,4,3
    char.xp = 100 + d20()                 # 101-120 110
    # fixup movement speeds
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    tacklebonus = -flat(1,2)
    char.bonuses.append("tackle and block bonus " + str(tacklebonus))
    sneakbonus = 0
    if roll(50):
        sneakbonus = flat(1,3)
        char.bonuses.append("sneak bonus +" + str(sneakbonus))
    findbonus = 0
    if roll(50):
        findbonus = flat(1,3)
        char.bonuses.append("find bonus +" + str(findbonus))
    gossipbonus = 0
    if roll(80):
        gossipbonus = flat(1,3)
        char.bonuses.append("gossip bonus +" + str(gossipbonus))
    char.money = str(d4())+" gold, "+str(d8())+" silver, "+str(d20())+" copper"
    char.extras.append("Halflings gain psy+1 for 24h when eating good "
            +"food (3x price)")
    # skills
    char.skills.append("Common " + str(flat(3,4+int(char.int/3))))
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
    char.int = r2d5() -2                  #  0 -  8   4
    char.psy = r2d5() -2                  #  0 -  8   4
    char.per = r2d5()                     #  2 - 10   6
    char.cha = r2d5() -3                  # -1 -  7   3
    # secondary                                       1,2,3,4,5,6,7,8,9
    char.hp = 6 + r2d9()                  #  8 - 24  16
    char.m = 1 + int(d10() / 9)           #  1 -  2   8,2
    char.w = 2 + int(d10() / 3)           #  2 -  5     2,3,3,2
    char.r = 4 + int(d10() / 3)           #  4 -  7         2,3,3,2
    char.d = 6 + int(d10() / 3)           #  6 -  9             2,3,3,2
    char.stam = 3 + d10()                 #  4 - 14   8
    char.visRange = 10 + d10()            # 11 - 20  15
    char.visArc = 120 + d60()             # 121-180 150
    char.visMode = "dusk"
    char.mana = r2d10() -5                # -3 - 15   6
    char.ap = 3 + int(d10() / 9)          #  3 -  4   8,2
    char.xp = 90 + d20()                  # 91 -110 100
    # fixup movement speeds
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    veteranbonus = flat(0,2)
    if veteranbonus > 0:
        char.bonuses.append("veteran bonus +" + str(veteranbonus))
    brawlbonus = flat(0,3)
    if brawlbonus > 0:
        char.bonuses.append("brawl bonus +" + str(brawlbonus))
    char.money = (str(d6())+" silver, "+str(d10())+" copper\n    "
            +str(d4()) + " large teeth/claws")
    # skills
    char.skills.append("Svartlingo " + str(flat(2,4)))
    char.skills.append("Common " + str(flat(1,3)))
    #char.skills["veteran (incl bonus)"] = max(veteranbonus, d3())
    brawlskill = flat(1,4-brawlbonus)
    if brawlbonus > 0:
        char.skills.append("brawl "+str(brawlskill+brawlbonus)
                +"("+str(brawlskill)+"+"+str(brawlbonus)+")")
    else:
        char.skills.append("brawl "+str(brawlskill))
    # maneuvers
    if roll(50):
        char.skills.append("strength bonus")
    # extras
    char.extras.append("double con against poisons")
    char.extras.append("Orcs without any war trophies suffer psy-1 mod, \n"
            +"until honour reclaimed.")
    # attacks
    bitedam = flat(1,5)
    fistdam = int(char.str/3)                          # 1-4 (1,3,3,2)
    kickdam = int(char.str/3)+2                        # 3-6
    char.extras.append("brawl fist: "+str(brawlskill)+" dam "
            +str(fistdam) + " fast+1")
    char.extras.append("brawl kick: "+str(brawlskill)+" dam "+str(kickdam))
    char.extras.append("brawl bite: "+str(brawlskill)+" dam "+str(bitedam)
            +" slow-1, gives +1 extra pain")
    if roll(33):
        clawdam = fistdam -1
        if roll(50):
            clawdam = fistdam +1
            if roll(25):
                clawdam = fistdam +2
        char.extras.append("brawl claw: "+str(brawlskill)+" dam "
                +str(clawdam)+" fast+1 first two attacks don't require stamina")
    # done
    return char


#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80
def rollGoblin():
    char = Character()
    char.race = "goblin"
    # primary
    char.str = r2d4() -2                  #  0 -  6   3
    char.dex = r2d6()                     #  2 - 12   7
    char.con = r2d5() -2                  #  0 -  8   4
    char.int = r2d5() -2                  #  0 -  8   4
    char.psy = r2d5() -2                  #  0 -  8   4
    char.per = r2d5()                     #  2 - 10   6
    char.cha = r2d4() -2                  #  0 -  8   3
    # secondary                                       1,2,3,4,5,6,7,8
    char.hp = 6 + d6()                    #  7 - 12  10
    char.m = 1 + int(d10() / 10)          #  1 -  2   9,1
    char.w = 2 + int(d10() / 4)           #  2 -  4     3,4,3
    char.r = 3 + int(d10() / 3)           #  3 -  6       2,3,3,2
    char.d = 5 + int(d10() / 3)           #  5 -  8           2,3,3,2
    char.stam = 2+d5()                    #  4 -  7   5
    char.visRange = 10 + d15()            # 11 - 25  17
    char.visArc = 180 + d90()             # 181-270 225
    char.visMode = "dusk"
    char.mana = r2d8()-4                  # -2 - 12   5
    char.ap = 3 + int(d10() / 4)          #  3 -  5   3,4,3
    char.xp = 80 + d20()                  # 81 -100  90
    # fixup movement speeds
    char.w = max(char.m + 1, char.w)
    char.r = max(char.w + 1, char.r)
    char.d = max(char.r + 1, char.d)
    # tertiary
    tacklebonus = -flat(2,3)
    char.bonuses.append("tackle and block " + str(tacklebonus))
    sneakbonus = d3()
    sneakskill = d2() -1
    sneaktot = sneakskill + sneakbonus
    char.bonuses.append("sneak bonus +" + str(sneakbonus))
    # ? Nullskull
    if char.mana < 0 and roll(50):
        char.mana = -99
        char.skills.append("Nullskull")
    # skills
    char.skills.append("Svartlingo " + str(flat(2,4)))
    char.skills.append("Common " + str(flat(1,3)))
    brawlskill = flat(1,3)
    char.skills.append("brawl " + str(brawlskill))
    # extras
    char.extras.append("goblins can live on half rations "
            +"and can eat spoiled food")
    fistdam = int(char.str/3)                          # 1-4 (1,3,3,2)
    kickdam = int(char.str/3)+2                        # 3-6
    bitedam = 1+int(d10()/3)                                     # 1-4 (2,3,3,2)
    scratchdam = int(1+d10()/10)                                 # 1-2 (9,1)
    char.extras.append("brawl fist: "+str(brawlskill)+" dam "
            +str(fistdam) + " fast+1")
    char.extras.append("brawl kick: "+str(brawlskill)+" dam "
            +str(kickdam))
    char.extras.append("brawl bite: "+str(brawlskill)+" dam "+str(bitedam)+" "
            +"3ap (2ap if both hands free)")
    char.extras.append("brawl scratch: "+str(brawlskill)+" dam "
            +str(scratchdam)+" 2ap (1ap if both hands free)\n" + "    "
            +"every second attack costs 0 stamina")
    char.money = (str(int(d10()/4))+" silver, "+str(d12())+" copper\n    "
            +str(d4())+" teeth, " + str(d3())+ " stones, "
            +str(d2())+ " feathers, "+ str(d3())+" glass beads")
    # done
    return char




#--------|---------|---------|---------|---------|---------|---------|---------|
#       10        20        30        40        50        60        70        80


print("\n\n\n")


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




# controlled exit
sys.exit(0)
