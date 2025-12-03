#/usr/bin/bash

unset SLURM_JOBID
mpirun --bind-to none -np 128 solid_dmft
