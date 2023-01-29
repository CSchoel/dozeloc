#!/bin/bash
# builds distribution zip file of Dozeloc
# must be run from within this directory

# clear distribution folder if it exists
rm -rf dist/

# create distribution folders
mkdir -p dist
EXERCISE_SOURCE=./exercises
EXERCISE_REGEX='.*/[0-9]+\_.*'
EXCOUNT=$(find "${EXERCISE_SOURCE}" -maxdepth 1 -type d -regex "${EXERCISE_REGEX}" | grep -c /)
DIRVERSION="dozeloc-$(cat version)+${EXCOUNT}"
DIST="dist/${DIRVERSION}"

mkdir -p $DIST

# copy main files
cp dozeloc.py $DIST/
cp version $DIST/
cp default_settings.json $DIST/settings.json

# copy all exercise directories
mkdir -p $DIST/exercises
find "${EXERCISE_SOURCE}" -maxdepth 1 -type d -regex "${EXERCISE_REGEX}" -exec cp -r {} $DIST/exercises/ \;
# exclude last_xyz.txt setting files
find $DIST/exercises/ -name "last_*.txt" -exec rm {} \;
# remove solution files
# NOTE: -depth is needed to switch to depth-first traversal,
# which avoids warnings due to not being able to traverse the deleted directories
find $DIST/exercises/  -depth -type d -name "src" -exec rm -rf {} \;

# zip distribution folder contents
cd dist
zip -r "${DIRVERSION}.zip" "${DIRVERSION}/"
cd ..
