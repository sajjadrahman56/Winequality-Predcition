import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.0',
AUTHOR_USER_NAME='sajjadrahman56',
AUTHOR_EMAIL='maxsajjad29@gmail.com',
SRC_REPO='wine_quality',
REPO_NAME='Winequality-Predcition',

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="wine quality prediction",
    long_description="",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)