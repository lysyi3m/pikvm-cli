# pikvm-cli

A command-line interface (CLI) for controlling PIKVM devices.

## Installation

You can install the `pikvm-cli` package from PyPI:

```sh
$ pip install pikvm-cli
```

## Usage

To use the `pikvm-cli` tool, you must first configure it with the URL, username, and password of your PIKVM device:

```sh
$ pikvm-cli configure --url https://example.com --username admin --password password
```

_Note:_ configuration file is located at `~/.pikvm-cli`

Once the tool is configured, you can use it to retrieve information about your device:

```sh
$ pikvm-cli info
```

You can also use it to control the power of your device:

```sh
$ pikvm-cli atx on
$ pikvm-cli atx off
$ pikvm-cli atx off_hard
$ pikvm-cli atx reset
```

_Note:_ for the full list of available commands, run `pikvm-cli --help`

### Multiple Devices

If you have multiple PIKVM devices, you can configure the tool to use a specific device by passing the `--name` flag:

```sh
$ pikvm-cli info --name pikvm-1
```

_Note:_ if `--name` is not passed, "default" configuration will be used
