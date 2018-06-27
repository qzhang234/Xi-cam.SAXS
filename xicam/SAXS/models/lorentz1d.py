from astropy.modeling.models import Lorentz1D
from xicam.plugins.FittableModelPlugin import Fittable1DModelPlugin


class Lorentz1D(Lorentz1D, Fittable1DModelPlugin):
    pass
