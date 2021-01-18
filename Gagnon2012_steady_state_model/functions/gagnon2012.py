def FluxPar(Dx, gamma, XCa_0, XCa_coral):
    """
    Biomineral composition (X/Ca) as a function of transport dynamics (gamma)

    Parameters
    ----------
    Dx
    gamma
    XCa_0
    XCa_coral

    Returns
    -------
    
    """
    return (1/(Dx - 1.0 + gamma)) * (XCa_0 * (1.0/XCa_coral) - 1.0)