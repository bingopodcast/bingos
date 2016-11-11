#!/bin/bash

cd /home/nbaldridge/bingo_emulator

killall -9 python
python menu.py $1
