import pygame
import sys
import pygame_gui
from account2 import Account
import json
from pygame.font import Font


# Initialize Pygame
pygame.init()

# Constants for the window dimensions
WIDTH = 1000
HEIGHT = 800

# Constants for colors
WHITE = (255, 255, 255)
BLACK=(0,0,0)

# Create a Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("AMONGESE BANKS")

# Load ATM image
Atm_main = pygame.image.load("IMAGES/atm.png")
Atm_main = pygame.transform.scale(Atm_main, (750, 750))
Atm_rect = Atm_main.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Create button images
button_unpressed = pygame.image.load("IMAGES/unbutton.png")
button_pressed = pygame.image.load("IMAGES/button.png")

# Create button class
class ImageButton:
    def __init__(self, x, y, width, height, normal_image, pressed_image):
        self.image_normal = pygame.transform.scale(normal_image, (width, height))
        self.image_pressed = pygame.transform.scale(pressed_image, (width, height))
        self.rect = self.image_normal.get_rect(topleft=(x, y))
        self.is_pressed = False

    def draw(self, surface):
        surface.blit(self.image_pressed if self.is_pressed else self.image_normal, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_pressed = False
        return False


# Create buttons
buttons = [
    ImageButton(680, 140, 70, 70, button_unpressed, button_pressed),
    ImageButton(680, 275, 70, 70, button_unpressed, button_pressed),
    ImageButton(680, 410, 70, 70, button_unpressed, button_pressed),
    ImageButton(250, 142, 70, 70, button_unpressed, button_pressed),
    ImageButton(250, 277, 70, 70, button_unpressed, button_pressed),
    ImageButton(250, 412, 70, 70, button_unpressed, button_pressed)
]

# Create UI manager
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

current_Account=None
login_successful = False  # Add this boolean variable


text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((375, 300), (250, 30)),
                                                         manager=manager)

text_entry2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((375, 250), (250, 30)),manager=manager)
text_entry2.hide()


with open("database.json", 'r') as json_file:
    db = json.load(json_file)


font3 = Font("FONTS/Pokemon GB.ttf", 8)
back_option="Back"
back_surface = font3.render(back_option, True, BLACK)


def login(text_entry,current_screen,Accounts):
    global login_successful  # Use the global variable
    current_Account=None

    font1 = Font('FONTS/Pokemon GB.ttf', 20)
    hello_surface = font1.render(" Welcome to \nAmongese Bank", True, BLACK)
    window.blit(hello_surface, (378, 210))
    font2 = Font('FONTS/Pokemon GB.ttf', 12)
    enter_pass_surface = font2.render("Enter Password: ", True, BLACK)
    window.blit(enter_pass_surface, (378, 285))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:


            while current_Account is None:
                for account in Accounts:
                    if text_entry.get_text() == account['properties']['password']:
                        current_Account = Account(account['properties']['isim'], account['properties']['password'],
                                                 account['properties']['soyisim'], account['properties']['tel_no'],
                                                 account['properties']['baslangic_parasi'])

                        login_successful = True  # Set the login_successful flag
                        current_screen="Home"

                        return current_Account,current_screen
                if current_Account==None:
                    print("terbiyeli biseyler")
                    break
            text_entry.clear()

    return current_Account, current_screen
# a flag to track which screen should be on
current_screen="Login"
def Homepage(current_Account:Account):
    font1 = Font('FONTS/Pokemon GB.ttf', 13)
    font2 = Font("FONTS/AmongUs-Regular.ttf", 20)

    # Enter the messages
    info = f"""
Name: {current_Account.isim}

Surname: {current_Account.soyisim}

{current_Account.tel_no}

Balance: {current_Account.başlangıç_parası}
"""
    amogus = "A"
    withraw_option = "Withdraw"
    deposit_option="Deposit"
    transfer_option="Transfer"
    login_option="Login"

    # Enter the surfaces
    info_surface = font1.render(info, True, BLACK)
    withdraw_surface = font3.render(withraw_option, True, BLACK)
    deposit_surface = font3.render(deposit_option, True, BLACK)
    transfer_surface = font3.render(transfer_option, True, BLACK)

    login_surface = font3.render(login_option, True, BLACK)
    amogus_surface = font2.render(amogus, True, BLACK)

    # Enter the blits
    window.blit(info_surface, (420, 153))
    window.blit(amogus_surface, (545+len(str(current_Account.başlangıç_parası))*12, 240))
    window.blit(withdraw_surface, (593, 309))
    window.blit(deposit_surface, (599, 171))
    window.blit(transfer_surface, (599, 441))
    window.blit(login_surface, (345, 309))
    window.blit(back_surface, (345, 441))


errormassageshow=False


