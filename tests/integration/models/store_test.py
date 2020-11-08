from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_empty_list(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test-store')

            self.assertIsNone(StoreModel.find_by_name('test-store'),
                              "Found an item with name {}, but expected not to.".format(store.name))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test-store'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test-store'))

    def test_store_json_empty_items(self):
        with self.app_context():
            store = StoreModel('test-store')
            expected = {
                'name': 'test-store',
                'items': []
            }

            self.assertDictEqual(store.json(), expected)

    def test_store_json(self):
        with self.app_context():
            store = StoreModel('test-store')
            item = ItemModel('test', 19.99,1)
            expected = {
                'name': 'test-store',
                'items': [{'name': 'test', 'price': 19.99}]
            }

            store.save_to_db()
            item.save_to_db()

            self.assertDictEqual(store.json(), expected)

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test-item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test-item')

