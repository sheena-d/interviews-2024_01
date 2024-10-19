# Technical Interview Exercise 2024_01

## Overall Approach
My goal is to create a framework that is as flexible as possible without being unduly difficult to use or 
maintain. To that end, the script can accept a single test suite that covers all platforms that need testing, but will 
only execute the tests that are relevant for the active platform. For simple tasks, such as file creation and 
modification, a test case definition can be platform-agnostic (e.g. creating a file at a relative path) or can be tagged for
a specific platform (e.g. for editing a specific file within the host OS). This allows the test maintainers to write as 
little duplicate test definitions as possible.

In addition, the code within the testing application is written such that tasks that are applicable to all test cases 
(e.g. determining the username that initiated the process) are handled in a parent class, which is extended in child classes 
where more specific tasks are defined. In addition, platform support is determined on the most specific class level 
possible, so that one test suite definition can be used for all platforms whether that particular test case is supported
for all platforms or not.

## Test Case & Platform Coverage
for each platform: Support is written / Support is verified (Y/Y, Y/N, N/N)

| Test Type           | Linux | Windows | Darwin |
|---------------------|-------|---------|--------| 
| File Creation       | Y/Y   | Y/N     | Y/N    |
| File Modification   | Y/Y   | N/N     | Y/N    |
| File Deletion       | Y/Y   | Y/N     | Y/N    |
| Network Transfer    | Y/Y   | N/N     | Y/N    |
| Process Execution   | Y/Y   | Y/N     | Y/N    |

## Usage Instructions
Test cases are defined in a JSON file. `test_suite.json` is provided as an example and is the default file used by the 
script. Each test case defined in the JSON file have the following attributes:
- `type`: Class name of the test to be run
- `platform`: Optional attribute to restrict the test run to a specific OS platform
- `test_name`: arbitrary name for the test, for matching output to test case and/or tracking failures of test cases.
- `args`: a list of arguments to be passed to the test Class.

To perform the tests:
    from the project root directory
```shell
$ python src/os_process_logging/__init__.py -i input_file.json -o output_file.json
```
Omitting the `-i` and `-o` arguments will utilize the default files `test_suite.json` and `test_logs.json`

