import pygame
import time
import math

pygame.init()  # pgame, i'n'it?

diswidth = 1250
disheight = 600

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

gameDisplay = pygame.display.set_mode((diswidth, disheight))

font = pygame.font.SysFont("pressstart2pregular", 30)

pygame.display.set_caption('Super Calcio')
clock = pygame.time.Clock()

# set a default

calcioright = pygame.image.load('calcio.png')
calcioleft = pygame.image.load('calcioleft.png')
dinomode = 0

# define colors for menu boxes
black = (0, 0, 0)
white = (255, 255, 255)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 173, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 105, 255)
bright_yellow = (255, 255, 0)
yellow = (200, 200, 0)

background1 = pygame.image.load('background.png').convert()
background1 = pygame.transform.scale(background1, (1250, 600))
background2 = pygame.image.load('background2.png').convert()
background2 = pygame.transform.scale(background2, (1250, 600))

addImg = pygame.image.load('add.png')
subImg = pygame.image.load('sub.png')
divImg = pygame.image.load('div.png')
multiImg = pygame.image.load('mult.png')
oneImg = pygame.image.load('one.png')
twoImg = pygame.image.load('two.png')
threeImg = pygame.image.load('three.png')
fourImg = pygame.image.load('four.png')
fiveImg = pygame.image.load('five.png')
sixImg = pygame.image.load('six.png')
sevenImg = pygame.image.load('seven.png')
eightImg = pygame.image.load('eight.png')
nineImg = pygame.image.load('nine.png')
zeroImg = pygame.image.load('zero.png')
backspaceImg = pygame.image.load('backspace.png')
equalImg = pygame.image.load('equal.png')
powerImg = pygame.image.load('power.png')
leftparenImg = pygame.image.load('leftparen.png')
rightparenImg = pygame.image.load('rightparen.png')
sinImg = pygame.image.load('sin.png')
cosImg = pygame.image.load('cos.png')
tanImg = pygame.image.load('tan.png')
cscImg = pygame.image.load('csc.png')
secImg = pygame.image.load('sec.png')
cotImg = pygame.image.load('cot.png')
factImg = pygame.image.load('factorial.png')
ansImg = pygame.image.load('ans.png')
lnImg = pygame.image.load('ln.png')
eImg = pygame.image.load('e.png')
piImg = pygame.image.load('pi.png')

