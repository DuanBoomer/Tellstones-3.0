import turtle as t
import random as r
#Registering Shapes---------------------------------------------------------------
shapes=["crown.gif","flag.gif","scale.gif","sword.gif","hammer.gif","knight.gif","shield.gif","bob.gif","name.gif","line.gif","bg.gif"]
for shape in shapes:
	t.register_shape(shape)
#Screen----------------------------------------------------------------------------
wn=t.Screen()
wn.tracer(0)
wn.bgcolor("#DBD49C")
screen=t.Turtle()
screen.pu()
screen.shape("name.gif")
screen.goto(50,250)
screen.stamp()
screen.shape("bob.gif")
screen.goto(-450,-260)
screen.stamp()
screen.shape("line.gif")
screen.goto(580,0)
screen.stamp()
screen.goto(-55,-70)
screen.shape("bg.gif")
#Defining line(l)------------------------------------------------------------------
l=t.Turtle()
l.hideturtle()
l.color("darkslateblue")
l.pu()
l.begin_fill()
l.sety(130)
l.pd()
l.setx(-580)
l.sety(-130)
l.setx(580)
l.sety(130)
l.setx(0)
l.end_fill()
l.pu()
l.color("silver")
l.sety(130-30)
l.pd()
l.pensize(3)
l.setx(-580+30)
l.sety(-130+30)
l.setx(580-30)
l.sety(130-30)
l.setx(0)
l.pu()
l.sety(130-40)
l.pd()
l.pensize(1)
l.setx(-580+40)
l.sety(-130+40)
l.setx(580-40)
l.sety(130-40)
l.setx(0)
#Defining Stones-----------------------------------------------------------------
stones=[]
for _ in range(7):
	stones.append(t.Turtle())
x=450
for stone in stones:
	stone.pu()
	stone.goto(x,-250)
	x-=150
crown=stones[0]
flag=stones[1]
scale=stones[2]
sword=stones[3]
hammer=stones[4]
knight=stones[5]
shield=stones[6]
crown.shape("crown.gif")
flag.shape("flag.gif")
scale.shape("scale.gif")
sword.shape("sword.gif")
hammer.shape("hammer.gif")
knight.shape("knight.gif")
shield.shape("shield.gif")

wn.update()
wn.tracer(1)

place_r=0
place_l=0
run=True

crown_placed=False
flag_placed=False
hammer_placed=False
knight_placed=False
scale_placed=False
shield_placed=False
sword_placed=False

crown_hidden=False
flag_hidden=False
hammer_hidden=False
knight_hidden=False
scale_hidden=False
shield_hidden=False
sword_hidden=False

def sword_swap_r(x,y):
	global sword_placed
	if sword_placed==True:
		sword.seth(90)
		sword.circle(-75,180)
		if scale.xcor()>sword.xcor()-10 and scale.xcor()<sword.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(75,180)
			
		if crown.xcor()>sword.xcor()-10 and crown.xcor()<sword.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(75,180)
			
		if flag.xcor()>sword.xcor()-10 and flag.xcor()<sword.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(75,180)
			
		if hammer.xcor()>sword.xcor()-10 and hammer.xcor()<sword.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(75,180)
			
		if shield.xcor()>sword.xcor()-10 and shield.xcor()<sword.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(75,180)
			
		if knight.xcor()>sword.xcor()-10 and knight.xcor()<sword.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(75,180)

def sword_swap_l(x,y):
	global sword_placed
	if sword_placed==True:
		sword.seth(90)
		sword.circle(75,180)
		if scale.xcor()>sword.xcor()-10 and scale.xcor()<sword.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(-75,180)
			
		if crown.xcor()>sword.xcor()-10 and crown.xcor()<sword.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(-75,180)
			
		if flag.xcor()>sword.xcor()-10 and flag.xcor()<sword.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(-75,180)
			
		if hammer.xcor()>sword.xcor()-10 and hammer.xcor()<sword.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(-75,180)
			
		if shield.xcor()>sword.xcor()-10 and shield.xcor()<sword.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(-75,180)
			
		if knight.xcor()>sword.xcor()-10 and knight.xcor()<sword.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(-75,180)

