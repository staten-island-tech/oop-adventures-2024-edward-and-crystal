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
                    Battles.FleeCoward(player)
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
        if enemy.currenthp <= 0:
            enemy.currenthp = 0
            youractiontwo = font.render(f'The {enemy.name} has died!', True, (255, 255, 255))
            
            try:
                enemies.remove(enemy)
                enemiesfought.append(enemy)
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
            if enemy.currenthp <= 0:
                enemiesfought.append(enemy)
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
            if isinstance(enemy, Enemy):
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
                    enemy.GrifterHeal(10)
                elif action == 1:
                    steal = Grifter.GrifterCalc(enemy)                
                    player.gold *= steal
                    enemy.lastaction = 'stole gold!'
                    action = 'stole gold!'
                else:
                    enemy.GrifterHeal(10)
                    enemy.lastaction = 'healed!'
                    action = 'healed!'
                    
            elif isinstance(enemy, BossEnemy):
                import random
                action = random.randint(1, 100)
                if (enemy.currenthp/enemy.maxhp) <= 0.3:
                    enemy.EnemyHeal(15)
                    enemy.lastaction = 'healed!'
                    action = 'healed!'
                elif enemy.currenthp/enemy.maxhp >= 1:
                    if action < 90:
                        damage = Character.CharacterDamageCalc(enemy)
                        player.currenthp -= damage
                        enemy.lastaction = 'attacked you!'
                        action = 'attacked you!'
                        if player.currenthp < 1:
                            print('HAHAHAHAHA')
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
                            print('HAHAHAHAHA')
                            battle = False
                    elif action < 91 and action > 70:
                        enemy.EnemyHeal(15)
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
        
        
    def FleeCoward(player):
        global battle, block, blockdone
        import random
        chancetoflee = 100 - (100*(player.currenthp / player.maxhp))
        if chancetoflee < 45:
            chancetoflee = 45
            
        areyarunning = random.randint(1, 100)
        if areyarunning >= chancetoflee:
            battle = False
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
                if isinstance(enemy, Enemy):
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
                        enemy.GrifterHeal(10)
                    elif action == 1:
                        steal = Grifter.GrifterCalc(enemy)                
                        player.gold *= steal
                        enemy.lastaction = 'stole gold!'
                        action = 'stole gold!'
                    else:
                        enemy.GrifterHeal(10)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                elif isinstance(enemy, BossEnemy):
                    import random
                    action = random.randint(1, 100)
                    if (enemy.currenthp/enemy.maxhp) <= 0.3:
                        enemy.EnemyHeal(15)
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
                            enemy.EnemyHeal(15)
                            enemy.lastaction = 'healed!'
                            action = 'healed!'
                        else:
                            enemy.EnemySummon(enemies)
                            enemy.lastaction = 'spawned an Orc!'
                            action = 'spawned an Orc!'
            else:
                if isinstance(enemy, Enemy):
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
                            print('HAHAHAHAHA')
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
                        enemy.GrifterHeal(10)
                    elif action == 1:
                        steal = Grifter.GrifterCalc(enemy)                
                        player.gold *= steal
                        enemy.lastaction = 'stole gold!'
                        action = 'stole gold!'
                    else:
                        enemy.GrifterHeal(10)
                        enemy.lastaction = 'healed!'
                        action = 'healed!' 
                    
                elif isinstance(enemy, BossEnemy):
                    import random
                    action = random.randint(1, 100)
                    if (enemy.currenthp/enemy.maxhp) <= 0.3:
                        enemy.EnemyHeal(15)
                        enemy.lastaction = 'healed!'
                        action = 'healed!'
                    elif enemy.currenthp/enemy.maxhp >= 1:
                        if action < 90:
                            damage = Character.CharacterDamageCalc(enemy)
                            player.currenthp -= damage
                            enemy.lastaction = 'attacked you!'
                            action = 'attacked you!'
                            if player.currenthp < 1:
                                print('HAHAHAHAHA')
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
                                print('HAHAHAHAHA')
                                battle = False
                        elif action < 91 and action > 70:
                            enemy.EnemyHeal(15)
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
        global battle, events, x
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
        
        if x == 1:
            x += 1
            for enemy in enemiesfought:
                player.MainCharacterGetEXP(enemy.expdrop)
                if player.level >= 30:
                    player.level = 30
                    player.exp = 0
                if isinstance(enemy, Enemy):
                    if isinstance(enemy.weapondrop, Weapon) or isinstance(enemy.weapondrop, HealingItem):
                        if len(player.inventory) < 24: # capacity
                            player.inventory.append(enemy.weapondrop)
                    enemiesfought.remove(enemy)
        
    def BattleMenu(player, enemies):
        global wasactiondone, running, attackpressed, attack, enemy, attacksteptwo, x, y, theyblocking, block, events # im gonna be real i would be 
        # saying what x and y are but im so tired ive been programming multiple hours a day across today and yesterday
        global blockdone, chosenenemy, enemiesfought, weaponbroken
        wasactiondone = False
        attackpressed = False
        attack = False
        attacksteptwo = False
        theyblocking = False
        block = False
        blockdone = False
        chosenenemy = None
        weaponbroken = False
        enemiesfought = []
        x = 1
        y = 0
        z = 1
        while battle:
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
            if battle == False:
                break # idk maybe
            
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
                
            if theyblocking == True:
                Battles.Block(player)
                
            if blockdone == True:
                if z == 1:
                    z += 1
                    y = 0
                Battles.BlockTwo(player, enemies)
                    
            if attack == True:
                if chosenenemy != None:
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
            screen.fill((255, 255, 255)) # flashbanging me constantly as i debug bruh / do i change it? of course not
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
        global running, wasactiondone, battle
        running = False
        battle = True
        Battles.BattleMenu(player, enemies)