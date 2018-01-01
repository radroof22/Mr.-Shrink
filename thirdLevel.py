import sys, pygame, time
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

WIN_WIDTH = 800
WIN_HEIGHT = 600

gameDisplay = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

flag = pygame.image.load("winning_flag.png")

rectangles = [[0,500],[200,200],[600,300],[400,400],[100,100],[0,0],[200,-200],[300,-100],[500,-300],[700,-400],[400,-500],[200,-600],[500,-700],[600,-800],[200,-950],
              [300,-1000],[400,-1100],[500,-1200],[100,-1300],[300,-1400]]


black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
pink = (255,51,153)
aqua = (0,255,255)
yellow = (255,255,0)

X = 400
Y = 350

obstacles = []
LIVES = 5

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

		pygame.display.flip()
		
def lifeDead():

	OCEAN_Y = 600

	global X
	global Y
	X = 400
	Y = 350
	
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
			game_loop()
		
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

def get_obstacles(rectangles):
		global obstacles
		obst = []
		for rect in rectangles:
			x = ((rect[0] + 100) + rect[0]) / 2
			y = rect[1] - 20
			obst = [x,y]
			obstacles.append(obst)
	
def win():
	OCEAN_Y = 0
	
	largeText = pygame.font.SysFont("comicsansms", 100)
	TextSurf, TextRect = text_objects('You Won', largeText)
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

		pygame.draw.rect(gameDisplay, aqua, (0,OCEAN_Y,800,600))
		OCEAN_Y += .5
		gameDisplay.blit(TextSurf, TextRect)
		
		if OCEAN_Y >= 620:
			time.sleep(2)
			game_loop()
			
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
			
	
			

def game_loop():

	global MAX_LENGTH
	
	global obstacles
	
	global LIVES

	global X
	global Y
	
	global rectangles
	
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
				lifeDead()
				
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
			win()
			
		if Y > 580:
			LIVES -= 1
				
			if LIVES <= 0:
				gameOver()
			else:
				lifeDead()
				
		if rectangles[0][1] < 0:
			LIVES -= 1
			lifeDead()
			
		
		gameDisplay.fill(white)
		
			
		drawObject = Draw()
		drawObject.flag(dim)
		drawObject.rectangle_enemy(rectangles)
		drawObject.character(X,Y)
		drawObject.ground(rectangles,SAFETY_COLOR)
		drawObject.drawHealthMeter(MAX_LENGTH,LIVES)
		drawObject.draw_obstacle(obstacles)
		

		
		pygame.display.update()
		
get_obstacles(rectangles)

game_loop()

