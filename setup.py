# finds all packages that are available in the ml application directory
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
# Function returns a list of requirement packages to get install
def get_requirements(file_path:str)->List[str]:
    requirements = []

    # Opens the requriements.txt file as a temporary file_object 
    with open(file_path) as file_obj:
        # This reads the lines in the txt file one by one and tries to replaces the /n with blank
        requirements = file_obj.readlines()
        requirements = [req.replace('/n', "") for req in requirements]
        # To enable the setup.py while installing the requirements.txt file 
        # we should add -e . in the requirements.txt file, this will automatically trigger setup.py file

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

# metadata info about entire project
setup(
    name= 'machine_learning_project',
    version = '0.0.1',
    author = 'Chandana sree',
    author_email = 'chandana.sree145@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)