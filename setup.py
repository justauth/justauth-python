import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='justauth-PFinal',
    version='0.0.1',
    keywords='auth',
    description='Aggregate authorization extension libraries',
    long_description=long_description,
    license='MIT License',
    url='https://github.com/justauth/justauth-python',
    author='PFinal南丞',
    author_email='lampxiezi@163.com',
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    platforms='any',
    install_requires=[],
)
