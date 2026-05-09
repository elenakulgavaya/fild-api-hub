import warnings

# pylint: disable=wrong-import-position
warnings.warn(
    "fild-api-hub is deprecated and will no longer be maintained. "
    "Migrate to surety-api: pip install surety-api. "
    "Replace 'from fildapi import ApiCaller, ApiMethod, MockServer, HttpMethod' "
    "with 'from surety.api import ApiCaller, ApiContract, MockServer, HttpMethod'. "
    "Note: ApiMethod was renamed to ApiContract in surety-api. "
    "See https://github.com/elenakulgavaya/surety-api for details.",
    DeprecationWarning,
    stacklevel=2,
)

from .caller import ApiCaller
from .mock.service import MockServer
from .method import ApiMethod
from .schema import HttpMethod
