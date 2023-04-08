import os
import configparser
import requests
import json
import click

# The path of the configuration file
CONFIG_FILE_PATH = os.path.expanduser('~/.pikvm-cli')

# Load configuration from the configuration file
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)

def get_config(name=None):
  """
  Returns the configuration settings for the given name.

  Args:
    name (str): The name of the configuration. If None, uses the default name

  Returns:
    tuple: A tuple of (url, username, password) for the configuration

  Raises:
    click.UsageError: If the configuration for the given name is not found
  """
  if name not in config.sections():
    raise click.UsageError(f'Can\'t find configuration for "{name}". Run "configure" first.')

  url = config.get(name, 'url')
  username = config.get(name, 'username')
  password = config.get(name, 'password')

  return url, username, password

def make_request(method, url, username, password, params={}):
  """
  Makes a request to the PIKVM and prints the response.

  Args:
    method (str): The HTTP method of the request.
    url (str): The URL of the API endpoint.
    username (str): The username for the PIKVM.
    password (str): The password for the PIKVM.
    params (dict): The parameters to pass with the request.
  """
  try:
    response = requests.request(
      method=method,
      url=url,
      headers={
        'X-KVMD-User': username,
        'X-KVMD-Passwd': password,
      },
      params=params,
      timeout=5,
      verify=False,
    )

    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    click.echo(f'Request failed: {e}')
    return

  data = response.json()

  click.echo(json.dumps(data, indent=2))

@click.group()
@click.version_option("1.0.0")
def main():
  """
  CLI tool to control and manage PIKVM devices
  """
  pass

@main.command()
@click.option('--name', '-n', default='default', help='Name of the configuration')
@click.option('--url', prompt=True, help='PIKVM URL')
@click.option('--username', '-u', prompt=True, help='PIKVM user name')
@click.option('--password', '-p', prompt=True, hide_input=True, help='PIKVM user password')
def configure(name, url, username, password):
  """
  Configures the PIKVM connection(s)

  \b
  Args:
    name: (str) the name of the PIKVM configuration to use (default: "default")
    url (str): The URL of the PIKVM
    username (str): The username for the PIKVM
    password (str): The password for the PIKVM
  """
  config[name] = {
    'url': url,
    'username': username,
    'password': password,
  }

  with open(CONFIG_FILE_PATH, 'w') as configfile:
    config.write(configfile)

@main.command()
@click.option('--name', default='default', help='Name of the configuration')
def info(name):
  """
  Retrieves the device information from the PIKVM

  \b
  Args:
    name: (str) the name of the PIKVM configuration to use (default: "default")
  """
  url, username, password = get_config(name)

  make_request('GET', f'{url}/api/info', username, password)

@main.command()
@click.option('--name', '-n', default='default', help='Name of the configuration')
@click.argument('action', type=click.Choice(['on', 'off', 'off_hard', 'reset', 'status']))
def atx(name, action):
  """
  Power management control for the PIKVM device's ATX

  \b
  Args:
    name: (str) the name of the PIKVM configuration to use (default: "default")
    action: (str) the power management action to perform:
      * "on": power on the device
      * "off": perform a graceful shutdown of the device
      * "off_hard": perform a forced shutdown of the device (with a confirmation prompt)
      * "reset": perform a forced reset of the device (with a confirmation prompt)
      * "status": get the current power status of the device
  """
  url, username, password = get_config(name)

  if action == 'status':
    return make_request('GET', f'{url}/api/atx', username, password)

  if action == 'off_hard' and not click.confirm('This will forcefully turn off the device. Are you sure?'):
    return

  if action == 'reset' and not click.confirm('This will forcefully reset the device. Are you sure?'):
    return

  make_request('POST', f'{url}/api/atx/power', username, password, { 'action': action })

if __name__ == '__main__':
  main()
