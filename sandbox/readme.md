Sandbox
======

This sandbox is for unbridled shenanigans and extension testing.

# Audio & Recording testing
Alright, so I have spent quite a it of time here testing on the B+ and have come across loads of issues. Not to fear, I have not given up hope, if only held back for a bit.

* speech recognition requires pyaudio, which doesn not seem to work on the pi bi+ / arm system. it looks like [primary](http://people.csail.mit.edu/hubert/pyaudio/docs/) support is for python2, and that is what pip grabs unlike [py3](https://launchpad.net/ubuntu/utopic/armhf/python3-pyaudio/0.2.8-1)
* in recording testing, [arecord](http://maffulli.net/2013/03/23/streaming-audio-from-raspberry-pi-part-2/) is fuzzy because of hardware issues with the pi - I did exensive testing on different ranges of frequencies - I even tried
* next thing to do is look into [cmusphinx](http://cmusphinx.sourceforge.net/wiki/raspberrypi) and [other](https://sites.google.com/site/observing/Home/speech-recognition-with-the-raspberry-pi) implementations and [such](http://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/).
