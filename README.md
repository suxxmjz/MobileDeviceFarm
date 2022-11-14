# Mobile Food Marketing Scrapper

This repo contains code to run [airtest](https://airtest.netease.com/) on mobile devices. Each folder represents a different application.

`template.air` is a generic folder which can be used to start a new airtest project with less friction. Feel free to use this template and its functions in any app you wish to scrape data from. Most of the apps follow fairly similar patterns for scrapping data, albeit with minor but critical differences.

The folder structure is as follows:

```
AppName
-- AppName.py
-- .jpg // image triggers for airtest
```

Android SDKs are not included in this repo (since they are too large), nor are the ads (will be uploaded to the pipeline using the connector). You can download the sdks from [here](https://androidapksfree.com/) and include them in their respective folders.

Simulators are not supported.

## TODOS
- Include support for iOS devices

## Requirements
- Python 3.10.0
- pip 21.2.3
- Linux or Mac OS (iOS apps require xcode toolchain)
- ADB (for android)

## Setup
Developer permissions must be enabled on each device, you can follow [this](https://peter-pan.atlassian.net/wiki/spaces/DL/pages/335970309/Airtest+IDE) tutorial for further information.

## Getting Started

**Development:**

Ensure you are in the correct repository:
```
cd mobile-scrapper
```
Create a virtual environment:
```
python3 -m venv ./venv
```
Activate the virtual environment:
```
source ./venv/bin/activate
```
Install the required packages:
```
pip install -r requirements.txt
```

## To Run From Command Line

Run the streamlit app:
```
streamlit run app.py --server.maxUploadSize=500
```

If the application crashes during a session, close the web page and terminal. Then use start-up script below to re-run it:
```
./start.sh
```


## License
All Rights Reserved

Copyright (c) Sukriti Sharma 2022