addImg = pygame.transform.scale(addImg, (50, 50))
subImg = pygame.transform.scale(subImg, (50, 50))
divImg = pygame.transform.scale(divImg, (50, 50))
multiImg = pygame.transform.scale(multiImg, (50, 50))
oneImg = pygame.transform.scale(oneImg, (50, 50))
twoImg = pygame.transform.scale(twoImg, (50, 50))
threeImg = pygame.transform.scale(threeImg, (50, 50))
fourImg = pygame.transform.scale(fourImg, (50, 50))
fiveImg = pygame.transform.scale(fiveImg, (50, 50))
sixImg = pygame.transform.scale(sixImg, (50, 50))
sevenImg = pygame.transform.scale(sevenImg, (50, 50))
eightImg = pygame.transform.scale(eightImg, (50, 50))
nineImg = pygame.transform.scale(nineImg, (50, 50))
zeroImg = pygame.transform.scale(zeroImg, (50, 50))
backspaceImg = pygame.transform.scale(backspaceImg, (50, 50))
equalImg = pygame.transform.scale(equalImg, (50, 50))
powerImg = pygame.transform.scale(powerImg, (50, 50))
leftparenImg = pygame.transform.scale(leftparenImg, (50, 50))
rightparenImg = pygame.transform.scale(rightparenImg, (50, 50))
sinImg = pygame.transform.scale(sinImg, (50, 50))
cosImg = pygame.transform.scale(cosImg, (50, 50))
tanImg = pygame.transform.scale(tanImg, (50, 50))
cscImg = pygame.transform.scale(cscImg, (50, 50))
secImg = pygame.transform.scale(secImg, (50, 50))
cotImg = pygame.transform.scale(cotImg, (50, 50))
lnImg = pygame.transform.scale(lnImg, (50, 50))
factImg = pygame.transform.scale(factImg, (50, 50))
eImg = pygame.transform.scale(eImg, (50, 50))
ansImg = pygame.transform.scale(ansImg, (50, 50))
piImg = pygame.transform.scale(piImg, (50, 50))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("pressstart2pregular", 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException('The word ' + word + ' is too long to fit in the rect passed.')
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

            # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        # if accumulated_height + font.size(line)[1] >= rect.height:
        #   raise TextRectException('Once word-wrapped, the text string was too tall to fit in the rect.')
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException('Invalid justification argument: ' + str(justification))
        accumulated_height += font.size(line)[1]

    return surface


def game_intro():
    doneintroing = False
    while not doneintroing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneintroing = True

        gameDisplay.fill(white)
        logo = pygame.image.load('SuperCalcioLogo.png')
        gameDisplay.blit(logo, (500, 200))
        '''
        font = pygame.font.SysFont("pressstart2pregular", 30)

        mouse = pygame.mouse.get_pos()
        #print(mouse)
        '''

        button("GO!", 350, 450, 100, 50, green, bright_green, game_loop)
        button("Help", 500, 450, 100, 50, bright_blue, blue, help_loop)
        button("Settings", 650, 450, 100, 50, yellow, bright_yellow, dino_loop)
        button("Quit", 800, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(10)


def help_loop():
    donehelping = False
    while not donehelping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                donehelping = True
        diswidth = 1250
        disheight = 600

        gameDisplay = pygame.display.set_mode((diswidth, disheight))
        gameDisplay.fill(white)
        # make a question mark logo
        boxhelp = pygame.image.load('qbox.png')
        gameDisplay.blit(boxhelp, (900, 230))

        font1 = pygame.font.SysFont("pressstart2pregular", 30)
        string1 = "Help:"
        text1 = font1.render(string1, True, (0, 0, 0))
        gameDisplay.blit(text1, (100, 30))

        font2 = pygame.font.SysFont("pressstart2pregular", 30)
        string2 = "Keyboard Input:"
        text2 = font2.render(string2, True, (0, 0, 0))
        gameDisplay.blit(text2, (100, 70))

        font3 = pygame.font.SysFont("pressstart2pregular", 30)
        string3 = "Left arrow key moves calcio left"
        text3 = font3.render(string3, True, (0, 0, 0))
        gameDisplay.blit(text3, (100, 100))

        font4 = pygame.font.SysFont("pressstart2pregular", 30)
        string4 = "Right arrow key moves calcio right"
        text4 = font4.render(string4, True, (0, 0, 0))
        gameDisplay.blit(text4, (100, 130))

        font5 = pygame.font.SysFont("pressstart2pregular", 30)
        string5 = "Up arrow key makes calcio jump"
        text5 = font5.render(string5, True, (0, 0, 0))
        gameDisplay.blit(text5, (100, 160))

        font6 = pygame.font.SysFont("pressstart2pregular", 30)
        string6 = "'s' key for sine"
        text6 = font6.render(string6, True, (0, 0, 0))
        gameDisplay.blit(text6, (100, 190))

        font7 = pygame.font.SysFont("pressstart2pregular", 30)
        string7 = "'c' key for cosine"
        text7 = font7.render(string7, True, (0, 0, 0))
        gameDisplay.blit(text7, (100, 220))

        font8 = pygame.font.SysFont("pressstart2pregular", 30)
        string8 = "'t' key for tangent"
        text8 = font8.render(string8, True, (0, 0, 0))
        gameDisplay.blit(text8, (100, 250))

        font9 = pygame.font.SysFont("pressstart2pregular", 30)
        string9 = "'0-9' keys for number input "
        text9 = font9.render(string9, True, (0, 0, 0))
        gameDisplay.blit(text9, (100, 280))

        font10 = pygame.font.SysFont("pressstart2pregular", 30)
        string10 = "'e' key number e"
        text10 = font10.render(string10, True, (0, 0, 0))
        gameDisplay.blit(text10, (100, 310))

        font11 = pygame.font.SysFont("pressstart2pregular", 30)
        string11 = "'ctrl + m' switches mode between radians and degrees"
        text11 = font11.render(string11, True, (0, 0, 0))
        gameDisplay.blit(text11, (100, 340))

        font12 = pygame.font.SysFont("pressstart2pregular", 30)
        string12 = "'.' key for decimal"
        text12 = font12.render(string12, True, (0, 0, 0))
        gameDisplay.blit(text12, (100, 370))

        font13 = pygame.font.SysFont("pressstart2pregular", 30)
        string13 = "'delete' key for clear"
        text13 = font13.render(string13, True, (0, 0, 0))
        gameDisplay.blit(text13, (100, 400))

        font14 = pygame.font.SysFont("pressstart2pregular", 30)
        string14 = "'+', '-', '/', '*' for mathematical operations"
        text14 = font14.render(string14, True, (0, 0, 0))
        gameDisplay.blit(text14, (100, 430))

        font15 = pygame.font.SysFont("pressstart2pregular", 30)
        string15 = "'enter' key for = "
        text15 = font15.render(string15, True, (0, 0, 0))
        gameDisplay.blit(text15, (100, 460))

        font16 = pygame.font.SysFont("pressstart2pregular", 30)
        string16 = "'shift + 9' for ( "
        text16 = font16.render(string16, True, (0, 0, 0))
        gameDisplay.blit(text16, (100, 490))

        font17 = pygame.font.SysFont("pressstart2pregular", 30)
        string17 = "'shift + 0' for ) "
        text17 = font17.render(string17, True, (0, 0, 0))
        gameDisplay.blit(text17, (100, 520))

        pygame.display.update()
        clock.tick(10)


def dino_loop():
    diswidth = 1250
    disheight = 600

    gameDisplay = pygame.display.set_mode((diswidth, disheight))
    gameDisplay.fill(white)

    my_font = pygame.font.SysFont("pressstart2pregular", 30)

    my_string = "Choose your calcio :) "
    my_rect = pygame.Rect((530, 190, 215, 30))
    rendered_text = render_textrect(my_string, my_font, my_rect, white, black, 0)
    donepicking = False

    if rendered_text:
        gameDisplay.blit(rendered_text, my_rect.topleft)

        while not donepicking:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    donepicking = True

            button("Menu", 1050, 100, 100, 50, red, bright_red, game_intro)

            button("Calcuigi!", 200, 450, 100, 50, green, bright_green, set_calcuigi)
            sprite1 = pygame.image.load("calcuigi.png")
            gameDisplay.blit(sprite1, (200, 300))

            button("SuperCalcio!", 550, 450, 200, 50, bright_blue, blue, set_supercal)
            sprite2 = pygame.image.load("supercalcio.png")
            gameDisplay.blit(sprite2, (600, 300))

            button("Calcio!", 1000, 450, 100, 50, yellow, bright_yellow, set_calcio)
            sprite1 = pygame.image.load("calcio.png")
            gameDisplay.blit(sprite1, (1000, 300))

            pygame.display.update()
            clock.tick(10)


def set_calcio():
    global calcioleft
    calcioleft = pygame.image.load('calcioleft.png')
    global calcioright
    calcioright = pygame.image.load('calcio.png')
    global dinomode
    dinomode = 0


def set_supercal():
    global calcioleft
    calcioleft = pygame.image.load('supercalcioleft.png')
    calcioleft = pygame.transform.scale(calcioleft, (55, 70))
    global calcioright
    calcioright = pygame.image.load('supercalcio.png')
    calcioright = pygame.transform.scale(calcioright, (55, 70))
    global dinomode
    dinomode = 2


def set_calcuigi():
    global calcioleft
    calcioleft = pygame.image.load('calcuigiR.png')
    calcioleft = pygame.transform.scale(calcioleft, (75, 70))
    global calcioright
    calcioright = pygame.image.load('calcuigi.png')
    calcioright = pygame.transform.scale(calcioright, (75, 70))
    global dinomode
    dinomode = 1


def quit_game():
    pygame.quit()


def game_loop():
    pygame.mixer.music.load('smbTheme.wav')
    pygame.mixer.music.queue('smbTheme.wav')
    pygame.mixer.music.play(-1)
    mode = False  # bool for switching between radians and degrees. False for radians, True for degrees
    enter_pressed = False  # if the ENTER key is pressed, enter_pressed = True

    def sin(x):
        if mode == True:
            x = math.radians(x)
        return math.sin(x)

    def cos(x):
        if mode == True:
            x = math.radians(x)
        return math.cos(x)

    def tan(x):
        if mode == True:
            x = math.radians(x)
        return math.tan(x)

    def csc(x):
        return 1 / (sin(x))

    def sec(x):
        return 1 / (cos(x))

    def cot(x):
        return 1 / (tan(x))

    def log(x):
        return math.log(x)

    def fact(x):
        return math.factorial(x)

    def calcio(x, y):
        gameDisplay.blit(supercalcio, (x, y))
        calcio_rect = supercalcio.get_rect(center=(x, y))
        return calcio_rect

    def p_display(p):  # for displaying input
        if (p == []):
            return ''
        if (len(p) > 1):
            if (p[-1] == 'e' and p[-2] == 'pi') or (p[-1] == 'pi' and p[-2] == 'e'):
                p[-1] = '*' + p[-1]
        return (str(p_display(p[:-1])) + str(p[-1]))

    def new_eq(calc):
        if calc != []:
            x = calc[-1]
            calc = [x]
        return calc

    # initializing variables
    calciowidth = 30
    isCollide = False
    newEQ = False
    dead = False
    calcDisplay = []
    calculation = []
    fact_var_stored = []
    level = 1  # keeps track of which screen is being displayed
    result = ''
    e = math.e
    pi = math.pi
    switch = False  # provides a delay in loading a rect in level 2
    high_score = '0000'

    jump_sound = pygame.mixer.Sound('smw_jump.wav')
    coin_sound = pygame.mixer.Sound('smw_coin.wav')

    x = (diswidth * 0.45)
    y = (disheight * 0.8)

    x_change = 0
    y_change = 0
    supercalcio = calcioright

    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                    supercalcio = calcioleft
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                    supercalcio = calcioright
                elif event.key == pygame.K_UP:
                    y_change = -15
                    jump_sound.play()
                    y += y_change
                elif event.key == pygame.K_DELETE:
                    calcDisplay = []
                    calculation = []
                elif event.key == pygame.K_BACKSPACE:
                    calcDisplay = calcDisplay[:-1]
                    calculation = calculation[:-1]
                elif event.key == pygame.K_LEFTPAREN:
                    if newEQ == True:
                        calcDisplay = []
                        calculation = []
                        newEQ = False
                    calcDisplay = calcDisplay + ['(']
                    calculation = calculation + ['(']
                elif event.key == pygame.K_RIGHTPAREN:
                    if newEQ == True:
                        calcDisplay = []
                        calculation = []
                        newEQ = False
                    calcDisplay = calcDisplay + [')']
                    calculation = calculation + [')']
                elif event.key == pygame.K_s:
                    if newEQ == True:
                        calcDisplay = []
                        calculation = []
                        newEQ = False
                    calcDisplay = calcDisplay + ['sin'] + ['(']
                    calculation = calculation + ['sin'] + ['(']
                elif event.key == pygame.K_c:
                    if newEQ == True:
                        calcDisplay = []
                        calculation = []
                        newEQ = False
                    calcDisplay = calcDisplay + ['cos'] + ['(']
                    calculation = calculation + ['cos'] + ['(']
                elif event.key == pygame.K_t:
                    if newEQ == True:
                        calcDisplay = []
                        calculation = []
                        newEQ = False
                    calcDisplay = calcDisplay + ['tan'] + ['(']
                    calculation = calculation + ['tan'] + ['(']
                    calcDisplay = calcDisplay + ['tan'] + ['(']
                    calculation = calculation + ['tan'] + ['(']
                elif event.key == pygame.K_a:
                    calculation = calculation + [result]
                    calcDisplay = calcDisplay + ['ans']
                elif event.key == pygame.K_p:
                    calcDisplay = calcDisplay + ['π']
                    calculation = calculation + ['pi']
                elif event.key == pygame.K_e:
                    calcDisplay = calcDisplay + ['e']
                    calculation = calculation + ['e']
                elif event.key == pygame.K_l:
                    calcDisplay = calcDisplay + ['ln'] + ['(']
                    calculation = calculation + ['log'] + ['(']
                elif event.key == pygame.K_m and pygame.KMOD_CTRL:
                    # switches mode from radians to degrees and back again
                    mode = not mode
                elif event.key == pygame.K_d and pygame.KMOD_CTRL:
                    if dinomode == 0:
                        set_calcuigi()
                    elif dinomode == 1:
                        set_supercal()
                    elif dinomode == 2:
                        set_calcio()
                elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    if event.type == pygame.KEYDOWN:
                        if event.unicode == ")":
                            if newEQ == True:
                                calcDisplay = []
                                calculation = []
                                newEQ = False
                            calcDisplay = calcDisplay + [')']
                            calculation = calculation + [')']
                        else:
                            if newEQ:
                                calcDisplay = []
                                calculation = []
                            calcDisplay = calcDisplay + ['0']
                            calculation = calculation + ['0']
                            newEQ = False
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    if newEQ:
                        calcDisplay = []
                        calculation = []
                    calcDisplay = calcDisplay + ['1']
                    calculation = calculation + ['1']
                    newEQ = False
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    if newEQ:
                        calcDisplay = []
                        calculation = []
                    calcDisplay = calcDisplay + ['2']
                    calculation = calculation + ['2']
                    newEQ = False
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    if newEQ:
                        calcDisplay = []
                        calculation = []
                    calcDisplay = calcDisplay + ['3']
                    calculation = calculation + ['3']
                    newEQ = False
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    if newEQ:
                        calcDisplay = []
                        calculation = []
                    calcDisplay = calcDisplay + ['4']
                    calculation = calculation + ['4']
                    newEQ = False
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    if newEQ:
                        calcDisplay = []
                        calculation = []
                    calcDisplay = calcDisplay + ['5']
                    calculation = calculation + ['5']
                    newEQ = False
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    if event.type == pygame.KEYDOWN:
                        if event.unicode == "^":
                            if newEQ == True:
                                calcDisplay = new_eq(calcDisplay)
                                calculation = new_eq(calculation)
                                newEQ = False
                            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-'
                                    and calcDisplay[-1] != '*' and calcDisplay[-1] != '/'):
                                calcDisplay = calcDisplay + ['^']
                                calculation = calculation + ['**']
                        else:
                            if newEQ:
                                calcDisplay = []
                                calculation = []
                            calcDisplay = calcDisplay + ['6']
                            calculation = calculation + ['6']
                            newEQ = False
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    if newEQ:
                        calcDisplay = []
                        calculation = []
                    calcDisplay = calcDisplay + ['7']
                    calculation = calculation + ['7']
                    newEQ = False
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    if event.type == pygame.KEYDOWN:
                        if event.unicode == "*":
                            if newEQ == True:
                                calcDisplay = new_eq(calcDisplay)
                                calculation = new_eq(calculation)
                                newEQ = False
                            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-'
                                    and calcDisplay[-1] != '*' and calcDisplay[-1] != '/'):
                                calcDisplay = calcDisplay + ['*']
                                calculation = calculation + ['*']
                        else:
                            if newEQ:
                                calcDisplay = []
                                calculation = []
                            calcDisplay = calcDisplay + ['8']
                            calculation = calculation + ['8']
                            newEQ = False
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    if event.type == pygame.KEYDOWN:
                        if event.unicode == "(":
                            if newEQ == True:
                                calcDisplay = []
                                calculation = []
                                newEQ = False
                            calcDisplay = calcDisplay + ['(']
                            calculation = calculation + ['(']
                        else:
                            if newEQ:
                                calcDisplay = []
                                calculation = []
                            calcDisplay = calcDisplay + ['9']
                            calculation = calculation + ['9']
                            newEQ = False
                elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                    if newEQ == True:
                        calcDisplay = []
                        calculation = []
                        newEQ = False
                    calcDisplay = calcDisplay + ['.']
                    calculation = calculation + ['.']
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    enter_pressed = True
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    if newEQ == True:
                        calcDisplay = new_eq(calcDisplay)
                        calculation = new_eq(calculation)
                        newEQ = False
                    if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' \
                            and calcDisplay[-1] != '*' and calcDisplay[-1] != '/'):
                        calcDisplay = calcDisplay + ['-']
                        calculation = calculation + ['-']
                elif event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE:
                    if newEQ == True:
                        calcDisplay = new_eq(calcDisplay)
                        calculation = new_eq(calculation)
                        newEQ = False
                    if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' \
                            and calcDisplay[-1] != '*' and calcDisplay[-1] != '/'):
                        calcDisplay = calcDisplay + ['/']
                        calculation = calculation + ['/']
                elif event.key == pygame.K_KP_MULTIPLY:
                    if newEQ == True:
                        calcDisplay = new_eq(calcDisplay)
                        calculation = new_eq(calculation)
                        newEQ = False
                    if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' \
                            and calcDisplay[-1] != '*' and calcDisplay[-1] != '/'):
                        calcDisplay = calcDisplay + ['*']
                        calculation = calculation + ['*']
                elif event.type == pygame.KEYDOWN or event.key == pygame.K_KP_PLUS:
                    if event.unicode == "+":
                        if newEQ == True:
                            calcDisplay = new_eq(calcDisplay)
                            calculation = new_eq(calculation)
                            newEQ = False
                        if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' \
                                and calcDisplay[-1] != '*' and calcDisplay[-1] != '/'):
                            calcDisplay = calcDisplay + ['+']
                            calculation = calculation + ['+']
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if x < diswidth - calciowidth and x > 0:
            x += x_change
        elif x >= diswidth - calciowidth:
            x = x - 1
        elif x <= 0:
            x = x + 1

        if y < disheight * 0.8:
            y += y_change
        if y_change < 15:
            y_change += 1

        if level == 1:
            background = background1
        if level == 2:
            background = background2

        gameDisplay.blit(background, (0, 0))

        gameDisplay.blit(equalImg, (1120, 320))
        gameDisplay.blit(backspaceImg, (1200, 320))
        rect_equal = equalImg.get_rect(center=(1120, 320))
        rect_bkspace = backspaceImg.get_rect(center=(1200, 320))

        if level == 1:
            gameDisplay.blit(oneImg, (1, 320))
            gameDisplay.blit(twoImg, (80, 320))
            gameDisplay.blit(threeImg, (160, 320))
            gameDisplay.blit(fourImg, (240, 320))
            gameDisplay.blit(fiveImg, (320, 320))
            gameDisplay.blit(sixImg, (400, 320))
            gameDisplay.blit(sevenImg, (480, 320))
            gameDisplay.blit(eightImg, (560, 320))
            gameDisplay.blit(nineImg, (640, 320))
            gameDisplay.blit(zeroImg, (720, 320))

            rect1 = oneImg.get_rect(center=(1, 320))
            rect2 = twoImg.get_rect(center=(80, 320))
            rect3 = threeImg.get_rect(center=(160, 320))
            rect4 = fourImg.get_rect(center=(240, 320))
            rect5 = fiveImg.get_rect(center=(320, 320))
            rect6 = sixImg.get_rect(center=(400, 320))
            rect7 = sevenImg.get_rect(center=(480, 320))
            rect8 = eightImg.get_rect(center=(560, 320))
            rect9 = nineImg.get_rect(center=(640, 320))
            rect0 = zeroImg.get_rect(center=(720, 320))

            gameDisplay.blit(addImg, (800, 320))
            gameDisplay.blit(subImg, (880, 320))
            gameDisplay.blit(multiImg, (960, 320))
            gameDisplay.blit(divImg, (1040, 320))

            rect_add = addImg.get_rect(center=(800, 320))
            rect_sub = subImg.get_rect(center=(880, 320))
            rect_multi = multiImg.get_rect(center=(960, 320))
            rect_div = divImg.get_rect(center=(1040, 320))

            # initializes and then "zeroes out" the unused rects for level 1
            rect_lparen = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_rparen = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_sin = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_cos = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_tan = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_csc = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_sec = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_cot = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_e = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_power = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_fact = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_ln = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_pi = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_ans = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)

            switch = False
            levelrect = pygame.draw.rect(gameDisplay, (0, 0, 0), (1249, 1, 1, 600), 2)

        if level == 2:
            if x >= 75:
                switch = True

            gameDisplay.blit(eImg, (1, 320))
            gameDisplay.blit(piImg, (80, 320))
            gameDisplay.blit(factImg, (160, 320))
            gameDisplay.blit(powerImg, (240, 320))
            gameDisplay.blit(lnImg, (320, 320))
            gameDisplay.blit(sinImg, (400, 320))
            gameDisplay.blit(cosImg, (480, 320))
            gameDisplay.blit(tanImg, (560, 320))
            gameDisplay.blit(cscImg, (640, 320))
            gameDisplay.blit(secImg, (720, 320))
            gameDisplay.blit(cotImg, (800, 320))
            gameDisplay.blit(ansImg, (880, 320))
            gameDisplay.blit(leftparenImg, (960, 320))
            gameDisplay.blit(rightparenImg, (1040, 320))

            rect_e = eImg.get_rect(center=(1, 320))
            rect_pi = piImg.get_rect(center=(80, 320))
            rect_fact = factImg.get_rect(center=(160, 320))
            rect_power = powerImg.get_rect(center=(240, 320))
            rect_ln = lnImg.get_rect(center=(320, 320))
            rect_sin = sinImg.get_rect(center=(400, 320))
            rect_cos = cosImg.get_rect(center=(480, 320))
            rect_tan = tanImg.get_rect(center=(560, 320))
            rect_csc = cscImg.get_rect(center=(640, 320))
            rect_sec = secImg.get_rect(center=(720, 320))
            rect_cot = cotImg.get_rect(center=(800, 320))
            rect_ans = ansImg.get_rect(center=(880, 320))
            rect_lparen = leftparenImg.get_rect(center=(960, 320))
            rect_rparen = rightparenImg.get_rect(center=(1040, 320))

            # "zeroes out" unused rects in level 2
            rect_0 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_1 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_2 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_3 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_4 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_5 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_6 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_7 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_8 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_9 = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_add = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_sub = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_div = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)
            rect_multi = pygame.draw.rect(gameDisplay, (0, 0, 0), (0, 0, 0, 0), 0)

            if switch:
                levelrect = pygame.draw.rect(gameDisplay, (0, 0, 0), (-1, 1, 1, 600), 2)

        calcio_rectangle = calcio(x, y)

        if calcio_rectangle.colliderect(rect_add):
            if newEQ == True:
                calcDisplay = new_eq(calcDisplay)
                calculation = new_eq(calculation)
                newEQ = False
            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' and calcDisplay[-1] != '*' and
                calcDisplay[-1] != '/') and isCollide == False:
                calcDisplay = calcDisplay + ['+']
                calculation = calculation + ['+']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_sub):
            if newEQ == True:
                calcDisplay = new_eq(calcDisplay)
                calculation = new_eq(calculation)
                newEQ = False
            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' and calcDisplay[-1] != '*' and
                calcDisplay[-1] != '/') and isCollide == False:
                calcDisplay = calcDisplay + ['-']
                calculation = calculation + ['-']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_multi):
            if newEQ == True:
                calcDisplay = new_eq(calcDisplay)
                calculation = new_eq(calculation)
                newEQ = False
            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' and calcDisplay[-1] != '*' and
                calcDisplay[-1] != '/') and isCollide == False:
                calcDisplay = calcDisplay + ['*']
                calculation = calculation + ['*']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_div):
            if newEQ == True:
                calcDisplay = new_eq(calcDisplay)
                calculation = new_eq(calculation)
                newEQ = False
            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' and calcDisplay[-1] != '*' and
                calcDisplay[-1] != '/') and isCollide == False:
                calcDisplay = calcDisplay + ['/']
                calculation = calculation + ['/']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_power):
            if newEQ == True:
                calcDisplay = new_eq(calcDisplay)
                calculation = new_eq(calculation)
                newEQ = False
            if (calcDisplay != [] and calcDisplay[-1] != '+' and calcDisplay[-1] != '-' and calcDisplay[-1] != '*' and
                calcDisplay[-1] != '/') and isCollide == False:
                calcDisplay = calcDisplay + ['^']
                calculation = calculation + ['**']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_lparen):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['(']
                calculation = calculation + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_rparen):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + [')']
                calculation = calculation + [')']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_sin):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['sin'] + ['(']
                calculation = calculation + ['sin'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_cos):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['cos'] + ['(']
                calculation = calculation + ['cos'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_tan):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['tan'] + ['(']
                calculation = calculation + ['tan'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_csc):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['csc'] + ['(']
                calculation = calculation + ['csc'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_sec):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['sec'] + ['(']
                calculation = calculation + ['sec'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_cot):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['cot'] + ['(']
                calculation = calculation + ['cot'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_ln):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['ln'] + ['(']
                calculation = calculation + ['log'] + ['(']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_fact):
            if newEQ == True:
                calcDisplay = new_eq(calcDisplay)
                calculation = new_eq(calculation)
                newEQ = False
            if isCollide == False:
                fact_var = calcDisplay[-1]
                i = 1
                if calcDisplay[-1] == ')':
                    i = 2
                    while i < len(calcDisplay) and calcDisplay[-i] != '(':
                        i = i + 1
                    while i >= 1:
                        fact_var_stored = fact_var_stored + [calcDisplay[-i]]
                        i = i - 1
                    f_ans = p_display(fact_var_stored)
                    fact_var = eval(f_ans)
                    fact_var_stored = []
                calcDisplay = calcDisplay + ['!']
                t = len(calculation) - i
                calculation = calculation[1:1:t + 1] + ['fact'] + ['('] + [fact_var] + [')']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_e):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['e']
                calculation = calculation + ['e']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_pi):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calcDisplay = calcDisplay + ['π']
                calculation = calculation + ['pi']
            isCollide = True
        elif calcio_rectangle.colliderect(rect1):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [1]
                calcDisplay = calcDisplay + [1]
            isCollide = True
        elif calcio_rectangle.colliderect(rect2):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [2]
                calcDisplay = calcDisplay + [2]
            isCollide = True
        elif calcio_rectangle.colliderect(rect3):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [3]
                calcDisplay = calcDisplay + [3]
            isCollide = True
        elif calcio_rectangle.colliderect(rect4):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [4]
                calcDisplay = calcDisplay + [4]
            isCollide = True
        elif calcio_rectangle.colliderect(rect5):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [5]
                calcDisplay = calcDisplay + [5]
            isCollide = True
        elif calcio_rectangle.colliderect(rect6):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [6]
                calcDisplay = calcDisplay + [6]
            isCollide = True
        elif calcio_rectangle.colliderect(rect7):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [7]
                calcDisplay = calcDisplay + [7]
            isCollide = True
        elif calcio_rectangle.colliderect(rect8):
            if newEQ == True:
                calcDisplay = []
                calculation = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [8]
                calcDisplay = calcDisplay + [8]
            isCollide = True
        elif calcio_rectangle.colliderect(rect9):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [9]
                calcDisplay = calcDisplay + [9]
            isCollide = True
        elif calcio_rectangle.colliderect(rect0):
            if newEQ == True:
                calculation = []
                calcDisplay = []
                newEQ = False
            if isCollide == False:
                calculation = calculation + [0]
                calcDisplay = calcDisplay + [0]
            isCollide = True
        elif calcio_rectangle.colliderect(rect_bkspace):
            if isCollide == False:
                calculation = calculation[:-1]
                calcDisplay = calcDisplay[:-1]
            isCollide = True
        elif calcio_rectangle.colliderect(rect_ans):
            if isCollide == False:
                calculation = calculation + [result]
                calcDisplay = calcDisplay + ['ans']
            isCollide = True
        elif calcio_rectangle.colliderect(rect_equal) or enter_pressed:
            if isCollide == False:
                try:
                    answer = p_display(calculation)
                    result = eval(answer)
                    if result > float(high_score):
                        high_score = result
                    calcDisplay = calcDisplay + ['='] + [result]
                    calculation = calculation + ['='] + [result]
                except ZeroDivisionError:
                    calcDisplay = ['These maths are forbidden']
                except SyntaxError:
                    calcDisplay = ['Invalid expression']
                except ValueError:
                    calcDisplay = ['Domain error']
                newEQ = True
            isCollide = True
            enter_pressed = False

        # Allows for only hitting the block once on each jump
        if (isCollide == True):
            coin_sound.play()
            y_change = 8
            isCollide = False

        calcio(x, y)

        font = pygame.font.SysFont("pressstart2pregular", 30)
        current_calc = p_display(calcDisplay)
        text = font.render(current_calc, True, (0, 0, 0))
        gameDisplay.blit(text, (400, 100))

        high = p_display(['High Score: ' + str(high_score)])
        score = font.render(high, True, (0, 0, 0))
        gameDisplay.blit(score, (10, 10))

        degDisplay = font.render("Degrees", True, (0, 0, 0))
        radDisplay = font.render("Radians", True, (0, 0, 0))

        if mode == True:
            gameDisplay.blit(degDisplay, (1130, 5))
        else:
            gameDisplay.blit(radDisplay, (1130, 5))

        # moves calcio to appropriate starting position for each level
        if calcio_rectangle.colliderect(levelrect):
            if level == 1:
                level = 2
                x = 30
            elif level == 2:
                level = 1
                x = 1100
        pygame.display.update()
        clock.tick(60)


# main

game_intro()
# game_loop()
pygame.quit()
# quit()
