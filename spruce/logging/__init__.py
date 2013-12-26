"""Logging.

This is a wrapper and extension of :mod:`logging`.  Use it instead of
:mod:`logging`.  Mixing the two will work, but there is no need, since
this module provides a superset of the :mod:`logging` API.

"""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

from ._core import *
from ._pprint import *
