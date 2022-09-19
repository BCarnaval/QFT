# /usr/bin/env python3

"""Module de test des fonctionnalités de la librairie
Python Qutip. Les états ici discutés possèdent la forme

  --------------------------------------- (c^dagger_1)^n_1 up
 |
 |   ------------------------------------ (c^dagger_2)^n_2 up
 |  |                                             .
 |  |                                             .
 |  |                                             .
 |  |                                       
 |  |         --------------------------- (c^dagger_1)^n_1 down
 |  |        |
 |  |        |   ------------------------ (c^dagger_2)^n_2 down
 |  |        |  |                                 .
 |  |        |  |                                 .
 |  |        |  |                                 .
(      ...        ...)ket{0}
"""

from numpy.random import randint
from qutip import (Qobj, basis, create, destroy, num, tensor, identity)


SITES = 2
vaccum = basis(2)
creation = create(2)
anihilation = destroy(2)
number = num(2)
I = identity(2)


def scalar(m: Qobj, n=None):
  """Computes scalar product for Fock space vectors.

  scalar(m, n) = < m | n >.
  """
  if n:
    val = m.dag()*n
  else:
    val = m.dag()*m
  return val.tr()


def get_state(state: int, type="ket"):
    """Gives array-like representation of given state using 
    Qutip 'tensor' function.

    Parameters
    ----------
    state: int, default=None
        Integer representing state number in Fock space.
    type: str, default='ket'
        Type of vector outputed (bra, ket)

    Returns
    -------
    bra, ket: qutip.Qobj, shape (4^SITES, 1)
        Full vector representation.
    """
    binairy = format(state, 'b').zfill(SITES*2)
    ket = [*binairy]

    vec_state = []
    for presence in ket:
        if int(presence):
            vec_state.append(creation*vaccum)
        else:
            vec_state.append(vaccum)

    if type == "bra":
        return tensor(*vec_state).dag()
    elif type == "ket":
        return tensor(*vec_state)


def get_H(model: str, U: int, **kwargs):
    """Outputs the hamiltonian of specified many-body model.

    Parameters
    ----------
    model: str, default=None
        Fermions network configuration.
    U: int, default=None
        Module of interaction between fermions.
    **kwargs:
        t: int, default=None
            Probability amplitude for fermions to jump.

    Returns
    -------
    H: qutip.Qobj, shape (4^SITES, 4^SITES)
        Tensor object representing hamitonian for given 'model'.
    """
    if model == "Hubbard":
        H1, H2 = 0, 0
        t, = kwargs.values()

        for idx in range(SITES):
            sites = [i for i in range(SITES)]
            ops_1 = [I for i in range(SITES*2)]

            ops_1[idx] = number
            ops_1[SITES + idx] = number

            sites.remove(idx)
            H1 += tensor(*ops_1)

            for ext in sites:
                ops_2_up = [I for i in range(SITES*2)]
                ops_2_down = [I for i in range(SITES*2)]

                ops_2_up[idx] = creation
                ops_2_up[ext] = anihilation

                ops_2_down[SITES + idx] = creation
                ops_2_down[SITES + ext] = anihilation

                H2 += tensor(*ops_2_up) + tensor(*ops_2_down)

        H = U*H1 - t*H2

    elif model == "AIM" and SITES == 2:
        mu, theta, e = kwargs.values()

        H1 = tensor(I, number, I, number)
        H2 = tensor(I, number, I, I) + tensor(I, I, I, number)
        H3 = tensor(creation, anihilation, I, I) + tensor(anihilation,
                creation, I, I) + tensor(I, I, creation, anihilation) + tensor(I, I, anihilation, creation)
        H4 = tensor(number, I, I, I) + tensor(I, I, number, I)

        H = U*H1 - mu*H2 - theta*H3 + (e - mu)*H4

    return H


def get_E(H: Qobj, states: list):
    """Outputs a matrix element (energy) from the hamiltonian using 
    given kets on which perform projection.

    Parameters
    ----------
    model: str, default=None
        Fermions network configuration.
    states: array-like, shape (2, 1), default=None
        Vectors used to process scalar product on H.
        (ex: states=[bra, ket] as integers to convert from binairy)

    Returns
    -------
    E: qutip.Qobj.bra, shape (1, 1)
        Representation of projected vectors on H (energy).
    """
    bra, ket = get_state(states[0], type="bra"), get_state(states[1])
    E = bra*H*ket

    return E.tr()


def lanczos(H: Qobj, iters: int):
  """Docs
  """
  dim = H.shape[0]
  state = randint(dim - 1)
  phi_n = get_state(state=state)

  for iter in range(iters):
    if iter == 0:
      a_n = H.matrix_element(phi_n.dag(), phi_n) / scalar(phi_n)
      phi_n_plus = H*phi_n - a_n*phi_n

    else:
      a_n = H.matrix_element(phi_n_plus.dag(), phi_n_plus) / scalar(phi_n_plus)
      b_n = I.matrix_element(phi_n_plus.dag(), phi_n_plus) / scalar(phi_n)
      phi_n_plus = H*phi_n_plus - a_n*phi_n_plus - b_n**2*phi_n
      phi_n = phi_n_plus

  return phi_n_plus.unit()


if __name__ == "__main__":
    H = get_H(model="Hubbard", U=1, t=1)
    phi_n = lanczos(H=H, iters=10)
    print(phi_n)

