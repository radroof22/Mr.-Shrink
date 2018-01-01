#Setup Code
import sys, pygame, time
from pygame.locals import *
#init
pygame.init()
bubbles = pygame.mixer.Sound("bubbles.wav")
punch = pygame.mixer.Sound("punch.wav")
pygame.mixer.music.load("theEntertainer.mp3")

#variables
pause = False 


pygame.init()

clock = pygame.time.Clock()                                                                                                                                                                                                                                                               

WIN_WIDTH = 800
WIN_HEIGHT = 600
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

dim = [300,-1625]
dim_orig = [300,-1625]

#init
flag = pygame.image.load("winning_flag.png")
pygame.display.set_caption('Hopper')

#variables and lists

rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
rects_orig = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

GAME = 1

#Colors
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
pink = (255,51,153)
aqua = (0,255,255)
yellow = (255,255,0)
bright_yellow = (200,200,0)
bright_green = (0,200,0)
bright_blue = (0,0,200)

#vars
obstacles = []
LIVES = 5

def button(msg, x, y, w, h, a, i, action = None):
	mouse = pygame.mouse.get_pos()
	
	click = pygame.mouse.get_pressed()
	
	
	
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, a, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
			
	
	else:
	
		pygame.draw.rect(gameDisplay, i, (x, y, w, h))

	
	smallText = pygame.font.SysFont('comicsansms', 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( x+(w/2), (y + (h/2)) )
	gameDisplay.blit(textSurf, textRect)

def game_intro():
	get_obstacles(rectangles)

	intro = True
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		gameDisplay.fill(white)
		largeText = pygame.font.SysFont("comicsansms", 115)
		TextSurf, TextRect = text_objects('Hopper', largeText)
		TextRect.center = ((display_width / 2),(display_height / 2) )
		gameDisplay.blit(TextSurf, TextRect)
		
		button('Play',150, 450, 100, 50, green, bright_green, game_loop1)
		button('Instruction',350, 450, 110, 50, yellow, bright_yellow, inst)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)
		
