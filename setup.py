from setuptools import setup

setup(
	name = 'pixelscamp_api',
	version = '1.0',
	description = 'PixelsCamp API wrapper in python',
	url = 'https://github.com/tofran/pixelscamp-api',
	author = 'Francisco Marques',
	author_email = 'franscopcmarques@gmail.com',
	license = 'MIT',
	packages = ['pixelscamp_api'],
	zip_safe = True,
	install_requires = ['requests'],
    keywords='PixelsCamp REST API',
	)
