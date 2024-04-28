"""
Rynds_Spellcasting
"""
import random
prepnum=0
offense=24
defense=0
mobility=0
utility=8
bane=0
bless=0
ceremony=0
command=0
createordestroywater=0
curewounds=0
detectevilandgood=0
detectmagic=0
detectpoisonanddisease=0
guidingbolt=0
healingword=0
inflictwounds=0
protectionfromevilandgood=0
purifyfoodanddrink=0
sanctuary=0
shieldoffaith=0
aid=0
augury=0
blindnessdeafness=0
borrowedknowledge=0
calmemotions=0
continualflame=0
enhanceability=0
findtraps=0
gentlerepose=0
holdperson=0
lesserrestoration=0
locateobject=0
prayerofhealing=0
protectionfrompoison=0
silence=0
spiritualweapon=0
wardingbond=0
zoneoftruth=0
animatedead=0
auraofvitality=0
beaconofhope=0
bestowcurse=0
clairvoyance=0
createfoodandwater=0
daylight=0
dispelmagic=0
fastfriends=0
feigndeath=0
glyphofwarding=0
incitegreed=0
lifetransference=0
magiccircle=0
masshealingword=0
meldintostone=0
motivationalspeech=0
protectionfromenergy=0
removecurse=0
revivify=0
sending=0
speakwithdead=0
spiritguardians=0
spiritshroud=0
tongues=0
waterwalk=0
auraoflife=0
auraofpurity=0
banishment=0
deathward=0
divination=0
freedomofmovement=0
guardianoffaith=0
locatecreature=0
stoneshape=0
commune=0
contagion=0
dawn=0
dispelevilandgood=0
flamestrike=0
geas=0
greaterrestoration=0
hallow=0
holyweapon=0
legendlore=0
masscurewounds=0
planarbinding=0
raisedead=0
scrying=0
summoncelestial=0
while prepnum<13:
    x=input("Any Forced Spells? ")
    if x=="Bane":
        bane+=1
        offense+=1
        prepnum+=1
    elif x=="Bless":
        bless+=1
        utility+=1
        prepnum+=1
    elif x=="Ceremony":
        ceremony+=1
        utility+=1
        prepnum+=1
    elif x=="Command":
        command+=1
        utility+=1
        prepnum+=1
    elif x=="Create or Destroy Water":
        createordestroywater+=1
        utility+=1
        prepnum+=1
    elif x=="Cure Wounds":
        curewounds+=1
        defense+=1
        prepnum+=1
    elif x=="Detect Evil and Good":
        detectevilandgood+=1
        utility+=1
        prepnum+=1
    elif x=="Detect Magic":
        detectmagic+=1
        utility+=1
        prepnum+=1
    elif x=="Detect Poison and Disease":
        detectpoisonanddisease+=1
        utility+=1
        prepnum+=1
    elif x=="Guiding Bolt":
        guidingbolt+=1
        offense+=1
        prepnum+=1
    elif x=="Healing Word":
        healingword+=1
        defense+=1
        prepnum+=1
    elif x=="Inflict Wounds":
        inflictwounds+=1
        offense+=1
        prepnum+=1
    elif x=="Protection from Evil and Good":
        protectionfromevilandgood+=1
        defense+=1
        prepnum+=1
    elif x=="Purify Food and Drink":
        purifyfoodanddrink+=1
        utility+=1
        prepnum+=1
    elif x=="Sanctuary":
        sanctuary+=1
        defense+=1
        prepnum+=1
    elif x=="Shield of Faith":
        shieldoffaith+=1
        defense+=1
        prepnum+=1
    elif x=="Aid":
        aid+=1
        defense+=2
        prepnum+=1
    elif x=="Augury":
        augury+=1
        utility+=2
        prepnum+=1
    elif x=="Blindness/Deafness":
        blindnessdeafness+=1
        offense+=2
        prepnum+=1
    elif x=="Borrowed Knowledge":
        borrowedknowledge+=1
        utility+=2
        prepnum+=1
    elif x=="Calm Emotions":
        calmemotions+=1
        utility+=2
        prepnum+=1
    elif x=="Continual Flame":
        continualflame+=1
        utility+=2
        prepnum+=1
    elif x=="Enhance Ability":
        enhanceability+=1
        utility+=2
        prepnum+=1
    elif x=="Find Traps":
        findtraps+=1
        defense+=2
        prepnum+=1
    elif x=="Gentle Repose":
        gentlerepose+=1
        defense+=2
        prepnum+=1
    elif x=="Hold Person":
        holdperson+=1
        offense+=2
        prepnum+=1
    elif x=="Lesser Restoration":
        lesserrestoration+=1
        utility+=2
        prepnum+=1
    elif x=="Locate Object":
        locateobject+=1
        utility+=2
        prepnum+=1
    elif x=="Prayer of Healing":
        prayerofhealing+=1
        defense+=2
        prepnum+=1
    elif x=="Protection from Poison":
        protectionfrompoison+=1
        defense+=2
        prepnum+=1
    elif x=="Silence":
        silence+=1
        utility+=2
        prepnum+=1
    elif x=="Spiritual Weapon":
        spiritualweapon+=1
        utility+=1
        offense+=1
        prepnum+=1
    elif x=="Warding Bond":
        wardingbond+=1
        defense+=2
        prepnum+=1
    elif x=="Zone of Truth":
        zoneoftruth+=1
        defense+=2
        prepnum+=1
    elif x=="Animate Dead":
        animatedead+=1
        utility+=1
        offense+=2
        prepnum+=1
    elif x=="Aura of Vitality":
        auraofvitality+=1
        defense+=3
        prepnum+=1
    elif x=="Beacon of Hope":
        beaconofhope+=1
        defense+=3
        prepnum+=1
    elif x=="Bestow Curse":
        bestowcurse+=1
        offense+=2
        utility+=1
        prepnum+=1
    elif x=="Clairvoyance":
        clairvoyance+=1
        utility+=3
        prepnum+=1
    elif x=="Create Food and Water":
        createfoodandwater+=1
        utility+=3
        prepnum+=1
    elif x=="Daylight":
        daylight+=1
        utility+=3
        prepnum+=1
    elif x=="Dispel Magic":
        dispelmagic+=1
        utility+=3
        prepnum+=1
    elif x=="Fast Friends":
        fastfriends+=1
        utility+=3
        prepnum+=1
    elif x=="Feign Death":
        feigndeath+=1
        defense+=3
        prepnum+=1
    elif x=="Glyph of Warding":
        glyphofwarding+=1
        utility+=3
        prepnum+=1
    elif x=="Incite Greed":
        incitegreed+=1
        utility+=3
        prepnum+=1
    elif x=="Life Transference":
        lifetransference+=1
        defense+=2
        utility+=1
        prepnum+=1
    elif x=="Magic Circle":
        magiccircle+=1
        defense+=3
        prepnum+=1
    elif x=="Mass Healing Word":
        masshealingword+=1
        defense+=3
        prepnum+=1
    elif x=="Meld into Stone":
        meldintostone+=1
        mobility+=3
        prepnum+=1
    elif x=="Motivational Speech":
        motivationalspeech+=1
        defense+=1.5
        offense+=1.5
        prepnum+=1
    elif x=="Protection from Energy":
        protectionfromenergy+=1
        defense+=3
        prepnum+=1
    elif x=="Remove Curse":
        removecurse+=1
        defense+=3
        prepnum+=1
    elif x=="Revivify":
        revivify+=1
        defense+=3
        prepnum+=1
    elif x=="Sending":
        sending+=1
        mobility+=3
        prepnum+=1
    elif x=="Speak with Dead":
        speakwithdead+=1
        utility+=3
        prepnum+=1
    elif x=="Spirit Guardians":
        spiritguardians+=1
        defense+=1
        offense+=2
        prepnum+=1
    elif x=="Spirit Shroud":
        spiritshroud+=1
        offense+=3
        prepnum+=1
    elif x=="Tongues":
        tongues+=1
        utility+=3
        prepnum+=1
    elif x=="Water Walk":
        waterwalk+=1
        mobility+=3
        prepnum+=1
    elif x=="Aura of Life":
        auraoflife+=1
        defense+=4
        prepnum+=1
    elif x=="Aura of Purity":
        auraofpurity+=1
        defense+=4
        prepnum+=1
    elif x=="Banishment":
        banishment+=1
        offense+=4
        prepnum+=1
    elif x=="Death Ward":
        deathward+=1
        defense+=4
        prepnum+=1
    elif x=="Divination":
        divination+=1
        utility+=4
        prepnum+=1
    elif x=="Freedom of Movement":
        freedomofmovement+=1
        mobility+=4
        prepnum+=1
    elif x=="Guardian of Faith":
        guardianoffaith+=1
        offense+=4
        prepnum+=1
    elif x=="Locate Creature":
        locatecreature+=1
        utility+=4
        prepnum+=1
    elif x=="Stone Shape":
        stoneshape+=1
        utility+=4
        prepnum+=1
    elif x=="Commune":
        commune+=1
        utility+=5
        prepnum+=1
    elif x=="Contagion":
        contagion+=1
        offense+=5
        prepnum+=1
    elif x=="Dawn":
        dawn+=1
        offense+=5
        prepnum+=1
    elif x=="Dispel Evil and Good":
        dispelevilandgood+=1
        utility+=5
        prepnum+=1
    elif x=="Flame Strike":
        flamestrike+=1
        offense+=5
        prepnum+=1
    elif x=="Geas":
        geas+=1
        offense+=5
        prepnum+=1
    elif x=="Greater Restoration":
        greaterrestoration+=1
        defense+=5
        prepnum+=1
    elif x=="Hallow":
        hallow+=1
        defense+=5
        prepnum+=1
    elif x=="Holy Weapon":
        holyweapon+=1
        offense+=5
        prepnum+=1
    elif x=="Legend Lore":
        legendlore+=1
        utility+=5
        prepnum+=1
    elif x=="Mass Cure Wounds":
        masscurewounds+=1
        defense+=5
        prepnum+=1
    elif x=="Planar Binding":
        planarbinding+=1
        utility+=5
        prepnum+=1
    elif x=="Raise Dead":
        raisedead+=1
        utility+=5
        prepnum+=1
    elif x=="Scrying":
        scrying+=1
        utility+=5
        prepnum+=1
    elif x=="Summon Celestial":
        summoncelestial+=1
        utility+=5
        prepnum+=1
    else:
        break
