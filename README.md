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
$ pikvm-cli configure --url https://example.com --username admin --password secret
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
