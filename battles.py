from charactersitems import Character
from charactersitems import MainCharacter
from charactersitems import Enemy
from charactersitems import BossEnemy
from charactersitems import Grifter
from charactersitems import Weapon
from charactersitems import HealingItem
import pygame
pygame.init()

# is this code good?
# no
# does it work
# of course it does im an awesome programmer 👍

player = None

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Battles')
battle = True
running = True

class Battles:
    def BattleStartAnimation():
        import time
        curtainrect = pygame.Rect(0, 0, 0, 720)
        bottomrect = pygame.Rect(0, 720, 1280, 100)
        red = 255
        green = 255
        blue = 255
        color = (red, green, blue)
        lastmovetime = time.time()
        moving = True
        colorchange = False
        bottomrectmoving = False
        
        complete = False
        while not complete:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
            
            currenttime = time.time()
                
            pygame.draw.rect(screen, color, curtainrect)
            font = pygame.font.SysFont(None, 400, bold=True, italic=True)
            text = font.render("BATTLE", True, (20, 20, 25))
            surface = text.get_rect(center= (640, 160))
            text2 = font.render("TIME!", True, (20, 20, 25))
            surface2 = text.get_rect(center=(760, 560))
            
            screen.blit(text, surface)
            screen.blit(text2, surface2)
            
            if moving == True:
                if currenttime - lastmovetime > 0.01:
                    curtainrect[2] += 20
                    lastmovetime = currenttime
                    if curtainrect[2] > 1280:
                        moving = False
                        colorchange = True
                        lastmovetime = currenttime
            elif colorchange == True:
                if currenttime - lastmovetime > 0.015:
                    lastmovetime = currenttime
                    red -= (235/100)
                    green -= (235/100)
                    blue -= (230/100)
                    color = (red, green, blue)
                    
                    if color[0] < 20:
                        color = (20, 20, 25)
                        
                        lastmovetime = currenttime
                        colorchange = False
                        bottomrectmoving = True
            elif bottomrectmoving == True:
                pygame.draw.rect(screen, (200, 220, 240), bottomrect)
                if currenttime - lastmovetime > 0.005:
                    bottomrect[1] -= 2
                    if bottomrect[1] == 620:
                        complete = True
                        break
            
            pygame.display.update()
        
    def BossStartAnimation():
        import time
        complete = False
        radius = 0
        length = 0
        leftpos = 1280
        thickness = 0
        circles = True
        drawingx = False
        rectangles = False
        lastmovetime = time.time()
        colorchanging = False
        bottomrecttop = 720
        bottomrect = False
        red = green = blue = 255
        
        while not complete:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit
            
            currenttime = time.time()
            
            pygame.draw.circle(screen, (90, 10, 18), (0, 0), radius)
            pygame.draw.circle(screen, (90, 10, 18), (1280, 720), radius)
            if radius >= 10:
                pygame.draw.circle(screen, (150, 20, 30), (0, 0), radius-5, 5)
                pygame.draw.circle(screen, (150, 20, 30), (1280, 720), radius-5, 5)
            
            pygame.draw.line(screen, (200, 50, 60), (0, 0), (1280, 720), int(thickness))
            pygame.draw.line(screen, (200, 50, 60), (0, 720), (1280, 0), int(thickness))
            
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, length, 180)) 
            pygame.draw.rect(screen, (255, 255, 255), (0, 360, length, 180)) 
            pygame.draw.rect(screen, (255, 255, 255), (leftpos, 180, 1280, 180))
            pygame.draw.rect(screen, (255, 255, 255), (leftpos, 540, 1280, 180))
            
            if circles:
                if currenttime - lastmovetime > 0.01:
                    lastmovetime = currenttime
                    radius += 2.5
                    if radius == 500:
                        lastmovetime = currenttime
                        circles = False
                        drawingx = True
            
            elif drawingx:
                if currenttime - lastmovetime > 0.01:
                    lastmovetime = currenttime
                    thickness += 2.5
                    if thickness == 200:
                        lastmovetime = currenttime
                        drawingx = False
                        rectangles = True
                        
            elif rectangles:
                if currenttime - lastmovetime > 0.01:
                    lastmovetime = currenttime
                    length += 20
                    leftpos -= 20    
                    if leftpos == 0:
                        rectangles = False
                        colorchanging = True
                        
            elif colorchanging:
                pygame.draw.rect(screen, (red, green, blue), (0, 0, 1280, 720))
                if currenttime - lastmovetime > 0.01:
                    lastmovetime = currenttime
                    red -= (235/100)
                    green = red
                    blue -= (230/100)
                    
                    if red < 20:
                        colorchanging = False
                        red = green = 20
                        blue = 25
                        lastmovetime = currenttime
                        bottomrect = True
                        
            elif bottomrect == True:
                screen.fill((20, 20, 25))
                pygame.draw.rect(screen, (200, 220, 240), (0, bottomrecttop, 1280, 100))
                if currenttime - lastmovetime > 0.005:
                    bottomrecttop -= 2
                    if bottomrecttop == 620:
                        complete = True
                        break
            
            
            if bottomrect == False:
                font = pygame.font.SysFont(None, 400, bold=True, italic=True)
                text = font.render("BOSS", True, (20, 20, 25))
                surface = text.get_rect(center= (640, 160))
                text2 = font.render("TIME!", True, (20, 20, 25))
                surface2 = text.get_rect(center=(760, 560))
            
            screen.blit(text, surface)
            screen.blit(text2, surface2)
            pygame.display.update()
            
    def DictionaryEnemyToObjectEnemy(enemyname):
        import json
        with open('enemies.json', 'r') as file:
            enemies = json.load(file)
            
        for possibleenemy in enemies:
            if possibleenemy['name'] == enemyname:
                enemy = possibleenemy
                break
            
        if enemy['type'] == "REGULAR":
            name = enemy['name']
            maxhp = enemy['maxhp']
            currenthp = enemy['currenthp']
            strength = enemy['strength']
            golddrop = enemy['golddrop']
            expdrop = enemy['expdrop']
            weapon = Weapon("None", 0, 8192, 0)
            
            enemyweapondrop = enemy['weapondrop']
            if enemyweapondrop['type'] == "WEAPON":
                weaponname = enemyweapondrop['name']
                weaponstrength = enemyweapondrop['strength']
                weapondurability = enemyweapondrop['durability']
                weaponcost = enemyweapondrop['cost']
                weapondrop = Weapon(weaponname, weaponstrength, weapondurability, weaponcost)
            elif enemyweapondrop['type'] == "HEALING ITEM":
                itemname = enemyweapondrop['name']
                itemheal = enemyweapondrop['heal']
                itemcost = enemyweapondrop['cost']
                
                weapondrop = HealingItem(itemname, itemheal, itemcost)
            else:
                weapondrop = None
                
            enemy = Enemy(name, maxhp, currenthp, strength, weapon, golddrop, weapondrop, expdrop)
        
        elif enemy['type'] == "GRIFTER":
            name = enemy['name']
            maxhp = enemy['maxhp']
            currenthp = enemy['currenthp']
            strength = enemy['strength']
            steal = enemy['steal']
            golddrop = enemy['golddrop']
            expdrop = enemy['expdrop']
            weapon = Weapon("None", 0, 8192, 0)

            enemyweapondrop = enemy['weapondrop']
            if enemyweapondrop['type'] == "WEAPON":
                weaponname = enemyweapondrop['name']
                weaponstrength = enemyweapondrop['strength']
                weapondurability = enemyweapondrop['durability']
                weaponcost = enemyweapondrop['cost']
                weapondrop = Weapon(weaponname, weaponstrength, weapondurability, weaponcost)
            elif enemyweapondrop['type'] == "HEALING ITEM":
                itemname = enemyweapondrop['name']
                itemheal = enemyweapondrop['heal']
                itemcost = enemyweapondrop['cost']
                
                weapondrop = HealingItem(itemname, itemheal, itemcost)
            else:
                weapondrop = None
                
            enemy = Grifter(name, maxhp, currenthp, strength, weapon, golddrop, weapondrop, expdrop, steal)
        
        elif enemy['type'] == "BOSS":
            name = enemy['name']
            maxhp = enemy['maxhp']
            currenthp = enemy['currenthp']
            strength = enemy['strength']
            expdrop = enemy['expdrop']
            weapon = Weapon("None", 0, 16384, 0)
            
            enemy = BossEnemy(name, maxhp, currenthp, strength, weapon, expdrop)
        
        return enemy
    
    def SpawnBoss():
        strongslime = Battles.DictionaryEnemyToObjectEnemy("Strong Slime")
        strongorc = Battles.DictionaryEnemyToObjectEnemy("Strong Orc")
        boss = Battles.DictionaryEnemyToObjectEnemy("King Orc")
        
        return [strongslime, boss, strongorc]
    
    def SpawnEnemies(roomnumber):
        import json, random
        with open('rooms.json', 'r') as file:
            rooms = json.load(file)
            
        for potentialroom in rooms:
            if potentialroom['id'] == roomnumber:
                room = potentialroom 
                break
        
        spawntable = room['spawntable']
        enemycount = random.choice(spawntable['enemy count'])
        
        possibleenemies = [] 
        
        for i in range(spawntable['slime']):
            slime = Battles.DictionaryEnemyToObjectEnemy('Slime')
            possibleenemies.append(slime)
            
        for i in range(spawntable['goblin']):
            goblin = Battles.DictionaryEnemyToObjectEnemy('Goblin')
            possibleenemies.append(goblin)
            
        for i in range(spawntable['orc']):
            orc = Battles.DictionaryEnemyToObjectEnemy('Orc')
            possibleenemies.append(orc)
            
        for i in range(spawntable['strong slime']):
            strongslime = Battles.DictionaryEnemyToObjectEnemy('Strong Slime')
            possibleenemies.append(strongslime)
            
        for i in range(spawntable['strong orc']):
            strongorc = Battles.DictionaryEnemyToObjectEnemy('Strong Orc')
            possibleenemies.append(strongorc)
            
        for i in range(spawntable['grifter']):
            grifter = Battles.DictionaryEnemyToObjectEnemy('Grifter')
            possibleenemies.append(grifter)
            
        fightingenemies = []
        
        for i in range(enemycount):
            enemy = random.choice(possibleenemies)
            fightingenemies.append(enemy)
            possibleenemies.remove(enemy) # i rolled the 1/100 while testing that the exact same enemy spawned twice
        
        return fightingenemies
    
    def DrawActionButton(player, enemies, action):
        global wasactiondone, attackpressed, attack, enemy, theyblocking, events, x, y, z, chosenenemy
        x = 1
        y = 0
        z = 1
        menufont = pygame.font.Font(None, 30)
        actiontext = menufont.render(action, True, (255, 255, 255))
        if action == 'ATTACK':
            buttonrect = pygame.Rect((220, 635, 150, 50))
            if attackpressed == True:
                actiontext = menufont.render(action, True, (215, 230, 255))
        elif action == 'BLOCK':
            buttonrect = pygame.Rect((380, 635, 150, 50))
        elif action == 'FLEE (coward)':
            buttonrect = pygame.Rect((540, 635, 150, 50))
        mousepos = pygame.mouse.get_pos()
        if buttonrect.collidepoint(mousepos):
            color = (50, 50, 65)
        else:
            color = (25, 25, 32.5)
        
        pygame.draw.rect(screen, color, buttonrect)
        actionsurface = actiontext.get_rect(center=buttonrect.center)
        screen.blit(actiontext, actionsurface)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and buttonrect.collidepoint(mousepos):
                if action == 'FLEE (coward)':
                    Battles.FleeCoward(player, enemies)
                    wasactiondone = True
                elif action == 'ATTACK':
                    if attackpressed == True:
                        attackpressed = False
                    else:
                        attackpressed = True
                else:
                    wasactiondone = True
                    theyblocking = True
                    Battles.Block(player)
        
        if attackpressed == True:
            xcoordinate = 0
            for enemy in enemies:
                ycoordinate = 60
                if isinstance(enemy, BossEnemy):
                    xcoordinate += 30
                    ycoordinate = 0
                attackenemy = pygame.Rect(xcoordinate+15, 20+ycoordinate, 120, 30)
                font = pygame.font.Font(None, 20)
                if attackenemy.collidepoint(pygame.mouse.get_pos()):
                    color = (220, 220, 250)
                    text = font.render("ATTACK THIS", True, (0, 0, 0))
                else:
                    color = (200, 200, 220)
                    text = font.render("ATTACK THIS", True, (20, 20, 35))
                pygame.draw.rect(screen, color, attackenemy)
                textsurface = text.get_rect(center=attackenemy.center)
                screen.blit(text, textsurface)

                xcoordinate += 150
                if isinstance(enemy, BossEnemy):
                    xcoordinate += 30
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and attackenemy.collidepoint(pygame.mouse.get_pos()):
                        attackpressed = False
                        wasactiondone = True
                        attack = True
                        if enemy:
                            chosenenemy = enemy
                            
    def AttackAnimation(chosenenemy, enemies, player):    
        enemynumber = enemies.index(chosenenemy)
        numberofbosses = 0
        for enemy in enemies:
            if isinstance(enemy, BossEnemy):
                numberofbosses += 1
                
            if enemy == chosenenemy:
                break
            
        if isinstance(chosenenemy, BossEnemy):
            numberofbosses -= 0.5
        
        xcoordinate = 75
        xcoordinate += (enemynumber*150)
        xcoordinate += (numberofbosses*60)
        
        import random, time
        animationtype = random.randint(1, 2)
        
        wouldkill = False
        if player.weapon.strength + player.strength >= chosenenemy.currenthp:
            wouldkill = True
        
        height = 0
        top = 600
        
        if animationtype == 1:
            radius = 100
            complete = False
            circle = True
            lastmovetime = time.time()
            currenttime = time.time()
            while not complete:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        quit()
                screen.fill((20, 20, 25))
                Battles.MakeEnemies(enemies)
                
                pygame.draw.rect(screen, (200, 220, 240), (0, 620, 1280, 200))
                
                hppercentage = round(player.currenthp / player.maxhp, 2) 
                
                menufont = pygame.font.Font(None, 30)
                healthbar = pygame.Rect((10, 645, 200, 30))
                nameunderhealthbarrect = pygame.Rect((10, 675, 200, 30))
                pygame.draw.rect(screen, (75, 100, 125), (5, 640, 210, 40))
                pygame.draw.rect(screen, (25, 25, 32.5), healthbar)
                if hppercentage < .30:
                    uhohtext = menufont.render("!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, (120, 120, 130))
                    uhohsurface = uhohtext.get_rect(center=healthbar.center)
                    screen.blit(uhohtext, uhohsurface)
                
                pygame.draw.rect(screen, (100, 110, 140), (10, 645, 200*hppercentage, 30))
            
                hptext = menufont.render(f"{int(player.currenthp)} / {int(player.maxhp)} HP", True, (255, 255, 255))
                hpsurface = hptext.get_rect(center=healthbar.center)
                
                nameunderhealthbartext = menufont.render(player.name, True, 36)
                nameunderhbsurface = nameunderhealthbartext.get_rect(center=nameunderhealthbarrect.center)
                
                screen.blit(nameunderhealthbartext, nameunderhbsurface)
                screen.blit(hptext, hpsurface)
                
                if circle:
                    pygame.draw.circle(screen, (100, 0, 0), (xcoordinate, 250), radius, 10)
                else:
                    if not wouldkill:
                        animationtime = 0.3
                        pygame.draw.line(screen, (255, 145, 0), (xcoordinate-50, 100), (xcoordinate+50, 400), 10)    
                        pygame.draw.line(screen, (255, 145, 0), (xcoordinate-50, 400), (xcoordinate+50, 100), 10) 
                    if wouldkill:
                        animationtime = 2
                        if height < 200:
                            pygame.draw.circle(screen, (0, 100, 100), (xcoordinate, 250), 120)
                            pygame.draw.rect(screen, (0, 100, 100), (xcoordinate-50, 240, 100, 180))
                            
                            pygame.draw.circle(screen, (255, 255, 255), (xcoordinate, 250), 110)
                            pygame.draw.rect(screen, (255, 255, 255), (xcoordinate-40, 250, 80, 160))
                            pygame.draw.circle(screen, (0, 0, 0), (xcoordinate - 50, 250), 50)
                            pygame.draw.circle(screen, (0, 0, 0), (xcoordinate + 50, 250), 50)
                                
                            pygame.draw.line(screen, (0, 100, 100), (xcoordinate-30, 375), (xcoordinate-30, 410), 7)
                            pygame.draw.line(screen, (0, 100, 100), (xcoordinate, 375), (xcoordinate, 410), 7)
                            pygame.draw.line(screen, (0, 100, 100), (xcoordinate+30, 375), (xcoordinate+30, 410), 7)
                            
                            
                        pygame.draw.rect(screen, (20, 20, 25), (xcoordinate-70, top, 140, height))
                        if isinstance(enemy, BossEnemy):
                            pygame.draw.rect(screen, (20, 20, 25), (xcoordinate-90, top, 180, height))
                            
                        if currenttime - lastmovetime > 0.01:
                            lastmovetime = currenttime
                            height += 6
                            top -= 6
                            
                       
                    if currenttime - eksstarttime > animationtime:
                        complete = True
                        break
                    
                currenttime = time.time()
                
                if circle == True:
                    if currenttime - lastmovetime > 0.0025:
                        radius -= 3
                        lastmovetime = currenttime
                        if radius < 0:
                            eksstarttime = time.time()
                            circle = False
                
                pygame.display.update()
                
        else:
            complete = False
            drawinglines = True
            line = 1
            starttime = time.time()
            lastmovetime = time.time()
            lastgrowth = time.time()
            linelength = 0
            
            while not complete:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        quit()
                        
                screen.fill((20, 20, 25))
                Battles.MakeEnemies(enemies)
                
                pygame.draw.rect(screen, (200, 220, 240), (0, 620, 1280, 200))
                
                hppercentage = round(player.currenthp / player.maxhp, 2) 
                
                menufont = pygame.font.Font(None, 30)
                healthbar = pygame.Rect((10, 645, 200, 30))
                nameunderhealthbarrect = pygame.Rect((10, 675, 200, 30))
                pygame.draw.rect(screen, (75, 100, 125), (5, 640, 210, 40))
                pygame.draw.rect(screen, (25, 25, 32.5), healthbar)
                if hppercentage < .30:
                    uhohtext = menufont.render("!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, (120, 120, 130))
                    uhohsurface = uhohtext.get_rect(center=healthbar.center)
                    screen.blit(uhohtext, uhohsurface)
                
                pygame.draw.rect(screen, (100, 110, 140), (10, 645, 200*hppercentage, 30)) 
                
                hptext = menufont.render(f"{int(player.currenthp)} / {int(player.maxhp)} HP", True, (255, 255, 255))
                hpsurface = hptext.get_rect(center=healthbar.center)
                
                nameunderhealthbartext = menufont.render(player.name, True, 36)
                nameunderhbsurface = nameunderhealthbartext.get_rect(center=nameunderhealthbarrect.center)
                
                screen.blit(nameunderhealthbartext, nameunderhbsurface)
                screen.blit(hptext, hpsurface)
                
                currenttime = time.time()
                
                # x coordinate is the center
                # start and end positions for
                # line 1: xcoord - 100, 100 and xcoord+100, 400
                # line 3: xcoord + 100, 100 and xcoord-100, 400
                
                if drawinglines:
                    if line == 1:
                        if currenttime - lastgrowth > 0.0025:
                            linelength += 12
                            lastgrowth = currenttime
                            
                        pygame.draw.line(screen, (100, 0, 0), (xcoordinate - 100, 100), (xcoordinate - 100 + linelength, 100 + 1.5*linelength), 10)
                    elif line == 2:
                        if currenttime - lastgrowth > 0.0025:
                            linelength += 12
                            lastgrowth = currenttime
                        
                        pygame.draw.line(screen, (100, 0, 0), (xcoordinate - 100, 250), (xcoordinate - 100 + linelength, 250), 10)
                        
                    elif line == 3:
                        if currenttime - lastgrowth > 0.0025:
                            linelength += 12
                            lastgrowth = currenttime
                            
                        pygame.draw.line(screen, (100, 0, 0), (xcoordinate + 100, 400), (xcoordinate + 100 - linelength, 400 - 1.5*linelength), 10)
                        
                    elif line == 4:
                        if currenttime - lastgrowth > 0.0025:
                            linelength += 24
                            lastgrowth = currenttime
                        
                        pygame.draw.line(screen, (100, 0, 0), (xcoordinate, 100), (xcoordinate, 100 + linelength), 10)      
                        
                    if currenttime - starttime > 0.25:
                            line += 1
                            starttime = currenttime
                            lastgrowth = time.time()
                            linelength = 0
                            if line > 4:
                                drawinglines = False
                                eksstarttime = time.time()
                                
                else:
                    if not wouldkill:
                        animationtime = 0.3
                        pygame.draw.line(screen, (255, 145, 0), (xcoordinate-50, 100), (xcoordinate+50, 400), 10)    
                        pygame.draw.line(screen, (255, 145, 0), (xcoordinate-50, 400), (xcoordinate+50, 100), 10) 
                    if wouldkill:
                        animationtime = 2
                        if height < 200:
                            pygame.draw.circle(screen, (0, 100, 100), (xcoordinate, 250), 120)
                            pygame.draw.rect(screen, (0, 100, 100), (xcoordinate-50, 240, 100, 180))
                            
                            pygame.draw.circle(screen, (255, 255, 255), (xcoordinate, 250), 110)
                            pygame.draw.rect(screen, (255, 255, 255), (xcoordinate-40, 250, 80, 160))
                            pygame.draw.circle(screen, (0, 0, 0), (xcoordinate - 50, 250), 50)
                            pygame.draw.circle(screen, (0, 0, 0), (xcoordinate + 50, 250), 50)
                            
                            pygame.draw.line(screen, (0, 100, 100), (xcoordinate-30, 375), (xcoordinate-30, 410), 7)
                            pygame.draw.line(screen, (0, 100, 100), (xcoordinate, 375), (xcoordinate, 410), 7)
                            pygame.draw.line(screen, (0, 100, 100), (xcoordinate+30, 375), (xcoordinate+30, 410), 7)
                            
                        pygame.draw.rect(screen, (20, 20, 25), (xcoordinate-70, top, 140, height))
                        if isinstance(enemy, BossEnemy):
                            pygame.draw.rect(screen, (20, 20, 25), (xcoordinate-90, top, 180, height))
                        
                        if currenttime - lastmovetime > 0.0175:
                            lastmovetime = currenttime
                            height += 8
                            top -= 8
                            
                       
                    if currenttime - eksstarttime > animationtime:
                        complete = True
                        break
                            
                
                pygame.display.update()
                
                
        
        
                        
    def AttackStepTwo(player, enemy, enemies):
        global attacksteptwo, attack, events, x, damage, enemiesfought, weaponbroken
        if x == 1:
            x += 1
            damage = Character.CharacterDamageCalc(player)
            enemy.currenthp -= damage
            player.weapon.durability -= 1
            if player.weapon.durability == 0:
                player.weapon = Weapon('NONE', 0, 16384, 0)
                weaponbroken = True
        textbox = pygame.Rect(220, 630, 1000, 80) # !
        pygame.draw.rect(screen, (40, 40, 60), textbox) # !
        font = pygame.font.Font(None, 36)
        if enemy.currenthp < 1:
            enemy.currenthp = 0
            youractiontwo = font.render(f'The {enemy.name} has died!', True, (255, 255, 255))
            
            try:
                enemies.remove(enemy)
            except ValueError: #bc this code is gonna run over and over
                pass
        else:
            youractiontwo = font.render(f'The {enemy.name} lost {damage} HP!', True, (255, 255, 255))
        youractionone = font.render(f"You attack the {enemy.name}!", True, (255, 255, 255))
        youractiononesurface = youractionone.get_rect(center=(720, 655))
        youractiontwosurface = youractiontwo.get_rect(center=(720, 685))
        arrowfont = pygame.font.SysFont(None, 100, bold=True)
        
        screen.blit(youractionone, youractiononesurface)
        screen.blit(youractiontwo, youractiontwosurface)
              
        go_onHITBOX = pygame.Rect(1185, 625, 90, 90)
        if go_onHITBOX.collidepoint(pygame.mouse.get_pos()):
            go_onCOLOR = (120, 120, 180)
        else:
            go_onCOLOR = (80, 80, 120)
        go_on = arrowfont.render(">", True, (255, 255, 255)) # notice my use of the critical underscore lmao
        go_onsurface = go_on.get_rect(center=go_onHITBOX.center)
        pygame.draw.rect(screen, go_onCOLOR, go_onHITBOX)
        screen.blit(go_on, go_onsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and go_onCOLOR == (120, 120, 180):
                attacksteptwo = True
                attack = False 
                x = 1
    
    def AttackStepThree(player, enemies):
        global battle, x, y, attacksteptwo, wasactiondone, previousinputs, action, events, block
        previousinputs = 'ATTACK'
        block = False
        if y <= len(enemies) - 1:
            enemy = enemies[y]  
        else:
            pass
        try:
            if enemy.currenthp < 1:
                return
        except UnboundLocalError:
            pass
        textbox = pygame.Rect(220, 630, 1000, 80) # !
        pygame.draw.rect(screen, (40, 40, 60), textbox) # !
        go_onHITBOX = pygame.Rect(1185, 625, 90, 90)
        if go_onHITBOX.collidepoint(pygame.mouse.get_pos()):
            go_onCOLOR = (120, 120, 180)
        else:
            go_onCOLOR = (80, 80, 120)
            
        arrowfont = pygame.font.SysFont(None, 100, bold=True)
        go_on = arrowfont.render(">", True, (255, 255, 255)) 
        go_onsurface = go_on.get_rect(center=go_onHITBOX.center)
        pygame.draw.rect(screen, go_onCOLOR, go_onHITBOX)
        screen.blit(go_on, go_onsurface)
        textfont = pygame.font.Font(None, 36)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and go_onCOLOR == (120, 120, 180) and y <= len(enemies) - 1:
                x = 1 
            elif event.type == pygame.MOUSEBUTTONDOWN and go_onCOLOR == (120, 120, 180):
                wasactiondone = False
                attacksteptwo = False
                y = 0
                return
        if x == 1:
            x + 1
            import random
            try:
                enemy.currenthp += 0
            except UnboundLocalError: 
                return
            if isinstance(enemy, Enemy) and not isinstance(enemy, Grifter):
                action = random.randint(1, 5)
                if (enemy.currenthp/enemy.maxhp) <= 0.2:
                    enemy.EnemyHeal(5)
                    enemy.lastaction = 'healed!'
                    action = 'healed!'
                elif action in [1, 2, 3, 4] or (enemy.currenthp/enemy.maxhp) >= 1:
                    damage = Character.CharacterDamageCalc(enemy)
                    player.currenthp -= damage
                    enemy.lastaction = 'attacked you!'
                    action = 'attacked you!'
                    if player.currenthp < 1:
                        battle = False
                    else:
                        pass
                elif action == 5:
                    enemy.EnemyHeal(5)
                    enemy.lastaction = 'healed!'
                    action = 'healed!'
            elif isinstance(enemy, Grifter):
                action = random.randint(1, 2)
                if (enemy.currenthp/enemy.maxhp) <= 0.4:
                    enemy.GrifterHeal(40)
                    action = 'healed!'
                elif action == 1:
                    steal = Grifter.GrifterCalc(enemy)                
                    player.gold *= steal
                    enemy.lastaction = 'stole gold!'
                    action = 'stole gold!'
                else:
                    enemy.GrifterHeal(40)
                    enemy.lastaction = 'healed!'
                    action = 'healed!'
                    
            elif isinstance(enemy, BossEnemy):
                import random
                action = random.randint(1, 100)
                if (enemy.currenthp/enemy.maxhp) <= 0.3:
                    enemy.EnemyHeal(25)
                    enemy.lastaction = 'healed!'
                    action = 'healed!'
                elif enemy.currenthp/enemy.maxhp >= 1:
                    if action < 90:
                        damage = Character.CharacterDamageCalc(enemy)
                        player.currenthp -= damage
                        enemy.lastaction = 'attacked you!'
                        action = 'attacked you!'
                        if player.currenthp < 1:
                            battle = False
                    else:
                        enemy.EnemySummon(enemies)
                        enemy.lastaction = 'spawned an Orc!'
                        action = 'spawned an Orc!'
                        
                else:
                    if action < 71:
                        damage = Character.CharacterDamageCalc(enemy)
                        player.currenthp -= damage
                        enemy.lastaction = 'attacked you!'
                        action = 'attacked you!'
                        if player.currenthp < 1:
                            battle = False
                    elif action < 91 and action > 70:
                        enemy.EnemyHeal(25)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                    else:
                        enemy.EnemySummon(enemies)
                        enemy.lastaction = 'spawned an Orc!'
                        action = 'spawned an Orc!'
            x += 1
            y += 1
        if y == len(enemies) + 2:
            wasactiondone = False
            attacksteptwo = False
            y = 0
            return
        hawk1 = textfont.render(f"{enemies[y-1].name} has {action}", True, (255, 255, 255))
        hawk1surface = hawk1.get_rect(center=(720, 655)) # don't ask
        screen.blit(hawk1, hawk1surface)
        
        hawk2 = textfont.render(f"You now have {int(player.currenthp)} HP!", True, (255, 255, 255))
        hawk2surface = hawk2.get_rect(center=(720, 685))
        screen.blit(hawk2, hawk2surface)
        
        
    def FleeCoward(player, enemies):
        global battle, block, blockdone
        import random
        chancetoflee = 100 - (100*(player.currenthp / player.maxhp))
        if chancetoflee < 45:
            chancetoflee = 45

        for enemy in enemies:
            if isinstance(enemy, BossEnemy):
                chancetoflee = 10000000000 # come back here 
            
        areyarunning = random.randint(1, 100)
        if areyarunning >= chancetoflee:
            battle = False
            player.gold = int(player.gold)
        else:
            block = True
            blockdone = True # im too lazy to code this function again so what im doing is
            # i run the block function again but they didnt block
            
            
    # make a makeshift for loop that waits for confirm buttons to be pressed
    
    def Block(player):
        global block, x, y, youractiontwo, blockdone, theyblocking, events
        textbox = pygame.Rect(220, 630, 1000, 80) # !
        pygame.draw.rect(screen, (40, 40, 60), textbox) # !
        font = pygame.font.Font(None, 36)
        if x == 1: 
            x += 1
            if block == False:
                youractiontwo = font.render(f'Your block was a success! You healed 10HP', True, (255, 255, 255))
                player.PlayerHeal(5)
            elif block == True:
                youractiontwo = font.render(f'It sure was an attempt. An okay one at that. You Healed 2HP.', True, (255, 255, 255))
                player.PlayerHeal(1)
        
        youractionone = font.render(f"You attempt to block!", True, (255, 255, 255))
        youractiononesurface = youractionone.get_rect(center=(720, 655))

        youractiontwosurface = youractiontwo.get_rect(center=(720, 685)) # fix
        screen.blit(youractiontwo, youractiontwosurface) # fix

        arrowfont = pygame.font.SysFont(None, 100, bold=True)
        
        screen.blit(youractionone, youractiononesurface)
              
        go_onHITBOX = pygame.Rect(1185, 625, 90, 90)
        if go_onHITBOX.collidepoint(pygame.mouse.get_pos()):
            go_onCOLOR = (120, 120, 180)
        else:
            go_onCOLOR = (80, 80, 120)
        go_on = arrowfont.render(">", True, (255, 255, 255)) # notice my use of the critical underscore lmao
        go_onsurface = go_on.get_rect(center=go_onHITBOX.center)
        pygame.draw.rect(screen, go_onCOLOR, go_onHITBOX)
        screen.blit(go_on, go_onsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and go_onCOLOR == (120, 120, 180):
                y = 0
                blockdone = True
                theyblocking = False
                x = 1
                

    def BlockTwo(player, enemies):
        global x, y, battle, wasactiondone, block, theyblocking, blockdone, action, events # i might well explain what x and y are
        # x is just a check so it only runs action calculations once in the while loop
        # y is the index of the enemy within the enemy list, i can't use a for loop bc i cant repeat it until its done
        # whatevs chat
        textbox = pygame.Rect(220, 630, 1000, 80) # !
        textboxfont = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, (40, 40, 60), textbox) # !
        go_onHITBOX = pygame.Rect(1185, 625, 90, 90)
        if go_onHITBOX.collidepoint(pygame.mouse.get_pos()):
            go_onCOLOR = (120, 120, 180)
        else:
            go_onCOLOR = (80, 80, 120)
        arrowfont = pygame.font.SysFont(None, 100, bold=True)
        go_on = arrowfont.render(">", True, (255, 255, 255)) # notice my use of the critical underscore lmao
        go_onsurface = go_on.get_rect(center=go_onHITBOX.center)
        pygame.draw.rect(screen, go_onCOLOR, go_onHITBOX)
        screen.blit(go_on, go_onsurface)
        
        if y < len(enemies):
            enemy = enemies[y]  
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    wasactiondone = False
                    theyblocking = False
                    blockdone = False 
            x = 2
            
        if x == 1:
            x += 1
            if block == False:
                if isinstance(enemy, Enemy) and not isinstance(enemy, Grifter):
                    import random
                    action = random.randint(1, 5)
                    if (enemy.currenthp/enemy.maxhp) <= 0.2:
                        enemy.EnemyHeal(5)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                    elif action in [1, 2, 3, 4] or (enemy.currenthp/enemy.maxhp) >= 1:
                        damage = Character.CharacterDamageCalc(enemy)
                        enemy.lastaction = 'tried to attack, but was blocked!'
                        action = 'tried to attack, but was blocked!'
                        
                    elif action == 5:
                        enemy.EnemyHeal(5)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                elif isinstance(enemy, Grifter):
                    import random
                    action = random.randint(1, 2)
                    if (enemy.currenthp/enemy.maxhp) <= 0.4:
                        enemy.GrifterHeal(40)
                        action = 'healed!'
                    elif action == 1:
                        steal = Grifter.GrifterCalc(enemy)                
                        player.gold *= steal
                        enemy.lastaction = 'stole gold!'
                        action = 'stole gold!'
                    else:
                        enemy.GrifterHeal(40)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                elif isinstance(enemy, BossEnemy):
                    import random
                    action = random.randint(1, 100)
                    if (enemy.currenthp/enemy.maxhp) <= 0.3:
                        enemy.EnemyHeal(25)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                    elif enemy.currenthp/enemy.maxhp >= 1:
                        if action < 90:
                            damage = Character.CharacterDamageCalc(enemy)
                            enemy.lastaction = 'tried to attack, but was blocked!'
                            action = 'tried to attack, but was blocked!'
                        else:
                            enemy.EnemySummon(enemies)
                            enemy.lastaction = 'spawned an Orc!'
                            action = 'spawned an Orc!'
                        
                    else:
                        if action < 71:
                            damage = Character.CharacterDamageCalc(enemy)
                            enemy.lastaction = 'tried to attack, but was blocked!'
                            action = 'tried to attack, but was blocked!'
                        elif action < 91 and action > 70:
                            enemy.EnemyHeal(25)
                            enemy.lastaction = 'healed!'
                            action = 'healed!'
                        else:
                            enemy.EnemySummon(enemies)
                            enemy.lastaction = 'spawned an Orc!'
                            action = 'spawned an Orc!'
            else:
                if isinstance(enemy, Enemy) and not isinstance(enemy, Grifter):
                    import random
                    action = random.randint(1, 5)
                    if (enemy.currenthp/enemy.maxhp) <= 0.2:
                        enemy.EnemyHeal(5)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                    elif action in [1, 2, 3, 4] or (enemy.currenthp/enemy.maxhp) >= 1:
                        damage = Character.CharacterDamageCalc(enemy)
                        player.currenthp -= damage
                        enemy.lastaction = 'attacked you!'
                        action = 'attacked you!'
                        if player.currenthp < 1:
                            battle = False
                        else:
                            pass
                    elif action == 5:
                        enemy.EnemyHeal(5)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'   
                
                elif isinstance(enemy, Grifter):
                    import random
                    action = random.randint(1, 2)
                    if (enemy.currenthp/enemy.maxhp) <= 0.4:
                        enemy.GrifterHeal(40)
                        action = 'healed!'
                    elif action == 1:
                        steal = Grifter.GrifterCalc(enemy)                
                        player.gold *= steal
                        enemy.lastaction = 'stole gold!'
                        action = 'stole gold!'
                    else:
                        enemy.GrifterHeal(40)
                        enemy.lastaction = 'healed!'
                        action = 'healed!' 
                    
                elif isinstance(enemy, BossEnemy):
                    import random
                    action = random.randint(1, 100)
                    if (enemy.currenthp/enemy.maxhp) <= 0.3:
                        enemy.EnemyHeal(25)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                    elif enemy.currenthp/enemy.maxhp >= 1:
                        if action < 90:
                            damage = Character.CharacterDamageCalc(enemy)
                            player.currenthp -= damage
                            enemy.lastaction = 'attacked you!'
                            action = 'attacked you!'
                            if player.currenthp < 1:
                                battle = False
                        else:
                            enemy.EnemySummon(enemies)
                            enemy.lastaction = 'spawned an Orc!'
                            action = 'spawned an Orc!'
                        
                    else:
                        if action < 71:
                            damage = Character.CharacterDamageCalc(enemy)
                            player.currenthp -= damage
                            enemy.lastaction = 'attacked you!'
                            action = 'attacked you!'
                            if player.currenthp < 1:
                                battle = False
                        elif action < 91 and action > 70:
                            enemy.EnemyHeal(25)
                            enemy.lastaction = 'healed!'
                            action = 'healed!'
                        else:
                            enemy.EnemySummon(enemies)
                            enemy.lastaction = 'spawned an Orc!'
                            action = 'spawned an Orc!'
            
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    y += 1
                    x = 1
        try:
            text = textboxfont.render(f'{enemy.name} {action}', True, (255, 255, 255))
            textsurface = text.get_rect(center=textbox.center)
            screen.blit(text, textsurface)
        except UnboundLocalError:
            text = textboxfont.render(f'(continue)', True, (255, 255, 255))
            textsurface = text.get_rect(center=textbox.center)
            screen.blit(text, textsurface)
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    wasactiondone = False
                    theyblocking = False
                    blockdone = False 
                    block = True
    
    def MakeEnemies(enemies):
        xcoordinate = 0
        for enemy in enemies: 
            if isinstance(enemy, Enemy) and not isinstance(enemy, Grifter):
                pygame.draw.circle(screen, (200, 90, 75), (xcoordinate+75, 200), 50)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 225), (xcoordinate+75, 340), 35)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 340), (xcoordinate+35, 400), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 340), (xcoordinate+115, 400), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+35, 400), (xcoordinate+35, 425), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+115, 400), (xcoordinate+115, 425), 30)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 225), (xcoordinate+35, 340), 27)
                pygame.draw.line(screen, (200, 90, 75), (xcoordinate+75, 225), (xcoordinate+115, 340), 27)
                
                healthbarrect = pygame.Rect(xcoordinate+15, 530, 120, 30)
                pygame.draw.rect(screen, (100, 130, 140), healthbarrect)
                pygame.draw.rect(screen, (150, 195, 240), (xcoordinate+15, 530, (enemy.currenthp / enemy.maxhp) * 120, 30))
                
                font = pygame.font.Font(None, 28)
                healthbartext = font.render(f"{int(enemy.currenthp)} / {int(enemy.maxhp)} HP", True, (255, 255, 255))
                healthbarsurface = healthbartext.get_rect(center=healthbarrect.center)
                screen.blit(healthbartext, healthbarsurface)
            
            elif isinstance(enemy, Grifter):
                pygame.draw.circle(screen, (75, 190, 90), (xcoordinate+75, 200), 50)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+75, 225), (xcoordinate+75, 340), 35)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+75, 340), (xcoordinate+35, 400), 30)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+75, 340), (xcoordinate+115, 400), 30)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+35, 400), (xcoordinate+35, 425), 30)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+115, 400), (xcoordinate+115, 425), 30)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+75, 225), (xcoordinate+35, 340), 27)
                pygame.draw.line(screen, (75, 190, 90), (xcoordinate+75, 225), (xcoordinate+115, 340), 27)
                
                healthbarrect = pygame.Rect(xcoordinate+15, 530, 120, 30)
                pygame.draw.rect(screen, (100, 130, 140), healthbarrect)
                pygame.draw.rect(screen, (150, 195, 240), (xcoordinate+15, 530, (enemy.currenthp / enemy.maxhp) * 120, 30))
                
                font = pygame.font.Font(None, 28)
                healthbartext = font.render(f"{int(enemy.currenthp)} / {int(enemy.maxhp)} HP", True, (255, 255, 255))
                healthbarsurface = healthbartext.get_rect(center=healthbarrect.center)
                screen.blit(healthbartext, healthbarsurface)
                
            elif isinstance(enemy, BossEnemy):
                xcoordinate += 30
                pygame.draw.circle(screen, (150, 50, 55), (xcoordinate+75, 150), 70)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 210), (xcoordinate+75, 320), 50)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 320), (xcoordinate+35, 405), 45)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 320), (xcoordinate+115, 405), 45)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+35, 405), (xcoordinate+35, 435), 47)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+115, 405), (xcoordinate+115, 435), 47)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 210), (xcoordinate+25, 360), 42)
                pygame.draw.line(screen, (150, 50, 55), (xcoordinate+75, 210), (xcoordinate+125, 360), 42)

                healthbarrect = pygame.Rect(xcoordinate-15, 515, 180, 60)
                pygame.draw.rect(screen, (100, 130, 140), healthbarrect)
                pygame.draw.rect(screen, (150, 215, 240), (xcoordinate-15, 515, (enemy.currenthp / enemy.maxhp) * 180, 60))
                
                font = pygame.font.Font(None, 28)
                healthbartext = font.render(f"{int(enemy.currenthp)} / {int(enemy.maxhp)} HP", True, (255, 255, 255))
                healthbarsurface = healthbartext.get_rect(center=healthbarrect.center)
                screen.blit(healthbartext, healthbarsurface)
                
            # make this its own function / nah ima do my own thing
            nametagrect = pygame.Rect(xcoordinate+15, 450, 120, 40)
            listname = len((enemy.name))
            if listname < 7:
                nametagfont = pygame.font.Font(None, 36)
            elif listname > 6 and listname < 10:
                nametagfont = pygame.font.Font(None, 28)
            elif listname > 9 and listname < 15:
                nametagfont = pygame.font.Font(None, 21)
            else:
                nametagfont = pygame.font.Font(None, 16)
            nametagtext = nametagfont.render(f'{enemy.name}', True, (225, 10, 10))
            nametagsurface = nametagtext.get_rect(center=nametagrect.center)
            pygame.draw.rect(screen, (30, 30, 37.5), nametagrect)
            screen.blit(nametagtext, nametagsurface)
            xcoordinate += 150
            if isinstance(enemy, BossEnemy):
                xcoordinate +=30
                
    def EndBattle(enemiesfought, player):
        global battle, events, x, inbattle
        youwinrect = pygame.Rect(20, 20, 1240, 480)
        youwinfont = pygame.font.Font(None, 200)
        youwin2font = pygame.font.Font(None, 40)
        youwintext = youwinfont.render('YOU WIN!!', True, (255, 255, 255))
        youwin2text = youwin2font.render('Click to continue.', True, (255, 255, 255))
        youwin2surface = youwin2text.get_rect(centerx=youwinrect.centerx, centery=youwinrect.centery + 100)
        youwinsurface = youwintext.get_rect(center=youwinrect.center)
        screen.blit(youwintext, youwinsurface)
        screen.blit(youwin2text, youwin2surface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                battle = False
                inbattle = False
        
        
        player.gold = int(player.gold)
        import random
        if x == 1:
            x += 1
            for enemy in enemiesfought:
                player.MainCharacterGetEXP(enemy.expdrop)
                if not isinstance(enemy, BossEnemy):
                    player.gold += enemy.golddrop
                
                if isinstance(enemy, Enemy):
                    if isinstance(enemy.weapondrop, Weapon) or isinstance(enemy.weapondrop, HealingItem):
                        if random.randint(1, 100) >= 35:        
                            if len(player.inventory) < 24: # capacity
                                player.inventory.append(enemy.weapondrop)
                    enemiesfought.remove(enemy)
        
    def BattleMenu(player, enemies):
        global wasactiondone, running, attackpressed, attack, enemy, attacksteptwo, x, y, theyblocking, block, events # im gonna be real i would be 
        # saying what x and y are but im so tired ive been programming multiple hours a day across today and yesterday
        global blockdone, chosenenemy, enemiesfought, weaponbroken, inbattle, z
        wasactiondone = False
        attackpressed = False
        attack = False
        attacksteptwo = False
        theyblocking = False
        block = False
        blockdone = False
        chosenenemy = None
        weaponbroken = False
        x = 1
        y = 0
        z = 1
        while inbattle:
            screen.fill((20, 20, 25))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if len(enemies) == 0:
                if z == 1:
                    z += 1
                x = 1
                Battles.EndBattle(enemiesfought, player)
                wasactiondone = True
 # idk maybe
            
            pygame.draw.rect(screen, (200, 220, 240), (0, 620, 1280, 200))
            
            hppercentage = round(player.currenthp / player.maxhp, 2) 
            
            menufont = pygame.font.Font(None, 30)
            healthbar = pygame.Rect((10, 645, 200, 30))
            nameunderhealthbarrect = pygame.Rect((10, 675, 200, 30))
            pygame.draw.rect(screen, (75, 100, 125), (5, 640, 210, 40))
            pygame.draw.rect(screen, (25, 25, 32.5), healthbar)
            if hppercentage < .30:
                uhohtext = menufont.render("!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, (120, 120, 130))
                uhohsurface = uhohtext.get_rect(center=healthbar.center)
                screen.blit(uhohtext, uhohsurface)
            
            pygame.draw.rect(screen, (100, 110, 140), (10, 645, 200*hppercentage, 30))
        
            hptext = menufont.render(f"{int(player.currenthp)} / {int(player.maxhp)} HP", True, (255, 255, 255))
            hpsurface = hptext.get_rect(center=healthbar.center)
            
            nameunderhealthbartext = menufont.render(player.name, True, 36)
            nameunderhbsurface = nameunderhealthbartext.get_rect(center=nameunderhealthbarrect.center)
            
            screen.blit(nameunderhealthbartext, nameunderhbsurface)
            screen.blit(hptext, hpsurface)
            
            if wasactiondone == False:
                Battles.DrawActionButton(player, enemies, "ATTACK")
                Battles.DrawActionButton(player, enemies, "BLOCK")
                Battles.DrawActionButton(player, enemies, "FLEE (coward)")
                if battle == False:
                    break
                
            if theyblocking == True:
                Battles.Block(player)
                
            if blockdone == True:
                if z == 1:
                    z += 1
                    y = 0
                Battles.BlockTwo(player, enemies)
                    
            if attack == True:
                if chosenenemy != None:
                    if z == 1:
                        Battles.AttackAnimation(chosenenemy, enemies, player)
                        z += 1
                    Battles.AttackStepTwo(player, chosenenemy, enemies)          
            
            if attacksteptwo == True:
                Battles.AttackStepThree(player, enemies) 
            
            if weaponbroken == True or player.weapon.name == 'NONE':
                weaponbrokenoutline = pygame.Rect(10, 10, 300, 50)
                weaponbrokenrect = pygame.Rect(15, 15, 290, 40)
                pygame.draw.rect(screen, (30, 30, 40), weaponbrokenoutline)
                pygame.draw.rect(screen, (40, 40, 60), weaponbrokenrect)
                font = pygame.font.Font(None, 24)
                text = font.render('YOUR WEAPON IS BROKEN!', True, (255, 24, 25))
                textsurface = text.get_rect(centerx=weaponbrokenrect.centerx, centery = weaponbrokenrect.centery -9)
                screen.blit(text, textsurface)
                text2 = font.render(f'YOUR STRENGTH: {int(player.strength)}', True, (255, 24, 25))
                text2surface = text2.get_rect(centerx=weaponbrokenrect.centerx, centery = weaponbrokenrect.centery +11)
                screen.blit(text2, text2surface)
            
            Battles.MakeEnemies(enemies)
            pygame.display.update() 

        endingbattle = True
        while endingbattle:
            # placeholder until i figure out how i will set you back in the open world
         # flashbanging me constantly as i debug bruh / do i change it? of course not
            for event in events:
                if event.type == pygame.QUIT:
                    endingbattle = False
                    pygame.quit()
                    exit()
                    break
            
            Battles.EndBattle(enemiesfought, player)        
            pygame.display.update()
            x += 1
            if x == 5:
                endingbattle = False
                break

    def Battle(player, enemies):
        global running, wasactiondone, battle, battling, inbattle, enemiesfought
        running = False
        inbattle = True
        battle = True
        enemiesfought = []
        for enemy in enemies:
            enemiesfought.append(enemy)
        Battles.BattleMenu(player, enemies)
        battling = False