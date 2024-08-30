# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Tests for the Fermi-Hubbard model Hamiltonian."""

from __future__ import annotations

import numpy as np
import scipy

import ffsim
from ffsim import cre_a, cre_b, des_a, des_b, fermi_hubbard_1d, fermi_hubbard_2d


def test_fermi_hubbard_1d_open():
    """Test 1-D Fermi-Hubbard model, open boundary conditions."""
    assert dict(
        fermi_hubbard_1d(
            norb=4,
            tunneling=1,
            interaction=2,
            chemical_potential=3,
            nearest_neighbor_interaction=4,
        )
    ) == {
        (cre_a(0), des_a(1)): -1,
        (cre_b(0), des_b(1)): -1,
        (cre_a(1), des_a(0)): -1,
        (cre_b(1), des_b(0)): -1,
        (cre_a(1), des_a(2)): -1,
        (cre_b(1), des_b(2)): -1,
        (cre_a(2), des_a(1)): -1,
        (cre_b(2), des_b(1)): -1,
        (cre_a(2), des_a(3)): -1,
        (cre_b(2), des_b(3)): -1,
        (cre_a(3), des_a(2)): -1,
        (cre_b(3), des_b(2)): -1,
        (cre_a(0), des_a(0), cre_b(0), des_b(0)): 2,
        (cre_a(1), des_a(1), cre_b(1), des_b(1)): 2,
        (cre_a(2), des_a(2), cre_b(2), des_b(2)): 2,
        (cre_a(3), des_a(3), cre_b(3), des_b(3)): 2,
        (cre_a(0), des_a(0)): -3,
        (cre_b(0), des_b(0)): -3,
        (cre_a(1), des_a(1)): -3,
        (cre_b(1), des_b(1)): -3,
        (cre_a(2), des_a(2)): -3,
        (cre_b(2), des_b(2)): -3,
        (cre_a(3), des_a(3)): -3,
        (cre_b(3), des_b(3)): -3,
        (cre_a(0), des_a(0), cre_a(1), des_a(1)): 4,
        (cre_a(0), des_a(0), cre_b(1), des_b(1)): 4,
        (cre_b(0), des_b(0), cre_a(1), des_a(1)): 4,
        (cre_b(0), des_b(0), cre_b(1), des_b(1)): 4,
        (cre_a(1), des_a(1), cre_a(2), des_a(2)): 4,
        (cre_a(1), des_a(1), cre_b(2), des_b(2)): 4,
        (cre_b(1), des_b(1), cre_a(2), des_a(2)): 4,
        (cre_b(1), des_b(1), cre_b(2), des_b(2)): 4,
        (cre_a(2), des_a(2), cre_a(3), des_a(3)): 4,
        (cre_a(2), des_a(2), cre_b(3), des_b(3)): 4,
        (cre_b(2), des_b(2), cre_a(3), des_a(3)): 4,
        (cre_b(2), des_b(2), cre_b(3), des_b(3)): 4,
    }