def scale_swap_r(x,y):
	global scale_placed
	if scale_placed==True:
		scale.seth(90)
		scale.circle(-75,180)
		if sword.xcor()>scale.xcor()-10 and sword.xcor()<scale.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(75,180)
			
		if crown.xcor()>scale.xcor()-10 and crown.xcor()<scale.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(75,180)
			
		if flag.xcor()>scale.xcor()-10 and flag.xcor()<scale.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(75,180)
			
		if hammer.xcor()>scale.xcor()-10 and hammer.xcor()<scale.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(75,180)
			
		if shield.xcor()>scale.xcor()-10 and shield.xcor()<scale.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(75,180)
			
		if knight.xcor()>scale.xcor()-10 and knight.xcor()<scale.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(75,180)

def scale_swap_l(x,y):
	global scale_placed
	if scale_placed==True:
		scale.seth(90)
		scale.circle(75,180)
		if sword.xcor()>scale.xcor()-10 and sword.xcor()<scale.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(-75,180)
			
		if crown.xcor()>scale.xcor()-10 and crown.xcor()<scale.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(-75,180)
			
		if flag.xcor()>scale.xcor()-10 and flag.xcor()<scale.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(-75,180)
			
		if hammer.xcor()>scale.xcor()-10 and hammer.xcor()<scale.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(-75,180)
			
		if shield.xcor()>scale.xcor()-10 and shield.xcor()<scale.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(-75,180)
			
		if knight.xcor()>scale.xcor()-10 and knight.xcor()<scale.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(-75,180)

def crown_swap_r(x,y):
	global crown_placed
	if crown_placed==True:
		crown.seth(90)
		crown.circle(-75,180)
		if scale.xcor()>crown.xcor()-10 and scale.xcor()<crown.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(75,180)
			
		if sword.xcor()>crown.xcor()-10 and sword.xcor()<crown.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(75,180)
			
		if flag.xcor()>crown.xcor()-10 and flag.xcor()<crown.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(75,180)
			
		if hammer.xcor()>crown.xcor()-10 and hammer.xcor()<crown.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(75,180)
			
		if shield.xcor()>crown.xcor()-10 and shield.xcor()<crown.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(75,180)
			
		if knight.xcor()>crown.xcor()-10 and knight.xcor()<crown.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(75,180)

def crown_swap_l(x,y):
	global crown_placed
	if crown_placed==True:
		crown.seth(90)
		crown.circle(75,180)
		if scale.xcor()>crown.xcor()-10 and scale.xcor()<crown.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(-75,180)
			
		if sword.xcor()>crown.xcor()-10 and sword.xcor()<crown.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(-75,180)
			
		if flag.xcor()>crown.xcor()-10 and flag.xcor()<crown.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(-75,180)
			
		if hammer.xcor()>crown.xcor()-10 and hammer.xcor()<crown.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(-75,180)
			
		if shield.xcor()>crown.xcor()-10 and shield.xcor()<crown.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(-75,180)
			
		if knight.xcor()>crown.xcor()-10 and knight.xcor()<crown.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(-75,180)

def hammer_swap_r(x,y):
	global hammer_placed
	if hammer_placed==True:
		hammer.seth(90)
		hammer.circle(-75,180)
		if scale.xcor()>hammer.xcor()-10 and scale.xcor()<hammer.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(75,180)
			
		if crown.xcor()>hammer.xcor()-10 and crown.xcor()<hammer.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(75,180)
			
		if flag.xcor()>hammer.xcor()-10 and flag.xcor()<hammer.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(75,180)
			
		if sword.xcor()>hammer.xcor()-10 and sword.xcor()<hammer.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(75,180)
			
		if shield.xcor()>hammer.xcor()-10 and shield.xcor()<hammer.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(75,180)
			
		if knight.xcor()>hammer.xcor()-10 and knight.xcor()<hammer.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(75,180)

