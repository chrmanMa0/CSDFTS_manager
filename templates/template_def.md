## Run Template Definition
Each run of CSDFTS will be defined by a template file.  It
will contain a block for global parameters (common for all models)
which will include the name of the model to be used.  It will
also include a block for the model specific parameters to be used.
Some of the global parameters can result in additional configuration
blocks for that choice (pH Model Nanoparticles for instance).

##Global Parameters
Currently the following are the global parameters:

Parameter Name             | Options
---------------------------| ------------
Model Type                 | NLPB, MPB1, MPB2, PM, SPM
Solute                     | Sphere, Cylinder, Nanochannel, Plate
pH Model                   | Nanoparticles, Proteins, None
Resolution                 | Float
Type Tolerance             | Float
Multigrid Approach         | T/F
Density Profile Out        | T/F
Electrostatic Potential Out| T/F
Ion Contribution Out       | T/F
Pressure Out               | T/F
Integrated Charge Out      | T/F
pH Out                     | T/F

##Model Specific Parameters
These are definitions for parameter blocks for pH model, and the numerical model types.

###pH Model
Parameter Name | Type | Description
---------------|------|-------------
pH Min         | Float| The minimum pH value for run
pH Max         | Float| The maximum pH value for run
pH Stride      | Float| The increment value for going from min to max pH



