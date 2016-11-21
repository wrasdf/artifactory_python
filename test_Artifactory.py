# Simple tests as this philosophy makes sense
# http://softwareengineering.stackexchange.com/questions/252748/is-it-actually-worth-unit-testing-an-api-client

import unittest
from mock import patch
from Artifactory import Artifactory

URL = {
    'USERS': '/security/users',
    'API': '/security/apiKey'
}

class ArtifactoryTestCase(unittest.TestCase):
    """ Tests for `Artifactory.py` """

    @classmethod
    def setUpClass(self):
        self.artifactory = Artifactory('admin','password')

    def test_get_users(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_users()
            mock.assert_called_once_with(URL['USERS'])

    def test_get_user(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_user('tim')
            mock.assert_called_once_with('/security/users/tim')

    def test_create_user(self):
        with patch.object(Artifactory, 'put') as mock:
            self.artifactory.create_user('tim')
            mock.assert_called_once_with('/security/users/tim', {
                'password': 'password',
                'email': 'tim@email.com'
            })

    def test_delete_user(self):
        with patch.object(Artifactory, 'delete') as mock:
            self.artifactory.delete_user('tim')
            mock.assert_called_once_with('/security/users/tim')

    def test_get_api_key(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_create_api_key(self):
        with patch.object(Artifactory, 'post') as mock:
            self.artifactory.create_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_regenerate_api_key(self):
        with patch.object(Artifactory, 'put') as mock:
            self.artifactory.regenerate_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_revoke_api_key(self):
        with patch.object(Artifactory, 'delete') as mock:
            self.artifactory.revoke_api_key()
            mock.assert_called_once_with(URL['API'])

if __name__ == '__main__':
    unittest.main()