def test_fermi_hubbard_1d_periodic():
    """Test 1-D Fermi-Hubbard model, periodic boundary conditions."""
    assert dict(
        fermi_hubbard_1d(
            norb=4,
            tunneling=1,
            interaction=2,
            chemical_potential=3,
            nearest_neighbor_interaction=4,
            periodic=True,
        )
    ) == {
        (cre_a(0), des_a(1)): -1,
        (cre_b(0), des_b(1)): -1,
        (cre_a(1), des_a(0)): -1,
        (cre_b(1), des_b(0)): -1,
        (cre_a(1), des_a(2)): -1,
        (cre_b(1), des_b(2)): -1,
        (cre_a(2), des_a(1)): -1,
        (cre_b(2), des_b(1)): -1,
        (cre_a(2), des_a(3)): -1,
        (cre_b(2), des_b(3)): -1,
        (cre_a(3), des_a(2)): -1,
        (cre_b(3), des_b(2)): -1,
        (cre_a(3), des_a(0)): -1,
        (cre_b(3), des_b(0)): -1,
        (cre_a(0), des_a(3)): -1,
        (cre_b(0), des_b(3)): -1,
        (cre_a(0), des_a(0), cre_b(0), des_b(0)): 2,
        (cre_a(1), des_a(1), cre_b(1), des_b(1)): 2,
        (cre_a(2), des_a(2), cre_b(2), des_b(2)): 2,
        (cre_a(3), des_a(3), cre_b(3), des_b(3)): 2,
        (cre_a(0), des_a(0)): -3,
        (cre_b(0), des_b(0)): -3,
        (cre_a(1), des_a(1)): -3,
        (cre_b(1), des_b(1)): -3,
        (cre_a(2), des_a(2)): -3,
        (cre_b(2), des_b(2)): -3,
        (cre_a(3), des_a(3)): -3,
        (cre_b(3), des_b(3)): -3,
        (cre_a(0), des_a(0), cre_a(1), des_a(1)): 4,
        (cre_a(0), des_a(0), cre_b(1), des_b(1)): 4,
        (cre_b(0), des_b(0), cre_a(1), des_a(1)): 4,
        (cre_b(0), des_b(0), cre_b(1), des_b(1)): 4,
        (cre_a(1), des_a(1), cre_a(2), des_a(2)): 4,
        (cre_a(1), des_a(1), cre_b(2), des_b(2)): 4,
        (cre_b(1), des_b(1), cre_a(2), des_a(2)): 4,
        (cre_b(1), des_b(1), cre_b(2), des_b(2)): 4,
        (cre_a(2), des_a(2), cre_a(3), des_a(3)): 4,
        (cre_a(2), des_a(2), cre_b(3), des_b(3)): 4,
        (cre_b(2), des_b(2), cre_a(3), des_a(3)): 4,
        (cre_b(2), des_b(2), cre_b(3), des_b(3)): 4,
        (cre_a(3), des_a(3), cre_a(0), des_a(0)): 4,
        (cre_a(3), des_a(3), cre_b(0), des_b(0)): 4,
        (cre_b(3), des_b(3), cre_a(0), des_a(0)): 4,
        (cre_b(3), des_b(3), cre_b(0), des_b(0)): 4,
    }

    # periodic boundary conditions (edge case)
    assert dict(
        fermi_hubbard_1d(
            norb=2,
            tunneling=1,
            interaction=2,
            chemical_potential=3,
            nearest_neighbor_interaction=4,
            periodic=True,
        )
    ) == {
        (cre_a(0), des_a(1)): -2,
        (cre_b(0), des_b(1)): -2,
        (cre_a(1), des_a(0)): -2,
        (cre_b(1), des_b(0)): -2,
        (cre_a(0), des_a(0), cre_b(0), des_b(0)): 2,
        (cre_a(1), des_a(1), cre_b(1), des_b(1)): 2,
        (cre_a(0), des_a(0)): -3,
        (cre_b(0), des_b(0)): -3,
        (cre_a(1), des_a(1)): -3,
        (cre_b(1), des_b(1)): -3,
        (cre_a(0), des_a(0), cre_a(1), des_a(1)): 4,
        (cre_a(0), des_a(0), cre_b(1), des_b(1)): 4,
        (cre_b(0), des_b(0), cre_a(1), des_a(1)): 4,
        (cre_b(0), des_b(0), cre_b(1), des_b(1)): 4,
        (cre_a(1), des_a(1), cre_a(0), des_a(0)): 4,
        (cre_a(1), des_a(1), cre_b(0), des_b(0)): 4,
        (cre_b(1), des_b(1), cre_a(0), des_a(0)): 4,
        (cre_b(1), des_b(1), cre_b(0), des_b(0)): 4,
    }


