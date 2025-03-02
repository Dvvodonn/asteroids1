from setuptools import setup, find_packages
print('hello world')
setup(
    name="mypackage",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "asteroids=asteroids.cli:main",
        ],
    },
)
