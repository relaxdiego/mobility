import os
import pytest

from mobility.framework.configuration import Configuration


class TestConfiguration(object):

    def test_init_with_valid_config(self):
        configuration = Configuration()
        assert configuration.valid

    def test_init_with_missing_key(self):
        path = os.path.abspath(os.path.join(
            __file__, '..', '..', 'support', 'config_with_missing_key.yml'))

        with pytest.raises(Configuration.MissingKeyError):
            Configuration(path)
