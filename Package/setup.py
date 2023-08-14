from setuptools import (
    setup,
    find_namespace_packages
)

setup(
	name='bedbug',
	version='0.1.12',
	description='A light-weight package for visual debugging',
	url='https://github.com/Bedbug-Debugger/Bedbug-Python',
	author='Ali Hadizadeh Moghadam, Ali Shayanpoor',
	author_email='hadizadeh.ali@gmail.com, shayanpoor.ali66@gmail.com',
	license='MIT',
    
	package_dir={"": "src"},
	packages=find_namespace_packages(where='src'),

	install_requires=[
		"matplotlib >= 3.7.2"
	],
	zip_safe=False,
    
	include_package_data=True,
)
