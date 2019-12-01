import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_mdadm_install(host):
    pkg = host.package('mdadm')

    assert pkg.is_installed


def test_mount(host):
    mount = host.mount_point("/srv")

    assert mount.exists
