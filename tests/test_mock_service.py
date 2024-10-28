import os

import pytest

from fildapi.config import Cfg
from fildapi.schema import get_default_app_url


@pytest.fixture
def reset_config():
    Cfg.initialize(
        config_file=f'{os.path.dirname(__file__)}/etc/config_no_mock.yaml',
    )
    yield
    Cfg.initialize()


def test_no_default_app_url():
    assert get_default_app_url() is None
