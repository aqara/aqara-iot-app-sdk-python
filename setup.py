from setuptools import find_packages, setup


def requirements():
    with open("requirements.txt") as fileobj:
        return [line.strip() for line in fileobj]


with open("README.md", encoding="utf-8") as fh:
    doc_long_description = fh.read()


setup(
    name="aqara-iot-py-sdk",
    url="https://github.com/aqara/aqara-iot-app-sdk-python",
    author="Aqara Inc.",
    author_email="developer@aqara.com",
    keywords="aqara iot app sdk python",
    long_description=doc_long_description,
    long_description_content_type="text/markdown",
    description="A Python sdk for Aqara Open API, which provides IoT capabilities, maintained by Aqara official",
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/aqara/aqara-iot-app-sdk-python/issues",
        "Changes": "https://github.com/aqara/aqara-iot-python-sdk/wiki/Aqara-IoT-Python-SDK-Release-Notes",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    version="1.0.9",
    install_requires=requirements(),
    test_suite="runtests.runtests",
    entry_points={"nose.plugins": []},
    packages=find_packages(),
    python_requires=">=3.7",
)
