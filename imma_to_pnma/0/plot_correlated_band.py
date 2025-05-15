import numpy as np
import importlib, sys
import matplotlib.pyplot as plt
from matplotlib import cm
from timeit import default_timer as timer

from ase.io.espresso import read_espresso_in

from h5 import HDFArchive
from solid_dmft.postprocessing import plot_correlated_bands as pcb

'''
kslice = False

bands_config = {'tb': True, 'alatt': True, 'qp_bands': False}
config = bands_config

archive = HDFArchive('./svo.h5','r')
dft_fermi_energy = archive['dft_misc_input']['dft_fermi_energy']

w90_path = './'
w90_dict = {'w90_seed': 'svo', 'w90_path': w90_path, 'mu_tb': dft_fermi_energy, 'n_orb': 14, 'N':1,
            'orbital_order_w90': ['dxz', 'dyz', 'dxy', 'dx2-y2', 'dz2']}

orbital_order_to = ['dxy', 'dxz', 'dyz', 'dx2-y2', 'dz2']
proj_on_orb = None # or 'dxy' etc
'''

scf_in = './svo.scf.in'

# read scf file
atoms = read_espresso_in(scf_in)
# set up cell and path
lat = atoms.cell.get_bravais_lattice()
path = atoms.cell.bandpath('', npoints=100)
kpts_dict = path.todict()['special_points']

for key, value in kpts_dict.items():
    print(key, value)
lat.plot_bz()

'''
# band specs
tb_bands = {'bands_path': [('R', 'G'), ('G', 'X'), ('X', 'M'), ('M', 'G')], 'Z': np.array([0,0,0.5]), 'n_k': 50}
tb_bands.update(kpts_dict)

tb_config = tb_bands

freq_mesh_bands = {'window': [-10, 10], 'n_w': int(1e3)}
freq_mesh = freq_mesh_bands

grisb_path = './svo.h5'

proj_on_orb = orbital_order_to.index(proj_on_orb) if proj_on_orb else None
grisb_dict = {'grisb_path': grisb_path, 'it': 'last_iter', 'orbital_order_grisb': orbital_order_to,
              'eta': 0.05, 'w_mesh': freq_mesh, 'linearize': False, 'proj_on_orb' : proj_on_orb}

plot_config = {'colorscheme_alatt': 'coolwarm', 'colorscheme_bands': 'coolwarm',
               'colorscheme_qpbands': 'Greens', 'vmin': 0.0}

tb_data, alatt_k_w, freq_dict = pcb.get_grisb_bands(fermi_slice=kslice,
                                                    orbital_order_to=orbital_order_to, qp_bands=config['qp_bands'],
                                                    **w90_dict, **tb_config, **grisb_dict)

fig, ax = plt.subplots(1, figsize=(6,3), dpi=200)

pcb.plot_bands(fig, ax, alatt_k_w, tb_data, freq_dict, w90_dict['n_orb'],
               tb=config['tb'], alatt=config['alatt'], qp_bands=config['qp_bands'], **plot_config)
plt.ylabel('ω(eV)')
plt.tight_layout()
Plt.show()
'''
