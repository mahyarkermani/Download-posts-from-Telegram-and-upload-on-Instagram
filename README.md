# Warning

Support for this source code (repository) ended in April 2022 and this source will no longer be updated. So, the code may have bugs and you can run it and debug it (and send the modified version to my email to publish with your name) or use the forks of this repository.


# Introduction

This module receives Telegram channel posts that are sent after the robot starts working
and uploads them to your Instagram account.
The program constantly monitors a telegram channel.
If the desired telegram channel sends a new post (photo or video), it will download it and upload it to your Instagram account.



# How does the program work?

This app will receive the following information from you:

- Telegram API ID
- Telegram API HASH
- Your channel id (Telegram)
- Your username (Instagram)
- Your password (Instagram)

Then, using this information, The app will log into your Instagram and Telegram accounts. After that,
the program continuously checks the Telegram channel, whose address you entered. If a new post is posted on the channel after the robot is launched (photos and videos),
the robot will download it and upload it to your Instagram account.
This program is built with a few basic features and in the future its bugs will be fixed and various options will be added to it,
so be careful in using it (enter your information completely and accurately and from Make sure the robot is set up correctly)


# Abilities

- Show logs in a window
- At the first launch, the robot will ask you for telegram information such as phone number, etc.,
and then create a session that will help itself remember your account (your information is not published anywhere, only next time)
When the robot is set up, it will be easier to identify your Telegram account
- If no new post is published on your channel, the app will pause for 1 minute and then check your Telegram channel again (all steps are automatic)


# Tested on

Currently, this program has only been tested on Windows 10, and with Python 3, and will be compatible with other operating systems in the future.
So please customize it if needed.


# Introducing the tool

This program is provided in the form of Python source code, and in this section we will introduce
the folders and tools available in the program.
The first folder is plugin, Where the webdriver of the browser is located (to run programs and scraper, we need this software).
In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

- Firefox download link: [Mozila Page](https://www.mozilla.org/en-US/firefox/download/thanks/)
- Webdriver download link: [Github Page](https://github.com/mozilla/geckodriver/releases/)

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.
The next folder is the software, where we usually put the software needed in the Windows operating system so that you can install them if needed.

The media folder is where the files downloaded from the channel you want are located.


# Prerequisites

This program is written with Python 3.9 but supports Python 3 and all versions.
The required modules of this program are located in the 'prerequisites' file in the plugin folder, and you can install the required modules with the following command:

```
python -m pip install --upgrade pip
python -m pip install -r plugin\\prerequisites.txt
```


In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

- Firefox download link: [Mozila Page](https://www.mozilla.org/en-US/firefox/download/thanks/)
- Webdriver download link: [Github Page](https://github.com/mozilla/geckodriver/releases/)


Also, visit the website below to get API-ID and API-HASH:

- Telegram apps: [Telegram Page](https://my.telegram.org/apps/)

You must also enter the username, password and channel ID of the channel you want (you will be asked when launching the robot).


# About the author

This program was written by a young Iranian and this person tries to keep his GitHub programs always up to date.
If would you like to contact me, you can send a message to my personal email:

- **mohammadmahyarkermani@gmail.com**


# Report bugs

Since this program is written as a scraper and with a small change on Instagram, it may crash,
Please if you have any problems with how the program runs and works, please publish your error in the issue section of GitHub
or send it to my email to fix the bugs of the program as soon as possible. Thank you for your cooperation :)