def hammer_swap_l(x,y):
	global hammer_placed
	if hammer_placed==True:
		hammer.seth(90)
		hammer.circle(75,180)
		if scale.xcor()>hammer.xcor()-10 and scale.xcor()<hammer.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(-75,180)
			
		if crown.xcor()>hammer.xcor()-10 and crown.xcor()<hammer.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(-75,180)
			
		if flag.xcor()>hammer.xcor()-10 and flag.xcor()<hammer.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(-75,180)
			
		if sword.xcor()>hammer.xcor()-10 and sword.xcor()<hammer.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(-75,180)
			
		if shield.xcor()>hammer.xcor()-10 and shield.xcor()<hammer.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(-75,180)
			
		if knight.xcor()>hammer.xcor()-10 and knight.xcor()<hammer.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(-75,180)

def flag_swap_r(x,y):
	global flag_placed
	if flag_placed==True:
		flag.seth(90)
		flag.circle(-75,180)
		if scale.xcor()>flag.xcor()-10 and scale.xcor()<flag.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(75,180)
			
		if crown.xcor()>flag.xcor()-10 and crown.xcor()<flag.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(75,180)
			
		if sword.xcor()>flag.xcor()-10 and sword.xcor()<flag.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(75,180)
			
		if hammer.xcor()>flag.xcor()-10 and hammer.xcor()<flag.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(75,180)
			
		if shield.xcor()>flag.xcor()-10 and shield.xcor()<flag.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(75,180)
			
		if knight.xcor()>flag.xcor()-10 and knight.xcor()<flag.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(75,180)

def flag_swap_l(x,y):
	global flag_placed
	if flag_placed==True:
		flag.seth(90)
		flag.circle(75,180)
		if scale.xcor()>flag.xcor()-10 and scale.xcor()<flag.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(-75,180)
			
		if crown.xcor()>flag.xcor()-10 and crown.xcor()<flag.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(-75,180)
			
		if sword.xcor()>flag.xcor()-10 and sword.xcor()<flag.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(-75,180)
			
		if hammer.xcor()>flag.xcor()-10 and hammer.xcor()<flag.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(-75,180)
			
		if shield.xcor()>flag.xcor()-10 and shield.xcor()<flag.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(-75,180)
			
		if knight.xcor()>flag.xcor()-10 and knight.xcor()<flag.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(-75,180)

def shield_swap_r(x,y):
	global shield_placed
	if shield_placed==True:
		shield.seth(90)
		shield.circle(-75,180)
		if scale.xcor()>shield.xcor()-10 and scale.xcor()<shield.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(75,180)
			
		if crown.xcor()>shield.xcor()-10 and crown.xcor()<shield.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(75,180)
			
		if flag.xcor()>shield.xcor()-10 and flag.xcor()<shield.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(75,180)
			
		if hammer.xcor()>shield.xcor()-10 and hammer.xcor()<shield.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(75,180)
			
		if sword.xcor()>shield.xcor()-10 and sword.xcor()<shield.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(75,180)
			
		if knight.xcor()>shield.xcor()-10 and knight.xcor()<shield.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(75,180)

def shield_swap_l(x,y):
	global shield_placed
	if shield_placed==True:
		shield.seth(90)
		shield.circle(75,180)
		if scale.xcor()>shield.xcor()-10 and scale.xcor()<shield.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(-75,180)
			
		if crown.xcor()>shield.xcor()-10 and crown.xcor()<shield.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(-75,180)
			
		if flag.xcor()>shield.xcor()-10 and flag.xcor()<shield.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(-75,180)
			
		if hammer.xcor()>shield.xcor()-10 and hammer.xcor()<shield.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(-75,180)
			
		if sword.xcor()>shield.xcor()-10 and sword.xcor()<shield.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(-75,180)
			
		if knight.xcor()>shield.xcor()-10 and knight.xcor()<shield.xcor()+10 and knight.ycor()>-150:
			knight.seth(90)
			knight.circle(-75,180)

