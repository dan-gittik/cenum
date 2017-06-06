import setuptools


package = dict(
    name             = 'cenum',
    version          = '0.1.0',
    author           = 'Dan Gittik',
    author_email     = 'dan.gittik@gmail.com',
    description      = 'A nifty decorator that allows C-style enum definitions in Python.',
    license          = 'MIT',
    url              = 'https://github.com/dan-gittik/cenum',
    packages         = setuptools.find_packages(),
    install_requires = [
    ],
    tests_require    = [
        'pytest',
    ],
)


if __name__ == '__main__':
	setuptools.setup(**package)
