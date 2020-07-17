# Lab1

* Create a simple python script with a Factorial class with the following interfaces:

```
class Factorial():
    ...
    def compute(n: int) -> int:
        ...
```
* Create a Makefile with the following targets:
    - environment: shall install following python dependencies "environs, semantic_version"
    - test: shall run a test 'pytest' validating defined class 
    - run: shall run the script accepting an argument and printing the value on terminal.
* Any code that is not being used in either of files (i.e. Makefile, script, test) shall be removed.
* Argument 'n' shall be passed to the script as part of 'make run' target 

 
# Lab2

* Start from the previous lab.
* Replace the earlier create script with a FastAPI server (single file server.py) and update the Makefile 'run' target to run a FastAPI webserver.
* Add an HTTP endpoint  *POST /compute/factorial* which will accept a number and will return following JSON response:

```
{
  "input": n,
  "factorial": xyz,
  "time_taken": "0.003ms"
}
```

* Write test cases for the endpoint
* Any code that is not being used in either of files (i.e. Makefile, script, test) shall be removed. 
* Add a 'package' target which will create a docker image of the service
 

# Lab3

* Start from the previous lab.
* Breakdown the earlier server.py into existing git service structure i.e. api, models, services structure. 
* Add another HTTP endpoint  POST /compute/checkPrime which will accept a number and will return following JSON response:

```
{
  "input": n,
  "is_prime": true,
  "time_taken": "0.053ms"
}
```
 
* add another section for text modification, and add HTTP endpoint POST /text/removeDuplicate which will accept a text string and will return following JSON response by removing duplicate characters (excluding spaces):

```
{ 
  "input": "hello how are you",
  "result": "helo w ar yu", 
  "time_taken": "0.023ms"
}
```

* Write test cases for the added endpoint
* Any code that is not being used in either of files (i.e. Makefile, script, test) shall be removed. 
* Add a 'package' target which will create a docker image of the service

Each lab has been done on a new branch
Credits for the bootcamp lab- Hemant Kashniyal