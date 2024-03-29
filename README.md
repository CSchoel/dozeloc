# Dozeloc

Dozeloc is a teaching tool for the local and automated checking of Python programming exercises.
It allows students to select exercises and run unit tests on their machine with little to no setup by just running a python script that opens a minimalistic and intuitive GUI.

## Quick start

1. Make sure you have Python 3.8 or higher installed on your operating system. Also ensure that this is a full python installation that includes the `tkinter` standard library. You might have to install a package called `python-tk` or `python3-tk` if Dozeloc complains that it can't find `tkininter`.
2. Download the `dozeloc-X.Y.Z+N.zip` from the latest [release](https://github.com/CSchoel/dozeloc/releases).
3. Extract the ZIP archive.
4. Execute the file `dozeloc.py` with Python, for example from a terminal with `python3 dozeloc.py`.

This will bring up the following GUI:

![window with exercise selection and test result on the left and exercise text on the right](dozeloc.gif)

## Structure of exercise folders

You can specify an exercise folder to use either in `settings.json` or by calling `python3 dozeloc.py path/to/exercise/folder`.
The exercise folders must have the following structure where `code` formatting indicates fixed names and normal formatting indicates names that can change to your liking:

* nameOfFirstExercise
  * `test`
    * nameOfUnittest.py
    * nameOfOtherUnittest.py
  * exerciseDescription.md
* nameOfSecondExercise
  * `test`
    * nameOfUnittest.py
    * fileThatStudentsHaveToParse.csv
  * secondExerciseDescription.md
* ...

The unit test files should contain unit tests written with the module `unittest`.

## How to get a folder with exercises for testing Dozeloc

The release version of Dozeloc comes with a set of English exercises exported from  [exercise-heap](https://github.com/CSchoel/exercise-heap).
If you want exercises in a different language (only German is currently available), you can get them by cloning the exercise-heap repo and calling the export script:

```bash
git clone https://github.com/CSchoel/exercise-heap.git
python exercise-heap/scripts/export/export_dozeloc.py -l de-DE -o ./exercises
python dozeloc.py exercises
```

## Known issues

Dozeloc does not require any packages outside the Python standard library.
However, some distributions (including Ubuntu) do not install the full standard library but leave out the `tkinter` module.
In these cases you need to install the additional package `python-tk` or `python3-tk`.
