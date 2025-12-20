#!/bin/bash                                                                      
#SBATCH --nodes=2
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=128
#SBATCH --job-name=test
#SBATCH -p ccq
#SBATCH -C rome
#SBATCH --time=48:00:00

echo $LD_LIBRARY_PATH
./run.sh >> out.log
