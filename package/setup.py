import os

from setuptools import setup, find_packages

setup(
   name='studentNFT_API',
   version='1.2.0',
   maintainer='Sabine Bertram',
   maintainer_email='sabine.bertram@mailbox.org',
   package_dir={'': 'src'},
   packages=find_packages('src'),
   package_data={'swagger_server': ['swagger/swagger.yaml']},

   install_requires=[
      'connexion[swagger-ui]', 
      'pymongo',
      'flask_cors', 
      'web3',
      'registree-auth @ git+https://github.com/registreerocks/registree-auth.git'
   ],
   test_require = [
      'pytest', 
      'mock'
   ],
)
