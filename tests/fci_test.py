# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Tests for FCI utils."""

from __future__ import annotations

import itertools
from typing import Sequence, cast

import numpy as np
import pytest

import ffsim
from ffsim.fci import (
    contract_diag_coulomb,
    contract_num_op_sum,
    diag_coulomb_to_linop,
    get_dimension,
    num_op_sum_to_linop,
)
from ffsim.states import slater_determinant


@pytest.mark.parametrize("norb", [4, 5])
def test_contract_diag_coulomb(norb: int):
    """Test contracting a diagonal Coulomb matrix."""
    rng = np.random.default_rng()
    for _ in range(50):
        n_alpha = rng.integers(1, norb + 1)
        n_beta = rng.integers(1, norb + 1)
        nelec = (n_alpha, n_beta)
        alpha_orbitals = cast(Sequence[int], rng.choice(norb, n_alpha, replace=False))
        beta_orbitals = cast(Sequence[int], rng.choice(norb, n_beta, replace=False))
        occupied_orbitals = (alpha_orbitals, beta_orbitals)
        state = slater_determinant(norb, occupied_orbitals)

        mat = ffsim.random.random_real_symmetric_matrix(norb, seed=rng)
        mat_alpha_beta = ffsim.random.random_real_symmetric_matrix(norb, seed=rng)
        result = contract_diag_coulomb(
            state, mat, norb=norb, nelec=nelec, mat_alpha_beta=mat_alpha_beta
        )

        eig = 0
        for i, j in itertools.product(range(norb), repeat=2):
            for sigma, tau in itertools.product(range(2), repeat=2):
                if i in occupied_orbitals[sigma] and j in occupied_orbitals[tau]:
                    this_mat = mat if sigma == tau else mat_alpha_beta
                    eig += 0.5 * this_mat[i, j]
        expected = eig * state

        np.testing.assert_allclose(result, expected, atol=1e-8)


@pytest.mark.parametrize("norb", [4, 5])
def test_contract_diag_coulomb_z_representation(norb: int):
    """Test contracting a diagonal Coulomb matrix in the Z representation."""
    rng = np.random.default_rng()
    for _ in range(50):
        n_alpha = rng.integers(1, norb + 1)
        n_beta = rng.integers(1, norb + 1)
        nelec = (n_alpha, n_beta)
        alpha_orbitals = cast(Sequence[int], rng.choice(norb, n_alpha, replace=False))
        beta_orbitals = cast(Sequence[int], rng.choice(norb, n_beta, replace=False))
        occupied_orbitals = (alpha_orbitals, beta_orbitals)
        state = slater_determinant(norb, occupied_orbitals)

        mat = ffsim.random.random_real_symmetric_matrix(norb, seed=rng)
        mat_alpha_beta = ffsim.random.random_real_symmetric_matrix(norb, seed=rng)
        result = contract_diag_coulomb(
            state,
            mat,
            norb=norb,
            nelec=nelec,
            mat_alpha_beta=mat_alpha_beta,
            z_representation=True,
        )

        eig = 0
        for a, b in itertools.combinations(range(2 * norb), 2):
            sigma, i = divmod(a, norb)
            tau, j = divmod(b, norb)
            sign_i = -1 if i in occupied_orbitals[sigma] else 1
            sign_j = -1 if j in occupied_orbitals[tau] else 1
            this_mat = mat if sigma == tau else mat_alpha_beta
            eig += 0.25 * sign_i * sign_j * this_mat[i, j]
        expected = eig * state

        np.testing.assert_allclose(result, expected, atol=1e-8)


@pytest.mark.parametrize("norb", [4, 5])
def test_contract_num_op_sum(norb: int):
    """Test contracting sum of number operators."""
    rng = np.random.default_rng()
    for _ in range(50):
        n_alpha = rng.integers(1, norb + 1)
        n_beta = rng.integers(1, norb + 1)
        nelec = (n_alpha, n_beta)
        alpha_orbitals = cast(Sequence[int], rng.choice(norb, n_alpha, replace=False))
        beta_orbitals = cast(Sequence[int], rng.choice(norb, n_beta, replace=False))
        occupied_orbitals = (alpha_orbitals, beta_orbitals)
        state = slater_determinant(norb, occupied_orbitals)

        coeffs = rng.standard_normal(norb)
        result = contract_num_op_sum(state, coeffs, norb=norb, nelec=nelec)

        eig = 0
        for i in range(norb):
            for sigma in range(2):
                if i in occupied_orbitals[sigma]:
                    eig += coeffs[i]
        expected = eig * state

        np.testing.assert_allclose(result, expected, atol=1e-8)


def test_diag_coulomb_to_linop():
    """Test converting a diagonal Coulomb matrix to a linear operator."""
    norb = 5
    rng = np.random.default_rng()
    n_alpha = rng.integers(1, norb + 1)
    n_beta = rng.integers(1, norb + 1)
    nelec = (n_alpha, n_beta)
    dim = get_dimension(norb, nelec)

    mat = ffsim.random.random_real_symmetric_matrix(norb, seed=rng)
    vec = ffsim.random.random_statevector(dim, seed=rng)

    linop = diag_coulomb_to_linop(mat, norb=norb, nelec=nelec)
    result = linop @ vec
    expected = contract_diag_coulomb(vec, mat, norb=norb, nelec=nelec)

    np.testing.assert_allclose(result, expected, atol=1e-8)


def test_num_op_sum_to_linop():
    """Test converting a diagonal Coulomb matrix to a linear operator."""
    norb = 5
    rng = np.random.default_rng()
    n_alpha = rng.integers(1, norb + 1)
    n_beta = rng.integers(1, norb + 1)
    nelec = (n_alpha, n_beta)
    dim = get_dimension(norb, nelec)

    coeffs = rng.standard_normal(norb)
    vec = ffsim.random.random_statevector(dim, seed=rng)

    linop = num_op_sum_to_linop(coeffs, norb=norb, nelec=nelec)
    result = linop @ vec
    expected = contract_num_op_sum(vec, coeffs, norb=norb, nelec=nelec)

    np.testing.assert_allclose(result, expected, atol=1e-8)