def knight_swap_r(x,y):
	global knight_placed
	if knight_placed==True:
		knight.seth(90)
		knight.circle(-75,180)
		if scale.xcor()>knight.xcor()-10 and scale.xcor()<knight.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(75,180)
			
		if crown.xcor()>knight.xcor()-10 and crown.xcor()<knight.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(75,180)
			
		if flag.xcor()>knight.xcor()-10 and flag.xcor()<knight.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(75,180)
			
		if hammer.xcor()>knight.xcor()-10 and hammer.xcor()<knight.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(75,180)
			
		if shield.xcor()>knight.xcor()-10 and shield.xcor()<knight.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(75,180)
			
		if sword.xcor()>knight.xcor()-10 and sword.xcor()<knight.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(75,180)

def knight_swap_l(x,y):
	global knight_placed
	if knight_placed==True:
		knight.seth(90)
		knight.circle(75,180)
		if scale.xcor()>knight.xcor()-10 and scale.xcor()<knight.xcor()+10 and scale.ycor()>-150:
			scale.seth(90)
			scale.circle(-75,180)
			
		if crown.xcor()>knight.xcor()-10 and crown.xcor()<knight.xcor()+10 and crown.ycor()>-150:
			crown.seth(90)
			crown.circle(-75,180)
			
		if flag.xcor()>knight.xcor()-10 and flag.xcor()<knight.xcor()+10 and flag.ycor()>-150:
			flag.seth(90)
			flag.circle(-75,180)
			
		if hammer.xcor()>knight.xcor()-10 and hammer.xcor()<knight.xcor()+10 and hammer.ycor()>-150:
			hammer.seth(90)
			hammer.circle(-75,180)
			
		if shield.xcor()>knight.xcor()-10 and shield.xcor()<knight.xcor()+10 and shield.ycor()>-150:
			shield.seth(90)
			shield.circle(-75,180)
			
		if sword.xcor()>knight.xcor()-10 and sword.xcor()<knight.xcor()+10 and sword.ycor()>-150:
			sword.seth(90)
			sword.circle(-75,180)

def hide_scale():
	global scale_placed
	global scale_hidden
	if scale_placed==True and scale_hidden==False:
		scale_hidden=True
		scale.shape("circle")
		scale.shapesize(6.5,6.5)
		scale.color("#E7DED2")
		scale.onclick(scale_swap_r,btn=3)
		scale.onclick(scale_swap_l)

def hide_hammer():
	global hammer_placed
	global hammer_hidden
	if hammer_placed==True and hammer_hidden==False:
		hammer_hidden=True
		hammer.shape("circle")
		hammer.shapesize(6.5,6.5)
		hammer.color("#E7DED2")
		hammer.onclick(hammer_swap_r,btn=3)
		hammer.onclick(hammer_swap_l)
	
def hide_crown():
	global crown_placed
	global crown_hidden
	if crown_placed==True and crown_hidden==False:
		crown_hidden=True
		crown.shape("circle")
		crown.shapesize(6.5,6.5)
		crown.color("#E7DED2")
		crown.onclick(crown_swap_r,btn=3)
		crown.onclick(crown_swap_l)
	
def hide_sword():
	global sword_placed
	global sword_hidden
	if sword_placed==True and sword_hidden==False:
		sword_hidden=True
		sword.shape("circle")
		sword.shapesize(6.5,6.5)
		sword.color("#E7DED2")
		sword.onclick(sword_swap_r,btn=3)
		sword.onclick(sword_swap_l)
	
def hide_flag():
	global flag_placed
	global flag_hidden
	if flag_placed==True and flag_hidden==False:
		flag_hidden=True
		flag.shape("circle")
		flag.shapesize(6.5,6.5)
		flag.color("#E7DED2")
		flag.onclick(flag_swap_r,btn=3)
		flag.onclick(flag_swap_l)
	
def hide_knight():
	global knight_placed
	global knight_hidden
	if knight_placed==True and knight_hidden==False:
		knight_hidden=True
		knight.shape("circle")
		knight.shapesize(6.5,6.5)
		knight.color("#E7DED2")
		knight.onclick(knight_swap_r,btn=3)
		knight.onclick(knight_swap_l)
	
