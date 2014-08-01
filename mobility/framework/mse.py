# This uses the Requests library to communicate
# with the MSE API http://docs.python-requests.org/
import requests

from mobility.framework.configuration import Configuration


class MSE(object):

    # ==============
    # PUBLIC METHODS
    # ==============

    def get(self, path):
        """
        Calls a given API path using HTTP GET. The path is appended
        to 'https://<hostname>:<port>/api/contextaware/<api_version>/'.
        Values above with angle brackets will be read from config.yml

        Therefore a path of 'maps' will produce:

            https://<hostname>:<port>/api/contextaware/<api_version>/maps

        While a path of 'maps/count' will produce

            https://<hostname>:<port>/api/contextaware/<api_version>/maps/count

        This method expects the MSE server to return a json string. This method
        will then process the json string and pass it back to the original
        caller as a regular Python dictionary.
        """
        c = self._config

        url = "{}/{}".format(self._base_url, path)

        # This uses the Requests library to communicate
        # with the MSE API http://docs.python-requests.org/
        response = requests.get(
            url,
            verify=c['verify_ssl'],
            auth=(c['auth']['username'], c['auth']['password']),
            headers={'accept': 'application/json'}
        )

        return response.json()

    # ===========
    # INITIALIZER
    # ===========

    def __init__(self):
        self._config = Configuration()

    # ==================
    # PRIVATE PROPERTIES
    # ==================

    @property
    def _base_url(self):
        c = self._config
        return "https://{}:{}/api/contextaware/{}".format(
            c['hostname'], c['port'], c['api_version'])
