from setuptools import setup

setup(
	name='bedbug',
	version='0.1.2',
	description='A light-weight package for visual debugging',
	url='https://github.com/Bedbug-Debugger/Bedbug-Python',
	author='Ali Hadizadeh Moghadam, Ali Shayanpoor',
	author_email='hadizadeh.ali@gmail.com, shayanpoor.ali66@gmail.com',
	license='MIT',
      
	install_requires=[
        'matplotlib'
	],
	packages=['bedbug'],
	zip_safe=False,
    
	include_package_data=True,
)
