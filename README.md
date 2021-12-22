# Python Parallel Execution using pytest

## Pre-requisites

- Python Editor
- Latest Python
- Latest pip
- Latest selenium
- Latest Webdriver-manager
- Virtual environment for pytest

## Description

In this project we are going to execute our testcases in parallel mode on our local machine. We are using **pytest** & **pytest-xdist** packages to run tests in parallel. We are using **webdriver-manager** so we can make our script environment independent. So We wont have to download our web driver everytime on update or for new browsers. 

**test_one.py**, **test_two.py** & **test_parallel.py** are the file where we have written our test cases which we want to run parallelly.

Before using pytest you will need to create your virtual env. So whatever package you will require for your execution will be installed in that environment. It will help you execution to run on different version of packages without affecting the global setting ot environment. 

## Steps to setup

Please follow below setup steps:

- clone the repo
- check if pre requisites are properly installed
- Add all the necessary packages added inside requirement.txt.
- Add Python files and add testcases inside them just like I did in **test_one.py**, **test_two.py** & **test_parallel.py**

## Create virtual environment:

- Install the virtualenv package
```sh
pip install virtualenv
```
- Create the virtual environment
```sh
virtualenv mypython
```
Note: mypython is your envronment name
- Activate the virtual environment
```sh
source mypython/bin/activate
```
Note: mypython is your envronment name
- Deactivate the virtual environment
```sh
deactivate
```

## Installation

To install all the packages in requirements.txt run this command

```sh
pip install -r requirements.txt
```
or 
```sh
pip3 install -r requirements.txt
```
## Steps to run tests in Parallel in One Browser Eg - all tests in Chrome:

open terminal navigate to the project folder

```sh
pytest -n 5
```
**Note:** 5 indicate parallel thread count or number of browsers or number or chrome instances
 
 Lets say if you have 10 testcases and you are hitting below command then first 2 testcases will get execute and other will be in queue then next 2 and rest of the test cases will be in queue.
 ```sh
pytest -n 2
```
 
 ## references:
 **Python Virtual Environments**
 [https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/]
 **Pytest-xdist: Run tests in parallel**
 [https://qxf2.com/blog/xdist-run-tests-parallel-pytest/]
 
 
***😉Lets kill 🐞 together😉***