print()
while prepnum<13:
    x=random.randint(1,10920)
    if x<=195 and bane==0:
        bane+=1
        offense+=1
        prepnum+=1
    elif x<=390 and bless==0:
        bless+=1
        utility+=1
        prepnum+=1
    elif x<=585 and ceremony==0:
        ceremony+=1
        utility+=1
        prepnum+=1
    elif x<=780 and command==0:
        command+=1
        utility+=1
        prepnum+=1
    elif x<=975 and createordestroywater==0:
        createordestroywater+=1
        utility+=1
        prepnum+=1
    elif x<=1170 and curewounds==0:
        curewounds+=1
        defense+=1
        prepnum+=1
    elif x<=1365 and detectevilandgood==0:
        detectevilandgood+=1
        utility+=1
        prepnum+=1
    elif x<=1560 and detectmagic==0:
        detectmagic+=1
        utility+=1
        prepnum+=1
    elif x<=1755 and detectpoisonanddisease==0:
        detectpoisonanddisease+=1
        utility+=1
        prepnum+=1
    elif x<=1950 and guidingbolt==0:
        guidingbolt+=1
        offense+=1
        prepnum+=1
    elif x<=2145 and healingword==0:
        healingword+=1
        defense+=1
        prepnum+=1
    elif x<=2340 and inflictwounds==0:
        inflictwounds+=1
        offense+=1
        prepnum+=1
    elif x<=2535 and protectionfromevilandgood==0:
        protectionfromevilandgood+=1
        defense+=1
        prepnum+=1
    elif x<=2730 and purifyfoodanddrink==0:
        purifyfoodanddrink+=1
        utility+=1
        prepnum+=1
    elif x<=2925 and sanctuary==0:
        sanctuary+=1
        defense+=1
        prepnum+=1
    elif x<=3120 and shieldoffaith==0:
        shieldoffaith+=1
        defense+=1
        prepnum+=1
    elif x<=3250 and aid==0:
        aid+=1
        defense+=2
        prepnum+=1
    elif x<=3380 and augury==0:
        augury+=1
        utility+=2
        prepnum+=1
    elif x<=3510 and blindnessdeafness==0:
        blindnessdeafness+=1
        offense+=2
        prepnum+=1
    elif x<=3640 and borrowedknowledge==0:
        borrowedknowledge+=1
        utility+=2
        prepnum+=1
    elif x<=3770 and calmemotions==0:
        calmemotions+=1
        utility+=2
        prepnum+=1
    elif x<=3900 and continualflame==0:
        continualflame+=1
        utility+=2
        prepnum+=1
    elif x<=4030 and enhanceability==0:
        enhanceability+=1
        utility+=2
        prepnum+=1
    elif x<=4160 and findtraps==0:
        findtraps+=1
        defense+=2
        prepnum+=1
    elif x<=4290 and gentlerepose==0:
        gentlerepose+=1
        defense+=2
        prepnum+=1
    elif x<=4420 and holdperson==0:
        holdperson+=1
        offense+=2
        prepnum+=1
    elif x<=4550 and lesserrestoration==0:
        lesserrestoration+=1
        utility+=2
        prepnum+=1
    elif x<=4680 and locateobject==0:
        locateobject+=1
        utility+=2
        prepnum+=1
    elif x<=4810 and prayerofhealing==0:
        prayerofhealing+=1
        defense+=2
        prepnum+=1
    elif x<=4940 and protectionfrompoison==0:
        protectionfrompoison+=1
        defense+=2
        prepnum+=1
    elif x<=5070 and silence==0:
        silence+=1
        utility+=2
        prepnum+=1
    elif x<=5200 and spiritualweapon==0:
        spiritualweapon+=1
        utility+=1
        offense+=1
        prepnum+=1
    elif x<=5330 and wardingbond==0:
        wardingbond+=1
        defense+=2
        prepnum+=1
    elif x<=5460 and zoneoftruth==0:
        zoneoftruth+=1
        defense+=2
        prepnum+=1
    elif x<=5550 and animatedead==0:
        animatedead+=1
        utility+=1
        offense+=2
        prepnum+=1
    elif x<=5640 and auraofvitality==0:
        auraofvitality+=1
        defense+=3
        prepnum+=1
    elif x<=5730 and beaconofhope==0:
        beaconofhope+=1
        defense+=3
        prepnum+=1
    elif x<=5820 and bestowcurse==0:
        bestowcurse+=1
        offense+=2
        utility+=1
        prepnum+=1
    elif x<=5910 and clairvoyance==0:
        clairvoyance+=1
        utility+=3
        prepnum+=1
    elif x<=6000 and createfoodandwater==0:
        createfoodandwater+=1
        utility+=3
        prepnum+=1
    elif x<=6090 and daylight==0:
        daylight+=1
        utility+=3
        prepnum+=1
    elif x<=6180 and dispelmagic==0:
        dispelmagic+=1
        utility+=3
        prepnum+=1
    elif x<=6270 and fastfriends==0:
        fastfriends+=1
        utility+=3
        prepnum+=1
    elif x<=6360 and feigndeath==0:
        feigndeath+=1
        defense+=3
        prepnum+=1
    elif x<=6450 and glyphofwarding==0:
        glyphofwarding+=1
        utility+=3
        prepnum+=1
    elif x<=6540 and incitegreed==0:
        incitegreed+=1
        utility+=3
        prepnum+=1
    elif x<=6630 and lifetransference==0:
        lifetransference+=1
        defense+=2
        utility+=1
        prepnum+=1
    elif x<=6720 and magiccircle==0:
        magiccircle+=1
        defense+=3
        prepnum+=1
    elif x<=6810 and masshealingword==0:
        masshealingword+=1
        defense+=3
        prepnum+=1
    elif x<=6900 and meldintostone==0:
        meldintostone+=1
        mobility+=3
        prepnum+=1
    elif x<=6990 and motivationalspeech==0:
        motivationalspeech+=1
        defense+=1.5
        offense+=1.5
        prepnum+=1
    elif x<=7080 and protectionfromenergy==0:
        protectionfromenergy+=1
        defense+=3
        prepnum+=1
    elif x<=7170 and removecurse==0:
        removecurse+=1
        defense+=3
        prepnum+=1
    elif x<=7260 and revivify==0:
        revivify+=1
        defense+=3
        prepnum+=1
    elif x<=7350 and sending==0:
        sending+=1
        mobility+=3
        prepnum+=1
    elif x<=7440 and speakwithdead==0:
        speakwithdead+=1
        utility+=3
        prepnum+=1
    elif x<=7530 and spiritguardians==0:
        spiritguardians+=1
        defense+=1
        offense+=2
        prepnum+=1
    elif x<=7620 and spiritshroud==0:
        spiritshroud+=1
        offense+=3
        prepnum+=1
    elif x<=7710 and tongues==0:
        tongues+=1
        utility+=3
        prepnum+=1
    elif x<=7800 and waterwalk==0:
        waterwalk+=1
        mobility+=3
        prepnum+=1
    elif x<=8060 and auraoflife==0:
        auraoflife+=1
        defense+=4
        prepnum+=1
    elif x<=8320 and auraofpurity==0:
        auraofpurity+=1
        defense+=4
        prepnum+=1
    elif x<=8580 and banishment==0:
        banishment+=1
        offense+=4
        prepnum+=1
    elif x<=8840 and deathward==0:
        deathward+=1
        defense+=4
        prepnum+=1
    elif x<=9100 and divination==0:
        divination+=1
        utility+=4
        prepnum+=1
    elif x<=9360 and freedomofmovement==0:
        freedomofmovement+=1
        mobility+=4
        prepnum+=1
    elif x<=9620 and guardianoffaith==0:
        guardianoffaith+=1
        offense+=4
        prepnum+=1
    elif x<=9880 and locatecreature==0:
        locatecreature+=1
        utility+=4
        prepnum+=1
    elif x<=10140 and stoneshape==0:
        stoneshape+=1
        utility+=4
        prepnum+=1
    elif x<=10192 and commune==0:
        commune+=1
        utility+=5
        prepnum+=1
    elif x<=10244 and contagion==0:
        contagion+=1
        offense+=5
        prepnum+=1
    elif x<=10296 and dawn==0:
        dawn+=1
        offense+=5
        prepnum+=1
    elif x<=10348 and dispelevilandgood==0:
        dispelevilandgood+=1
        utility+=5
        prepnum+=1
    elif x<=10400 and flamestrike==0:
        flamestrike+=1
        offense+=5
        prepnum+=1
    elif x<=10452 and geas==0:
        geas+=1
        offense+=5
        prepnum+=1
    elif x<=10504 and greaterrestoration==0:
        greaterrestoration+=1
        defense+=5
        prepnum+=1
    elif x<=10556 and hallow==0:
        hallow+=1
        defense+=5
        prepnum+=1
    elif x<=10608 and holyweapon==0:
        holyweapon+=1
        offense+=5
        prepnum+=1
    elif x<=10660 and legendlore==0:
        legendlore+=1
        utility+=5
        prepnum+=1
    elif x<=10712 and masscurewounds==0:
        masscurewounds+=1
        defense+=5
        prepnum+=1
    elif x<=10764 and planarbinding==0:
        planarbinding+=1
        utility+=5
        prepnum+=1
    elif x<=10816 and raisedead==0:
        raisedead+=1
        utility+=5
        prepnum+=1
    elif x<=10868 and scrying==0:
        scrying+=1
        utility+=5
        prepnum+=1
    elif x<=10920 and summoncelestial==0:
        summoncelestial+=1
        utility+=5
        prepnum+=1
