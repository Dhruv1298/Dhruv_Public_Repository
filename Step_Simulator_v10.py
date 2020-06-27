import pygame

maze = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

]

exploration = [
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
    ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],

]

global maze_wall
maze_wall = [

    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
    ['e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!','e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e', '!', 'e',],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',],
]

# Defining few variables
global constant
global k
constant = 37.5
k = 10
executed = False
orientation = ''
last_row = 300
last_col = 300
last_orientation = ''
steps_right = 0
steps_left = 0
w2 = 0
h2 = 0
turn_constant = 0
turning = ''

t_col = int(input('Enter the target column : '))
t_row = int(input('Enter the target row : '))
col = int(input('Enter the starting column : '))
row = int(input('Enter the starting row : '))
next_col = col
next_row = row
pi = 3.14159265359
step_angle = float(input('Please enter the necessary step angle : '))
wheel_size = float(input('Please enter the required Diameter(cm) :  '))
dist_btwn_wheels = float(input('Please enter the width of the robot(cm) :  '))
turn_type = int(input('Please enter 1 for Single Motor or 2 for Double Motor :  '))
current_distance = 0
turning_space = (18-dist_btwn_wheels)/2
total_distance = 0
total_steps_right = 0
Single_Motor = False
Single_Motor_Space = 18 - ((18-dist_btwn_wheels)/2)
Single_Motor_Pixels = ((constant*Single_Motor_Space)/18)
total_steps_left = 0
right_wheel_direction = ''
left_wheel_direction = ''
undo = False
circumference = pi * wheel_size

# Initializing pygame and the font
pygame.init()
pygame.font.init()
# Creating the screen
screen = pygame.display.set_mode((1270, 650))

# Setting the caption and the font for the pygame window
pygame.display.set_caption("Navigator Grid")
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 15)

# The click detect function allows the user to enter the walls accordingly into the maze
def click_detect():
    # Infinite Loop
    running = True
    pressed = False
    save = False
    fill()
    while running:

        check_b = True
        check_l = True
        check_r = True
        check_t = True

        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                if event.key == pygame.K_s:
                    save = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                (x, y) = pygame.mouse.get_pos()
                # Recognises which cell the mouse pointer is in
                x_dist = x % 37.5
                y_dist = y % 37.5
                x_wall = x - x_dist
                y_wall = y - y_dist
                x_wall = int((x_wall / 37.5) * 2)
                y_wall = int((y_wall / 37.5) * 2)

                if y_wall < 32 and x_wall < 32 :

                    if x_wall == 0:
                        check_l = False

                    if y_wall == 0:
                        check_t = False

                    if y_wall == 31:
                        check_b = False

                    if check_l == True and x_dist < 7:
                        if maze_wall[y_wall][x_wall - 1] == 'w':
                            maze_wall[y_wall][x_wall - 1] = 'e'
                        else:
                            maze_wall[y_wall][x_wall - 1] = 'w'


                    elif x_dist > 45:
                        if maze_wall[y_wall][x_wall + 1] == 'w':
                            maze_wall[y_wall][x_wall + 1] = 'e'
                        else:
                            maze_wall[y_wall][x_wall + 1] = 'w'

                    elif check_t == True and y_dist < 25:
                        if maze_wall[y_wall - 1][x_wall] == 'e':
                            maze_wall[y_wall - 1][x_wall] = 'w'
                        else:
                            maze_wall[y_wall - 1][x_wall] = 'w'

                    elif check_b == True and y_dist > 32:
                        if maze_wall[y_wall + 1][x_wall] == 'w':
                            maze_wall[y_wall + 1][x_wall] = 'e'
                        else:
                            maze_wall[y_wall + 1][x_wall] = 'w'

        for x in range(17):
            pygame.draw.line(screen, (250,102,0), (37.5 * x, 0), (37.5 * x, 600))
        for x in range(17):
            pygame.draw.line(screen, (250,102,0), (0, 37.5 * x), (600, 37.5 * x))
        wall_detect()
        image = pygame.image.load('Step Simulator Image.png')
        image = pygame.transform.scale(image, (670, 600))
        screen.blit(image, (600, 0))
        pressed = False
        write(0, 610, 'Enter Walls by clicking on the Grid Lines , Once done click enter',(86,49,132))
        pygame.display.update()

def write(x, y, val,color):
    num = font.render(val, True, color)
    screen.blit(num, (x, y))

def write2(x, y, val,color):
    num = font2.render(val, True, color)
    screen.blit(num, (x, y))

