import numpy as np
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.local_env import VoronoiNN
from pymatgen.io.ase import AseAtomsAdaptor  # Import the ASE to Pymatgen converter

def get_surface_sites(adslab): # input type: adslab

    pymatgen_structure = AseAtomsAdaptor.get_structure(adslab)
    a = SpacegroupAnalyzer(pymatgen_structure)
    ucell = a.get_symmetrized_structure()
    cn_dict = {}
    v = VoronoiNN()
    unique_indices = [equ[0] for equ in ucell.equivalent_indices]
    for i in unique_indices:
        el = ucell[i].species_string
        if el not in cn_dict.keys():
            cn_dict[el] = []
        cn = v.get_cn(ucell, i, use_weights=True)
        cn = float("%.5f" % (round(cn, 5)))
        if cn not in cn_dict[el]:
            cn_dict[el].append(cn)
    v = VoronoiNN()
    surf_sites =  []
    z_median = np.median([site.frac_coords[2] for site in pymatgen_structure]) # z_median are considered as top surface sites.A cutoff value (cutoff
    
    for i, site in enumerate(pymatgen_structure):
        if site.frac_coords[2] > z_median:  # Consider only top surface sites
            cutoff = 1 # Surface에서 minimum coordination + cutoff_value 이하인것만 surface sites로 identify
            try:
                cn = float("%.5f" % (round(v.get_cn(pymatgen_structure, i, use_weights=True), 5)))
                if cn < min(cn_dict[site.specie.symbol]) + cutoff:
                    surf_sites.append(site)
            except RuntimeError:
                surf_sites.append(site)
    return surf_sites

'''
# example usage: 
#"undercoordinated되어있다?--> surface일거다." 는 가정(bulk가 surface보다 Coordination number(CN)이 일반적으로 높으니까.)으로 짜여있고, 
# cutoff value만큼 undercoord범위를 늘림. 
# cutoff를 조정하면 surface sites를 덜 찾을거라서 optimum point를 찾아야됨. OC에서는 cutoff를 몇으로 했는지 참고하면 좋을듯함. 

from site_finder import get_surface_sites
surf_sites_dict = get_surface_sites(adslab)
print("Top Surface Sites:")
for site, index in surf_sites_dict["top"]:
    print("Index:", index, "Element:", site.specie.symbol, "Coordinates:", site.coords)

'''
