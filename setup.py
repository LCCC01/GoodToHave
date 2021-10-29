import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='GoodToHave',
    version='0.0.2',
    author='Linnea Canblad',
    author_email='linnea.canblad@gmail.com',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LCCC01/GoodToHave',
    project_urls = {
        "Bug Tracker": "https://github.com/LCCC01/GoodToHave/issues"
    },
    license='MIT',
    packages=['GoodToHave'],
    install_requires=['requests']
)