if bane==1:
    print("Bane")
if bless==1:
    print("Bless")
if ceremony==1:
    print("Ceremony")
if command==1:
    print("Command")
if createordestroywater==1:
    print("Create or Destroy Water")
if curewounds==1:
    print("Cure Wounds")
if detectevilandgood==1:
    print("Detect Evil and Good")
if detectmagic==1:
    print("Detect Magic")
if detectpoisonanddisease==1:
    print("Detect Poison and Disease")
print("Fog Cloud")
if guidingbolt==1:
    print("Guiding Bolt")
if healingword==1:
    print("Healing Word")
if inflictwounds==1:
    print("Inflict Wounds")
if protectionfromevilandgood==1:
    print("Protection from Evil and Good")
if purifyfoodanddrink==1:
    print("Purify Food and Drink")
if sanctuary==1:
    print("Sanctuary")
if shieldoffaith==1:
    print("Shield of Faith")
print("Thunderwave")
if aid==1:
    print("Aid")
if augury==1:
    print("Augury")
if blindnessdeafness==1:
    print("Blindness/Deafness")
if borrowedknowledge==1:
    print("Borrowed Knowledge")
if calmemotions==1:
    print("Calm Emotions")
if continualflame==1:
    print("Continual Flame")
if enhanceability==1:
    print("Enhance Ability")
