from models.store import StoreModel
from tests.base_test import BaseTest
import json

class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as c:
            with self.app_context():
                r = c.post('/store/test')

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.loads(r.data))

    def test_create_dulpicate_store(self):
        with self.app() as c:
            with self.app_context():
                c.post('/store/test')
                r = c.post('/store/test')
                self.assertEqual(r.status_code, 400)
                self.assertDictEqual({'message': "A store with name 'test' already exists."},
                json.loads(r.data))

    def test_delete_store(self):
        with self.app() as c:
            with self.app_context():
                store = StoreModel('test')
                store.save_to_db()
                r = c.delete('/store/test')
                self.assertIsNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'message': "Store deleted"},
                json.loads(r.data))


    def test_store_not_found(self):
        with self.app() as c:
            with self.app_context():
                r = c.get('/store/test')
                self.assertEqual(r.status_code, 404)
                self.assertDictEqual({'message': "Store not found"},
                                     json.loads(r.data))