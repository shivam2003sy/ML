from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(filename):
    '''
    Get requirements from requirements.txt
    '''
    requirements = []
    with open(filename, 'r') as f:
        requirements = f.readlines()
        requirements = [r.replace('/n' ,'') for r in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlp",
    version="0.0.1",
    author="Shivam",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
