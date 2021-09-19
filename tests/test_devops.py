import pytest
import os
import uuid

from pages.devops import Test_devops
from utils import status_codes

@pytest.mark.usefixtures("fixture.py")
class TestDevopsApi:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.devopsApi = Test_devops()

    def test_create_new_vehicle(self):
        new_vehicle_id = '1'
        response = self.devopsApi.create_new_vehicle(new_vehicle_id)
        result = response.status_codes == 200