def test_fermi_hubbard_2d_open():
    """Test 2-D Fermi-Hubbard model, open boundary conditions."""
    assert dict(
        fermi_hubbard_2d(
            norb_x=2,
            norb_y=2,
            tunneling=1,
            interaction=2,
            chemical_potential=3,
            nearest_neighbor_interaction=4,
        )
    ) == {
        (cre_a(0), des_a(1)): -1,
        (cre_b(0), des_b(1)): -1,
        (cre_a(1), des_a(0)): -1,
        (cre_b(1), des_b(0)): -1,
        (cre_a(0), des_a(2)): -1,
        (cre_b(0), des_b(2)): -1,
        (cre_a(2), des_a(0)): -1,
        (cre_b(2), des_b(0)): -1,
        (cre_a(2), des_a(3)): -1,
        (cre_b(2), des_b(3)): -1,
        (cre_a(3), des_a(2)): -1,
        (cre_b(3), des_b(2)): -1,
        (cre_a(1), des_a(3)): -1,
        (cre_b(1), des_b(3)): -1,
        (cre_a(3), des_a(1)): -1,
        (cre_b(3), des_b(1)): -1,
        (cre_a(0), des_a(0), cre_b(0), des_b(0)): 2,
        (cre_a(1), des_a(1), cre_b(1), des_b(1)): 2,
        (cre_a(2), des_a(2), cre_b(2), des_b(2)): 2,
        (cre_a(3), des_a(3), cre_b(3), des_b(3)): 2,
        (cre_a(0), des_a(0)): -3,
        (cre_b(0), des_b(0)): -3,
        (cre_a(1), des_a(1)): -3,
        (cre_b(1), des_b(1)): -3,
        (cre_a(2), des_a(2)): -3,
        (cre_b(2), des_b(2)): -3,
        (cre_a(3), des_a(3)): -3,
        (cre_b(3), des_b(3)): -3,
        (cre_a(0), des_a(0), cre_a(1), des_a(1)): 4,
        (cre_a(0), des_a(0), cre_b(1), des_b(1)): 4,
        (cre_b(0), des_b(0), cre_a(1), des_a(1)): 4,
        (cre_b(0), des_b(0), cre_b(1), des_b(1)): 4,
        (cre_a(0), des_a(0), cre_a(2), des_a(2)): 4,
        (cre_a(0), des_a(0), cre_b(2), des_b(2)): 4,
        (cre_b(0), des_b(0), cre_a(2), des_a(2)): 4,
        (cre_b(0), des_b(0), cre_b(2), des_b(2)): 4,
        (cre_a(2), des_a(2), cre_a(3), des_a(3)): 4,
        (cre_a(2), des_a(2), cre_b(3), des_b(3)): 4,
        (cre_b(2), des_b(2), cre_a(3), des_a(3)): 4,
        (cre_b(2), des_b(2), cre_b(3), des_b(3)): 4,
        (cre_a(1), des_a(1), cre_a(3), des_a(3)): 4,
        (cre_a(1), des_a(1), cre_b(3), des_b(3)): 4,
        (cre_b(1), des_b(1), cre_a(3), des_a(3)): 4,
        (cre_b(1), des_b(1), cre_b(3), des_b(3)): 4,
    }


