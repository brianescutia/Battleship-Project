
Battleship Game

This project implements a console-based Battleship game in Python. Players can place ships on a grid and take turns firing at each other's ships until all ships of one player are destroyed.

Features

    * Board Setup: Players can place their ships on a grid by specifying coordinates and orientation.
    * Firing Mechanics: Players take turns to fire at their opponent's ships, with the board updating based on hits and misses.
    * Ship Models: Different ship types with specific lengths are supported.
    * Game Over Detection: The game ends when all ships of one player are destroyed.
  
Files Included

    * board.py: Contains the Board, PlacementBoard, and FiringBoard classes that manage the game board, ship placement, and firing mechanics.
    * main.py: The main script that runs the game, handling player input, ship placement, firing, and checking for the game over condition.
    * readfile.py: Contains the ReadFile class, which reads the configuration file to set up the game board and ship types.
    * ship.py: Defines the Ship and Coordinates classes, representing ships and their positions on the board, and ShipModels for managing ship information.

Getting Started

Prerequisites

    * Python 3.x

Installation

    * Clone the repository:
    * git clone https://github.com/your-username/repo-name.git
    * cd repo-name

Run the game:

    * python3 main.py

Game Overview
Ship Placement
    Each player must place their ships on the board by providing the starting coordinates and the orientation (horizontal or vertical).

Firing
    Players take turns firing at their opponent's grid. The game board updates to show hits (X) and misses (O).

Winning the Game
    The game continues until all ships of one player are destroyed. The first player to destroy all the opponent's ships wins.

Example Output
Ship Placement Example:

Player 1, enter the orientation of your Battleship, which is 4 long: horizontal

Player 1, enter the starting location for your Battleship, which is 4 long: 1 1

Firing Example:
Player 1's Firing Board
* * * * * 
* * O * * 
* * * * * 
* * * * * 
* * * * * 

Player 1's Placement Board.
* * * * * 
* B B B B 
* * * * * 
* * * * * 
* * * * * 

Player 1, enter the location you want to fire at in the form row col: 2 1

Player 1 hit Player 2's Destroyer!

Notes

    * The game currently supports only two players.
    * All input is managed through the console, with players taking turns on the same machine.
    * Future improvements could include adding AI for single-player mode 
    
Authors
Brian Escutia


