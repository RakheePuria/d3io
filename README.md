Project Name:d3io

Features:
This is the python project which is created to execute the testcase specified in 
https://github.com/gridsingularity/interview_tasks/blob/master/quality_assurance/task_description.md
The project is enabled to be executed on chrome browser.

Pre-requisites:
1) Install Python 2.7.14 or above
2) The requirement.txt file contains the dependencies to be included before running the testcases:
behave==1.2.7.dev2
selenium==3.141.0

The project contains: 
a)Feature file : Which contains the scenarios to be executed
b)StepDefinition file: Which contains the glue to the test steps
c)Environment.py file contains steps to be executed before any test is executed and after the tests are executed
d)set.cfg file acts as a property file which contains environment related parameters
e)The testcases are written in BDD format i.e in the form of Given,When,Then


Execution steps:
1)Go to project folder
2)Run command: behave .\tests\feature\