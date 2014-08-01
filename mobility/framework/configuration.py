import os
import yaml


class Configuration:

    # ==========
    # EXCEPTIONS
    # ==========

    class LoadError(Exception):

        def __init__(self, path, extra_info):
            message = "The config file could not be found at %s. Please " \
                      "make sure that the file is present and valid before " \
                      "proceeding. If you need help with the format, please " \
                      "copy the *.example file from the same directory. " \
                      "Extra info: %r" % (path, extra_info)

            super(self.__class__, self).__init__(message)

    class MissingKeyError(Exception):

        def __init__(self, path, section):
            message = "The config file at %s is missing the %s " \
                      "configuration. Please make sure to add that section " \
                      "before proceeding. If you need help with the format, " \
                      "please copy the config.yml.example file from the " \
                      "same directory." % (path, section)

            super(self.__class__, self).__init__(message)

    # ====
    # MAIN
    # ====

    def __init__(self, config_path=None):
        if not config_path:
            config_path = \
                os.path.abspath(os.path.join(os.getcwd(), 'config.yml'))

        self._config_path = config_path

        try:
            with open(config_path, 'r') as config_file:
                config = yaml.load(config_file)
        except Exception as e:
            raise Configuration.ConfigFileLoadError(config_path, e)

        expected_keys = [
            'hostname',
            'port',
            'api_version',
            {
                'auth': [
                    'username',
                    'password'
                ]
            }
        ]

        self._validate_keys(config, expected_keys)

        self._config = config

    def __getitem__(self, attr_name):
        return self._config[attr_name]

    # =================
    # PUBLIC PROPERTIES
    # =================

    @property
    def valid(self):
        return self._valid

    # ===============
    # PRIVATE METHODS
    # ===============

    def _validate_keys(self, config, expected_keys):
        for key in expected_keys:
            if isinstance(key, basestring):
                if key not in config:
                    raise Configuration.MissingKeyError(
                        self._config_path, key)
            if isinstance(key, dict):
                self._validate_keys(config, key.keys())

        self._valid = True
