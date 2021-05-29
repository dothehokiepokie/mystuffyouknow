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


each left or right pixel the ball is on = a pixel value copied roughly by the paddle
the paddle can guess that the ball moves rought some number of values left or right for each row of pixels and goes to the row the ball meets the paddle.
the wall changes the direction of the ball so changes the wasd and so changes the left or right pixels the paddle moves too.


the ball eventually goes to the pixel line the paddle is on.
this pixel line = a value of left or right pixels for the paddle to move to meet the ball.


the paddle meeting the ball can be in three different spots on the paddle;
middle
left
right


from google:
"
Most Breakout clones take the position of the ball where it hits the paddle and use that to affect the angle. If it hits the left then it goes left, and vice versa. But only the outer edges might actually change the angle or force. The middle of the paddle would only mirror the Y speed.


Some will take into account the speed the paddle and ball are moving as well.


And some, the badly coded ones, will always use 45º angles.


Also some will put checks in to detect if the ball has not hit the paddle in a certain amount of time and assumes it's stuck in a loop between the walls and some unbreakable blocks and will change its angle very slightly to help it get back into the game.


You could do some research on YouTube with playthroughs of some Breakout clones. My favorite is Thunder and Lightning. I believe this one only changes the angle from 45º to 30º if you are moving when you hit the ball. Really it's all up to the developer to use your own method.
"
https://love2d.org/forums/viewtopic.php?p=189361&sid=f45ac6f0ef6f22861bf1b0e60b3348fa#p189361


sarcasm starts out with the input from crypto of where the ball will meet the paddle.


sarcasm then makes the bricks a input sentence to get to the most valuable brick.
each brick is a line of pixels from the paddle up to the brick.
moved through from the paddle up to the brick in reverse order from how the ball fell.
for each row the ball moves left or right some value and eventually meets the intended brick.


then sarcasm moves the paddle throguh each brick each brick = a word in the input sentence.
to point the ball at the most valuable brick.
then the ball goes to the top of the bricks and bounces down multiple times.


the sarcasm moves the ball to this brick because it is the highest value of sarcasm.
because it is the word with the most matches.
a match can be where the ball breaks a brick.
