import unittest
import wunderpy2
import requests
import random
import string

import tests_config
from endpoint_test_case import EndpointTestCase

class TestFoldersEndpoint(EndpointTestCase):
    def setUp(self):
        ''' Does normal endpoint setup and also sets up tracking of any folders that were created during the course of testing '''
        super(TestFoldersEndpoint, self).setUp()
        # We set this up to track any folders that were created during the course of testing, so we can clean them up afterwards
        self._folder_ids_to_cleanup = set()

    def tearDown(self):
        ''' Cleans up any folders created in the course of testing '''
        # TODO Obviously, this isn't ideal - it depends on the very functionality being tested - but the alternative is re-implementing folder-specific delete logic here,
        #  which sucks worse.
        for folder_id in self._folder_ids_to_cleanup:
            try:
                folder_obj = self.client.get_folder(folder_id)
                revision = folder_obj[wunderpy2.model.Folder.REVISION]
                self.client.delete_folder(folder_id, revision)
            except ValueError:
                # There was an issue retrieving or deleting the folder; it might be deleted already and we've done the best we can
                continue

    def _create_test_folder(self):
        random_title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        test_list = self.client.create_list(random_title)
        list_ids = [test_list[wunderpy2.model.List.ID]]
        random_title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return self.client.create_folder(random_title, list_ids)

    def _get_test_folder(self):
        ''' Creates a new folder with a random ID that gets cleaned up after the test is run '''
        new_folder = self._create_test_folder()
        self._folder_ids_to_cleanup.add(new_folder[wunderpy2.model.Folder.ID])
        return new_folder

    def test_get_folders(self):
        ''' Test basic all folders retrieval '''
        self.client.get_folders()

    def test_get_folder(self):
        ''' Test getting of a specific folder '''
        new_folder = self._get_test_folder()
        new_folder_id = new_folder[wunderpy2.model.Folder.ID]
        retrieved_folder = self.client.get_folder(new_folder_id)
        self.assertDictEqual(new_folder, retrieved_folder)

    def test_create_folder(self):
        ''' Test folder creation '''
        new_folder = self._create_test_folder()
        self._folder_ids_to_cleanup.add(new_folder[wunderpy2.model.Folder.ID])

    def test_update_folder(self):
        ''' Test updating folder '''
        new_folder = self._get_test_folder()
        new_folder_id = new_folder[wunderpy2.model.Folder.ID]
        new_folder_revision = new_folder[wunderpy2.model.Folder.REVISION]

        updated_title = "DELETEME!"
        list_ids = [1, 2, 3] # todo: create lists
        updated_folder = self.client.update_folder(new_folder_id, new_folder_revision, title=updated_title, list_ids=list_ids)
        self.assertEqual(updated_title, updated_folder[wunderpy2.model.Folder.TITLE])

    def test_delete_folder(self):
        ''' Test folder deletion '''
        new_folder = self._get_test_folder()
        new_folder_id = new_folder[wunderpy2.model.Folder.ID]
        new_folder_revision = new_folder[wunderpy2.model.Folder.REVISION]
        self.client.delete_folder(new_folder_id, new_folder_revision)
        self.assertRaises(ValueError, self.client.get_folder, new_folder_id)

    def test_get_folder_revisions(self):
        self.client.get_folder_revisions()

if __name__ == "__main__":
    unittest.main()
