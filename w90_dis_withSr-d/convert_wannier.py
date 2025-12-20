#%%
from triqs_ghostGA.wannier90 import Wannier90Converter
Converter = Wannier90Converter(seedname='smo', rot_mat_type='none')
Converter.convert_dft_input()
# %%
