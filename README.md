## SuperWASP Lens Heater daemon

`lensheaterd` wraps a RKC MA901 temperature controller attached via a USB-RS232 adaptor and
makes the latest measurement available for other services via Pyro.

`lensheater` is a commandline utility that reports the latest data from the SuperWASP lensheater.


### Configuration

Configuration is read from json files that are installed by default to `/etc/lensheaterd`.
A configuration file is specified when launching the server, and the `lensheater` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "superwasp_lensheater", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "lensheaterd",        # The name to use when writing messages to the observatory log.
  "serial_port": "/dev/lensheater", # The serial port device to use
  "serial_baud": 19200,             # The serial baud rate to use
  "serial_timeout": 5,              # The serial time out to use
  "channels": 4,                    # Number of temperature channels to monitor
  "query_delay": 30                 # Delay (in seconds) between measurement updates
}
```

### Initial Installation

The automated packaging scripts will push 6 RPM packages to the observatory package repository:

| Package                          | Description                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| rockit-lensheater-server         | Contains the `lensheaterd` server and systemd service file.                                     |
| rockit-lensheater-client         | Contains the `lensheater` commandline utility for querying the lens heater server. |
| python3-rockit-lensheater        | Contains the python module with shared code.                                                    |
| rockit-lensheater-data-superwasp | Contains the json configuration and udev rules for SuperWASP                                    |

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now lensheaterd@superwasp
```

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart lensheaterd@<config>
```

### Testing Locally

The server and client can be run directly from a git clone:
```
./lensheater test.json
LENSHEATERD_CONFIG_PATH=./test.json ./lensheater status
```