if findtraps==1:
    print("Find Traps")
if gentlerepose==1:
    print("Gentle Repose")
print("Gust of Wind")
if holdperson==1:
    print("Hold Person")
if lesserrestoration==1:
    print("Lesser Restoration")
if locateobject==1:
    print("Locate Object")
if prayerofhealing==1:
    print("Prayer of Healing")
if protectionfrompoison==1:
    print("Protection from Poison")
print("Shatter")
if silence==1:
    print("Silence")
if spiritualweapon==1:
    print("Spiritual Weapon")
if wardingbond==1:
    print("Warding Bond")
if zoneoftruth==1:
    print("Zone of Truth")
if animatedead==1:
    print("Animate Dead")
if auraofvitality==1:
    print("Aura of Vitality")
if beaconofhope==1:
    print("Beacon of Hope")
if bestowcurse==1:
    print("Bestow Curse")
print("Call Lightning")
if clairvoyance==1:
    print("Clairvoyance")
if createfoodandwater==1:
    print("Create Food and Water")
if daylight==1:
    print("Daylight")
if dispelmagic==1:
    print("Dispel Magic")
if fastfriends==1:
    print("Fast Friends")
if feigndeath==1:
    print("Feign Death")
if glyphofwarding==1:
    print("Glyph of Warding")
