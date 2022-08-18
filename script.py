import psp2d
font = psp2d.Font("resource/font.png")
img = psp2d.Image(480, 272)
screen = psp2d.Screen()
blank = psp2d.Color(0, 0, 0)

#img.clear(blank)
#font.drawText(img, 0, 0, "Press to a button")
#screen.blit(img)
#screen.swap()

# ^^^^^^ Somehow pad.analogX and Y works better than this??? (it prints back to "Press to a button" when you stop holding the button for some reason)
ctrl = True

def buttonprint(text):
	img.clear(blank)
	font.drawText(img, 0, 0, text)
	screen.blit(img)
	screen.swap()


while ctrl == True:
	pad = psp2d.Controller()
	if pad.circle:
		buttonprint("You pressed O")

	elif pad.cross:
		buttonprint("You pressed X")

	elif pad.triangle:
		buttonprint("You pressed /\\")

	elif pad.square:
		buttonprint("You pressed []")

	elif pad.up:
		buttonprint("You pressed UP DPAD")

	elif pad.down:
		buttonprint("You pressed DOWN DPAD")

	elif pad.left:
		buttonprint("You pressed LEFT DPAD")

	elif pad.right:
		buttonprint("You pressed RIGHT DPAD")

	elif pad.l:
		buttonprint("You pressed LEFT TRIGGER")

	elif pad.r:
		buttonprint("You pressed RIGHT TRIGGER")

	elif pad.start:
		buttonprint("You pressed START")

	elif pad.select:
		buttonprint("You pressed SELECT")

	elif pad.analogX or pad.analogY:
		buttonprint("Press to a button")
