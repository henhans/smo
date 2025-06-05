#/usr/bin/bash
module load gompi/espresso
ulimit -s hard
nohup mpirun --bind-to numa -np 64 solid_dmft > output.log 2>&1 &
