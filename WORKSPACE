load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Specify the version of the rules_python you want to use
http_archive(
    name = "rules_python",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
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

