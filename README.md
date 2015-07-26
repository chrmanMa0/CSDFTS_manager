# CSDFTS_manager
The CSDFTS manager is an tool for providing batch run functionality when using the CSDFTS system.
It takes a set of parameter ranges and generates template files for the ranges in question
and batch executes each template on a separate process up to the max number of processes.

## Prerequisites
Python 2.7+
pyyaml 

    sudo apt-get install python-yaml


## Installing
To install the software just execute

    git clone https://github.com/chrmanMa0/CSDFTS_manager.git

from the dirctory where you would like to install the project.
For instance, if you keep all of your projects in `~/workspaces` you would change
to the workspaces directory and execute the above command.  You might then have a
directory structure that looks something like

    .
    ├── CSDFTS_manager
    │   ├── .git
    │   └── README.md
    └── fortran
        └── src

Since the project is currently a python (mostly) project it should be ready.