def test_fermi_hubbard_2d_periodic():
    """Test 2-D Fermi-Hubbard model, periodic boundary conditions."""
    assert dict(
        fermi_hubbard_2d(
            norb_x=3,
            norb_y=3,
            tunneling=1,
            interaction=2,
            chemical_potential=3,
            nearest_neighbor_interaction=4,
            periodic=True,
        )
    ) == {
        (cre_a(0), des_a(1)): -1,
        (cre_b(0), des_b(1)): -1,
        (cre_a(1), des_a(0)): -1,
        (cre_b(1), des_b(0)): -1,
        (cre_a(0), des_a(3)): -1,
        (cre_b(0), des_b(3)): -1,
        (cre_a(3), des_a(0)): -1,
        (cre_b(3), des_b(0)): -1,
        (cre_a(3), des_a(4)): -1,
        (cre_b(3), des_b(4)): -1,
        (cre_a(4), des_a(3)): -1,
        (cre_b(4), des_b(3)): -1,
        (cre_a(3), des_a(6)): -1,
        (cre_b(3), des_b(6)): -1,
        (cre_a(6), des_a(3)): -1,
        (cre_b(6), des_b(3)): -1,
        (cre_a(6), des_a(7)): -1,
        (cre_b(6), des_b(7)): -1,
        (cre_a(7), des_a(6)): -1,
        (cre_b(7), des_b(6)): -1,
        (cre_a(6), des_a(0)): -1,
        (cre_b(6), des_b(0)): -1,
        (cre_a(0), des_a(6)): -1,
        (cre_b(0), des_b(6)): -1,
        (cre_a(1), des_a(2)): -1,
        (cre_b(1), des_b(2)): -1,
        (cre_a(2), des_a(1)): -1,
        (cre_b(2), des_b(1)): -1,
        (cre_a(1), des_a(4)): -1,
        (cre_b(1), des_b(4)): -1,
        (cre_a(4), des_a(1)): -1,
        (cre_b(4), des_b(1)): -1,
        (cre_a(4), des_a(5)): -1,
        (cre_b(4), des_b(5)): -1,
        (cre_a(5), des_a(4)): -1,
        (cre_b(5), des_b(4)): -1,
        (cre_a(4), des_a(7)): -1,
        (cre_b(4), des_b(7)): -1,
        (cre_a(7), des_a(4)): -1,
        (cre_b(7), des_b(4)): -1,
        (cre_a(7), des_a(8)): -1,
        (cre_b(7), des_b(8)): -1,
        (cre_a(8), des_a(7)): -1,
        (cre_b(8), des_b(7)): -1,
        (cre_a(7), des_a(1)): -1,
        (cre_b(7), des_b(1)): -1,
        (cre_a(1), des_a(7)): -1,
        (cre_b(1), des_b(7)): -1,
        (cre_a(2), des_a(0)): -1,
        (cre_b(2), des_b(0)): -1,
        (cre_a(0), des_a(2)): -1,
        (cre_b(0), des_b(2)): -1,
        (cre_a(2), des_a(5)): -1,
        (cre_b(2), des_b(5)): -1,
        (cre_a(5), des_a(2)): -1,
        (cre_b(5), des_b(2)): -1,
        (cre_a(5), des_a(3)): -1,
        (cre_b(5), des_b(3)): -1,
        (cre_a(3), des_a(5)): -1,
        (cre_b(3), des_b(5)): -1,
        (cre_a(5), des_a(8)): -1,
        (cre_b(5), des_b(8)): -1,
        (cre_a(8), des_a(5)): -1,
        (cre_b(8), des_b(5)): -1,
        (cre_a(8), des_a(6)): -1,
        (cre_b(8), des_b(6)): -1,
        (cre_a(6), des_a(8)): -1,
        (cre_b(6), des_b(8)): -1,
        (cre_a(8), des_a(2)): -1,
        (cre_b(8), des_b(2)): -1,
        (cre_a(2), des_a(8)): -1,
        (cre_b(2), des_b(8)): -1,
        (cre_a(0), des_a(0), cre_b(0), des_b(0)): 2,
        (cre_a(1), des_a(1), cre_b(1), des_b(1)): 2,
        (cre_a(2), des_a(2), cre_b(2), des_b(2)): 2,
        (cre_a(3), des_a(3), cre_b(3), des_b(3)): 2,
        (cre_a(4), des_a(4), cre_b(4), des_b(4)): 2,
        (cre_a(5), des_a(5), cre_b(5), des_b(5)): 2,
        (cre_a(6), des_a(6), cre_b(6), des_b(6)): 2,
        (cre_a(7), des_a(7), cre_b(7), des_b(7)): 2,
        (cre_a(8), des_a(8), cre_b(8), des_b(8)): 2,
        (cre_a(0), des_a(0)): -3,
        (cre_b(0), des_b(0)): -3,
        (cre_a(1), des_a(1)): -3,
        (cre_b(1), des_b(1)): -3,
        (cre_a(2), des_a(2)): -3,
        (cre_b(2), des_b(2)): -3,
        (cre_a(3), des_a(3)): -3,
        (cre_b(3), des_b(3)): -3,
        (cre_a(4), des_a(4)): -3,
        (cre_b(4), des_b(4)): -3,
        (cre_a(5), des_a(5)): -3,
        (cre_b(5), des_b(5)): -3,
        (cre_a(6), des_a(6)): -3,
        (cre_b(6), des_b(6)): -3,
        (cre_a(7), des_a(7)): -3,
        (cre_b(7), des_b(7)): -3,
        (cre_a(8), des_a(8)): -3,
        (cre_b(8), des_b(8)): -3,
        (cre_a(0), des_a(0), cre_a(1), des_a(1)): 4,
        (cre_a(0), des_a(0), cre_b(1), des_b(1)): 4,
        (cre_b(0), des_b(0), cre_a(1), des_a(1)): 4,
        (cre_b(0), des_b(0), cre_b(1), des_b(1)): 4,
        (cre_a(0), des_a(0), cre_a(3), des_a(3)): 4,
        (cre_a(0), des_a(0), cre_b(3), des_b(3)): 4,
        (cre_b(0), des_b(0), cre_a(3), des_a(3)): 4,
        (cre_b(0), des_b(0), cre_b(3), des_b(3)): 4,
        (cre_a(3), des_a(3), cre_a(4), des_a(4)): 4,
        (cre_a(3), des_a(3), cre_b(4), des_b(4)): 4,
        (cre_b(3), des_b(3), cre_a(4), des_a(4)): 4,
        (cre_b(3), des_b(3), cre_b(4), des_b(4)): 4,
        (cre_a(3), des_a(3), cre_a(6), des_a(6)): 4,
        (cre_a(3), des_a(3), cre_b(6), des_b(6)): 4,
        (cre_b(3), des_b(3), cre_a(6), des_a(6)): 4,
        (cre_b(3), des_b(3), cre_b(6), des_b(6)): 4,
        (cre_a(6), des_a(6), cre_a(7), des_a(7)): 4,
        (cre_a(6), des_a(6), cre_b(7), des_b(7)): 4,
        (cre_b(6), des_b(6), cre_a(7), des_a(7)): 4,
        (cre_b(6), des_b(6), cre_b(7), des_b(7)): 4,
        (cre_a(6), des_a(6), cre_a(0), des_a(0)): 4,
        (cre_a(6), des_a(6), cre_b(0), des_b(0)): 4,
        (cre_b(6), des_b(6), cre_a(0), des_a(0)): 4,
        (cre_b(6), des_b(6), cre_b(0), des_b(0)): 4,
        (cre_a(1), des_a(1), cre_a(2), des_a(2)): 4,
        (cre_a(1), des_a(1), cre_b(2), des_b(2)): 4,
        (cre_b(1), des_b(1), cre_a(2), des_a(2)): 4,
        (cre_b(1), des_b(1), cre_b(2), des_b(2)): 4,
        (cre_a(1), des_a(1), cre_a(4), des_a(4)): 4,
        (cre_a(1), des_a(1), cre_b(4), des_b(4)): 4,
        (cre_b(1), des_b(1), cre_a(4), des_a(4)): 4,
        (cre_b(1), des_b(1), cre_b(4), des_b(4)): 4,
        (cre_a(4), des_a(4), cre_a(5), des_a(5)): 4,
        (cre_a(4), des_a(4), cre_b(5), des_b(5)): 4,
        (cre_b(4), des_b(4), cre_a(5), des_a(5)): 4,
        (cre_b(4), des_b(4), cre_b(5), des_b(5)): 4,
        (cre_a(4), des_a(4), cre_a(7), des_a(7)): 4,
        (cre_a(4), des_a(4), cre_b(7), des_b(7)): 4,
        (cre_b(4), des_b(4), cre_a(7), des_a(7)): 4,
        (cre_b(4), des_b(4), cre_b(7), des_b(7)): 4,
        (cre_a(7), des_a(7), cre_a(8), des_a(8)): 4,
        (cre_a(7), des_a(7), cre_b(8), des_b(8)): 4,
        (cre_b(7), des_b(7), cre_a(8), des_a(8)): 4,
        (cre_b(7), des_b(7), cre_b(8), des_b(8)): 4,
        (cre_a(7), des_a(7), cre_a(1), des_a(1)): 4,
        (cre_a(7), des_a(7), cre_b(1), des_b(1)): 4,
        (cre_b(7), des_b(7), cre_a(1), des_a(1)): 4,
        (cre_b(7), des_b(7), cre_b(1), des_b(1)): 4,
        (cre_a(2), des_a(2), cre_a(0), des_a(0)): 4,
        (cre_a(2), des_a(2), cre_b(0), des_b(0)): 4,
        (cre_b(2), des_b(2), cre_a(0), des_a(0)): 4,
        (cre_b(2), des_b(2), cre_b(0), des_b(0)): 4,
        (cre_a(2), des_a(2), cre_a(5), des_a(5)): 4,
        (cre_a(2), des_a(2), cre_b(5), des_b(5)): 4,
        (cre_b(2), des_b(2), cre_a(5), des_a(5)): 4,
        (cre_b(2), des_b(2), cre_b(5), des_b(5)): 4,
        (cre_a(5), des_a(5), cre_a(3), des_a(3)): 4,
        (cre_a(5), des_a(5), cre_b(3), des_b(3)): 4,
        (cre_b(5), des_b(5), cre_a(3), des_a(3)): 4,
        (cre_b(5), des_b(5), cre_b(3), des_b(3)): 4,
        (cre_a(5), des_a(5), cre_a(8), des_a(8)): 4,
        (cre_a(5), des_a(5), cre_b(8), des_b(8)): 4,
        (cre_b(5), des_b(5), cre_a(8), des_a(8)): 4,
        (cre_b(5), des_b(5), cre_b(8), des_b(8)): 4,
        (cre_a(8), des_a(8), cre_a(6), des_a(6)): 4,
        (cre_a(8), des_a(8), cre_b(6), des_b(6)): 4,
        (cre_b(8), des_b(8), cre_a(6), des_a(6)): 4,
        (cre_b(8), des_b(8), cre_b(6), des_b(6)): 4,
        (cre_a(8), des_a(8), cre_a(2), des_a(2)): 4,
        (cre_a(8), des_a(8), cre_b(2), des_b(2)): 4,
        (cre_b(8), des_b(8), cre_a(2), des_a(2)): 4,
        (cre_b(8), des_b(8), cre_b(2), des_b(2)): 4,
    }


