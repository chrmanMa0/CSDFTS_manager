#!/usr/bin/python
import yaml
class PHModelConfig:

    def __init__(self, pH_min, pH_max, pH_stride, pKA, pKB, Ntotal):
        self.pH_min = pH_min
        self.pH_max = pH_max
        self.pH_stride = pH_stride
        self.pKA = pKA
        self.pKB = pKB
        self.Ntotal = Ntotal

    def __repr__(self):
        return  """\
                %s(ph_min=%r, ph_max=%r, ph_stride=%r, pKA=%r, pKB=%r, Ntotal=%r)\
                % (self__class__.__name__, self.ph_min, self.ph_max, self.ph_stride, \
                  self.pKA, self.pKB, self.Ntotal)\
                """
    def store(self, filename):
        stream = file(filename, 'w')
        yaml.dump(self, stream)
        print yaml.dump(self)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__

        except AttributeError:
            return False

    def __str__(self):
        return str(self.__dict__)

