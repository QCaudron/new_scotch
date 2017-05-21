from setuptools import setup

setup(
    name="scotch",
    version="1.0",
    description="Simulating continuous-time Markov chains in Python.",
    url="http://github.com/qcaudron/scotch2",
    author="Quentin CAUDRON",
    author_email="quentincaudron@gmail.com",
    license="MIT",
    packages=["scotch"],
    zip_safe=False,
    test_suite="tests",
    install_requires=[
        "numpy",
        "scipy",
        "cython"
    ]
)