def explored():
    exploration[row][col] = 'e'

def draw(color):
    for b in range(16):
        for a in range(16):
            if exploration[a][b] == 'e':
                pygame.draw.rect(screen,color,[(b*constant) + 4,(a*constant) + 4,constant - 6,constant - 6])

def wall_detect():
    for wall_y in range(31):
        for wall_x in range(31):
            if maze_wall[wall_x][wall_y] == 'w':
                check_b = True
                check_l = True
                check_r = True
                check_t = True
                if wall_y == 0:
                    check_l = False

                if wall_x == 0:
                    check_t = False

                # If there is a cell surrounding the wall on the left, then draw a rectangle which is vertical
                if check_l == True and maze_wall[wall_x][wall_y - 1] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y + 1) / 2 * constant - 2, (wall_x) / 2 * constant, 4, 39])

                # If there is a cell surrounding the wall on the top, then draw a rectangle which is horizontal
                if check_t == True and maze_wall[wall_x - 1][wall_y] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y) / 2 * constant, (wall_x + 1) / 2 * constant - 2, 39, 4])


def rotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] + min_box[0] - pivot_move[0], pos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)


def step():
    global steps_left
    global steps_right
    global step_angle
    global last_orientation
    global total_distance
    global orientation
    global step_angle
    global total_steps_left
    global total_steps_right
    global dist_btwn_wheels
    global wheel_size
    global turning
    global turn_type
    global current_distance
    global right_wheel_direction
    global left_wheel_direction
    global undo
    global circumference
    global Single_Motor
    global Single_Motor_Space
    global Single_Motor_Pixels
    if Single_Motor == True:
        steps_left = 36 - Single_Motor_Space
        steps_right = 36 - Single_Motor_Space
        right_wheel_direction = 'forward'
        left_wheel_direction = 'forward'
        Single_Motor = False
    elif turning == '':
        current_distance = 18
        steps_right = (current_distance/circumference)*(360/step_angle)
        steps_left = (current_distance / circumference) * (360 / step_angle)
        left_wheel_direction = 'forward'
        right_wheel_direction = 'forward'
    elif turn_type == 2:
        undo = True
        right_wheel_direction = 'backward'
        left_wheel_direction = 'forward'
        steps_right = (pi * (dist_btwn_wheels)) / 4
        steps_left = (pi * (dist_btwn_wheels)) / 4
        if turning == 'right':
            pass
        if turning == 'left':
            left_wheel_direction = 'backward'
            right_wheel_direction = 'forward'
        if turning == 'u_turn':
            steps_left *= 2
            steps_right *= 2
    elif turn_type == 1:
        undo = True
        right_wheel_direction = '--'
        left_wheel_direction = '--'
        steps_left = (pi*dist_btwn_wheels*2)/4
        steps_right = (pi*dist_btwn_wheels*2)/4
        if turning == 'right':
            Single_Motor = True
            left_wheel_direction = 'forward'
            steps_right = 0
        if turning == 'left':
            Single_Motor = True
            right_wheel_direction = 'forward'
            steps_left = 0
        if turning == 'u_turn':
            right_wheel_direction = 'backward'
            left_wheel_direction = 'forward'
            steps_right = (pi * (dist_btwn_wheels)) / 2
            steps_left = (pi * (dist_btwn_wheels)) / 2
    total_steps_right += steps_right
    total_steps_left += steps_left



def moved():
    global row
    global col
    global last_row
    global last_col
    global orientation
    global last_orientation
    if last_col != 300:
        last_orientation = orientation

        if last_col - 1 == col :
            orientation = 'left'
        if last_col + 1 == col :
            orientation = 'right'
        if last_row - 1 == row :
            orientation = 'top'
        if last_row + 1 == row :
            orientation = 'bottom'
    else:
        orientation = 'top'

def show_num(x, y, val):
    num = font.render(val, True, (0, 0, 0))
    screen.blit(num, (x, y))

