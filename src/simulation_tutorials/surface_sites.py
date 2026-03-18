"""Surface-site search helpers extracted from the original tutorial script."""

from __future__ import annotations

import numpy as np
from pymatgen.analysis.local_env import VoronoiNN
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def get_surface_sites(adslab, *, coordination_buffer: float = 1.0):
    """Return under-coordinated sites on the top side of an adsorbate slab."""

    pymatgen_structure = AseAtomsAdaptor.get_structure(adslab)
    analyzer = SpacegroupAnalyzer(pymatgen_structure)
    symmetrized = analyzer.get_symmetrized_structure()

    cn_dict = {}
    voronoi = VoronoiNN()
    unique_indices = [equivalent_group[0] for equivalent_group in symmetrized.equivalent_indices]

    for index in unique_indices:
        element = symmetrized[index].species_string
        cn_dict.setdefault(element, [])
        coordination_number = float(f"{round(voronoi.get_cn(symmetrized, index, use_weights=True), 5):.5f}")
        if coordination_number not in cn_dict[element]:
            cn_dict[element].append(coordination_number)

    surface_sites = []
    z_median = np.median([site.frac_coords[2] for site in pymatgen_structure])

    for index, site in enumerate(pymatgen_structure):
        if site.frac_coords[2] <= z_median:
            continue

        try:
            coordination_number = float(
                f"{round(voronoi.get_cn(pymatgen_structure, index, use_weights=True), 5):.5f}"
            )
            if coordination_number < min(cn_dict[site.specie.symbol]) + coordination_buffer:
                surface_sites.append(site)
        except RuntimeError:
            surface_sites.append(site)

    return surface_sites
