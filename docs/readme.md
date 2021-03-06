docs
======

FERGUS documentation is planned to be driven by [sphinx](http://sphinx-doc.org/), but will simply be [Markdown](http://daringfireball.net/projects/markdown/syntax) for now.

# Core System
The FERGUS core is designed to take in a verbal command, parse the commmand and query a database of known commands, execute the command, and return an appropriate result.  As one might be able to imagine, the core and library designs are heavily influenced by operating system infrastructure.

Essentially, this all breaks down to combining different available modules and adding necessary components to tie them together.  This is what make up the core of this Extendable System.

## Speech Recognition (speech to text)
Using the [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) cross-platform audio I/O library, FERGUS can transcribe and parse user input.  Although it looks like PyAudio is kindof outdated and [Speech Recognition](https://pypi.python.org/pypi/SpeechRecognition) should better fit the task.

## Speech Analysis
With the use of a [Natural Language Toolkit](http://www.nltk.org/), [NumPy](www.numpy.org), and [General Hidden Markov Models](http://ghmm.org/), the FERGUS core is being designed to parse human speech into computer useable commands.

## Command Database
The basic commands are defined withing the [core](https://github.com/andrewbates09/FERGUS/tree/master/core).  Community added applications interfaces and commands exist within the [library](https://github.com/andrewbates09/FERGUS/tree/master/library).  To start out, the core will have the commands necessary to interact with a user-extendable [SQLite](http://www.sqlite.org/) database, which can record the call-count of different FERGUS functions.

## Text to Speech
For response handling, output will be directed through [pyttsx](http://pyttsx.readthedocs.org/en/latest/index.html), a cross-platform text-to-speech module, which is included in [PyPI](https://pypi.python.org/pypi).

# Installation
This project has a lot of dependencies. Initially to use, everyone is going to just have to download the dependencies on their own to use the core.  In the future, I hope to implement an internal dependency handler.  You might have gotten a feel of the dependencies from the documentation above, but I will go ahead and make a list so it is easy.
1. [pip](https://pip.pypa.io/en/latest/installing.html#id7)
2. [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)
3. [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition)


TODO: installation and basic useage instructions go here

# Testing
TODO: add initial testing documentation here, refer to tests

# Extending
This project will be designed with security in mind, but more time is needed fully implement [cryptographic services](https://docs.python.org/3.4/library/crypto.html) for maintaining the database.

Possible ways of extending the project includes but is certainly not limited to utilizing [OpenCV](http://docs.opencv.org/) to add [image processing](http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc), [video analysis](http://docs.opencv.org/trunk/doc/py_tutorials/py_video/py_table_of_contents_video/py_table_of_contents_video.html#py-table-of-content-video), and [object detection](http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_table_of_contents_objdetect/py_table_of_contents_objdetect.html#py-table-of-content-objdetection).

Ability to see networks and devices - [sys](https://docs.python.org/3/library/sys.html), [nmap](https://pypi.python.org/pypi/python-nmap), [wi-finder](https://github.com/mpescimoro/wi-finder/blob/master/wifinder.py) - or infrastructure monitor [Nagios](http://www.nagios.org/)

Daily data log, probably kept in a sql db log file.
- log#, date, data - see [datatypes](https://www.sqlite.org/datatype3.html) and [limits](https://www.sqlite.org/limits.html)

TODO: add documentation about FERGUS, the core, installation, and extension
