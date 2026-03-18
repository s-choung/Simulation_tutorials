"""Shared structure-relaxation helpers for the tutorial notebooks."""

from __future__ import annotations

from copy import deepcopy

import numpy as np
from ase.constraints import ExpCellFilter
from ase.optimize import LBFGS


def relax_structure(
    atoms,
    calculator=None,
    *,
    lattice_relax: bool = False,
    copy_atoms: bool = True,
    set_unit_tags: bool = True,
    fmax: float = 0.05,
    steps: int = 100,
    return_atoms: bool = False,
):
    """Relax a structure and optionally return the relaxed atoms."""

    working_atoms = deepcopy(atoms) if copy_atoms else atoms

    if calculator is not None:
        working_atoms.calc = calculator

    if set_unit_tags:
        working_atoms.set_tags(np.ones(len(working_atoms)))

    target = ExpCellFilter(working_atoms) if lattice_relax else working_atoms
    optimizer = LBFGS(target)
    optimizer.run(fmax=fmax, steps=steps)

    energy = working_atoms.get_potential_energy()
    if return_atoms:
        return energy, working_atoms
    return energy
