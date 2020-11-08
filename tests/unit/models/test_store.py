from tests.unit.unit_base_test import UnitBaseTest

from models.store import StoreModel


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         "The name of the store after creation does not equal the constructor argument.")


