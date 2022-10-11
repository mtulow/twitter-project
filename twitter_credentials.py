import os
import yaml
import json
from dotenv import load_dotenv
from pathlib import Path

keys = dict(
    consumer_key="5X8FhSn5xW8fsM0Ellmec8yXw",
    consumer_secret="qzdBAvIM1DSyMwKCkFaT6hOHC6gz0ZqiSxM6c8NZi1ROz6EVCr",
    access_token="3055207272-Ga25uXvPwayWwbxbwryRxqsNQNS685HteVirOZr",
    access_token_secret="05DDeGdw33G10zereIEs08CdxOkeItQXuXxcN02K25pgF",
    bearer_token="AAAAAAAAAAAAAAAAAAAAAA0giAEAAAAAAPJN9TbE40IoMRw6%2FjbtA8UWFzQ%3DUXdg0CNIn9kwrnNOBkka8NyMeGFAtigkEIBQnWOthD1wfB5iyE"
)


def store_credentials(filename: str, keys: dict)-> bool:
    """
    Stores Twitter API Keys & Secrets in the given file.
    """
    filename = filename if (filename.endswith('.yaml') or filename.endswith('.yml')) else filename+".yaml"

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    for k,v in keys.items():
        yaml.safe_dump()
    credentials = yaml.safe_dump(keys)

    with open(filename, 'w') as f:
        f.write(credentials)

    return os.path.exists(filename), "Failed to store credentials in file: %s" % filename

def get_credentials(filename: str=None)-> dict:
    """
    Returns a dictionary of credentials for the given filename.
    """
    # Default credentials
    filename = filename or (Path(os.getenv('HOME')) / '.twitter/.twitter-keys.json')
    # Process credentials
    with open(filename, 'r') as f:
        if filename.endswith('.json'):
            keys = json.loads(f)
        elif filename.endswith('.yaml'):
            keys = json.safe_loads_all(f)
        else:
            raise ValueError('Invalid filename: %s' % filename)
    return keys


def get_auth():
    # TODO: load and access environment variables
    pass



if __name__ == '__main__':
    filename = os.path.join(os.getenv('HOME'), '.twitter/.twitter-keys.json')

    store_credentials(filename, keys)
    keys = get_credentials(filename)

    print(keys)