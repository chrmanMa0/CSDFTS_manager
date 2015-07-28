#!/usr/bin/python
import yaml

class NLPBModelConfig:

    def __init__(self, library_type, diameter_min, diameter_max, diameter_stride
                 ion, valence, concentration_min, concentration_max, concentration_stride
                 dielectric, temperature_min, temperature_max, temperature_stride):
        self.library_type = library_type
        self.diameter_min = diameter_min
        self.ion = ion
        self.diameter_max = diameter_max
        self.diameter_stride = diameter_stride
        self.valence = valence
        self.concentration_min = concentration_min
        self.concentration_max = concentration_max
        self.concentration_stride = concentration_stride
        self.dielectric = dielectric
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.temperature_stride = temperature_stride

    def __repr__(self):
        return """\
            %s(library_type=%r, diameter_min=%r, diameter_max=%r, diameter_stride=%r, \
            ion=%r, valence=%r, concentration_min=%r, concentration_max=%r, concentration_stride=%r, \
            dielectric=%r, temperature_min=%r, temperature_max=%r, temperature_stride=%r) % \
            (self.__class__.__name__, self.library_type, self.diameter_min, self.diameter_max \
            self.diameter_stride, self.ion, self.valence, self.concentration_min, \
            self.concentration_max, self.concentration_stride, self.dielectric, \
            self.temperature_min, self.temperature_max, self.temperature_stride)
            """

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return False

