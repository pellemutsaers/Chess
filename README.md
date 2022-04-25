# Chess
This project was made to settle a beef between two weirdo's who thought making a chess engine is a fun thing to do. It's mainly based on the chess module which allows me to be lazy and not code the entire set of rules chess is notorious for. However, the idea behind it is to try and code the engine part from scratch and optimize it as much as possible and eventually... let our creations battle one another to the death. 

There are two main dependencies consisting of the "chess" and "pygame" modules. I believe I also included Fore from Colorama to print nice red error messages. Other than that, the repo should be good to be deployed. "Random", "math" and "time" are also used, but if you don't have those already, you're just weird. Notice that there is also an executable included for now, which should maybe hopefully work, this is because the engine is actually a bit faster in this form. And goddamn, it's 47 MB, so maybe just ignore it.

For actual usage: run the test2.py file, which should work fine on windows, but will need some slash conversions from forward to backward or the other way around in the places in the code where the directory system is used, for example in when loading the PNGs for the pieces, when using MacOS. Next, you will need to state if any or both players will be the computer. When a human is up to move, you can either type SAN notation and enter by clicking the spacebar, this should appear on the bottom of the pygame window. There is also the option of using the mouse by clicking the beginning en then ending square of a move. Please note, that this for example when promoting isn't possible because of the promoting piece needing to be identified. Computer moves will be made automatically. Please keep an eye on the terminal as this will at times show important information. Note that the pygame window easily crashes.

P.S. (idk if this is a correctly used english abbreviation) I'm very garbage at coding, and as a direct result of that this project itself is also incredibly garbage, please send me your prayers because I will most definitely get demolished.