def fill():
    check_t = True
    check_r = True
    check_b = True
    check_l = True
    c = 0
    enter = True
    while enter:
        enter = False
        # Checking all the cells in the maze
        for b in range(16):
            for a in range(16):
                if maze[a][b] == c:
                    enter = True
                    check_b = True
                    check_l = True
                    check_r = True
                    check_t = True
                    # Checking whether there is a wall between the cell and its adjecent cells
                    if b == 0 or maze_wall[a * 2][(b * 2) - 1] == 'w':
                        check_l = False

                    if b == 15 or maze_wall[a * 2][(b * 2) + 1] == 'w':
                        check_r = False

                    if a == 0 or maze_wall[(a * 2) - 1][b * 2] == 'w':
                        check_t = False

                    if a == 15 or maze_wall[(a * 2) + 1][b * 2] == 'w':
                        check_b = False

                    # If there is no wall and the cell does not have a number then it assigns the cell with a value of c+1
                    if check_l == True and maze[a][b - 1] == 'e':
                        maze[a][b - 1] = c + 1

                    if check_r == True and maze[a][b + 1] == 'e':
                        maze[a][b + 1] = c + 1

                    if check_t == True and maze[a - 1][b] == 'e':
                        maze[a - 1][b] = c + 1

                    if check_b == True and maze[a + 1][b] == 'e':
                        maze[a + 1][b] = c + 1
        # C is incremented by one so when it finishes all the cells with a value of c, it moves on to the next number that is c+1
        c += 1

def num_detect():
    for y in range(16):
        for x in range(16):
            d = maze[x][y]
            show_num(y * constant + k, x * constant + k, str(d))

def to_turn():
    global last_orientation
    global orientation
    global turning
    global h2
    global w2
    global turn_constant
    if last_orientation == orientation:
        turning = ''
    elif last_orientation == 'top':
        if orientation == 'right':
            turning = 'right'
            w2 = 1
            h2 = 1
            turn_constant = 1
        elif orientation == 'left':
            turning = 'left'
            w2 = 0
            h2 = 1
            turn_constant = -1
        elif orientation == 'bottom':
            turning = 'u_turn'
    elif last_orientation == 'left':
        if orientation == 'top':
            turning = 'right'
            w2 = 1
            h2 = 0
            turn_constant = -1
        elif orientation == 'bottom':
            turning = 'left'
            w2 = 1
            h2 = 1
            turn_constant = 1
        elif orientation == 'right':
            turning = 'u_turn'
    elif last_orientation == 'bottom':
        if orientation == 'left':
            turning = 'right'
            w2 = 0
            h2 = 0
            turn_constant = -1
        elif orientation == 'top':
            turning = 'u_turn'
        elif orientation == 'right':
            turning = 'left'
            w2 = 1
            h2 = 0
            turn_constant = -1
    elif last_orientation == 'right':
        if orientation == 'top':
            turning = 'left'
            w2 = 0
            h2 = 0
            turn_constant = 1
        elif orientation == 'bottom':
            turning = 'right'
            w2 = 0
            h2 = 1
            turn_constant = 1
        elif orientation == 'left':
            turning = 'u_turn'


