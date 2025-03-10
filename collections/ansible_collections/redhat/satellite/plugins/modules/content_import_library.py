#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2024, Partha Aji
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: content_import_library
version_added: 4.1.0
short_description: Manage library content imports
description:
    - Import library content.
author:
    - "Partha Aji (@parthaa)"
extends_documentation_fragment:
  - redhat.satellite.foreman
  - redhat.satellite.foreman.organization
  - redhat.satellite.foreman.katelloimport
'''

EXAMPLES = '''
- name: "Import library content from metadata"
  redhat.satellite.content_import_library:
    path: "/var/lib/pulp/imports/example-content"
    metadata: "{{ lookup('file', '/tmp/metadata.json') | from_json }}"
    username: "admin"
    password: "changeme"
    server_url: "https://satellite.example.com"
    organization: "Default Organization"

- name: "Import library content with specific metadata json"
  redhat.satellite.content_import_library:
    path: "/var/lib/pulp/imports/example-content"
    metadata_file: "/tmp/metadata.json"
    username: "admin"
    password: "changeme"
    server_url: "https://satellite.example.com"
    organization: "Default Organization"
    destination_server: "airgapped.example.com"
    fail_on_missing_content: true
'''

from ansible_collections.redhat.satellite.plugins.module_utils.foreman_helper import KatelloContentImportBaseModule


class KatelloContentImportModule(KatelloContentImportBaseModule):
    pass


def main():
    module = KatelloContentImportModule(
        import_action='library'
    )

    with module.api_connection():
        module.run()


if __name__ == '__main__':
    main()
