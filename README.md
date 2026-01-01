Ansible Role: mdadm
=========
[![CI](https://github.com/brianhartsock/ansible-role-mdadm/actions/workflows/ci.yml/badge.svg)](https://github.com/brianhartsock/ansible-role-mdadm/actions/workflows/ci.yml)

Super simple role that installs mdadm and mounts raid arrays.

Requirements
------------

This role has been tested on Ubuntu 22.04, and 24.04, however it should work on most Debian systems.


Role Variables
--------------

The only role variable for this repository is a list of mount points.

```
mdadm_mounts:
  - path: /srv
    src: /dev/md0
    fstype: ext4

```

Dependencies
------------

None

Example Playbook
----------------

MDADM will require root privileges, so ensure you use become to elevate privileges.

    - hosts: servers
      roles:
         - role: brianhartsock.mdadm
           become: true

License
-------

MIT

Author Information
------------------

Created with love by [Brian Hartsock](http://blog.brianhartsock.com).
