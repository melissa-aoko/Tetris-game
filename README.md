# Tetris Game

A classic Tetris game implemented in Python using the **Pygame** library.
Experience smooth block movement, rotation, line clearing, score tracking, and next-piece preview in a clean, object-oriented design.

---

## Features

* Classic Tetris gameplay mechanics: falling tetrominoes, rotation, and line clearing
* Next piece preview panel
* Score tracking and game-over conditions
* Modular design with separate classes for blocks, grid, and game logic
* Built with Python 3 and Pygame for graphical interface

---

## Demo

Watch the gameplay demo here:
[![Tetris Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://youtu.be/YOUR_VIDEO_ID)

---

## Installation

1. Make sure you have Python 3 installed:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Install Pygame library:

   ```bash
   pip install pygame
   ```

3. Clone this repository:

   ```bash
   git clone https://github.com/melissa-aoko/tetris-game.git
   cd tetris-game
   ```

---

## How to Play

Run the main script:

```bash
python main.py
```

**Controls:**

* Left Arrow: Move block left
* Right Arrow: Move block right
* Down Arrow: Move block down faster
* Up Arrow: Rotate block
* Press any key to restart after Game Over
* Close the window to quit the game

---

## Project Structure

* `main.py` – Main game loop and event handling
* `game.py` – Game logic, block spawning, scoring, and state management
* `block.py` / `blocks.py` – Tetromino shape classes and movement logic
* `grid.py` – Grid management and line clearing
* `position.py` – Helper class for block coordinates
* `colors.py` – Color definitions for blocks and UI

---

## Future Improvements

* Add sound effects and music
* Implement hold piece functionality
* Add levels with increasing speed
* Save high scores locally or online
* Create a web-based version with JavaScript and Canvas

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Created by Melissa Aoko
[GitHub](https://github.com/melissa-aoko) | [Portfolio](https://melissa-aoko.github.io/personal-portfolio/)

---

