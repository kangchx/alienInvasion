<p align="center">
    <h1 align="center">ALIENINVASION</h1>
</p>
<p align="center">
    <em>Ship Shooting Game</em>
</p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
   <img src="https://img.shields.io/badge/Pygame-3776AB.svg?style=default&logo=pygame&logoColor=white" alt="PyGame">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Modules](#modules)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The Alien Invasion project is an ship shooting game designed to challenge players by defending against waves of descending aliens. The game features a player-controlled spaceship, interactive buttons for navigation, and dynamically updated scores and game statistics. Alien, bullet, and ship classes interact to facilitate actions such as shooting and dodging, enhancing playability. Settings ensure customizable game configurations, promoting varied difficulty levels.

---

##  Repository Structure

```sh
└── alienInvasion/
    ├── alien.py
    ├── alienInvasion.py
    ├── bullet.py
    ├── button.py
    ├── gameStats.py
    ├── main.py
    ├── README.md
    ├── scoreBoard.py
    ├── screenStart.py
    ├── settings.py
    ├── ship.py
    ├── requirements.txt
    ├── images
    │   ├── alien.bmp
    │   └── ship.bmp
```

---

##  Modules

<details open><summary>.</summary>

| File                                 | Summary |
| ---                                  | --- |
| [alien.py](alien.py)                 | `alien.py` defines the Alien class, encapsulating behavior and attributes of aliens in the Alien Invasion game, such as initialization, movement across and down the screen, and boundary checks to determine screen edge and bottom collisions. It interacts closely with game settings and the main game class for functionality.                   |
| [alienInvasion.py](alienInvasion.py) | Manages the core gameplay mechanics and user interactions for the Alien Invasion game, including initializing game components, processing user inputs, updating game states, and managing game screens. It integrates various modules like settings, game statistics, and screen displays to facilitate the games operation.                         |
| [bullet.py](bullet.py)               | Manages bullet functionality within the Alien Invasion game, creating, updating, and drawing bullets that the ship fires.                     |
| [button.py](button.py)               | `button.py` defines the Button class for creating interactive elements in the AlienInvasion game, managing the graphical rendering, positioning, and display of buttons with customizable messages, enhancing user interface capabilities within the games architecture.                                                                               |
| [gameStats.py](gameStats.py)         | `gameStats.py` tracks and updates game statistics in Alien Invasion, managing player scores, levels, and remaining ships. It initializes game states, such as active or paused statuses, and ensures the high score persists across sessions without resetting.                                                                                        |
| [main.py](main.py)                   | `main.py` serves as the entry point for the Alien Invasion game, where an Alien Invasion instance is created and the main game loop is initiated, managing the core gameplay mechanics and user interactions as defined in the alienInvasion.py and associated modules within the repository.                                                          |
| [scoreBoard.py](scoreBoard.py)       | `scoreBoard.py` manages the visual representation of scoring within the Alien Invasion game, dynamically displaying and updating player scores, high scores, and levels using pygame for rendering text-based graphics strategically positioned on the game screen. It ensures score information is consistently refreshed and accurately displayed.   |
| [screenStart.py](screenStart.py)     | `screenStart.py` establishes the introductory screen for the Alien Invasion game, setting up text instructions and initial configuration using Pygame. It visually prepares and organizes screen elements, providing users with navigation and gameplay controls before the game begins.                                                               |
| [settings.py](settings.py)           | `settings.py` centralizes configuration management for the Alien Invasion game, maintaining both static and dynamic parameters such as screen size, ship limits, and bullet properties, facilitating easy adjustments to gameplay mechanics and difficulty progression through methods that scale game speed and scoring.                              |
| [ship.py](ship.py)                   | `ship.py` manages the player-controlled spaceship in the Alien Invasion game, handling its initialization, movements, and rendering. The ship is critical for player interaction, supporting bidirectional movement and re-spawning mechanisms without recreation of the ship instance, integrating closely with game settings and display components. |
| [requirements.txt](requirements.txt)                   | Contains packages needed. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `3.12.2`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the repository:
>
> ```console
> $ git clone https://github.com/kangchengX/alienInvasion.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd alienInvasion
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Use the command below:
> ```console
> $ python main.py
> ```

---

##  Acknowledgments

Thanks for turing's python book, which is the basis of the project, and first led me to the colorful python world.

[**Return**](#overview)

---
