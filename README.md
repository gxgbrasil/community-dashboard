# Community Dashboard

> Know more your communities

[![Build Status](https://snap-ci.com/anapaulagomes/community-dashboard/branch/master/build_image)](https://snap-ci.com/anapaulagomes/community-dashboard/branch/master)

Know more about your communities from [Meetup.com](http://meetup.com). You may just type the URL (after [meetup.com/]((http://meetup.com))). Have fun! [Community Dashboard](http://communitydashboard.heroku.com)

## Meetup API Access

To retrieve the information available on groups of [meetup.com]((http://meetup.com) you need to get an [new API key](https://secure.meetup.com/meetup_api/key/). After this, save as environment variable $MEETUPAPIKEY with the value of you API key.

## Requirements

- Python 2.7
- Flask
- VCR.py
- Requests
- Selenium

## Development Setup

With [pip](https://pypi.python.org/pypi/pip) installed, use them to install all requirements:

```
pip install -r requirements.txt
```

To run the application, execute:

```
python run.py
```

After run, you can access [http://localhost:5000](http://localhost:5000).

## Tests

To run the tests suite, execute:

```
python -m unittest tests.unit
python -m unittest tests.functional
```

## Credits

- Ana Paula Gomes: idea and development
- Carlysson: responsible for the great design of this application.

## License

Distributed under the XYZ license. See ``LICENSE`` for more information.
