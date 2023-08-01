#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""Helper function to validate and parse the json config file"""

import json
from rockit.common import daemons, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': ['daemon', 'log_name', 'serial_port', 'serial_baud', 'serial_timeout', 'channels', 'query_delay'],
    'properties': {
        'daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'log_name': {
            'type': 'string',
        },
        'serial_port': {
            'type': 'string',
        },
        'serial_baud': {
            'type': 'number',
            'min': 0
        },
        'serial_timeout': {
            'type': 'number',
            'min': 0
        },
        'channels': {
            'type': 'number',
            'min': 1,
            'max': 8
        },
        'query_delay': {
            'type': 'number',
            'min': 0
        }
    }
}

class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validators = {
            'daemon_name': validation.daemon_name_validator
        }

        validation.validate_config(config_json, CONFIG_SCHEMA, validators)

        self.daemon = getattr(daemons, config_json['daemon'])
        self.log_name = config_json['log_name']
        self.serial_port = config_json['serial_port']
        self.serial_baud = int(config_json['serial_baud'])
        self.serial_timeout = int(config_json['serial_timeout'])
        self.channels = int(config_json['channels'])
        self.query_delay = config_json['query_delay']
