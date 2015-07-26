#!/usr/bin/python

import global_config
import unittest
import os.path
import yaml
class GlobalConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.scratch_global_config = global_config.GlobalConfig("NLPB", "sphere", "blah",6.4000000000000001E-002, 1.0E-6,
                 False, True, True,
                 True, True, True,
                 True)

    def tearDown(self):
        self.scratch_global_config = None

    def test_model_type(self):
        self.assertEqual(self.scratch_global_config.model_type, "NLPB")

    def test_resolution(self):
        self.assertEqual(self.scratch_global_config.resolution, 6.4000000000000001E-002)

    def test_store_and_load(self):
        filename = 'test_global_config.yaml'
        if(os.path.isfile(filename)):
            #delete the file
            print 'would delete file now'

        self.scratch_global_config.store(filename)
        stream = file(filename, 'r')
        test_load_config = yaml.load(stream)
        self.assertEqual(self.scratch_global_config, test_load_config)
        print test_load_config
if __name__ == '__main__':
    unittest.main()
