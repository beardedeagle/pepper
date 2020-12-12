# -*- coding: utf-8 -*-
"""Pepper is a CLI front-end to salt-api."""
from typing import Tuple

import pkg_resources

from pepper.libpepper import Pepper, PepperException

__all__: Tuple[str, str, str] = ("__version__", "Pepper", "PepperException")

__version__: str
try:
    __version__ = pkg_resources.get_distribution("salt_pepper").version
except pkg_resources.DistributionNotFound:
    # package is not installed
    __version__ = ""

# For backwards compatibility
version: str = __version__
sha: None = None
