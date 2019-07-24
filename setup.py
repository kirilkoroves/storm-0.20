import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='storm',  
     version='0.20',
     author="",
     author_email="",
     description="Storm package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kirilkoroves/storm-0.20",
     packages=setuptools.find_packages(),
     install_requires=[
          'zope.interface',
      ],
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Operating System :: OS Independent",
     ],

 )
