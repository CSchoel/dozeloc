#!/bin/bash
# Cleans up dozeloc cache files

# delete dozeloc settings
find "../uebungen/dozentron" -name "last_result.txt" -exec rm {} \;
find "../uebungen/dozentron" -name "last_solution_path.txt" -exec rm {} \;

# delete python cache files
find "../uebungen/dozentron" -name "__pycache__" -exec rm -rf {} \;

# delete empty directories
# NOTE: "-exec rmdir {} \;" would issue warnings due to BFS-traversal
find "../uebungen/dozentron" -type d -empty -delete
