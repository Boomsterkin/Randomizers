import random
v=0
spidey=raw_input("Peter or Miles? ")
print
print("Suit:")
suit=random.randint(1,39)
if spidey!="Miles":
    if suit==1:
        print("Advanced Suit 2.0")
        v+=1
    elif suit==2:
        print("Black Suit")
    elif suit==3:
        print("Symbiote Suit")
    elif suit==4:
        print("Anti-Venom Suit")
    elif suit==5:
        print("Classic Suit")
        v+=1
    elif suit==6:
        print("Scarlet III Suit")
        v+=1
    elif suit==7:
        print("Advanced Suit")
        v+=1
    elif suit==8:
        print("Kumo Suit")
        v+=1
    elif suit==9:
        print("No Way Home Suit")
    elif suit==10:
        print("Amazing Suit")
    elif suit==11:
        print("Amazing 2 Suit")
    elif suit==12:
        print("2099 Suit")
        v+=1
    elif suit==13:
        print("Scarlet Suit")
        v+=1
    elif suit==14:
        print("Superior Suit")
        v+=1
    elif suit==15:
        print("Anti-Ock Suit")
        v+=1
    elif suit==16:
        print("Arachknight Suit")
        v+=1
    elif suit==17:
        print("ITSV Noir Suit")
    elif suit==18:
        print("Homemade Suit")
    elif suit==19:
        print("Spider-Punk")
        v+=1
    elif suit==20:
        print("Civil War Suit")
        v+=1
    elif suit==21:
        print("Iron Spider Armour")
        v+=1
    elif suit==22:
        print("Webbed Black Suit")
    elif suit==23:
        print("Webbed Suit")
    elif suit==24:
        print("Homecoming Suit")
    elif suit==25:
        print("New Blue Suit")
        v+=1
    elif suit==26:
        print("Far From Home Suit")
    elif suit==27:
        print("Night Monkey Suit")
    elif suit==28:
        print("Classic Black Suit")
        v+=1
    elif suit==29:
        print("Nanotech Iron Spider")
    elif suit==30:
        print("New Red Suit")
    elif suit==31:
        print("Inside-Out Suit")
    elif suit==32:
        print("Life Story Suit")
        v+=1
    elif suit==33:
        print("Last Hunt Suit")
        v+=1
    elif suit==34:
        print("Saving Lives Suit")
        v+=1
    elif suit==35:
        print("Aurantia Suit")
    elif suit==36:
        print("Apunkalyptic Suit")
    elif suit==37:
        print("Tactical Suit")
    elif suit==38:
        print("Stone Monkey Suit")
    else:
        print("25th Century Suit")
else:
    if suit==1:
        print("Upgraded Suit")
        v+=1
    elif suit==2:
        print("Evolved Suit")
        v+=1
    elif suit==3:
        print("Family Business Suit")
        v+=1
    elif suit==4:
        print("Classic Suit")
        v+=1
    elif suit==5:
        print("T.R.A.C.K. Suit")
        v+=1
    elif suit==6:
        print("Brooklyn 2099 Suit")
        v+=1
    elif suit==7:
        print("Sportswear Suit")
        v+=1
    elif suit==8:
        print("Life Story Suit")
        v+=1
    elif suit==9:
        print("2099 Suit")
        v+=1
    elif suit==10:
        print("Advanced Tech Suit")
        v+=1
    elif suit==11:
        print("Shadow-Spider Suit")
        v+=1
    elif suit==12:
        print("2020 Suit")
        v+=1
    elif suit==13:
        print("Purple Reign Suit")
        v+=1
    elif suit==14:
        print("Bodega Cat Suit")
        v+=1
    elif suit==15:
        print("Forever Suit")
        v+=1
    elif suit==16:
        print("Homemade Suit")
        v+=1
    elif suit==17:
        print("ITSV Suit")
    elif suit==18:
        print("ITSV Cape Suit")
    elif suit==19:
        print("The End Suit")
        v+=1
    elif suit==20:
        print("10th Anniversary Suit")
        v+=1
    elif suit==21:
        print("Programmable Matter Suit")
        v+=1
    elif suit==22:
        print("S.T.R.I.K.E. Suit")
        v+=1
    elif suit==23:
        print("Agent of SHIELD Suit")
        v+=1
    elif suit==24:
        print("Great Responsibility Suit")
        v+=1
    elif suit==25:
        print("ATSV Suit")
    elif suit==26:
        print("Crimson Cowl Suit")
        v+=1
    elif suit==27:
        print("Best There Is Suit")
        v+=1
    elif suit==28:
        print("Dark Ages Suit")
        v+=1
    elif suit==29:
        print("Absolute Carnage Suit")
        v+=1
    elif suit==30:
        print("King in Black Suit")
        v+=1
    elif suit==31:
        print("Boricua Suit")
        v+=1
    elif suit==32:
        print("Smoke & Mirrors Suit")
        v+=1
    elif suit==33:
        print("Most Dangerous Game Suit")
        v+=1
    elif suit==34:
        print("City Sounds Suit")
        v+=1
    elif suit==35:
        print("Encoded Suit")
    elif suit==36:
        print("Biomechanical Suit")
    elif suit==37:
        print("Tokusatsu Suit")
    elif suit==38:
        print("Agimat Suit")
    else:
        print("Red Spectre Suit")
if v==1:
    print("Variation "+str(random.randint(1,4)))
print
print("Perks:")
x=random.randint(1,2)
if x==1:
    print("Confidence Boost")
else:
    print("Rejuvenating Parry")
x=random.randint(1,2)
if x==1:
    print("The Best Defense")
else:
    print("Life Link")
x=random.randint(1,2)
if x==1:
    print("Air Marshal")
else:
    print("Focused Parry")
x=random.randint(1,2)
if x==1:
    print("Combo King")
else:
    print("The Floor is Lava")
x=random.randint(1,2)
if x==1:
    print("Focused Strike")
else:
    print("Target Acquisition")
x=random.randint(1,2)
if x==1:
    print("Perfect Sight")
else:
    print("Eyes on Target")
x=random.randint(1,2)
if x==1:
    print("Acrobat")
else:
    print("Charged")
x=random.randint(1,2)
if x==1:
    print("All Seeing")
else:
    print("Active Spider")
print
print("Abilities:")
if spidey=="Peter":
    x=random.randint(1,3)
    if x==1:
        print("Spider-Barrage")
    elif x==2:
        print("Anti-Venom Punch")
    else:
        print("Anti-Venom Bomb")
    x=random.randint(1,2)
    if x==1:
        print("Spider-Rush")
    else:
        print("Anti-Venom Strike")
    x=random.randint(1,2)
    if x==1:
        print("Spider-Shock")
    else:
        print("Anti-Venom Blast")
    x=random.randint(1,3)
    if x==1:
        print("Spider-Whiplash")
    elif x==2:
        print("Anti-Venom Yank")
    else:
        print("Anti-Venom Tempest")
else:
    x=random.randint(1,2)
    if x==1:
        print("Venom Punch")
    else:
        print("Chain Lightning")
    x=random.randint(1,2)
    if x==1:
        print("Venom Dash")
    else:
        print("Thunder Step")
    x=random.randint(1,2)
    if x==1:
        print("Venom Smash")
    else:
        print("Reverse Flux")
    x=random.randint(1,2)
    if x==1:
        print("Venom Jump")
    else:
        print("Galvanize")