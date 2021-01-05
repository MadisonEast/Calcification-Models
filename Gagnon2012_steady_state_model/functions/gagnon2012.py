def FluxPar(D, gamma, XCa_0, XCa_coral):
    """
    Biomineral composition (X/Ca) as a function of transport dynamics (gamma)

    Parameters
    ----------
    D
    gamma
    XCa_0
    XCa_coral

    Returns
    -------
    
    """
    return (1/(Dmg - 1.0 + gamma)) * (MgCa_0 * (1.0/MgCa_coral) - 1.0)