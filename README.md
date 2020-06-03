# DiscordBot

A simple python discord bot announcing when a user joins a channel using Google
TTS library and discord.py wrapper.

## Pre-requisites

* Python >= 3.6
* ffmpeg
* a Discord bot token

## Installation

Install the required python libraries or use a virtualenv

`pip3 -r install requirements.txt`

Set your API keys in a config.py file

```python
touch config.py
echo "CLIENT_ID=yourclientid" >> config.py
echo "TOKEN=yourtoken" >> config.py
```

## Usage

Run 

`python3 application.py`

## TODO

- [x] Implement announcing function
- [ ] Implement a thread pool
- [ ] Implement a reddit scrapper
- [ ] Schedule a post every Wednesday (my dudes)

## Author
* [BadMiscuit](https://github.com/BadMiscuit) - Initial work 
