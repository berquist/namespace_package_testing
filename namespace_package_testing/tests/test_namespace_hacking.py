from namespace_package_testing.component_api_helper import package_hook


def test_namespace_hacking():
    # as you would normally do
    from namespace_package_testing.foo.bar.baz.meep import CONSTANT

    # this is from the top-level __init__.py
    from namespace_package_testing import meep  # set_child_as_subpackage
    import namespace_package_testing
    print(namespace_package_testing.meep.CONSTANT)  # set_child_as_attr

    import namespace_package_testing.baz  # is this the unfortunate side-effect?

    # this is in-place
    package_hook("namespace_package_testing", "numpy.linalg")
    from namespace_package_testing.linalg import norm