def hide_shield():
	global shield_placed
	global shield_hidden
	if shield_placed==True and shield_hidden==False:
		shield_hidden=True
		shield.shape("circle")
		shield.shapesize(6.5,6.5)
		shield.color("#E7DED2")
		shield.onclick(shield_swap_r,btn=3)
		shield.onclick(shield_swap_l)
		
def unhide_scale():
	global scale_placed
	global scale_hidden
	if scale_placed==True and scale_hidden==True:
		scale_hidden=False
		scale.shape("scale.gif")
		scale.onclick(scale_swap_r,btn=3)
		scale.onclick(scale_swap_l)
		
def unhide_hammer():
	global hammer_placed
	global hammer_hidden
	if hammer_placed==True and hammer_hidden==True:
		hammer_hidden=False
		hammer.shape("hammer.gif")
		hammer.onclick(hammer_swap_r,btn=3)
		hammer.onclick(hammer_swap_l)
		
def unhide_crown():
	global crown_placed
	global crown_hidden
	if crown_placed==True and crown_hidden==True:
		crown_hidden=False
		crown.shape("crown.gif")
		crown.onclick(crown_swap_r,btn=3)
		crown.onclick(crown_swap_l)
		
def unhide_sword():
	global sword_placed
	global sword_hidden
	if sword_placed==True and sword_hidden==True:
		sword_hidden=False
		sword.shape("sword.gif")
		sword.onclick(sword_swap_r,btn=3)
		sword.onclick(sword_swap_l)
		
def unhide_flag():
	global flag_placed
	global flag_hidden
	if flag_placed==True and flag_hidden==True:
		flag_hidden=False
		flag.shape("flag.gif")
		flag.onclick(flag_swap_r,btn=3)
		flag.onclick(flag_swap_l)
		
def unhide_knight():
	global knight_placed
	global knight_hidden
	if knight_placed==True and knight_hidden==True:
		knight_hidden=False
		knight.shape("knight.gif")
		knight.onclick(knight_swap_r,btn=3)
		knight.onclick(knight_swap_l)
		
def unhide_shield():
	global shield_placed
	if shield_placed==True and shield_hidden==True:
		shield_hidden=False
		shield.shape("shield.gif")
		shield.onclick(shield_swap_r,btn=3)
		shield.onclick(shield_swap_l)

def place_scale_r(x,y):
	global place_r
	global place_l
	global run
	global scale_placed
	if scale_placed==False:
		scale_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			scale.goto(place_r,0)
			place_r+=150
		scale.onclick(scale_swap_r,btn=3)
		scale.onclick(scale_swap_l)

def place_hammer_r(x,y):
	global place_r
	global place_l
	global run
	global hammer_placed
	if hammer_placed==False:
		hammer_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			hammer.goto(place_r,0)
			place_r+=150
		hammer.onclick(hammer_swap_r,btn=3)
		hammer.onclick(hammer_swap_l)

def place_crown_r(x,y):
	global place_r
	global place_l
	global run
	global crown_placed
	if crown_placed==False:
		crown_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			crown.goto(place_r,0)
			place_r+=150
		crown.onclick(crown_swap_r,btn=3)
		crown.onclick(crown_swap_l)

def place_sword_r(x,y):
	global place_r
	global place_l
	global run
	global sword_placed
	if sword_placed==False:
		sword_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			sword.goto(place_r,0)
			place_r+=150
		sword.onclick(sword_swap_r,btn=3)
		sword.onclick(sword_swap_l)
	
def place_flag_r(x,y):
	global place_r
	global place_l
	global run
	global flag_placed
	if flag_placed==False:
		flag_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			flag.goto(place_r,0)
			place_r+=150
		flag.onclick(flag_swap_r,btn=3)
		flag.onclick(flag_swap_l)

def place_knight_r(x,y):
	global place_r
	global place_l
	global run
	global knight_placed
	if knight_placed==False:
		knight_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			knight.goto(place_r,0)
			place_r+=150
		knight.onclick(knight_swap_r,btn=3)
		knight.onclick(knight_swap_l)

