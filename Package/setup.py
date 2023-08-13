from setuptools import setup

setup(
	name='bedbug',
	version='0.1.3',
	description='A light-weight package for visual debugging',
	url='https://github.com/Bedbug-Debugger/Bedbug-Python',
	author='Ali Hadizadeh Moghadam, Ali Shayanpoor',
	author_email='hadizadeh.ali@gmail.com, shayanpoor.ali66@gmail.com',
	license='MIT',
    
	package_dir={"": "src"},

	install_requires=[
		'matplotlib'
	],
	packages=['bedbug'],
	zip_safe=False,
    
	include_package_data=True,
)
