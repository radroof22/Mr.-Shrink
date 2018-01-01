import sys, pygame, time
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

WIN_WIDTH = 800
WIN_HEIGHT = 600

gameDisplay = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

flag = pygame.image.load("winning_flag.png")

black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
pink = (255,51,153)
aqua = (0,255,255)

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
	
def drawFlag(dim):
	gameDisplay.blit(flag, (dim[0],dim[1]))
	
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
		
class BlockInt:
	
	def top(self,X,Y,rectangles,JUMPBOOL):
	
		
		global Y_CHANGE
		global CHANGE_BOOL
		
		RECT_TOP = 0
		for val in rectangles:
		
			if (rectangles[RECT_TOP][1] + 50) > Y > (rectangles[RECT_TOP][1]-35) and (rectangles[RECT_TOP][0] - 25) < X < (rectangles[RECT_TOP][0] + 100) and JUMPBOOL == False:
				Y = rectangles[RECT_TOP][1] - 25
				CHANGE_BOOL = True
				Y_CHANGE = 0
				
			elif rectangles[RECT_TOP][0] > X > 0 or rectangles[RECT_TOP][0] + 100 < X < 800 and JUMPBOOL == False:
			#	print("HELLO")
				Y_CHANGE = .25
				
			RECT_TOP += 1
			
	def bot(self,X,Y,rectangles,JUMPBOOL):
				
		global Y_CHANGE
		global CHANGE_BOOL
		
		RECT_BOT = 0
		for val in rectangles:
			if (rectangles[RECT_BOT][1] + 50) > Y > rectangles[RECT_BOT][1] + 30 and rectangles[RECT_BOT][0] < X < (rectangles[RECT_BOT][0] + 100):
				Y = rectangles[RECT_BOT][1] + 65
				CHANGE_BOOL = True
				Y_CHANGE = 0
				
			elif rectangles[RECT_BOT][0] > X > 0 and rectangles[RECT_BOT][0] + 100 < X < 800:
				Y_CHANGE = .25
				
			RECT_BOT +=1
			
	def rig(self,X,Y,rectangles,JUMPBOOL):
	
		global Y_CHANGE
		global CHANGE_BOOL
		
		RECT_RIG = 0
		for val in rectangles:
			if (rectangles[RECT_RIG][1] + 75) > Y > rectangles[RECT_RIG][1] and (rectangles[RECT_RIG][0] + 100) < X < (rectangles[RECT_RIG][0] + 110) and JUMPBOOL == False:
				X = rectangles[RECT_RIG][0] + 110
				CHANGE_BOOL = True
				Y_CHANGE = 0
			elif rectangles[RECT_RIG][0] > X > 0 and rectangles[RECT_RIG][0] + 100 < X < 800:
				Y_CHANGE = .25
				
			RECT_RIG +=1
	
	def lef(self,X,Y,rectangles,JUMPBOOL):
		
		global Y_CHANGE
		global CHANGE_BOOL
		
		RECT_LIF = 0
		for val in rectangles:
			if (rectangles[RECT_LIF][1] + 75) > Y > rectangles[RECT_LIF][1] and rectangles[RECT_LIF][0] < X < (rectangles[RECT_LIF][0] - 10) and JUMPBOOL == False:
				X = rectangles[RECT_LIF][0] - 10
				CHANGE_BOOL = True
				Y_CHANGE = 0
			elif rectangles[RECT_LIF][0] > X > 0 and rectangles[RECT_LIF][0] + 100 < X < 800:
				
				Y_CHANGE = .25
				
			RECT_LIF +=1
			
	def noJump(self,X,Y,rectangles,JUMPBOOL,dim,Y_CHANGE):
	
		if JUMPBOOL == False:
			Y += Y_CHANGE
			for block in rectangles:
				block[1] -= Y_CHANGE / 4
			dim[1] -= Y_CHANGE / 4
			
	def jump(self,X,Y,Y_CHANGE,rectangles,JUMPBOOL,dim):
		
		if JUMPBOOL == True:
			Y -= Y_CHANGE
			for block in rectangles:
					block[1] += Y_CHANGE / 4
			dim[1] += Y_CHANGE / 4
			
	def linear(self,X,X_CHANGE):
		X += X_CHANGE
		
	def win(self,rectangles,Y,X,JUMPBOOL):
				
		if (rectangles[-1][1] + 50) > Y > (rectangles[-1][1]-35) and (rectangles[-1][0] - 25) < X < (rectangles[-1][0] + 100) and JUMPBOOL == False:
			win()
			
	def loser(self,Y,LIVES):
	
		if Y > 580:
			LIVES -= 1
				
			if LIVES <= 0:
				gameOver()
			else:
				lifeDead()
				

def game_loop():

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
					
					Y_CHANGE = -1
					
				if event.key == pygame.K_LEFT:
					X_CHANGE = -.25
					
				if event.key == pygame.K_RIGHT:
					X_CHANGE = .25

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
		
		pygame.display.update()


game_loop()

