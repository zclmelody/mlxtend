# Sebastian Raschka 2014-2015
# mlxtend Machine Learning Library Extensions
# Submodules with preprocessing functions.

from .iris import iris_data
from .wine import wine_data
from .autompg import autompg_data
from .mnist import mnist_data
from .boston_housing import boston_housing_data

__all__ = ["iris_data", "wine_data", "autompg_data", "mnist_data",
           "boston_housing_data"]