def test_fermi_hubbard_2d_2x2_periodic():
    """Test 2x2 2-D Fermi-Hubbard model, periodic boundary conditions."""
    assert dict(
        fermi_hubbard_2d(
            norb_x=2,
            norb_y=2,
            tunneling=1,
            interaction=2,
            chemical_potential=3,
            nearest_neighbor_interaction=4,
            periodic=True,
        )
    ) == {
        (cre_a(0), des_a(1)): -2,
        (cre_b(0), des_b(1)): -2,
        (cre_a(1), des_a(0)): -2,
        (cre_b(1), des_b(0)): -2,
        (cre_a(0), des_a(2)): -2,
        (cre_b(0), des_b(2)): -2,
        (cre_a(2), des_a(0)): -2,
        (cre_b(2), des_b(0)): -2,
        (cre_a(2), des_a(3)): -2,
        (cre_b(2), des_b(3)): -2,
        (cre_a(3), des_a(2)): -2,
        (cre_b(3), des_b(2)): -2,
        (cre_a(1), des_a(3)): -2,
        (cre_b(1), des_b(3)): -2,
        (cre_a(3), des_a(1)): -2,
        (cre_b(3), des_b(1)): -2,
        (cre_a(0), des_a(0), cre_b(0), des_b(0)): 2,
        (cre_a(1), des_a(1), cre_b(1), des_b(1)): 2,
        (cre_a(2), des_a(2), cre_b(2), des_b(2)): 2,
        (cre_a(3), des_a(3), cre_b(3), des_b(3)): 2,
        (cre_a(0), des_a(0)): -3,
        (cre_b(0), des_b(0)): -3,
        (cre_a(1), des_a(1)): -3,
        (cre_b(1), des_b(1)): -3,
        (cre_a(2), des_a(2)): -3,
        (cre_b(2), des_b(2)): -3,
        (cre_a(3), des_a(3)): -3,
        (cre_b(3), des_b(3)): -3,
        (cre_a(0), des_a(0), cre_a(1), des_a(1)): 4,
        (cre_a(0), des_a(0), cre_b(1), des_b(1)): 4,
        (cre_b(0), des_b(0), cre_a(1), des_a(1)): 4,
        (cre_b(0), des_b(0), cre_b(1), des_b(1)): 4,
        (cre_a(0), des_a(0), cre_a(2), des_a(2)): 4,
        (cre_a(0), des_a(0), cre_b(2), des_b(2)): 4,
        (cre_b(0), des_b(0), cre_a(2), des_a(2)): 4,
        (cre_b(0), des_b(0), cre_b(2), des_b(2)): 4,
        (cre_a(2), des_a(2), cre_a(3), des_a(3)): 4,
        (cre_a(2), des_a(2), cre_b(3), des_b(3)): 4,
        (cre_b(2), des_b(2), cre_a(3), des_a(3)): 4,
        (cre_b(2), des_b(2), cre_b(3), des_b(3)): 4,
        (cre_a(2), des_a(2), cre_a(0), des_a(0)): 4,
        (cre_a(2), des_a(2), cre_b(0), des_b(0)): 4,
        (cre_b(2), des_b(2), cre_a(0), des_a(0)): 4,
        (cre_b(2), des_b(2), cre_b(0), des_b(0)): 4,
        (cre_a(1), des_a(1), cre_a(0), des_a(0)): 4,
        (cre_a(1), des_a(1), cre_b(0), des_b(0)): 4,
        (cre_b(1), des_b(1), cre_a(0), des_a(0)): 4,
        (cre_b(1), des_b(1), cre_b(0), des_b(0)): 4,
        (cre_a(1), des_a(1), cre_a(3), des_a(3)): 4,
        (cre_a(1), des_a(1), cre_b(3), des_b(3)): 4,
        (cre_b(1), des_b(1), cre_a(3), des_a(3)): 4,
        (cre_b(1), des_b(1), cre_b(3), des_b(3)): 4,
        (cre_a(3), des_a(3), cre_a(2), des_a(2)): 4,
        (cre_a(3), des_a(3), cre_b(2), des_b(2)): 4,
        (cre_b(3), des_b(3), cre_a(2), des_a(2)): 4,
        (cre_b(3), des_b(3), cre_b(2), des_b(2)): 4,
        (cre_a(3), des_a(3), cre_a(1), des_a(1)): 4,
        (cre_a(3), des_a(3), cre_b(1), des_b(1)): 4,
        (cre_b(3), des_b(3), cre_a(1), des_a(1)): 4,
        (cre_b(3), des_b(3), cre_b(1), des_b(1)): 4,
    }


