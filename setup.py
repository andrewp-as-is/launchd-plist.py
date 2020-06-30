import setuptools

setuptools.setup(
    name='launchd-plist',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
