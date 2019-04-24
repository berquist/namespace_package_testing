from namespace_package_testing.component_api_helper import package_hook


def test_namespace_hacking():
    from namespace_package_testing.foo.bar.baz.meep import CONSTANT
    from namespace_package_testing import meep
    package_hook("namespace_package_testing", "numpy.linalg")
    from namespace_package_testing.linalg import norm