if incitegreed==1:
    print("Incite Greed")
if lifetransference==1:
    print("Life Transference")
if magiccircle==1:
    print("Magic Circle")
if masshealingword==1:
    print("Mass Healing Word")
if meldintostone==1:
    print("Meld into Stone")
if motivationalspeech==1:
    print("Motivational Speech")
if protectionfromenergy==1:
    print("Protection from Energy")
if removecurse==1:
    print("Remove Curse")
if revivify==1:
    print("Revivify")
if sending==1:
    print("Sending")
print("Sleet Storm")
if speakwithdead==1:
    print("Speak with Dead")
if spiritguardians==1:
    print("Spirit Guardians")
if spiritshroud==1:
    print("Spirit Shroud")
if tongues==1:
    print("Tongues")
if waterwalk==1:
    print("Water Walk")
if auraoflife==1:
    print("Aura of Life")
if auraofpurity==1:
    print("Aura of Purity")
if banishment==1:
    print("Banishment")
print("Control Water")
if deathward==1:
    print("Death Ward")
if divination==1:
    print("Divination")
if freedomofmovement==1:
    print("Freedom of Movement")
if guardianoffaith==1:
    print("Guardian of Faith")
print("Ice Storm")
if locatecreature==1:
    print("Locate Creature")
if stoneshape==1:
    print("Stone Shape")
print("Storm Sphere")
if commune==1:
    print("Commune")
if contagion==1:
    print("Contagion")
if dawn==1:
    print("Dawn")
print("Destructive Wave")
if dispelevilandgood==1:
    print("Dispel Evil and Good")
if flamestrike==1:
    print("Flame Strike")
if geas==1:
    print("Geas")
if greaterrestoration==1:
    print("Greater Restoration")
if hallow==1:
    print("Hallow")
if holyweapon==1:
    print("Holy Weapon")
print("Insect Plague")
if legendlore==1:
    print("Legend Lore")
if masscurewounds==1:
    print("Mass Cure Wounds")
if planarbinding==1:
    print("Planar Binding")
if raisedead==1:
    print("Raise Dead")
if scrying==1:
    print("Scrying")
if summoncelestial==1:
    print("Summon Celestial")
print()
print("Offense:"+str(offense)+" Defense:"+str(defense)+" Mobility:"+str(mobility)+" Utility:"+str(utility))