def inst():
	
	#setup text
	smallText = pygame.font.SysFont('comicsansms', 15)
	largeText = pygame.font.SysFont("comicsansms", 100)
	
	#Create texts
	TextSurf, TextRect = text_objects('Instructions', largeText)
	TextSurf2, TextRect2 = text_objects('You are Hopper, and you are trying to get to the flag, where you advance to the next level.', smallText)
	TextSurf3, TextRect3 = text_objects('Press the up key to jump, and the left and right keys to go left and right.', smallText)
	TextSurf4, TextRect4 = text_objects("You can land on the red blocks, but if you fall, then you'll alnd in the water in drown.", smallText)
	TextSurf5, TextRect5 = text_objects("On the third and forth level will have yellow enemies that will punch you.", smallText)
	TextSurf6, TextRect6 = text_objects("Now go out there and good luck, Hopper!!!", smallText)
	
	#Center texts
	TextRect.center = ((display_width / 2),50 )
	TextRect2.center = ((display_width / 2),125 )
	TextRect3.center = ((display_width / 2),150 )
	TextRect4.center = ((display_width / 2),175 )
	TextRect5.center = ((display_width / 2),200 )
	TextRect6.center = ((display_width / 2),225 )
	gameDisplay.blit(TextSurf, TextRect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
					
	#Draw Text
		gameDisplay.fill(white)
		
		gameDisplay.blit(TextSurf, TextRect)
		gameDisplay.blit(TextSurf2, TextRect2)
		gameDisplay.blit(TextSurf3, TextRect3)
		gameDisplay.blit(TextSurf4, TextRect4)
		gameDisplay.blit(TextSurf5, TextRect5)
		gameDisplay.blit(TextSurf6, TextRect6)

		#create back button
		button('Back',20, 450, 100, 50, blue, bright_blue, game_intro)
		
		
		pygame.display.update()
		clock.tick(15)
		
def paused():
	pygame.mixer.music.pause()
	
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects('Paused', largeText)
	TextRect.center = ((display_width / 2),(display_height / 2) )
	gameDisplay.blit(TextSurf, TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
					
		button('Continue',150, 450, 100, 50, green, bright_green, unpause)
		
		button('Quit',550, 450, 100, 50, blue, bright_blue, quit_one)
		
		
		pygame.display.update()
		clock.tick(15)

def unpause():
	global pause
	pause = False
	
	pygame.mixer.music.unpause()

def text_objects(text, font):
	textSurface = font.render(text, True, pink)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.SysFont("comicsansms", 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((WIN_WIDTH / 2),(WIN_HEIGHT / 2) )
	gameDisplay.blit(TextSurf, TextRect)                                           
	
	pygame.display.update()
	
def gameOver():
	
	OCEAN_Y = 600
	
	largeText = pygame.font.SysFont("comicsansms", 100)
	TextSurf, TextRect = text_objects('Game Over', largeText)
	TextRect.center = ((WIN_WIDTH / 2),(WIN_HEIGHT / 2) )
	gameDisplay.blit(TextSurf, TextRect)
	A = 0
	while A < 10000:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYUP:
				
				if event.key == pygame.K_ESCAPE:
					terminate()

		pygame.draw.rect(gameDisplay, blue, (0,OCEAN_Y,800,600))
		OCEAN_Y -= .5
		gameDisplay.blit(TextSurf, TextRect)
		A+=1
		pygame.display.flip()
	sys.exit()
		
def lifeDead():
	
	global rectangles
	global rects_orig
	global obstacles
	
	OCEAN_Y = 600
	
	largeText = pygame.font.SysFont("comicsansms", 100)
	TextSurf, TextRect = text_objects('What Next...', largeText)
	TextRect.center = ((WIN_WIDTH / 2),(WIN_HEIGHT / 2) )
	gameDisplay.blit(TextSurf, TextRect)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYUP:
				
				if event.key == pygame.K_ESCAPE:
					terminate()

		pygame.draw.rect(gameDisplay, blue, (0,OCEAN_Y,800,600))
		OCEAN_Y -= .5
		gameDisplay.blit(TextSurf, TextRect)
		
		if OCEAN_Y <= -20:
			time.sleep(2)
			#trb shoot
			#rectangles = rects_orig
			#dim = dim_orig
			if GAME == 1:
				
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				rects_orig = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				obstacles = [[50.0, 480], [250.0, 180], [650.0, 280], [450.0, 380], [150.0, 80], [50.0, -20], [250.0, -220], [350.0, -120], [550.0, -320], [750.0, -420], [450.0, -520], [250.0, -620], [550.0, -720], [650.0, -820], [250.0, -970], [350.0, -1020], [450.0, -1120], [550.0, -1220], [150.0, -1320], [350.0, -1420]]
				#print(obstacles)

				game_loop1()
			if GAME == 2:
				
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				rects_orig = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				obstacles = [[50.0, 480], [250.0, 180], [650.0, 280], [450.0, 380], [150.0, 80], [50.0, -20], [250.0, -220], [350.0, -120], [550.0, -320], [750.0, -420], [450.0, -520], [250.0, -620], [550.0, -720], [650.0, -820], [250.0, -970], [350.0, -1020], [450.0, -1120], [550.0, -1220], [150.0, -1320], [350.0, -1420]]
				#print(obstacles)

				game_loop2()
			elif GAME == 3:
				
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				rects_orig = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				obstacles = [[50.0, 480], [250.0, 180], [650.0, 280], [450.0, 380], [150.0, 80], [50.0, -20], [250.0, -220], [350.0, -120], [550.0, -320], [750.0, -420], [450.0, -520], [250.0, -620], [550.0, -720], [650.0, -820], [250.0, -970], [350.0, -1020], [450.0, -1120], [550.0, -1220], [150.0, -1320], [350.0, -1420]]
				#print(obstacles)

				game_loop3()
			elif GAME == 4:
				
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				rects_orig = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]				
				obstacles = [[50.0, 480], [250.0, 180], [650.0, 280], [450.0, 380], [150.0, 80], [50.0, -20], [250.0, -220], [350.0, -120], [550.0, -320], [750.0, -420], [450.0, -520], [250.0, -620], [550.0, -720], [650.0, -820], [250.0, -970], [350.0, -1020], [450.0, -1120], [550.0, -1220], [150.0, -1320], [350.0, -1420]]
				#print(obstacles)

				game_loop4()				
		pygame.display.flip()
		
def terminate():
	pygame.quit()
	sys.exit()
	
def drawRect(rectangles):
	pygame.draw.rect(gameDisplay, red, (rectangles[0],rectangles[1],100,50))

def drawObst(obstacle):
	pygame.draw.rect(gameDisplay, yellow, (obstacle[0],obstacle[1],20,20))
	
def drawFlag(dim):
	gameDisplay.blit(flag, (dim[0],dim[1]))

def quit_one():	
	sys.exit()
	
def get_obstacles(rectangles):
		global obstacles
		obst = []
		for rect in rectangles:
			x = ((rect[0] + 100) + rect[0]) / 2
			y = rect[1] - 20
			obst = [x,y]
			obstacles.append(obst)
	
def win():
	global GAME
	global rectangles
	global rects_orig
	global obstacles
	

	
	OCEAN_Y = 0
	
	GAME += 1
	
	largeText = pygame.font.SysFont("comicsansms", 100)
	medText = pygame.font.SysFont("comicsansms", 75)
	if GAME != 4:
		
		TextSurf, TextRect = text_objects('Next...', largeText)
	else:
		TextSurf, TextRect = text_objects("You've Won!!!", largeText)
		
		TextRect.center = ((WIN_WIDTH / 2),(50) )
		
		gameDisplay.blit(TextSurf, TextRect)
		
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYUP:
				
				if event.key == pygame.K_ESCAPE:
					terminate()

		pygame.draw.rect(gameDisplay, aqua, (0,OCEAN_Y,800,600))
		OCEAN_Y += .5
		gameDisplay.blit(TextSurf, TextRect)
		
		if OCEAN_Y >= 620:
			time.sleep(2)
			
			if GAME == 2:
				
				rectangles = rects_orig
				game_loop2()
			elif GAME == 3:
				
				rectangles = rects_orig
				game_loop3()
			elif GAME == 4:
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				rects_orig = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				obstacles = [[50.0, 480], [250.0, 180], [650.0, 280], [450.0, 380], [150.0, 80], [50.0, -20], [250.0, -220], [350.0, -120], [550.0, -320], [750.0, -420], [450.0, -520], [250.0, -620], [550.0, -720], [650.0, -820], [250.0, -970], [350.0, -1020], [450.0, -1120], [550.0, -1220], [150.0, -1320], [350.0, -1420]]
				time.sleep(4)
				sys.exit()
				game_loop4()
			else:
				pass
		pygame.display.flip()
		
class Draw:
	
	def rectangle_enemy(self,rectangles):
		for rect in rectangles:
			drawRect(rect)
			
	def draw_obstacle(self, obstacles):
		for obst in obstacles:
			drawObst(obst)
			
	def character(self,X,Y):
		pygame.draw.rect(gameDisplay, orange, (X,Y,25,25))
		
	def flag(self,dim):
		drawFlag(dim)
	
	def ground(self,rectangles,SAFETY_COLOR):
		pygame.draw.rect(gameDisplay, SAFETY_COLOR, (rectangles[0][0],rectangles[0][1],800,1000))
		
	def drawHealthMeter(self,MAX_LENGTH,currentHealth):
		for i in range(currentHealth):
			pygame.draw.rect(gameDisplay, black, (15,5 +(10 * MAX_LENGTH) - i * 10,20,10))
		for i in range(MAX_LENGTH):
			pygame.draw.rect(gameDisplay, pink, (15, 5 + (10 * MAX_LENGTH) - i * 10,20,10), 1)
			
def game_loop1():
	pygame.mixer.music.play(-1)
	global pause
	global MAX_LENGTH
	global LIVES
	
	CHANGE_BOOL = False
	
	dim = [300,-1625]
	
	MAX_LENGTH = 5
	
	rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
	
	SAFETY_COLOR = green
	
	X_CHANGE = 0
	X = 400
	Y = 350
	Y_CHANGE = 0 
	JUMPBOOL = False
	
	JUMPDOWN = 0
	
	while True:
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					
					JUMPBOOL = True
					
					SAFETY_COLOR = blue
					
					Y_CHANGE = -5
					
				elif event.key == pygame.K_LEFT:
					X_CHANGE = -.5
					
				elif event.key == pygame.K_RIGHT:
					X_CHANGE = .5
					
				elif event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					#gravity
#Y_CHANGE = .25
					Y_CHANGE = 0
					JUMPBOOL = False
					JUMPDOWN = 0
					
				elif event.key == pygame.K_LEFT:
					X_CHANGE = 0
					
				elif event.key == pygame.K_RIGHT:
					X_CHANGE = 0
					
				
				elif event.key == pygame.K_ESCAPE:
					terminate()
			
		
		val = 0
		for lsts in rectangles:
			if (rectangles[val][1] + 75) > Y > rectangles[val][1] and rectangles[val][0] < X < (rectangles[val][0] - 10) and JUMPBOOL == False:
				X = rectangles[val][0] - 10
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
				
			elif (rectangles[val][1] + 75) > Y > rectangles[val][1] and (rectangles[val][0] + 100) < X < (rectangles[val][0] + 110) and JUMPBOOL == False:
				X = rectangles[val][0] + 110
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif (rectangles[val][1] + 50) > Y > rectangles[val][1] + 30 and rectangles[val][0] < X < (rectangles[val][0] + 100):
				Y = rectangles[val][1] + 65
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif ((rectangles[val][1] + 50) > Y > (rectangles[val][1]-35) and (rectangles[val][0] - 25) < X < (rectangles[val][0] + 100)) and JUMPBOOL == False:
				Y = rectangles[val][1] - 25
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif rectangles[val][0] > X > 0 or rectangles[val][0] + 100 < X < 800 and JUMPBOOL == False:
				Y_CHANGE = .25
				
				
			val += 1
				
		
			
		if JUMPBOOL == False:
			Y += Y_CHANGE
			for block in rectangles:
				block[1] -= Y_CHANGE / 1.1
			dim[1] -= Y_CHANGE / 1.1
			
		elif JUMPBOOL == True:
			Y -= Y_CHANGE
			for block in rectangles:
					block[1] += Y_CHANGE / 1.1
			dim[1] += Y_CHANGE / 1.1
		
		X += X_CHANGE
		
		if (rectangles[-1][1] + 50) > Y > (rectangles[-1][1]-35) and (rectangles[-1][0] - 25) < X < (rectangles[-1][0] + 100) and JUMPBOOL == False:
			win()
			
		elif Y > 580:
			LIVES -= 1
				
			if LIVES <= 0:
				gameOver()
			else:
				lifeDead()
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(bubbles)
				
		elif rectangles[0][1] < 0:
			LIVES -= 1
			lifeDead()
			pygame.mixer.music.stop()
			pygame.mixer.Sound.play(bubbles)
			
		
		gameDisplay.fill(white)
		
		
		drawObject = Draw()
		drawObject.flag(dim)
		drawObject.rectangle_enemy(rectangles)
		drawObject.character(X,Y)
		drawObject.ground(rectangles,SAFETY_COLOR)
		drawObject.drawHealthMeter(MAX_LENGTH,LIVES)
		
		pygame.display.update()
		clock.tick(800)
		
def game_loop2():
	pygame.mixer.music.play(-1)

	global MAX_LENGTH
	global pause
	global LIVES

	CHANGE_BOOL = False
	
	dim = [300,-1625]
	
	MAX_LENGTH = 5
	
	rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
	
	SAFETY_COLOR = green
	
	X_CHANGE = 0
	X = 400
	Y = 350
	Y_CHANGE = 0 
	JUMPBOOL = False
	
	JUMPDOWN = 0
	
	while True:
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					
					JUMPBOOL = True
					
					SAFETY_COLOR = blue
					
					Y_CHANGE = -5
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = -.5
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = .5
				if event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					#gravity
					Y_CHANGE = .25
					JUMPBOOL = False
					JUMPDOWN = 0
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = 0
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = 0
					
				
				if event.key == pygame.K_ESCAPE:
					terminate()
			
		
		RECT_TOP = 0
		for val in rectangles:
			if ((rectangles[RECT_TOP][1] + 50) > Y > (rectangles[RECT_TOP][1]-35) and (rectangles[RECT_TOP][0] - 25) < X < (rectangles[RECT_TOP][0] + 100)) and JUMPBOOL == False:
				Y = rectangles[RECT_TOP][1] - 25
				CHANGE_BOOL = True
				Y_CHANGE = 0
				
			elif rectangles[RECT_TOP][0] > X > 0 or rectangles[RECT_TOP][0] + 100 < X < 800 and JUMPBOOL == False and ((rectangles[RECT_TOP][1] + 50) > Y > (rectangles[RECT_TOP][1]-35) and (rectangles[RECT_TOP][0] - 25) < X < (rectangles[RECT_TOP][0] + 100)) == False:
				Y_CHANGE = .25
					
			RECT_TOP += 1
		
		RECT_BOT = 0
		for val in rectangles:
			if (rectangles[RECT_BOT][1] + 50) > Y > rectangles[RECT_BOT][1] + 30 and rectangles[RECT_BOT][0] < X < (rectangles[RECT_BOT][0] + 100):
				Y = rectangles[RECT_BOT][1] + 65
				CHANGE_BOOL = True
				Y_CHANGE = 0
				
			elif rectangles[RECT_BOT][0] > X > 0 and rectangles[RECT_BOT][0] + 100 < X < 800:
				Y_CHANGE = .25
				
			RECT_BOT +=1
		
		RECT_RIG = 0
		for val in rectangles:
			if (rectangles[RECT_RIG][1] + 75) > Y > rectangles[RECT_RIG][1] and (rectangles[RECT_RIG][0] + 100) < X < (rectangles[RECT_RIG][0] + 110) and JUMPBOOL == False:
				X = rectangles[RECT_RIG][0] + 110
				CHANGE_BOOL = True
				Y_CHANGE = 0
			elif rectangles[RECT_RIG][0] > X > 0 and rectangles[RECT_RIG][0] + 100 < X < 800:
				Y_CHANGE = .25
				
			RECT_RIG +=1
			
		RECT_LIF = 0
		for val in rectangles:
			if (rectangles[RECT_LIF][1] + 75) > Y > rectangles[RECT_LIF][1] and rectangles[RECT_LIF][0] < X < (rectangles[RECT_LIF][0] - 10) and JUMPBOOL == False:
				X = rectangles[RECT_LIF][0] - 10
				CHANGE_BOOL = True
				Y_CHANGE = 0
			elif rectangles[RECT_LIF][0] > X > 0 and rectangles[RECT_LIF][0] + 100 < X < 800:
				
				Y_CHANGE = .25
				
			RECT_LIF +=1
			
		if JUMPBOOL == False:
			Y += Y_CHANGE
			for block in rectangles:
				block[1] -= Y_CHANGE / 1.1
			dim[1] -= Y_CHANGE / 1.1
			
		if JUMPBOOL == True:
			Y -= Y_CHANGE
			for block in rectangles:
					block[1] += Y_CHANGE / 1.1
			dim[1] += Y_CHANGE / 1.1
		
		X += X_CHANGE
		
		if (rectangles[-1][1] + 50) > Y > (rectangles[-1][1]-35) and (rectangles[-1][0] - 25) < X < (rectangles[-1][0] + 100) and JUMPBOOL == False:
			win()
			
		elif Y > 580:
			LIVES -= 1
				
			if LIVES <= 0:
				gameOver()
			else:
				lifeDead()
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(bubbles)
				
		if rectangles[0][1] < 0:
			LIVES -= 1
			lifeDead()
			pygame.mixer.music.stop()
			pygame.mixer.Sound.play(bubbles)
			
		
		gameDisplay.fill(white)
					
		drawObject = Draw()
		drawObject.flag(dim)
		drawObject.rectangle_enemy(rectangles)
		drawObject.character(X,Y)
		drawObject.ground(rectangles,SAFETY_COLOR)
		drawObject.drawHealthMeter(MAX_LENGTH,LIVES)
		
		pygame.display.update()
		clock.tick(800)	
def game_loop3():
	pygame.mixer.music.play(-1)

	global MAX_LENGTH
	global pause
	global obstacles
	
	global LIVES
	
	global rectangles
	global rects_orig
	
	CHANGE_BOOL = False
	
	dim = [300,-1625]
	
	MAX_LENGTH = 5
	
	
	obst_change = .05
	
	SAFETY_COLOR = green
	
	X_CHANGE = 0
	X = 400
	Y = 350
	Y_CHANGE = 0 
	JUMPBOOL = False
		
	JUMPDOWN = 0
	#get_obstacles(rectangles)

	while True:
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					
					JUMPBOOL = True
					
					SAFETY_COLOR = blue
					
					Y_CHANGE = -1
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = -.25
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = .25
					
				if event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					#gravity
#Y_CHANGE = .25
					Y_CHANGE = 0
					JUMPBOOL = False
					JUMPDOWN = 0
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = 0
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = 0
					
				
				if event.key == pygame.K_ESCAPE:
					terminate()
	
		
		val = 0
		for lsts in rectangles:
			if (rectangles[val][1] + 75) > Y > rectangles[val][1] and rectangles[val][0] < X < (rectangles[val][0] - 10) and JUMPBOOL == False:
				X = rectangles[val][0] - 10
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
				
			elif (rectangles[val][1] + 75) > Y > rectangles[val][1] and (rectangles[val][0] + 100) < X < (rectangles[val][0] + 110) and JUMPBOOL == False:
				X = rectangles[val][0] + 110
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif (rectangles[val][1] + 50) > Y > rectangles[val][1] + 30 and rectangles[val][0] < X < (rectangles[val][0] + 100):
				Y = rectangles[val][1] + 65
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif ((rectangles[val][1] + 50) > Y > (rectangles[val][1]-35) and (rectangles[val][0] - 25) < X < (rectangles[val][0] + 100)) and JUMPBOOL == False:
				Y = rectangles[val][1] - 25
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif rectangles[val][0] > X > 0 or rectangles[val][0] + 100 < X < 800 and JUMPBOOL == False:
				Y_CHANGE = .25
				
				
			val += 1
				
		for obst in obstacles:
			if obst[0] + 20 > X > obst[0] -20 and obst[1] - 20 < Y < obst[1] + 20:
				LIVES -= 1
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

				lifeDead()
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(punch)
				
				
		num = 0			
		for obst in obstacles:
			if num > 19:
				num = 0
			if obst[0] < rectangles[num][0]:
				obst_change = 0.05
				obst[0] += obst_change
			elif obst[0] > rectangles[num][0] + 100:
				obst_change = -0.05
				obst[0] += obst_change
			else:
				obst[0] += obst_change
			num += 1				
				
		if JUMPBOOL == False:
			Y += Y_CHANGE
			for block in rectangles:
				block[1] -= Y_CHANGE / 1.1
			for obst in obstacles:
				obst[1] -= Y_CHANGE / 1.1
			dim[1] -= Y_CHANGE / 1.1
			
		if JUMPBOOL == True:
			Y -= Y_CHANGE
			for block in rectangles:
					block[1] += Y_CHANGE / 1.1
			for obst in obstacles:
				obst[1]+= Y_CHANGE / 1.1
			dim[1] += Y_CHANGE / 1.1
		
		X += X_CHANGE
		
		if (rectangles[-1][1] + 50) > Y > (rectangles[-1][1]-35) and (rectangles[-1][0] - 25) < X < (rectangles[-1][0] + 100) and JUMPBOOL == False:
			rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

			win()
			
		if Y > 580:
			LIVES -= 1
				
			if LIVES <= 0:
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

				gameOver()
				

			else:
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				LIVES-=1
				lifeDead()
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(bubbles)
				
		if rectangles[0][1] < 0:
			LIVES -= 1
			rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

			lifeDead()
			pygame.mixer.music.stop()
			pygame.mixer.Sound.play(bubbles)
			
		
		gameDisplay.fill(white)
		
			
		drawObject = Draw()
		drawObject.flag(dim)
		drawObject.rectangle_enemy(rectangles)
		drawObject.character(X,Y)
		drawObject.ground(rectangles,SAFETY_COLOR)
		drawObject.drawHealthMeter(MAX_LENGTH,LIVES)
		drawObject.draw_obstacle(obstacles)
		
		
		pygame.display.update()
		clock.tick(800)
def game_loop4():
	pygame.mixer.music.play(-1)
	

	global MAX_LENGTH
	global pause
	global obstacles
	
	global LIVES
	
	global rectangles
	global rects_orig
	
	CHANGE_BOOL = False
	
	dim = [300,-1625]
	
	MAX_LENGTH = 5
	
	
	obst_change = .05
	
	SAFETY_COLOR = green
	
	X_CHANGE = 0
	X = 400
	Y = 350
	Y_CHANGE = 0 
	JUMPBOOL = False
		
	JUMPDOWN = 0
	print(obstacles)

	while True:
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					
					JUMPBOOL = True
					
					SAFETY_COLOR = blue
					
					Y_CHANGE = -1
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = -.25
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = .25
					
				if event.key == pygame.K_p:
					pause = True
					paused()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					#gravity
#Y_CHANGE = .25
					Y_CHANGE = 0
					JUMPBOOL = False
					JUMPDOWN = 0
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = 0
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = 0
					
				
				if event.key == pygame.K_ESCAPE:
					terminate()
	
		
		val = 0
		for lsts in rectangles:
			if (rectangles[val][1] + 75) > Y > rectangles[val][1] and rectangles[val][0] < X < (rectangles[val][0] - 10) and JUMPBOOL == False:
				X = rectangles[val][0] - 10
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
				
			elif (rectangles[val][1] + 75) > Y > rectangles[val][1] and (rectangles[val][0] + 100) < X < (rectangles[val][0] + 110) and JUMPBOOL == False:
				X = rectangles[val][0] + 110
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif (rectangles[val][1] + 50) > Y > rectangles[val][1] + 30 and rectangles[val][0] < X < (rectangles[val][0] + 100):
				Y = rectangles[val][1] + 65
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif ((rectangles[val][1] + 50) > Y > (rectangles[val][1]-35) and (rectangles[val][0] - 25) < X < (rectangles[val][0] + 100)) and JUMPBOOL == False:
				Y = rectangles[val][1] - 25
				CHANGE_BOOL = True
				Y_CHANGE = 0
				break
				
			elif rectangles[val][0] > X > 0 or rectangles[val][0] + 100 < X < 800 and JUMPBOOL == False:
				Y_CHANGE = .25
				
				
			val += 1
				
		for obst in obstacles:
			if obst[0] + 20 > X > obst[0] -20 and obst[1] - 20 < Y < obst[1] + 20:
				LIVES -= 1
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

				lifeDead()
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(punch)
				
				
		num = 0			
		for obst in obstacles:
			if num > 19:
				num = 0
			if obst[0] < rectangles[num][0]:
				obst_change = 0.05
				obst[0] += obst_change
			elif obst[0] > rectangles[num][0] + 100:
				obst_change = -0.05
				obst[0] += obst_change
			else:
				obst[0] += obst_change
			num += 1				
				
		if JUMPBOOL == False:
			Y += Y_CHANGE
			for block in rectangles:
				block[1] -= Y_CHANGE / 1.1
			for obst in obstacles:
				obst[1] -= Y_CHANGE / 1.1
			dim[1] -= Y_CHANGE / 1.1
			
		if JUMPBOOL == True:
			Y -= Y_CHANGE
			for block in rectangles:
					block[1] += Y_CHANGE / 1.1
			for obst in obstacles:
				obst[1]+= Y_CHANGE / 1.1
			dim[1] += Y_CHANGE / 1.1
		
		X += X_CHANGE
		
		if (rectangles[-1][1] + 50) > Y > (rectangles[-1][1]-35) and (rectangles[-1][0] - 25) < X < (rectangles[-1][0] + 100) and JUMPBOOL == False:
			rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

			win()
			
		if Y > 580:
			LIVES -= 1
				
			if LIVES <= 0:
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

				gameOver()
				

			else:
				rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]
				LIVES-=1
				lifeDead()
				pygame.mixer.music.stop()
				pygame.mixer.Sound.play(bubbles)
				
		if rectangles[0][1] < 0:
			LIVES -= 1
			rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],[300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]

			lifeDead()
			pygame.mixer.music.stop()
			pygame.mixer.Sound.play(bubbles)
			
		
		gameDisplay.fill(white)
		
			
		drawObject = Draw()
		drawObject.flag(dim)
		drawObject.rectangle_enemy(rectangles)
		drawObject.character(X,Y)
		drawObject.ground(rectangles,SAFETY_COLOR)
		drawObject.drawHealthMeter(MAX_LENGTH,LIVES)
		drawObject.draw_obstacle(obstacles)
		

		
		pygame.display.update()
		clock.tick(800)
		
game_intro()


