from charactersitems import Character
from charactersitems import MainCharacter
from charactersitems import Weapon
from charactersitems import HealingItem
import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Menu')

class Menu:
    def DrawButtonMainMenu(buttontitle, events):
        global menurunning, mainmenu, statsrunning, shop, inventory, save
        
        # draws buttons
        if buttontitle == 'YOUR   STATS':
            buttonrect = pygame.Rect(0, 110, 500, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        elif buttontitle == 'INVENTORY':
            buttonrect = pygame.Rect(0, 220, 400, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        elif buttontitle == "SHOP":
            buttonrect = pygame.Rect(0, 330, 335, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        elif buttontitle == "SAVE":
            buttonrect = pygame.Rect(0, 440, 270, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (100, 110, 140)
            else:
                color = (50, 50, 75)
            pygame.draw.rect(screen, color, buttonrect)
        else:
            buttonrect = pygame.Rect(0, 600, 450, 100) 
            if buttonrect.collidepoint(pygame.mouse.get_pos()):
                color = (110, 160, 185)
            else:
                color = (90, 100, 150)
            pygame.draw.rect(screen, color, buttonrect)
            
        textfont = pygame.font.SysFont(None, 90, bold = True)
        text = textfont.render(buttontitle, True, (200, 220, 255))
        textsurface = text.get_rect(left=buttonrect.left + 10, centery = buttonrect.centery)
        screen.blit(text, textsurface)
        
        # title
        if buttontitle == 'YOUR   STATS':
            titlefont = pygame.font.SysFont(None, 110, bold = True)
            title = titlefont.render('MAIN MENU', True, (255, 255, 255))
            titlesurface = title.get_rect(centerx=buttonrect.centerx-10, centery = 60)
            screen.blit(title, titlesurface)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and buttonrect.collidepoint(pygame.mouse.get_pos()): 
                mainmenu = False
                if buttontitle == 'CLOSE MENU':
                    menurunning = False
                elif buttontitle == 'YOUR   STATS':
                    statsrunning = True
                elif buttontitle == 'INVENTORY':
                    inventory = True
                elif buttontitle == 'SHOP':
                    shop = True
                elif buttontitle == 'SAVE':
                    save = True
    
    def StatScreen(player, events):
        global mainmenu, statsrunning
        
        titlefont = pygame.font.SysFont(None, 110, bold = True)
        subtitlefont = pygame.font.SysFont(None, 80, bold = True)
        littletitlefont = pygame.font.SysFont(None, 50, bold = True)
        textfont = pygame.font.Font(None, 45)
        
        # title
        titlerect = pygame.Rect(0, 110, 500, 100)
        title = titlefont.render(f"{player.name.upper()}'S STATS", True, (255, 255, 255))
        offset = len(player.name)
        titlesurface = title.get_rect(centerx=titlerect.centerx+(offset*23), centery = 60)
        screen.blit(title, titlesurface)
        
        # health
        healthtitlerect = pygame.Rect(10, 120, 250, 110)
        healthtitle = subtitlefont.render('HEALTH', True, (200, 220, 255))
        healthsurface = healthtitle.get_rect(center = healthtitlerect.center)
        screen.blit(healthtitle, healthsurface)
        
        healthbaroutline = pygame.Rect(300, 135, 700, 80)
        pygame.draw.rect(screen, (40, 40, 60), healthbaroutline)
        fullhealthbar = pygame.Rect(310, 145, 680, 60)
        pygame.draw.rect(screen, (60, 60, 90), fullhealthbar)
        hppercentage = player.currenthp / player.maxhp
        subhealthbar = pygame.Rect(310, 145, 680*hppercentage, 60)
        pygame.draw.rect(screen, (100, 120, 160), subhealthbar)
        
        healthbartext = subtitlefont.render(f'{player.currenthp} / {player.maxhp} HP', True, (255, 255, 255))
        healthbartextsurface = healthbartext.get_rect(centery=healthbaroutline.centery, centerx=healthbaroutline.centerx - 180)
        screen.blit(healthbartext, healthbartextsurface)
        
        # level and exp
        leveltitlerect = pygame.Rect(10, 250, 270, 110)
        leveltitle = subtitlefont.render(f'LEVEL {player.level}', True, (200, 220, 255))
        levelsurface = leveltitle.get_rect(center=leveltitlerect.center)
        screen.blit(leveltitle, levelsurface)
        
        expbaroutline = pygame.Rect(300, 265, 700, 80)
        pygame.draw.rect(screen, (40, 40, 60), expbaroutline)
        fullexpbar = pygame.Rect(310, 275, 680, 60)
        pygame.draw.rect(screen, (60, 60, 90), fullexpbar)
        expneeded = 75 + 5*player.level
        exppercentage = player.exp / expneeded
        subexpbar = pygame.Rect(310, 275, 680*exppercentage, 60)
        pygame.draw.rect(screen, (100, 120, 160), subexpbar)
        
        exptext = subtitlefont.render(f'{player.exp} / {expneeded} XP', True, (255, 255, 255))
        exptextsurface = exptext.get_rect(centery=expbaroutline.centery, centerx = expbaroutline.centerx - 177)
        screen.blit(exptext, exptextsurface)
        
        # strength
        strengthrectoutline = pygame.Rect(20, 380, 400, 300)
        pygame.draw.rect(screen, (40, 40, 60), strengthrectoutline)
        strengthrect = pygame.Rect(30, 390, 380, 280)
        pygame.draw.rect(screen, (60, 60, 90), strengthrect)
        
        lineoneA = littletitlefont.render('STRENGTH', True, (200, 220, 255))
        lineoneB = lineoneA.get_rect(centerx=strengthrect.centerx, centery=strengthrect.centery - 100)
        screen.blit(lineoneA, lineoneB)
        
        linetwoA = textfont.render(f'BASE STRENGTH: {player.strength}', True, (255, 255, 255))
        linetwoB = linetwoA.get_rect(centerx=strengthrect.centerx, centery=strengthrect.centery - 55)
        screen.blit(linetwoA, linetwoB)
        
        linethreeA = textfont.render(f'WEAPON STRENGTH: {player.weapon.strength}', True, (255, 255, 255))
        linethreeB = linethreeA.get_rect(centerx=strengthrect.centerx, centery=strengthrect.centery - 20)
        screen.blit(linethreeA, linethreeB)
        
        linefourA = littletitlefont.render(f'TOTAL STRENGTH: {player.weapon.strength + player.strength}', True, (200, 220, 255))
        linefourB = linefourA.get_rect(centerx=strengthrect.centerx, centery=strengthrect.centery + 90)
        screen.blit(linefourA, linefourB)
        
        # gold
        goldrectoutline = pygame.Rect(440, 380, 400, 300)
        pygame.draw.rect(screen, (40, 40, 60), goldrectoutline)
        
        goldrect = pygame.Rect(450, 390, 380, 280)
        pygame.draw.rect(screen, (60, 60, 90), goldrect)
        
        goldfont = pygame.font.SysFont(None, 105, bold=True)
        lineoneA = goldfont.render(f'{player.gold} GOLD', True, (200, 220, 255))
        lineoneB = lineoneA.get_rect(centerx=goldrect.centerx, centery= goldrect.centery-90)
        screen.blit(lineoneA, lineoneB)
        
        linetwoA = textfont.render('JUDGEMENT:', True, (255, 255, 255))
        linetwoB = linetwoA.get_rect(centerx=goldrect.centerx, centery=goldrect.centery)
        screen.blit(linetwoA, linetwoB)

        if player.gold < 30:
            judgement = 'POOR!'
        elif player.gold < 100:
            judgement = 'AVERAGE'
        elif player.gold <= 999:
            judgement = 'RICH!'
        else:
            judgement = 'BALLING!'
        
        linethreeA = goldfont.render(judgement, True, (255, 245, 200))
        linethreeB = linethreeA.get_rect(centerx=goldrect.centerx, centery= goldrect.centery+90)
        screen.blit(linethreeA, linethreeB)
        
        # weapon
        weaponrectoutline = pygame.Rect(860, 380, 400, 300)
        pygame.draw.rect(screen, (40, 40, 60), weaponrectoutline)
        
        weaponrect = pygame.Rect(870, 390, 380, 280)
        pygame.draw.rect(screen, (60, 60, 90), weaponrect)
        
        lineoneA = littletitlefont.render('WEAPON', True, (200, 220, 255))
        lineoneB = lineoneA.get_rect(centerx=weaponrect.centerx, centery=weaponrect.centery-90)
        screen.blit(lineoneA, lineoneB)
        
        length = len(player.weapon.name)
        
        if length < 7:
            size = 100
        elif length < 15:
            size = 80
        elif length < 25:
            size = 60
        else:
            size = 45
        
        weaponfont = pygame.font.SysFont(None, size, bold=True)
        linetwoA = weaponfont.render(f'{player.weapon.name}', True, (255, 255, 255))
        linetwoB = linetwoA.get_rect(centerx=weaponrect.centerx, centery=weaponrect.centery)
        screen.blit(linetwoA, linetwoB)
        
        # back button
        backbutton = pygame.Rect(850, 25, 400, 90)
        if backbutton.collidepoint(pygame.mouse.get_pos()):
            color = (100, 110, 140)
        else:
            color = (50, 50, 75)

        pygame.draw.rect(screen, color, backbutton)
        backbuttontext = subtitlefont.render('MENU', True, (255, 255, 255))
        backbuttontextsurface = backbuttontext.get_rect(center = backbutton.center)
        screen.blit(backbuttontext, backbuttontextsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and backbutton.collidepoint(pygame.mouse.get_pos()):
                mainmenu = True
                statsrunning = False   
    
    def DrawInventoryButtons(player, events):
        global inventory, inventoryselectscreen, selecteditem
        xcoordinate = 10
        ycoordinate = 150
        
        for item in range(len(player.inventory)): # this will make sense
            theitem = player.inventory[item]
            
            size = 50 - int(1.5*len(theitem.name))
            if size < 17:
                size = 17
            itemfont = pygame.font.Font(None, size)
            
            # getting the coordinate
            itemxcoordinate = (item % 6) 
            itemycoordinate = int(item / 6) 
                
            itemrect = pygame.Rect(xcoordinate + 210*itemxcoordinate, ycoordinate + 110*itemycoordinate, 200, 100)
            itemrectinside = pygame.Rect(xcoordinate + 10 + 210*itemxcoordinate, ycoordinate + 10 + 110*itemycoordinate, 180, 80)
            
            
            if itemrect.collidepoint(pygame.mouse.get_pos()):
                color = (60, 60, 90)
            else:
                color = (40, 40, 60)
                
            pygame.draw.rect(screen, (30, 30, 40), itemrect)
            pygame.draw.rect(screen, color, itemrectinside)
            
            itemtext = itemfont.render(f'{theitem.name}', True, (255, 255, 255))
            itemsurface = itemtext.get_rect(center=itemrect.center)
            screen.blit(itemtext, itemsurface)
            
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and itemrect.collidepoint(pygame.mouse.get_pos()):
                    if isinstance(theitem, Weapon):
                        inventory = False
                        inventoryselectscreen = True
                        selecteditem = theitem
                    else:
                        inventory = False
                        inventoryselectscreen = True
                        selecteditem = theitem
                        
    def RouteInventoryFunction(selecteditem, events):
        if isinstance(selecteditem, Weapon):
            Menu.EquipWeapon(selecteditem, events)
        elif isinstance(selecteditem, HealingItem):
            Menu.HealingMenu(selecteditem, events)
            
    def EquipWeapon(selecteditem, events):
        global inventoryselectscreen, inventory
        titlefont = pygame.font.SysFont(None, 110, bold = True)
        subtitlefont = pygame.font.SysFont(None, 80, bold = True)
        littletitlefont = pygame.font.SysFont(None, 50, bold = True)
        textfont = pygame.font.Font(None, 45)
        
        # title
        titlerect = pygame.Rect(0, 110, 400, 100)
        title = titlefont.render("EQUIP WEAPON", True, (255, 255, 255))
        titlesurface = title.get_rect(centerx=titlerect.centerx+130, centery = 60)
        screen.blit(title, titlesurface)
        
        # putting the name of the weapon
        weapontitlerect = pygame.Rect(100, 135, 1060, 120)
        pygame.draw.rect(screen, (30, 30, 40), weapontitlerect)
        
        weapontitletext = subtitlefont.render(f'WEAPON: {selecteditem.name.upper()}', True, (255, 255, 255))
        weapontitlesurface = weapontitletext.get_rect(center = weapontitlerect.center)
        screen.blit(weapontitletext, weapontitlesurface)
        
        # 
        # STATS
        #
        
        statsboxoutline = pygame.Rect(20, 300, 900, 400)
        pygame.draw.rect(screen, (30, 30, 40), statsboxoutline)
        statsbox = pygame.Rect(30, 310, 880, 380)
        pygame.draw.rect(screen, (40, 40, 60), statsbox)
        
        # damage
        
        damagerect = pygame.Rect(50, 320, 840, 100)
        damagepercentage = selecteditem.strength / 100

        damagerectinside = pygame.Rect(60, 330, (840*damagepercentage) - 20, 80)
        pygame.draw.rect(screen, (20, 20, 30), damagerect)
        pygame.draw.rect(screen, (60, 60, 90), damagerectinside)
                
        damage = subtitlefont.render(f"DAMAGE: {selecteditem.strength}", True, (255, 255, 255))
        damagesurface = damage.get_rect(center=damagerect.center)
        screen.blit(damage, damagesurface)
        
        # back button
        backbutton = pygame.Rect(850, 25, 400, 90)
        if backbutton.collidepoint(pygame.mouse.get_pos()):
            color = (100, 110, 140)
        else:
            color = (50, 50, 75)

        pygame.draw.rect(screen, color, backbutton)
        backbuttontext = subtitlefont.render('INVENTORY', True, (255, 255, 255))
        backbuttontextsurface = backbuttontext.get_rect(center = backbutton.center)
        screen.blit(backbuttontext, backbuttontextsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and backbutton.collidepoint(pygame.mouse.get_pos()):
                inventory = True
                inventoryselectscreen = False
        
    def HealingMenu(selecteditem, events):
        global inventoryselectscreen, inventory

        titlefont = pygame.font.SysFont(None, 110, bold = True)
        subtitlefont = pygame.font.SysFont(None, 80, bold = True)
        littletitlefont = pygame.font.SysFont(None, 50, bold = True)
        textfont = pygame.font.Font(None, 45)
        
        # title
        titlerect = pygame.Rect(0, 110, 400, 100)
        title = titlefont.render("HEALING MENU", True, (255, 255, 255))
        offset = len(player.name)
        titlesurface = title.get_rect(centerx=titlerect.centerx+(offset*23), centery = 60)
        screen.blit(title, titlesurface)
        
        # back button
        backbutton = pygame.Rect(850, 25, 400, 90)
        if backbutton.collidepoint(pygame.mouse.get_pos()):
            color = (100, 110, 140)
        else:
            color = (50, 50, 75)
        
        pygame.draw.rect(screen, color, backbutton)
        backbuttontext = subtitlefont.render('INVENTORY', True, (255, 255, 255))
        backbuttontextsurface = backbuttontext.get_rect(center = backbutton.center)
        screen.blit(backbuttontext, backbuttontextsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and backbutton.collidepoint(pygame.mouse.get_pos()):
                inventory = True
                inventoryselectscreen = False   
    
    def Inventory(player, events):
        global inventory, mainmenu, inventoryselectscreen, selecteditem
        
        titlefont = pygame.font.SysFont(None, 110, bold = True)
        subtitlefont = pygame.font.SysFont(None, 80, bold = True)
        littletitlefont = pygame.font.SysFont(None, 50, bold = True)
        textfont = pygame.font.Font(None, 45)
        
        # title
        titlerect = pygame.Rect(0, 110, 500, 100)
        title = titlefont.render(f"INVENTORY", True, (255, 255, 255))
        titlesurface = title.get_rect(centerx=titlerect.centerx, centery = 60)
        screen.blit(title, titlesurface)
        
        # back button
        backbutton = pygame.Rect(850, 25, 400, 90)
        if backbutton.collidepoint(pygame.mouse.get_pos()):
            color = (100, 110, 140)
        else:
            color = (50, 50, 75)

        pygame.draw.rect(screen, color, backbutton)
        backbuttontext = subtitlefont.render('MENU', True, (255, 255, 255))
        backbuttontextsurface = backbuttontext.get_rect(center = backbutton.center)
        screen.blit(backbuttontext, backbuttontextsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and backbutton.collidepoint(pygame.mouse.get_pos()):
                mainmenu = True
                inventory = False 
                
        Menu.DrawInventoryButtons(player, events) 
        backbutton = pygame.Rect(850, 25, 400, 90)
        if backbutton.collidepoint(pygame.mouse.get_pos()):
            color = (100, 110, 140)
        else:
            color = (50, 50, 75)

        pygame.draw.rect(screen, color, backbutton)
        backbuttontext = subtitlefont.render('MENU', True, (255, 255, 255))
        backbuttontextsurface = backbuttontext.get_rect(center = backbutton.center)
        screen.blit(backbuttontext, backbuttontextsurface)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and backbutton.collidepoint(pygame.mouse.get_pos()):
                mainmenu = True
                inventory = False       

    def OpenMenuScreen(player):
        global menurunning, mainmenu, statsrunning, shop, inventory, inventoryselectscreen, save, selecteditem
        menurunning = True
        ending = True
        
        mainmenu = True
        statsrunning = False
        shop = False
        inventory = False
        save = False
        inventoryselectscreen = False
        selecteditem = None
        
        x = 0

        while menurunning:
            screen.fill((20, 20, 25))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
            radius = 400
            color = (20, 20, 25)
            redness = color[0]
            greenness = color[1]
            blueness = color[2]
        
            for i in range(100):
                pygame.draw.circle(screen, color, (640, 700), radius)
                radius -= 2
                redness += 0.5
                greenness += 1
                blueness += 2
                color = (redness, greenness, blueness)

            if mainmenu == True:
                buttontitles = ['YOUR   STATS', 'SHOP', 'INVENTORY', 'SAVE', 'CLOSE MENU']
                for buttontitle in buttontitles:
                    Menu.DrawButtonMainMenu(buttontitle, events)
                    
            elif statsrunning == True:
                Menu.StatScreen(player, events)
            
            elif shop == True:
                print('hi')
            
            elif inventory == True:
                Menu.Inventory(player, events)
            elif inventoryselectscreen == True:
                Menu.RouteInventoryFunction(selecteditem, events)
            
            elif save == True:
                pass
            
            pygame.display.update() 
        
        while ending:
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            x += 1
            print(x)
            if x > 99:
                ending = False
                break
            screen.fill((20, 20, 25))
            pygame.display.update()

weaponA = Weapon('AHHH', 40, 1, 1)
weaponB = Weapon('AHHH', 30, 1, 1)
weaponC = Weapon('AHHHHHHsadofjadslkfjadsk;lf', 100, 1, 1)
weaponD = Weapon('AHHH', 105, 1, 1)
weaponE = Weapon('AHHH', 90, 1, 1)
weaponF = Weapon('AHHH', 10, 1, 1)
weaponG = Weapon('AHHH', 19, 1, 1)
healingitem = HealingItem('AHHH', 37, 1)
weaponI = Weapon('AHHH', 32, 1, 1)

player = MainCharacter('player', 100, 59, 0, Weapon('aaaaaaaaaaaa', 100, 20, 30), [weaponA, weaponB, weaponC, weaponD, weaponE, weaponF, weaponG, healingitem, weaponI], 20, 20, 80)

Menu.OpenMenuScreen(player)