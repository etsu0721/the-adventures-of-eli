import json, os, glob
from contextlib import contextmanager
from datetime import datetime as dt

@contextmanager
def working_dir(path):
    init_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(init_dir)

def get_adventure_name(file):
    adventure_name = input('{} name: '.format(file))
    return adventure_name

def get_adventure_types(file):
    adventure_types = input('{} types (separated by commas): '.format(file))
    return adventure_types.split(',')

def get_adventure_gps_json_str(file):
    with working_dir('./data/json-unenhanced/'):
        with open(file, 'r') as f:
            return json.load(f)

def get_adventure_date(gps_json_str):
    return gps_json_str[0]['name']

def get_adventure_desc(file):
    adventure_desc = input('{} description: '.format(file))
    return adventure_desc

def convert_to_json(file, adventure):
    # Dump dict to JSON string
    json_str = json.dumps(adventure)

    # Write JSON string to JSON file
    with working_dir('./data/json-enhanced/'):
        with open(file, 'w') as f:
            f.write(json_str)
    return


def main():    
    # Get listing of JSON files to enhance
    with working_dir('./data/json-unenhanced'):
        listing = (file for file in glob.glob('*.json'))
    
    keep_going = 'y'

    while keep_going != 'n':
        f = next(listing)
        adventure = {}
        adventure['name'] = get_adventure_name(f)
        adventure['types'] = get_adventure_types(f)
        adventure['gps_json_str'] = get_adventure_gps_json_str(f)
        adventure['date'] = get_adventure_date(adventure['gps_json_str'])
        adventure['desc'] = get_adventure_desc(f)

        # Define new filename from date
        dt_obj = dt.strptime(adventure['date'], '%m/%d/%y, %I:%M %p')
        new_filename = dt_obj.strftime('%y-%m-%d_%H-%M') + '.json'

        convert_to_json(new_filename, adventure)

        with working_dir('./data/json-unenhanced'):
            os.remove(f)

        keep_going = input('Enter "n" to stop or any other key to continue: ')

    return

if __name__ == '__main__':
    main()