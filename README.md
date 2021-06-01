# rock-paper-scissors

# Description
  + This game allows the user to play Rock, Paper, Scissors against a computer.
  + The computer will randomly select a move by utilizing the 'random' module.


# Modules Needed
import random
import os
import dotenv

# Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip


'''PLEASE NOTE - Some of the code below was adapted from the README.md from the my-first-repo exercise
'''

## Installation

1. Fork this [remote repository](https://github.com/ts2905/rock-paper-scissors) under your own control, then "clone" or download your remote copy onto your local computer.
2. Navigate to the repository using Git Bash or your preferred shell:

```sh
cd rock-paper-scissors
```

3. Use Anaconda to create and activate a new virtual environment, perhaps called "rps-env":

```sh
conda create -n rps-env python=3.8
conda activate rps-env
```

4. After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

* Edit the .env file with the player's desired username.


## Usage

* Run the game script:

```py
python game.py