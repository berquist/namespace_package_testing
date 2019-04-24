from namespace_package_testing.version import version as __version__

from namespace_package_testing import component_api_helper

component_api_helper.package_hook(
    parent_package_str="namespace_package_testing",
    child_package_str="namespace_package_testing.foo.bar.baz.meep",
)
del component_api_helper
