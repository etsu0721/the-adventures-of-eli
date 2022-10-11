from gpxcsv import gpxtofile
from contextlib import contextmanager
import os, glob, shutil

@contextmanager
def working_dir(path):
    init_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(init_dir)

# Get list of unconverted GPX file names
with working_dir('./data/gpx-unconverted'):
    listing = [file for file in glob.glob('*.gpx')]

# If listing is empty, exit program
if len(listing) == 0:
    print('No GPX files found to convert...exiting')
    os._exit(status=0)

# For filename in listing, 
for fn in listing:
    # Convert GPX to JSON and organize
    fn_json = fn.replace('gpx', 'json')
    src_gpx = './data/gpx-unconverted-tmp/{}'.format(fn)
    dst_json = './data/json-unenhanced-tmp/{}'.format(fn_json)
    gpxtofile(
        src_gpx,
        dst_json,
        json=True
    )

    # Move GPX file to gpx-converted directory
    dst_gpx = './data/gpx-converted-tmp/{}'.format(fn)
    shutil.move(src=src_gpx, dst=dst_gpx)
