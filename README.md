a way to make this a artificial intelligence program:



if counter == 1: "no_letter_added"
= w on the keyboard wasd


elif counter == 2: "right_letter_added"
= a on the keyboard wasd


elif counter == 3: "left_letter_added"
= d on the keyboard wasd


elif counter == 4: "left_letter_added_right_letter_added"
= s on the keyboard wasd


as the ball moves its line of movement makes its point of convergence with the paddle


the ball moves in a line that line is made up of lines pixels that are moved through by various wasd key presses.
down wasd
left or right wasd

if the ball doesn't hit the wall:
ball on pixel row  x = down one pixel, left or right n number of pixels
ball on pixel row x1 = down one pixel, left or right n number of pixels
ball on pixel rox x2 = down one pixel, left or right n number of pixels


else:
#the wall changes the direction of the ball so change the (left to right) or (right to left)
ball on pixel row  x = down one pixel, left or right n number of pixels
ball on pixel row x1 = down one pixel, left or right n number of pixels
ball on pixel rox x2 = down one pixel, left or right n number of pixels


ball on pixel rows left or right wasd = (ball on pixel row  x = left or right n number of pixels) + (ball on pixel row  x1 = left or right n number of pixels) + (ball on pixel row  x2 = left or right n number of pixels)
ball on pixel rows down wasd =  (ball on pixel row  x = down one pixel) + (ball on pixel row  x1 = down one pixel) + (ball on pixel row  x2 = down one pixel)


for y in range ((total down wasd pixels) // (ball on pixel rows down wasd)): # the ball eventually goes to the pixel line the paddle is on.
move the paddle  (ball on pixel rows left or right wasd)

this ends the crypto program
what follows is the sarcasm program


sarcasm starts out with the input from crypto of where the ball will meet the paddle.


if the ball doesn't hit the wall:
ball on pixel row  x = up one pixel, angle_1 = (left or right n number of pixels), angle_2 = (left or right n number of pixels)
ball on pixel row x1 = up one pixel, angle_1 = (left or right n number of pixels), angle_2 = (left or right n number of pixels)
ball on pixel rox x2 = up one pixel, angle_1 = (left or right n number of pixels), angle_2 = (left or right n number of pixels)


else:
#the wall changes the direction of the ball so change the (left to right) or (right to left)
ball on pixel row  x = up one pixel, angle_1 = (left or right n number of pixels), angle_2 = (left or right n number of pixels)
ball on pixel row x1 = up one pixel, angle_1 = (left or right n number of pixels), angle_2 = (left or right n number of pixels)
ball on pixel rox x2 = up one pixel, angle_1 = (left or right n number of pixels), angle_2 = (left or right n number of pixels)


ball on pixel rows left or right wasd = (ball on pixel row  x = left or right n number of pixels) + (ball on pixel row  x1 = left or right n number of pixels) + (ball on pixel row  x2 = left or right n number of pixels)
ball on pixel rows up wasd =  (ball on pixel row  x = up one pixel) + (ball on pixel row  x1 = up one pixel) + (ball on pixel row  x2 = up one pixel)


paddle(middle, left, right):
middle angle 1 = (ball on pixel rows left or right wasd)
middle angle 2 = (ball on pixel rows left or right wasd)
left angle 1 = (ball on pixel rows left or right wasd)
left angle 2 = (ball on pixel rows left or right wasd)
right angle 1 = (ball on pixel rows left or right wasd)
right angle 2 = (ball on pixel rows left or right wasd)
# the paddle meeting the ball can be in three different spots on the paddle;
# middle = deflection,  depending on if the paddle is moving or still, two possible angles
# left = move ball left in variable angles, depending on if the paddle is moving or still, two possible angles
# right = move ball right in variable angles depending, on if the paddle is moving or still, two possible angles


# sarcasm then makes the bricks a input sentence to get to the most valuable brick.
for x in range bricks:
for y in range ((total up wasd pixels) // (ball on pixel rows up wasd)): # the ball eventually goes to the pixel line the brick is on.
x = x,[y = paddle(middle, left, right)] # the ball is moved by the paddle to the pixels the brick is on



each brick is a line of pixels from the paddle up to the brick.
moved through from the paddle up to the brick in reverse order from how the ball fell.
for each row the ball moves left or right some value and eventually meets the intended brick.


then sarcasm moves the paddle through each brick, each brick = a word in the input sentence.
to eventually get the ball to the most valuable brick.
which is when the ball goes to the top of the bricks and bounces down multiple times.


the sarcasm moves the ball to this brick because it is the highest value of sarcasm.
because it is the word with the most matches.
a match can be where the ball breaks a brick.
