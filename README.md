This is a formatter for python Behave testing framework, that generates a zip file compattible with Zepher for Scale

Results will be written to 'results/zephyr' folder.
JSON files will be generated named according to the tag used in Zephyr.
A .zip file allso be present, will can be used to upload to Zephyr to update test results.

Install:
pip install zephyr-behave

Usage:
behave features/*.feature --format=pretty --format=zephyr_behave.formatter:ZephyrFormatter 