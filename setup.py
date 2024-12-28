from setuptools import find_packages,setup
# for automating the packages 
from typing import List


# for getting all the packages
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        return requirements



setup(
    name='DiamondPricePrediction',
    version='0.01',
    author='Chaitanya',
    author_email='chaitanyahandore@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()



)