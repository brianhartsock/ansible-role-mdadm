ansible-role-mdadm
=========

Super simple role that installs mdadm and mounts raid arrays.

Requirements
------------

None

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

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: brianhartsock.mdadm

License
-------

MIT

Author Information
------------------

Created with love by [Brian Hartsock](http://blog.brianhartsock.com).
