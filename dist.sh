#!/bin/bash
# builds distribution zip file of Dozeloc
# must be run from within this directory

# clear distribution folder if it exists
rm -rf dist/

# create distribution folders
mkdir -p dist
DIST="dist/dozeloc-$(cat version)"
mkdir -p $DIST

# copy main files
cp dozeloc.py $DIST/
cp version $DIST/
cp default_settings.json $DIST/settings.json

# copy all exercise directories
mkdir -p $DIST/exercises
find ../uebungen/dozentron -maxdepth 1 -type d -regex '.*[0-9]+_[0-9+].*' -exec cp -r {} $DIST/exercises/ \;
# exclude last_xyz.txt setting files
find $DIST/exercises/ -name "last_*.txt" -exec rm {} \;
# remove solution files
find $DIST/exercises/ -type d -name "src" -exec rm -rf {} \;

# zip distribution folder contents
cd dist
zip -r "dozeloc-$(cat ../version).zip" "dozeloc-$(cat ../version)/"
