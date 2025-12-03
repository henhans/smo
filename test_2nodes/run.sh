#/usr/bin/bash

unset SLURM_JOBID
mpirun --bind-to none -np 256 solid_dmft
