# <ins>The Last Cookie</ins>

##by: Jo Baker,  Anna Robertson, Funmi Falegan, Karan Kaur & Ahartisha Selakanabarajah


###**1. What are we building?**

We are building a mystery, puzzle solver text adventure game based on object-oriented programming.

###**2. What does it do?**

The player is playing a detective that must solve the mystery of who ate the last cookie from the cookie jar. They will move through the game solving puzzles to find clues as to who the cookie eater is.

To interrogate the suspects, the detective must solve a puzzle – if successful the suspect/witness gives up a clue.

###**3. Key features**

The game will feature:

-	Rooms
-	Puzzles
-	Items/Journal
-	A system to win or lose – number of guesses – guess right = win, guess wrong =  lose
-	Graphics if time allows

###**4. Sample Architecture** 

The game will be created using python in the backend.
This will include files building classes for:

####<ins>Main character</ins>

- Name of character 
- Getters and setters for description

####<ins>Suspects</ins>
- Name of suspect
- Getters and setters for description
- Getters and setters for relationship to the other characters
- Getters and setters for why they are there
- Getters and setters for motive for eating the cookie
- Getters and setters for the room they are in
- Getters and setters for their dialogue

####<ins>Rooms</ins>
- Name of room
- Getters and setters for room description
- Getters and setters for suspect(s) in the room
- Getters and setters for item(s) in the room

####<ins>Items</ins>
- Name of the item
- Description of the item
- Item ability (healing etc)

####<ins>Puzzles</ins>
- A collection of the different puzzles that must be solved

####<ins>Main file</ins>

**A main file for running the various objects of the game.**

- Set the character
- Set the suspects
- Set the rooms and their connections to create a map
- Set the puzzles for the rooms
- Potentially set randomisation for replayability 

####<ins>A game info file</ins>
- Set the authors of the game
- Set a welcome message
- Set a static method for game info
- Set a class method for credits 

####<ins>Testing</ins>
- Using pytest and unittest to mock inputs for the game

###**5. Team approach** 

-	Funmi: Suspect class
-	Tish: Room class
-	Jo: Item class
-	Anna: game info file
-	Karan: main character class

We will each work on a room and suspect design and each create a puzzle. We will all design the dialogue/script and work
on tests for the parts of the game we create together.

