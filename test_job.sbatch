#!/bin/bash
#
#SBATCH --job-name=DEREK_TEST
#SBATCH --output=hello_out.txt
#SBATCH --time=1:00
#SBATCH --mem-per-cpu=100

srun Hello_World.sh
