#!/usr/bin/python

import ph_model_config
import unittest
import os.path
import yaml
class PHModelConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.scratch_ph_model_config = ph_model_config.PHModelConfig(4.0, 7.5, .5, 0.0, 0.0, 0.0)

    def tearDown(self):
        self.scratch_ph_model_config = None

    def test_configuration(self):
        self.assertEqual(self.scratch_ph_model_config.pH_min, 4.0)
        self.assertEqual(self.scratch_ph_model_config.pH_max, 7.5)
        self.assertEqual(self.scratch_ph_model_config.pH_stride, .5)
        self.assertEqual(self.scratch_ph_model_config.pKA, 0.0)
        self.assertEqual(self.scratch_ph_model_config.pKB, 0.0)
        self.assertEqual(self.scratch_ph_model_config.Ntotal, 0.0)


    def test_store_and_load(self):
        filename = 'test_ph_model_config.yaml'
        if(os.path.isfile(filename)):
            #delete the file
            print 'would delete file now'

        self.scratch_ph_model_config.store(filename)
        stream = file(filename, 'r')
        test_load_config = yaml.load(stream)
        self.assertEqual(self.scratch_ph_model_config, test_load_config)

if __name__ == '__main__':
    unittest.main()
