from charactersitems import Character
from charactersitems import MainCharacter
from charactersitems import Enemy
from charactersitems import BossEnemy
from charactersitems import Grifter
from charactersitems import Weapon
import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')
battle = True
running = True

class Battles:
    def DrawActionButton(player, enemies, action, events):
        global wasactiondone, attackpressed, attack, enemy
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
                    Battles.FleeCoward(player)
                    wasactiondone = True
                elif action == 'ATTACK':
                    if attackpressed == True:
                        attackpressed = False
                    else:
                        attackpressed = True
                else:
                    Battles.Block(player, enemies)
                    wasactiondone = True
        
        if attackpressed == True:
            xcoordinate = 0
            events = pygame.event.get()
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
                if attack == True:
                    break
                    
                        
    def AttackStepTwo(player, enemy, enemies):
        global attacksteptwo, attack, hi
        hi = ['oneelement']
        events = pygame.event.get()
        damage = Character.CharacterDamageCalc(player)
        enemy.currenthp -= damage
        textbox = pygame.Rect(220, 630, 1000, 80) # !
        pygame.draw.rect(screen, (40, 40, 60), textbox) # !
        font = pygame.font.Font(None, 36)
        if enemy.currenthp < 0:
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
            if event.type == pygame.MOUSEBUTTONDOWN and go_onHITBOX.collidepoint(pygame.mouse.get_pos()):
                attacksteptwo = True
                attack = False 
                x = 1
    
    def AttackStepThree(player, enemies):
        global battle, x, y
        
        enemy = enemies[y]
        
        events = pygame.event.get()
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
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and go_onHITBOX.collidepoint(pygame.mouse.get_pos()):
                x = 1  
        if x == 1:
            x + 1
            import random
            if isinstance(enemy, Enemy):
                action = random.randint(1, 5)
                print('action')
                if action in [1, 2, 3, 4]:
                    damage = Character.CharacterDamageCalc(enemy)
                    player.currenthp -= damage
                    
                    if player.currenthp < 1:
                        print('HAHAHAHAHA')
                        battle = False
                    else:
                        pass
                elif action == 5:
                    enemy.EnemyHeal(5)
                    print('heal')
                    
            if y < (len(enemies) - 1):
                y += 1
            else:
                x = 2
        
        textfont = pygame.font.Font(None, 36)
        hawk1 = textfont.render(f"{enemy.name} attacks you!", True, (255, 255, 255))
        hawk2 = textfont.render(f"You now have {player.currenthp} HP!", True, (255, 255, 255))
        hawk1surface = hawk1.get_rect(center=(720, 655))
        hawk2uhsurface = hawk2.get_rect(center=(720, 685))
        screen.blit(hawk1, hawk1surface)
        screen.blit(hawk2, hawk2uhsurface)
        
    def FleeCoward(player):
        global battle
        import random
        chancetoflee = 100 - (100*(player.currenthp / player.maxhp))
        if chancetoflee < 35:
            chancetoflee = 35
            
        areyarunning = random.randint(1, 100)
        if areyarunning >= chancetoflee:
            battle = False
        else:
            print('fail lolol')
            
    # make a makeshift for loop that waits for confirm buttons to be pressed
    
    def Block(player, enemies):
        for enemy in enemies:
            print(enemy.name)
    
    def MakeEnemies(enemies):
        xcoordinate = 0
        for enemy in enemies:
            if isinstance(enemy, Enemy):
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
                
                font = pygame.font.Font(None, 36)
                healthbartext = font.render(f"{enemy.currenthp} / {enemy.maxhp} HP", True, (255, 255, 255))
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
                
                font = pygame.font.Font(None, 46)
                healthbartext = font.render(f"{enemy.currenthp} / {enemy.maxhp} HP", True, (255, 255, 255))
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
    
    def BattleMenu(player, enemies):
        global wasactiondone, running, attackpressed, attack, enemy, attacksteptwo, x, y
        running = False
        wasactiondone = False
        attackpressed = False
        attack = False
        attacksteptwo = False
        x = 1
        y = 0
        while battle:
            screen.fill((20, 20, 25))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.draw.rect(screen, (200, 220, 240), (0, 620, 1280, 200))
            
            hppercentage = player.currenthp / player.maxhp
            
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
        
            hptext = menufont.render(f"{player.currenthp} / {player.maxhp} HP", True, (255, 255, 255))
            hpsurface = hptext.get_rect(center=healthbar.center)
            
            nameunderhealthbartext = menufont.render(player.name, True, 36)
            nameunderhbsurface = nameunderhealthbartext.get_rect(center=nameunderhealthbarrect.center)
            
            screen.blit(nameunderhealthbartext, nameunderhbsurface)
            screen.blit(hptext, hpsurface)
            
            if wasactiondone == False:
                Battles.DrawActionButton(player, enemies, "ATTACK", events)
                Battles.DrawActionButton(player, enemies, "BLOCK", events)
                Battles.DrawActionButton(player, enemies, "FLEE (coward)", events)
            
            if attack == True:
                Battles.AttackStepTwo(player, enemy, enemies)
            
            if attacksteptwo == True:
                Battles.AttackStepThree(player, enemies)
                x += 1
            Battles.MakeEnemies(enemies)
            
            pygame.display.update()      
                
player = MainCharacter('edward', 100, 90, 20, Weapon('supersword', 1, 1, 1), [], 100, 10, 1) 
goblin = Enemy('GoblinAAA', 2, 1, 40, Weapon('supersword', 1, 1, 1), 5, 6, 7)
goblina = Enemy('Goblin', 2, 1, 40, Weapon('supersword', 1, 1, 1), 5, 6, 7)

enemies = [goblin, goblina]
Battles.BattleMenu(player, enemies)