def withraw(current_account:Account):
    text_entry.show()
    withdraw_amount = 0
    window.blit(back_surface, (345, 441))
    global errormassageshow,current_screen
    if errormassageshow:
        font2 = Font("FONTS/Pokemon GB.ttf", 20)
        info2 = "sayi gir lan"
        info2_surface = font2.render(info2, True, (0, 0, 0))

        window.blit(info2_surface, (260, 150))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            try:
                withdraw_amount=int(text_entry.get_text())
                if current_account.paraCekimi(withdraw_amount):
                    with open('database.json', 'w') as json_file:
                        for account in db:
                            if account['properties']['isim'] == current_account.isim:
                                account['properties']["baslangic_parasi"] = current_account.başlangıç_parası
                                break
                        json.dump(db, json_file, indent=2)
                        text_entry.clear()
                        errormassageshow = False
                        current_screen = "Home"


            except ValueError:
                    errormassageshow=True




def deposit(current_account:Account):
    text_entry.show()
    deposit_amount = 0
    window.blit(back_surface, (345, 441))
    global errormassageshow, current_screen
    if errormassageshow:
        font2 = Font("FONTS/Pokemon GB.ttf", 20)
        info2 = "sayi gir lan"
        info2_surface = font2.render(info2, True, (0, 0, 0))

        window.blit(info2_surface, (260, 150))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            if current_account.
                try:
                    deposit_amount = int(text_entry.get_text())
                    current_account.paraYatirimi(deposit_amount)
                    with open('database.json', 'w') as json_file:
                        for account in db:
                            if account['properties']['isim'] == current_account.isim:
                                account['properties']["baslangic_parasi"] = current_account.başlangıç_parası
                                break
                        json.dump(db, json_file, indent=2)
                        text_entry.clear()
                        current_screen = "Home"
                        errormassageshow = False
                except ValueError:
                    print("value error ecourd")
                    errormassageshow = True



def transfer(current_account:Account):
    text_entry.show()
    deposit_amount = 0
    window.blit(back_surface, (345, 441))
    text_entry2.show()
    global errormassageshow, current_screen
    if errormassageshow:
        font2 = Font("FONTS/Pokemon GB.ttf", 10)
        info2 = "invalid amount or target account please check your balance and target account"
        info2_surface = font2.render(info2, True, BLACK)

        window.blit(info2_surface, (260, 150))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            try:
                transfer_amount = int(text_entry.get_text())
                transfer_account = text_entry2.get_text()
                for account in db:
                    if account['properties']['isim'] == transfer_account:
                        transfer_account = Account(account['properties']['isim'], account['properties']['password'],
                                                account['properties']['soyisim'], account['properties']['tel_no'],
                                                account['properties']['baslangic_parasi'])
                if current_account.paraAktarimi(transfer_account, transfer_amount):
                    with open('database.json', 'w') as json_file:
                        for account in db:
                            if account['properties']['isim'] == current_account.isim:
                                account['properties']["baslangic_parasi"] = current_account.başlangıç_parası
                            if account['properties']['isim'] == transfer_account.isim:
                                account['properties']["baslangic_parasi"] = transfer_account.başlangıç_parası
                        json.dump(db, json_file, indent=2)
                        text_entry.clear()
                        text_entry2.clear()
                        text_entry2.hide()
                        current_screen = "Home"
            except ValueError:
                errormassageshow = True










# Main game loop
running = True
# a flag to track which screen should be on


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)
        manager.process_events(event)

    # Clear the screen
    window.fill(WHITE)

    # Draw ATM image
    window.blit(Atm_main, Atm_rect)

    # Draw buttons
    for button in buttons:
        button.draw(window)

    #Check wether the user has logged in yet
    if login_successful:
        text_entry.hide()
        if current_screen == "Home":
            text_entry.clear()
            Homepage(current_Account)
            if event.type == pygame.MOUSEBUTTONUP:
                if buttons[0].rect.collidepoint(event.pos):
                    current_screen="Deposit"
                if buttons[1].rect.collidepoint(event.pos):
                    current_screen="Withdraw"
                if buttons[2].rect.collidepoint(event.pos):
                    current_screen = "Transfer"
                if buttons[4].rect.collidepoint(event.pos):
                    current_screen = "Login"
                if buttons[5].rect.collidepoint(event.pos):
                    current_screen = "Home"
    if current_screen=="Withdraw":
        withraw(current_Account)
        if event.type == pygame.MOUSEBUTTONUP:
            if buttons[5].rect.collidepoint(event.pos):
                current_screen = "Home"
                errormassageshow = False
    if current_screen=="Deposit":
        deposit(current_Account)
        if event.type == pygame.MOUSEBUTTONUP:
            if buttons[5].rect.collidepoint(event.pos):
                current_screen = "Home"
                errormassageshow = False
    if current_screen =="Transfer":
        transfer(current_Account)
        if event.type == pygame.MOUSEBUTTONUP:
            if buttons[5].rect.collidepoint(event.pos):
                current_screen = "Home"
                text_entry2.hide()

    else:
        # Draw the text entry only when not logged in
        if not login_successful:
            manager.update(0.03)
            manager.draw_ui(window)

    # get the user account from database
    if current_screen=="Login":
        text_entry.show()
        current_Account,current_screen = login(text_entry,current_screen,db)

    # Draw U
    manager.update(0.03)
    manager.draw_ui(window)





    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()