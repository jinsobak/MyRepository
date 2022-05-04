import setuptools

setuptools.setup (
  include_package_data = True,
  name = "mytestpackage_ver_0.0.1",
  version = "0.0.1",
  descruption = "oss-dev my calculator 0.0.1",
  author = "jinsobak",
  author_email="jinsobak@gmail.com",
  url = "https://github.com/jinsobak/MyRepository/",
  install_requires = ['pytest'],
  long_description = "oss development..."
  long_description_content_type = "text/markdown",
  classifiers = [
    "programming Language :: Python :: 3",
    "Operating System :: Os",
  ],
)
