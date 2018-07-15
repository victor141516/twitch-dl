# twitch-dl

## Description

Download videos from Twitch, even private ones

## Usage

1. Open the url where you have deployed this (instructions below)
2. Omit nefarious design
3. Type a twitch video url and upload a cookie file if the video is private (you can obtain it using [this Chrome extension](https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg/related?hl=en))
4. Click "download"
5. Profit

## Deployment

    $ git clone https://github.com/victor141516/twitch-dl
    $ docker build -t twitch-dl twitch-dl
    $ docker run -d -p 8000:8000 --name twitch-dl twitch-dl

Now you can access http://localhost:8000 and use twitch-dl

PD: If you plan to deploy twitch-dl on localhost and use it only from there, I suggest you to use youtube-dl instead. twitch-dl is intended for be deployed as a service.
