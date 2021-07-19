import unittest
from funpkg import funpkg


class TestUtil(unittest.TestCase):
    def test_store(self):
        tobj = funpkg.Util()
        storeval = 'some value'

        tobj.store(storeval)

        self.assertEqual(storeval, tobj.stored)

    def test_retrieve(self):
        tobj = funpkg.Util()
        storeval = 'some value'
        tobj.stored = storeval

        result = tobj.retrieve()

        self.assertEqual(storeval, result)


if __name__ == '__main__':
    unittest.main()
