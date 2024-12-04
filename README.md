# info-hub-lti

[![Build Status](https://github.com/uw-it-aca/info-hub-lti/workflows/Build%2C%20Test%20and%20Deploy/badge.svg?branch=main)](https://github.com/uw-it-aca/info-hub-lti/actions)


## Description
info-hub-lti is an LTI tool built to display
UW Teaching and Learning Resources for Canvas course members.

## Test Drive

To experience the tool in a development environment using mock data,
make sure docker is installed on your host and then run:
```
    # docker-compose up --build
```
Once built and running, you can start the LTI tool launch
sequence by visiting:
```
    http://your-host:8000/blti/dev
```
from your brower.
