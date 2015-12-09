from setuptools import setup

setup(
        name="mprint",
        version="0.1",
        description="Use tags to print markup text on console screen",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: User Interfaces",
            "Topic :: Terminals"
            ],
        keywords="print tags color markup",
        url="http://www.github.com/h0m3/python-mprint",
        author="Artur 'h0m3' Paiva",
        author_email="dr.hoome@gmail.com",
        license="MIT",
        packages=["mprint"],
        include_package_data=True,
        zip_safe=False
    )