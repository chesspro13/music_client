<h1>Home Wreker</h1>

This is a project to make a smart assistant (google home *[where it gets its name]*, alexa, siri, exc.) that will run on
a raspberry pi. This is mostly made from scratch, but uses several python libraries and two projects found on github.

There are two parts to this program. A web interface, and a client script.

1) The web interface uses javascript to call python functions in the Django project.
2) The python project creates a file in the folder ~/speaker/commands that describes the action
3) The client does a scan on the directory and if it finds a command file it will execute the command then remove the file.

First steps are to get the music client working.