load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Specify the version of the rules_python you want to use
http_archive(
    name = "rules_python",
    sha256 = "5fa3c738d33acca3b97622a13a741129f67ef43f5fdfcec63b29374cc0574c29",
    strip_prefix = "rules_python-0.9.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.9.0.tar.gz",
)
# Initialize rules_python
load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

# Load the pip_install rule
load("@rules_python//python:pip.bzl", "pip_install")

# Create a central repo that knows about the dependencies needed for our Python code.
pip_install(
    name = "my_deps",
    requirements = "//:requirements.txt",
)

