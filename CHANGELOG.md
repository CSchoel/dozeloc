## [1.0.6]

### Added

* Settings option `ttk_theme` to either let python choose the theme (`"auto"`) or manually enter a theme name to be used.

## [1.0.5]

### Fixed

* If PYTHONPATH did not exist, Dozeloc tried to write a Path object into the environment dict instead of a string.
* On Windows Dozeloc did not work, because it assumed that stdout and stderr used utf-8 as encoding.

## [1.0.4]

### Fixed

* Copy and paste from test output and exercise text is now possible on all platforms
* Selection in markdown widget is now shown above gray background for code.

### Changed

* Scroll bars of output and exercise text are now themed widgets from `ttk`.

## [1.0.3]

### Fixed

* `run_unittest` now enforces absolute paths to ensure that `cwd` parameter does not lead to missing test or solution files.

## [1.0.2]

### Fixed

* Current working directory is set to test directory when executing unit tests.

### Changed

* The solution chooser now only remembers file names that were actually used for checking a solution. If the `last_solution.txt` does not exist or contains a path to a directory and not a file, the value of the last selected exercise is kept instead.

### Added

* Dozeloc now remembers the last exercise that was selected in the exercise directory.

## [1.0.1]

### Changed

* Uses `sys.executable` to ensure internal python call uses same executable as external python call.
* Uses `usr/bin/python3` instead of `usr/bin/python` in shebang.

## [1.0.0]

First version to be tested by tutors

[1.0.6]: https://github.com/CSchoel/dozeloc/compare/v1.0.5..v1.0.6
[1.0.5]: https://github.com/CSchoel/dozeloc/compare/v1.0.4..v1.0.5
[1.0.4]: https://github.com/CSchoel/dozeloc/compare/v1.0.3..v1.0.4
[1.0.3]: https://github.com/CSchoel/dozeloc/compare/v1.0.2..v1.0.3
[1.0.2]: https://github.com/CSchoel/dozeloc/compare/v1.0.1..v1.0.2
[1.0.1]: https://github.com/CSchoel/dozeloc/compare/v1.0.0..v1.0.1
[1.0.0]: https://github.com/CSchoel/dozeloc/releases/tag/v1.0.0
