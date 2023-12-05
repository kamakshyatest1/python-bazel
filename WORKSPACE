load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    sha256 = "5fa3c738d33acca3b97622a13a741129f67ef43f5fdfcec63b29374cc0574c29",
    strip_prefix = "rules_python-0.9.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.9.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:repositories.bzl", "python_register_toolchains")


load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
   name = "my_deps",
   requirements_lock = "//:requirements.txt",
)
load("@my_deps//:requirements.bzl", "install_deps")
install_deps()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_endor",
    sha256 = "558323d0bcc9cbc1437b098eaad9ab50d1b3759199cf85318bad7b6a869e1537",
    strip_prefix = "rules_endor-1.1.1",
    urls = [
        "https://github.com/endorlabs/rules_endor/archive/refs/tags/v1.1.1.tar.gz",
    ],
)

load("@rules_endor//endorctl:repositories.bzl", "rules_endorctl_toolchains")
rules_endorctl_toolchains(repository_url = "https://api.staging.endorlabs.com", version = "1.6.66")