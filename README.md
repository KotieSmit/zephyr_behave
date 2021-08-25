
  

**zephyr-behave**

  

This is a formatter for python Behave testing framework, that generates a zip file compatible with Zephyr for Scale

  

Results will be written to '*results/zephyr'* folder.

JSON files will be generated named according to the tag used in Zephyr.

A .zip file also be present, which can be used to upload to Zephyr to update test results.

  

*Note:*  *Before each run, the results folder will be cleared*

  
  

**Install:**

`pip install zephyr-behave`

**Configure:**

Add your configuration options to the behave.ini file or supply at runtime in the terminal

*behave.ini file:*

    [behave.userdata]
    ZEPHYR_UPLOAD_RESULTS=true
    ZEPHYR_API_KEY=your-api-key
    ZEPHYR_API_URL=https://api.zephyrscale.smartbear.com/v2/automations/executions/cucumber
    ZEPHYR_PROJECT_KEY=your_jira_project_key
    ZEPHYR_AUTO_CREATE_TEST_CASES=false
    REMOVE_JSON_FILES=true

*command line:*

    behave  "-D zephyr_api_key=your-api-key" "-D ZEPHYR_PROJECT_KEY=demo"

**Usage:**

  

behave --format=pretty --format=zephyr_behave.formatter:ZephyrFormatter