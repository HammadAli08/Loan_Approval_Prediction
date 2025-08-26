from setuptools import find_packages, setup
from typing import List

Hypen_E_dot = "-e ."
def get_requirements(file_name:str)->List[str]:  # This function is for reading text from Requirments.txt
    reqiurements=[]
    with open(file_name) as object:
        reqiurements=object.readline()   # It make it read all lines
        reqiurements=reqiurements.split("\n")

        if Hypen_E_dot in reqiurements:
            reqiurements.remove(Hypen_E_dot)   #As -e . should not come into this list Get_requirements is Extracting
    return reqiurements


setup(
    name='ML Project',
    version='0.0.1',
    description='An end to end machine learning project',
    author='Hammad Ali Tahir',
    author_email='hammadalitahir8@gmail.com ',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
)