def path_finder():
    global row
    global col
    global orientation
    global last_col
    global last_row
    global total_distance
    global undo
    global Single_Motor_Pixels
    close = False
    running = True
    # Defining few variables
    executed = False
    while maze[row][col] != 0 and not close:

        angle = 0
        movement = 0
        last_undo = undo
        if executed:

            last_col = col
            last_row = row
            undo = False
            check_b = True
            check_l = True
            check_r = True
            check_t = True
            # Checking whether there is a wall between the adjecent cells
            if col == 0 or maze_wall[row * 2][col * 2 - 1] == 'w':
                check_l = False

            if col == 15 or maze_wall[row * 2][col * 2 + 1] == 'w':
                check_r = False

            if row == 0 or maze_wall[row * 2 - 1][col * 2] == 'w':
                check_t = False

            if row == 15 or maze_wall[row * 2 + 1][col * 2] == 'w':
                check_b = False

            # if there is no wall and the value of the adjecent cell is less than that of the current cell then the bot moves to that cell
            if check_l == True and maze[row][col - 1] < maze[row][col]:
                col -= 1

            elif check_r == True and maze[row][col + 1] < maze[row][col]:
                col += 1

            elif check_t == True and maze[row - 1][col] < maze[row][col]:
                row -= 1

            elif check_b == True and maze[row + 1][col] < maze[row][col]:
                row += 1


        moved()
        to_turn()
        if executed:
            Last_Single_Motor = Single_Motor
            step()
        if undo:
            row = last_row
            col = last_col
        elif not undo:
            total_distance += 18

        angle_right = 0
        angle_left = 0
        while running:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    explored()
                    running = False
                if event.type == pygame.QUIT:
                    running = False
                    close = True
            if angle_right > int(steps_right*step_angle*-1):
                angle_right -= 1
            if angle_left > int(steps_left*step_angle*-1):
                angle_left -= 1

            if angle > -90:
                angle -= 1
            else:
                explored()
            screen.fill((255, 255, 255))
            if movement < constant:
                movement += 1
            else:
                explored()
            # Creating the Grid
            for x in range(17):
                pygame.draw.line(screen, (250,102,0), (37.5 * x, 0), (37.5 * x, 600))
            for x in range(17):
                pygame.draw.line(screen, (250,102,0), (0, 37.5 * x), (600, 37.5 * x))

            if last_orientation == 'top':
                robot = pygame.image.load('Robot1.png')
            elif last_orientation == 'right':
                robot = pygame.image.load('Robot2.png')
            elif last_orientation == 'bottom':
                robot = pygame.image.load('Robot3.png')
            elif last_orientation == 'left':
                robot = pygame.image.load('Robot4.png')
            else:
                robot = pygame.image.load('Robot1.png')
            robot = pygame.transform.scale(robot, (38, 38))
            width ,height = robot.get_size()

            draw((255, 255, 0))

            if Single_Motor == True:
                rotate(screen,robot,((col * constant), (row * constant)),(width*w2,height*h2),angle*turn_constant)
            elif turning != '':
                rotate(screen,robot,((col * constant), (row * constant)),(width/2,height/2),angle*turn_constant)
            else:
                if orientation == 'top' and last_row > 0 and last_undo == False:
                    screen.blit(robot, ((last_col * constant), (last_row * constant) - movement))
                elif orientation == 'left' and last_col > 0 and last_undo == False:
                    screen.blit(robot, ((last_col * constant) - movement, (last_row * constant)))
                elif orientation == 'right' and last_col < 15 and last_undo == False:
                    screen.blit(robot, ((last_col * constant) + movement, (last_row * constant)))
                elif orientation == 'bottom' and last_row < 15 and last_undo == False:
                    screen.blit(robot, ((last_col * constant), (last_row * constant) + movement))
                elif last_undo == True and Last_Single_Motor == True:
                    screen.blit(robot, (col * constant, row * constant))
                elif last_undo == True :
                    if orientation == 'top' and last_row > 0 :
                        screen.blit(robot, ((last_col * constant), (last_row * constant) - movement))
                    elif orientation == 'left' and last_col > 0 :
                        screen.blit(robot, ((last_col * constant) - movement, (last_row * constant)))
                    elif orientation == 'right' and last_col < 15 :
                        screen.blit(robot, ((last_col * constant) + movement, (last_row * constant)))
                    elif orientation == 'bottom' and last_row < 15 :
                        screen.blit(robot, ((last_col * constant), (last_row * constant) + movement))
                else:
                    screen.blit(robot, (last_col * constant, last_row * constant))
            image = pygame.image.load('Step Simulator Image.png')
            image = pygame.transform.scale(image,(670,600))
            screen.blit(image,(600,0))
            write(1110,225,left_wheel_direction,(255,255,255))
            write(1110, 500, right_wheel_direction, (255, 255, 255))
            write(1110, 395, str(round(steps_right,2)), (255, 255, 255))
            write(1110, 120, str(round(steps_left, 2)), (255, 255, 255))
            write(620, 225, str(step_angle), (255, 255, 255))
            write(620, 135, str(wheel_size), (255, 255, 255))
            write(620, 322, str(dist_btwn_wheels), (255, 255, 255))
            write2(620, 422, str(round(total_steps_right,1)), (255, 255, 255))
            write2(690, 422, str(round(total_steps_left, 1)), (255, 255, 255))
            write2(620, 522, str(round(((total_steps_right*(step_angle/360))*circumference),2)), (255, 255, 255))
            write2(700, 522, str(round(((total_steps_left * (step_angle / 360)) * circumference), 2)), (255, 255, 255))
            write(1110, 450, str(round(((steps_right*(step_angle/360))*circumference),2)), (255, 255, 255))
            write(1110, 175, str(round(((steps_left * (step_angle / 360)) * circumference), 2)), (255, 255, 255))
            wheel = pygame.image.load('wheel.png')
            wheel = pygame.transform.scale(wheel,(130,130))
            w,h = wheel.get_size()
            rotate(screen,wheel,(826,390),(w/2,h/2),angle_right)
            rotate(screen, wheel, (826, 120), (w / 2, h / 2), angle_left)

            write(0, 610, 'Press any key to show the path of the robot', (86,49,132))
            wall_detect()

            pygame.display.update()

        running = True
        executed = True


click_detect()
maze[t_row][t_col] = 0
fill()
path_finder()
