This does work to record audio from the browser! Files are created on the backend. Not streaming, but promising.

```
docker-compose up
```

and then navigate to http://localhost:8888/

`Record` + `Stop` a recording; note that `*.wav` file is created as a result, and it does contain the recorded audio.

Whatever the "Encode" checkbox does seems to prevent the audio from being distorted.

## Original README.md below

# brautopy

BRowser webAUdio TO PYthon webserver

This sample application :

- Captures microphone input from a web browser (the webaudio API)
- Encodes audio stream with opus.js encoder
- Sends the stream to a python websocket server (tornado)
- Decodes the stream with python-opus & saves wav file on the server

**Installation**

Python3.6 recommended.

```
pip install -r requirements.txt
python server.py
```

In browser open: http://localhost:8888

On OSX & Windows, libopus have to be installed separately.

OSX:

```
brew install opus
```

Windows:

Download the opusfile windows zip (not the source) from here: https://www.opus-codec.org/downloads/
Copy the libopus-0.dll into PATH or brautopy directory.