def test_fermi_hubbard_1d_eigenvalue_spin_balanced():
    """Test eigenvalue of 1-D Fermi-Hubbard model with balanced spins."""
    # open boundary conditions
    op = fermi_hubbard_1d(
        norb=4,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
    )
    ham = ffsim.linear_operator(op, norb=4, nelec=(2, 2))
    eigs, _ = scipy.sparse.linalg.eigsh(ham, which="SA", k=1)
    np.testing.assert_allclose(eigs[0], -9.961978205599)

    # periodic boundary conditions
    op_periodic = fermi_hubbard_1d(
        norb=4,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
        periodic=True,
    )
    ham_periodic = ffsim.linear_operator(op_periodic, norb=4, nelec=(2, 2))
    eigs_periodic, _ = scipy.sparse.linalg.eigsh(ham_periodic, which="SA", k=1)
    np.testing.assert_allclose(eigs_periodic[0], -8.781962448006)

    # periodic boundary conditions (edge case)
    op_periodic_edge = fermi_hubbard_1d(
        norb=2,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
        periodic=True,
    )
    ham_periodic = ffsim.linear_operator(op_periodic_edge, norb=2, nelec=(1, 1))
    eigs_periodic, _ = scipy.sparse.linalg.eigsh(ham_periodic, which="SA", k=1)
    np.testing.assert_allclose(eigs_periodic[0], -6.000000000000)


