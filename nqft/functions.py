"""This module contains global functions used in the
expression and operation on Hubbard hamiltonian and
other Fock space operations.
"""

import glob
import numpy as np
from qutip import Qobj


def scalar(m: Qobj, n=None) -> float:
    """Computes scalar product for Fock space vectors such as

                    scalar(m, n) = < m | n >.

    Parameters
    ----------
    m: qutip.Qobj, default=None
        Bra on which perform scalar product.
    n: qutip.Qobj, default=None
        Ket on which perform scalar product.

    Returns
    -------
    -: int, float
        Result of scalar product.
    """
    if n:
        val = m.dag() * n
    else:
        val = m.dag() * m
    return val.tr()


def delta(j: int, k: int) -> float:
    """Kronecker delta function.

    Parameters
    ----------
    j: int, default=None
        First indice.
    k: int, default=None
        Second indice.

    Returns
    -------
    -: float (0.0 or 1.0)
    """
    return 1.0 if j == k else 0.0


def read_fermi_arc(path="./nqft/Data/fermi_arc_data/") -> dict:
    """Read Peter's data on spectral weight at Fermi
    level for a given number of sites.

    Parameters
    ----------
    path: str, default="./nqft/Data/fermi_arc_data/"
        Path to data directory.

    Returns
    -------
    arcs: dict, size=6
        A dict containing all spectral functions.
    """
    files = glob.glob(f"{path}*.npy")
    extensions = [file.split("_")[-1].split(".")[0] for file in files]
    arcs = {ext: np.load(file) for ext, file in zip(extensions, files)}

    return arcs


def flatten_fermi_arc(save_path="./nqft/Data/fermi_arc_data_1D/") -> None:
    """Saves Peter's Fermi arc numpy 2D arrays files as 1D
    arrays numpy files so they can be read in Rust/C.

    Parameters
    ----------
    save_path: str, default="./nqft/Data/fermi_arc_data_1D/"
        Path where to save flatten arrays.

    Returns
    -------
    None
    """
    arcs_files = read_fermi_arc()
    for (ext, array) in arcs_files.items():
        flat_array = np.ravel(array)
        np.save(f'{save_path}Akw_{ext}.npy', flat_array)
    return


def find_nearest(array, value):
    """Finds index in given array of the closest value
    of parameter 'value'.

    Parameters
    ----------
    array: array-like, shape=(m, n), default=None
        Array in which search for the value.

    value: int, float, default=None
        Value to search for in array.

    Returns
    -------
    idx: int
        Index at which user can find the closest value in array.
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


if __name__ == "__main__":
    flatten_fermi_arc()
