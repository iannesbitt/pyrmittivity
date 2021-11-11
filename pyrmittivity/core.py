from .constants import C_0, Mu_0, Eps_0
import math

def celerity(E_r):
    '''
    Calculate the wave velocity (:math:`C_r`) given the permittivity
    (:math:`\\varepsilon_r`) of the dielectric.

    .. math::
        :label: e6

        C_r = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_r \\varepsilon_0}}

    :param float E_r: Permittivity of the dielectric (:math:`\\varepsilon_r`)
    :rtype: float

    See Equation [6] of
    `Maxwell's Equations <https://maxwells-equations.com/materials/permittivity.php>`_.
    '''
    return 1/math.sqrt(Mu_0 * E_r * Eps_0)

def epsilon_r(C_r):
    '''
    Calculate the permittivity (:math:`\\varepsilon_r`) given the wave velocity
    through the dielectric (:math:`C_r`).

    .. math::
        :label: e6mod

        \\varepsilon_r = \\frac{\\frac{1}{C_r}^2}{\\mu_0 \\varepsilon_0}

    :param float C_r: Wave velocity through the dielectric (:math:`\\varepsilon_r`)
    :rtype: float

    See Equation [6] of
    `Maxwell's Equations <https://maxwells-equations.com/materials/permittivity.php>`_.
    '''
    return ((1/C_r)**2)/(Mu_0 * Eps_0)

def wavelength(f, E_r):
    '''
    Calculate the wavelength (:math:`\\lambda`) given the permittivity and
    frequency (:math:`\\varepsilon_r` and *f*).

    .. math::
        :label: e7

        \\lambda = \\frac{C_0}{f \\sqrt{\\varepsilon_r}}

    :param float f: Frequency of the wave (:math:`f`)
    :param float E_r: Permittivity of the dielectric (:math:`\\varepsilon_r`)
    :rtype: float

    See Equation [7] of
    `Maxwell's Equations <https://maxwells-equations.com/materials/permittivity.php>`_.
    '''
    return C_0 / (f * math.sqrt(E_r))

def m_per_ns(v):
    '''
    Calculate meters per nanosecond from meters per second.
    Can be useful for software that uses m/ns velocity definitions.

    .. math::
        :label: m_per_ns

        C_{m*ns^{-1}} = {C_r}^{-9}

    :param float v: Velocity of the wave (:math:`C_r`)
    :rtype: float
    '''
    return v ** (-9)

def m_per_sec(v):
    '''
    Calculate meters per second from meters per nanosecond.
    Can be useful for software that uses m/ns velocity definitions.

    .. math::
        :label: m_per_sec

        C_r = {C_{m*ns^{-1}}}^9

    :param float v: Velocity of the wave (:math:`C_r`)
    :rtype: float
    '''
    return v ** (9)