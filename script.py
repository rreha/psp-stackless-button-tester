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

while ctrl == True:
	pad = psp2d.Controller()
	if pad.circle:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed O")
		screen.blit(img)
		screen.swap()

	elif pad.cross:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed X")
		screen.blit(img)
		screen.swap()

	elif pad.triangle:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed /\\")
		screen.blit(img)
		screen.swap()

	elif pad.square:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed []")
		screen.blit(img)
		screen.swap()

	elif pad.up:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed UP D-PAD")
		screen.blit(img)
		screen.swap()

	elif pad.down:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed DOWN D-PAD")
		screen.blit(img)
		screen.swap()

	elif pad.left:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed LEFT D-PAD")
		screen.blit(img)
		screen.swap()

	elif pad.right:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed RIGHT D-PAD")
		screen.blit(img)
		screen.swap()

	elif pad.l:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed LEFT TRIGGER")
		screen.blit(img)
		screen.swap()

	elif pad.r:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed RIGHT TRIGGER")
		screen.blit(img)
		screen.swap()

	elif pad.start:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed START")
		screen.blit(img)
		screen.swap()

	elif pad.select:
		img.clear(blank)
		font.drawText(img, 0, 0, "You pressed SELECT")
		screen.blit(img)
		screen.swap()

	elif pad.analogX or pad.analogY:
		img.clear(blank)
		font.drawText(img, 0, 0, "Press to a button")
		screen.blit(img)
		screen.swap()