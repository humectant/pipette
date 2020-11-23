IDE Support
===========

### Pycharm
To use the interpreter from the local virtual environment created by pipenv, use Virtualenv Environment 
and select the virtual environment's python executable.

To use the interpreter from docker-compose, so that you can debug within a container, 
follow the instructions [here](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote
)

You can switch between the interpreters but note that PyCharm will take control of docker-compose and stop 
and start containers according to its whim. 

Use `your path/pipette/app/main.py` for a FastAPI run configuration. To keep 
all containers running set `Command and options` in the Run configuration to `up`.

To use the debugger, start a FastAPI run configuration and run in debug node. It will 
abide by your breakpoints.  Alternatively, you may run tests in debug mode. 