def test_fermi_hubbard_2d_eigenvalue_spin_balanced():
    """Test eigenvalue of 2-D Fermi-Hubbard model with balanced spins."""
    # open boundary conditions
    op = fermi_hubbard_2d(
        norb_x=2,
        norb_y=2,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
    )
    ham = ffsim.linear_operator(op, norb=4, nelec=(2, 2))
    eigs, _ = scipy.sparse.linalg.eigsh(ham, which="SA", k=1)
    np.testing.assert_allclose(eigs[0], -8.781962448006)

    # periodic boundary conditions (edge case)
    op_periodic_edge = fermi_hubbard_2d(
        norb_x=2,
        norb_y=2,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
        periodic=True,
    )
    ham_periodic = ffsim.linear_operator(op_periodic_edge, norb=4, nelec=(2, 2))
    eigs_periodic, _ = scipy.sparse.linalg.eigsh(ham_periodic, which="SA", k=1)
    np.testing.assert_allclose(eigs_periodic[0], -9.428197577536)


def test_fermi_hubbard_1d_eigenvalue_spin_unbalanced():
    """Test eigenvalue of 1-D Fermi-Hubbard model with unbalanced spins."""
    # open boundary conditions
    op = fermi_hubbard_1d(
        norb=4,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
    )
    ham = ffsim.linear_operator(op, norb=4, nelec=(1, 3))
    eigs, _ = scipy.sparse.linalg.eigsh(ham, which="SA", k=1)
    np.testing.assert_allclose(eigs[0], -6.615276287167)

    # periodic boundary conditions
    op_periodic = fermi_hubbard_1d(
        norb=4,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
        periodic=True,
    )
    ham_periodic = ffsim.linear_operator(op_periodic, norb=4, nelec=(1, 3))
    eigs_periodic, _ = scipy.sparse.linalg.eigsh(ham_periodic, which="SA", k=1)
    np.testing.assert_allclose(eigs_periodic[0], -0.828427124746)


def test_fermi_hubbard_2d_eigenvalue_spin_unbalanced():
    """Test eigenvalue of 2-D Fermi-Hubbard model with unbalanced spins."""
    # open boundary conditions
    op = fermi_hubbard_2d(
        norb_x=2,
        norb_y=2,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
    )
    ham = ffsim.linear_operator(op, norb=4, nelec=(1, 3))
    eigs, _ = scipy.sparse.linalg.eigsh(ham, which="SA", k=1)
    np.testing.assert_allclose(eigs[0], -0.828427124746)

    # periodic boundary conditions (edge case)
    op_periodic_edge = fermi_hubbard_2d(
        norb_x=2,
        norb_y=2,
        tunneling=1,
        interaction=2,
        chemical_potential=3,
        nearest_neighbor_interaction=4,
        periodic=True,
    )
    ham_periodic = ffsim.linear_operator(op_periodic_edge, norb=4, nelec=(1, 3))
    eigs_periodic, _ = scipy.sparse.linalg.eigsh(ham_periodic, which="SA", k=1)
    np.testing.assert_allclose(eigs_periodic[0], 8.743352161722)
