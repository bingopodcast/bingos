declare -x LD_LIBARARY_PATH="/usr/local/lib"
cd /home/nbaldridge/proc/bingo_emulator
ssh pi@10.0.0.51 reboot &
ssh pi@10.0.0.52 reboot &
./start_game.sh bright_lights
