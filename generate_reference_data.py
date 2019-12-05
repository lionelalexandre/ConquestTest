#!/usr/local/bin/python3

from env import set_env

cq_exe = "Conquest_master" # Conquest executable
nprocs = 1                 # Number of MPI process for CONQUEST
pp_path = "/Users/zamaan/Conquest/PPDB/" # Path to pseudo database
makeion_exe = "MakeIonFiles"             # MakeIonFiles executable
ase_path = "/Users/zamaan/Conquest/ase/conquest" # path to ASE (CONQUEST) root
set_env(cq_exe, nprocs, pp_path, makeion_exe, ase_path)

from water_molecule import run_water_molecule
from diamond import run_diamond
from silicon import run_silicon
from diamond_mssf import run_diamond_mssf
from pto import run_pto
from ice import run_ice
from mgo import run_mgo

run_water_molecule(1, ref=True)
set_env(cq_exe, 4, pp_path, makeion_exe, ase_path)
run_diamond(2, ref=True)
run_silicon(3, ref=True)
run_diamond_mssf(4, ref=True)
set_env(cq_exe, 2, pp_path, makeion_exe, ase_path)
run_pto(5, ref=True)
set_env(cq_exe, 4, pp_path, makeion_exe, ase_path)
run_ice(6, ref=True)
run_mgo(7, ref=True)
