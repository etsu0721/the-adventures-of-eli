#!/bin/sh

echo "Checking for GPX files..."

# Try to convert GPX to JSON
# -O option ignores AssertError
RES=$(python -O -m gpxcsv ./data/gpx-unprocessed/*.gpx -j)

# If RES is empty string, then no files to convert were found, exit
if [ "$RES" = "" ]
then
    echo "No GPX files found"
    exit 1
fi

# Otherwise conversion takes place and files are organized
echo "Found GPX files"
echo "Converting..."
echo "$RES"

echo "Moving JSON files..."
mv -v ./data/gpx-unprocessed/*.json ./data/json/

echo "Moving processed GPX files..."
mv -v ./data/gpx-unprocessed/*.gpx ./data/gpx-processed/
