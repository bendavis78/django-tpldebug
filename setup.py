from setuptools import setup, find_packages

setup(
    name='django-tpldebug', 
    version='0.1',
    author='Ben Davis',
    author_email='ben@savidworks.com',
    url='http://www.savidworks.com',
    description='Template debug tools for django',
    keywords='django template debug',
    packages = find_packages(),
    include_package_data = True
)
