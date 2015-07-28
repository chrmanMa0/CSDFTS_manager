import yaml

class GlobalConfig:
    def __init__(self, model_type, solute, ph_model, resolution, type_tolerance,
                 multigrid_approach, density_profile_out, elect_out,
                 ion_cont_out, pressure_out, integrated_charge_out,
                 ph_out):
        self.model_type = model_type
        self.solute = solute
        self.ph_model = ph_model
        self.resolution = resolution
        self.type_tolerance = type_tolerance
        self.multigrid_approach = multigrid_approach
        self.density_profile_out = density_profile_out
        self.elect_out = elect_out
        self.ion_cont_out = ion_cont_out
        self.pressure_out = pressure_out
        self.integrated_charge_out = integrated_charge_out
        self.ph_out = ph_out

    def __repr__(self):
        return """\
                    %s(model_type=%r, solute=%r, ph_model=%r, ph_model=%r,\
                    resolution=%r, type_tolerance=%r, multigrid_approach=%r,\
                    density_profile_out=%r, elect_out=%r, ion_cont_out=%r,\
                    pressure_out=%r, integrated_charge_out=%r, ph_out=%r\
                    )
               """ % (self.__class__.__name__, self.model_type, self.solute,
                      self.ph_model, self.resolution, self.type_tolerance,
                      self.multigrid_approach, self.density_profile,
                      self.elect_out, self.ion_cont_out, self.pressure_out,
                      self.integrated_charge_out, self.ph_out)

    def store(self, filename):
        stream = file(filename, 'w')
        yaml.dump(self, stream)

    def __eq__(self, other):
        try:

            return self.__dict__ == other.__dict__
        except AttributeError:
            return False

    def __str__(self):
        return str(self.__dict__)
