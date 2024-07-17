# Installation

In preparation for the Introduction to Python workshop, you will need to have
installed Python and a development environment for it.

## Installing Python

### Windows

You can install Python directly from the Windows Store. Microsoft provides
[installation instruction](https://learn.microsoft.com/en-us/windows/python/beginners#install-python).
You do not need to follow the Visual Studio Code or Git setup.

### macOS

> These instructions have not been tested

Depending on what version of macOS you have installed, you may have

If you need to install Python, you can find an installer for it on the
[Python website](https://www.python.org/downloads/macos/). Alternatively, if you
already have Homebrew installed you should be able to install python with
`brew install python`.

### Ubuntu Linux

Any Ubuntu installation should come with Python pre-installed. You can check
this by opening a terminal window and typing `python --version`.

On my machine I get the result below. The version number doesn't have to match
exactly, but it should at least be greater or equal to Python 3.7.

```sh
$ python --version
Python 3.12.3
```

While Python is installed by default, pip, the Python package manager, might
not be. Once again, you can check whether this is the case by running
`pip --version`.

```sh
$ pip --version
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

If you instead get an error saying the `pip` command was not found, you should
install it by running the following:

```sh
$ sudo apt install python3-pip
```

## Installing an IDE (Integrated Development Environment)

During the session I will be using Positron, a modified version of VS Code made
by the same people that make RStudio, as the development environment. As such,
it has a a similar look and experience as you might already be used to. While
you are free to use another editor if you prefer, I would recommend using
Positron too so it is easier to follow along.

You can download the latest version of Positron on their
[release page][positron-release].

### Setting up Positron

Before we can use Positron, we must make sure it is able to interact with your
Python installation.

1. Open up Positron
2. In the top-right corner, click on the "Start interpreter" button
3. Click on the "power button" for the listed Global Python.
4. You may be prompted to install a package called `ipykernel`. If this happens, answer "Yes".
5. If all goes well you should now see an interactive Python session in the lower half of the Positron window.

[positron-release]: https://github.com/posit-dev/positron/releases

