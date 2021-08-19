
**zephyr-behave**

This is a formatter for python Behave testing framework, that generates a zip file compatible with Zephyr for Scale

Results will be written to '*results/zephyr'* folder.
JSON files will be generated named according to the tag used in Zephyr.
A .zip file also be present, which can be used to upload to Zephyr to update test results.

*Note:* *Before each run, the results folder will be cleared*


Install:

    pip install zephyr-behave

Usage:

    behave --format=pretty --format=zephyr_behave.formatter:ZephyrFormatter 
