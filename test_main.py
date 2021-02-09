"""test_main.py"""
import tempfile
import pathlib
import unittest
from main import *


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def test_simple(self):
        self.assertEqual(True, True)

    def test_speedtest(self):
        """Test speedtest runs"""
        results = run_speedtest()
        self.assertIn('timestamp', results)
        self.assertIn('download', results)
        self.assertIn('upload', results)

    def test_create_csv(self):
        """Test csv file creation"""
        new_csvfile = pathlib.Path(self.temp_dir.name, 'test_create_csv.csv')
        self.assertFalse(new_csvfile.exists())
        create_csv(new_csvfile)
        self.assertTrue(new_csvfile.exists())

    def test_entrypoint(self):
        """Test that entrypoint creates a csvfile"""
        new_csvfile = pathlib.Path(self.temp_dir.name, 'test_entrypoint.csv')
        self.assertFalse(new_csvfile.exists())
        entrypoint(new_csvfile)
        self.assertTrue(new_csvfile.exists())

    def tearDown(self):
        if self.temp_dir:
            self.temp_dir.cleanup()


if __name__ == '__main__':
    unittest.main()