def place_shield_r(x,y):
	global place_r
	global place_l
	global run
	global shield_placed
	if shield_placed==False:
		shield_placed=True
		if place_r<460:
			if run==True:
				place_l-=150
				run=False
			shield.goto(place_r,0)
			place_r+=150
		shield.onclick(shield_swap_r,btn=3)
		shield.onclick(shield_swap_l)
	
def place_scale_l(x,y):
	global place_l
	global place_r
	global run
	global scale_placed
	if scale_placed==False:
		scale_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			scale.goto(place_l,0)
			place_l-=150
		scale.onclick(scale_swap_r,btn=3)
		scale.onclick(scale_swap_l)
	
def place_hammer_l(x,y):
	global place_l
	global place_r
	global run
	global hammer_placed
	if hammer_placed==False:
		hammer_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			hammer.goto(place_l,0)
			place_l-=150
		hammer.onclick(hammer_swap_r,btn=3)
		hammer.onclick(hammer_swap_l)

def place_crown_l(x,y):
	global place_l
	global place_r
	global run
	global crown_placed
	if crown_placed==False:
		crown_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			crown.goto(place_l,0)
			place_l-=150
		crown.onclick(crown_swap_r,btn=3)
		crown.onclick(crown_swap_l)
	
def place_sword_l(x,y):
	global place_l
	global place_r
	global run
	global sword_placed
	if sword_placed==False:
		sword_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			sword.goto(place_l,0)
			place_l-=150
		sword.onclick(sword_swap_r,btn=3)
		sword.onclick(sword_swap_l)

def place_flag_l(x,y):
	global place_l
	global place_r
	global run
	global flag_placed
	if flag_placed==False:
		flag_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			flag.goto(place_l,0)
			place_l-=150
		flag.onclick(flag_swap_r,btn=3)
		flag.onclick(flag_swap_l)

def place_knight_l(x,y):
	global place_l
	global place_r
	global run
	global knight_placed
	if knight_placed==False:
		knight_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			knight.goto(place_l,0)
			place_l-=150
		knight.onclick(knight_swap_r,btn=3)
		knight.onclick(knight_swap_l)
	
def place_shield_l(x,y):
	global place_l
	global place_r
	global run
	global shield_placed
	if shield_placed==False:
		shield_placed=True
		if place_l>-460:
			if run==True:
				place_r+=150
				run=False
			shield.goto(place_l,0)
			place_l-=150
		shield.onclick(shield_swap_r,btn=3)
		shield.onclick(shield_swap_l)

wn.listen()
#place bindings--------------------
scale.onclick(place_scale_r,btn=3)
hammer.onclick(place_hammer_r,btn=3)
crown.onclick(place_crown_r,btn=3)
flag.onclick(place_flag_r,btn=3)
sword.onclick(place_sword_r,btn=3)
knight.onclick(place_knight_r,btn=3)
shield.onclick(place_shield_r,btn=3)

scale.onclick(place_scale_l)
hammer.onclick(place_hammer_l)
crown.onclick(place_crown_l)
flag.onclick(place_flag_l)
sword.onclick(place_sword_l)
knight.onclick(place_knight_l)
shield.onclick(place_shield_l)

#hide bindings---------------------
t.onkeyrelease(hide_scale,'s')
t.onkeyrelease(hide_hammer,'h')
t.onkeyrelease(hide_crown,'c')
t.onkeyrelease(hide_flag,'f')
t.onkeyrelease(hide_sword,'x')
t.onkeyrelease(hide_knight,'k')
t.onkeyrelease(hide_shield,'z')

#unhide bindings--------------------
t.onkeyrelease(unhide_scale,'S')
t.onkeyrelease(unhide_hammer,'H')
t.onkeyrelease(unhide_crown,'C')
t.onkeyrelease(unhide_flag,'F')
t.onkeyrelease(unhide_sword,'X')
t.onkeyrelease(unhide_knight,'K')
t.onkeyrelease(unhide_shield,'Z')






t.mainloop()
