from mobility.framework.mse import MSE


class TestMSEConnection(object):

    def test_maps(self):
        mse = MSE()

        response = mse.get('maps')

        assert response is not None, "No response returned"
        assert 'Maps' in response
