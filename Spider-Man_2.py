import random
v=0
spidey=input("Peter or Miles? ")
print()
print("Suit:")
suit=random.randint(1,45)
if spidey!="Miles":
    if suit==1:
        print("Advanced 2.0")
        v+=1
    elif suit==2:
        print("Symbiote")
        v+=1
    elif suit==3:
        print("Venom")
        v+=1
    elif suit==4:
        print("Anti-Venom")
        v+=1
    elif suit==5:
        print("Classic")
        v+=1
    elif suit==6:
        print("Scarlet III")
        v+=1
    elif suit==7:
        print("Advanced 1.0")
        v+=1
    elif suit==8:
        print("Kumo")
        v+=1
    elif suit==9:
        print("Hybrid Holland")
    elif suit==10:
        print("Dark Garfield")
    elif suit==11:
        print("Light Garfield")
    elif suit==12:
        print("Spider-Man 2099")
        v+=1
    elif suit==13:
        print("Scarlet Spider")
        v+=1
    elif suit==14:
        print("Superior Spider-Man")
        v+=1
    elif suit==15:
        print("Anti-Ock Armour")
        v+=1
    elif suit==16:
        print("The Arachknight")
        v+=1
    elif suit==17:
        print("Spider-Man Noir")
    elif suit==18:
        print("Homemade Holland")
    elif suit==19:
        print("Spider-Punk")
        v+=1
    elif suit==20:
        print("Military Grade")
        v+=1
    elif suit==21:
        print("Iron Spider Armour")
        v+=1
    elif suit==22:
        print("Bully Maguire")
    elif suit==23:
        print("Tobey Maguire")
    elif suit==24:
        print("Homecoming Holland")
    elif suit==25:
        print("New Blue")
        v+=1
    elif suit==26:
        print("Homebound Holland")
    elif suit==27:
        print("Night Monkey")
    elif suit==28:
        print("Classic Symbiote")
        v+=1
    elif suit==29:
        print("Iron Spider Holland")
    elif suit==30:
        print("New Red")
    elif suit==31:
        print("Homewrecker Holland")
    elif suit==32:
        print("Life Story")
        v+=1
    elif suit==33:
        print("Last Hunt")
        v+=1
    elif suit==34:
        print("Saving Lives")
        v+=1
    elif suit==35:
        print("Aurantia")
    elif suit==36:
        print("Apunkalyptic")
    elif suit==37:
        print("Tactical")
    elif suit==38:
        print("Stone Monkey")
    elif suit==39:
        print("Spider-Man 2400")
    elif suit==40:
        print("Fly-Man")
    elif suit==41:
        print("Hellfire Gala")
    elif suit==42:
        print("Fluro")
        v+=1
    elif suit==43:
        print("Motorchic")
        v+=1
    elif suit==44:
        print("Last Stand")
        v+=1
    else:
        print("Spider-Verse")
else:
    if suit==1:
        print("Upgraded")
        v+=1
    elif suit==2:
        print("Evolved")
        v+=1
    elif suit==3:
        print("Family Business")
        v+=1
    elif suit==4:
        print("Classic")
        v+=1
    elif suit==5:
        print("T.R.A.C.K.")
        v+=1
    elif suit==6:
        print("Brooklyn 2099")
        v+=1
    elif suit==7:
        print("Sportswear")
        v+=1
    elif suit==8:
        print("Life Story")
        v+=1
    elif suit==9:
        print("Spider-Man 2099")
        v+=1
    elif suit==10:
        print("Advanced Tech")
        v+=1
    elif suit==11:
        print("Shadow-Spider")
        v+=1
    elif suit==12:
        print("Spider-Man 2020")
        v+=1
    elif suit==13:
        print("Purple Reign")
        v+=1
    elif suit==14:
        print("Bodega Cat")
        v+=1
    elif suit==15:
        print("Wakanda Forever")
        v+=1
    elif suit==16:
        print("Homemade")
        v+=1
    elif suit==17:
        print("ITSV")
    elif suit==18:
        print("ITSV Cape")
    elif suit==19:
        print("The End")
        v+=1
    elif suit==20:
        print("10th Anniversary")
        v+=1
    elif suit==21:
        print("Programmable Matter")
        v+=1
    elif suit==22:
        print("S.T.R.I.K.E.")
        v+=1
    elif suit==23:
        print("Agent of SHIELD")
        v+=1
    elif suit==24:
        print("Great Responsibility")
        v+=1
    elif suit==25:
        print("ATSV")
    elif suit==26:
        print("Crimson Cowl")
        v+=1
    elif suit==27:
        print("The Best There Is")
        v+=1
    elif suit==28:
        print("Dark Ages")
        v+=1
    elif suit==29:
        print("Absolute Carnage")
        v+=1
    elif suit==30:
        print("King in Black")
        v+=1
    elif suit==31:
        print("Boricua")
        v+=1
    elif suit==32:
        print("Smoke & Mirrors")
        v+=1
    elif suit==33:
        print("Most Dangerous Game")
        v+=1
    elif suit==34:
        print("City Sounds")
        v+=1
    elif suit==35:
        print("Encoded")
    elif suit==36:
        print("Biomechanical")
    elif suit==37:
        print("Tokusatsu")
    elif suit==38:
        print("Agimat")
    elif suit==39:
        print("Red Spectre")
    elif suit==40:
        print("Fresh-Man")
    elif suit==41:
        print("Hellfire Gala")
    elif suit==42:
        print("Metro")
        v+=1
    elif suit==43:
        print("Ginga")
        v+=1
    elif suit==44:
        print("Uptown Pride")
        v+=1
    else:
        print("Animated")
if v==1:
    print("V"+str(random.randint(1,4)))
print()
print("Suit Tech:")
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
print()
print("Gadgets:")
x=random.randint(1,2)
if x==1:
    print("Standard Web-Shooters")
else:
    print("Golden Web-Shooters")
x=random.randint(1,2)
if x==1:
    print("Standard Upshot")
else:
    print("Golden Upshot")
x=random.randint(1,2)
if x==1:
    print("Standard Web Grabber")
else:
    print("Golden Web Grabber")
x=random.randint(1,2)
if x==1:
    print("Standard Sonic Burst")
else:
    print("Golden Sonic Burst")
x=random.randint(1,2)
if x==1:
    print("Standard Ricochet Web")
else:
    print("Golden Ricochet Web")
print()
if spidey=="Peter":
    color=random.randint(1,2)
    if color==1:
        bw=""
    else:
        bw="Anti-"
    print("Abilities:")
    x=random.randint(1,3)
    if x==1:
        print("Waldo-Wham")
    elif x==2:
        print(bw+"Venom Vehemence")
    else:
        print(bw+"Venom Volley")
    x=random.randint(1,2)
    if x==1:
        print("Waldo-Whirl")
    else:
        print(bw+"Venom Vore")
    x=random.randint(1,2)
    if x==1:
        print("Waldo-Wire")
    else:
        print(bw+"Venom Violence")
    x=random.randint(1,3)
    if x==1:
        print("Waldo-Whiplash")
    elif x==2:
        print(bw+"Venom Vellicate")
    else:
        print(bw+"Venom Vortex")
    print()
    print("Symbiote Color:")    
    if color==1:
        print("Black")
    else:
        print("White")
else:
    print("Abilities:")
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
