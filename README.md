# Snake Game

Welcome to the classic Snake Game implemented in Python using Pygame! 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)

## Introduction

The Snake Game is a timeless classic where the player controls a snake to eat food and grow longer. The objective is to eat as much food as possible without colliding with the walls or the snake's own body. This implementation uses the Pygame library for graphics and game mechanics.

## Features

- Classic snake gameplay
- Increasing difficulty as the snake grows
- Simple and intuitive controls
- Score tracking

## Configuration
To change the field sizes, colors, initial settings, etc., change the corresponding settings in the file
_app/configuration.py_
During startup, the application will check the configuration settings for compatibility with each other.
And in case of an error, an exception will be thrown with the message
## Installation

To run the Snake Game, you need to have Python and Pygame installed on your system or create a virtual environment.

1. Clone the repository:

```bash
git clone https://github.com/SergeyKostylev/pySnake.git
```

2. Go to folder:

```bash
cd pySnake
```

3. Run app:

```bash
python3 start.py
```