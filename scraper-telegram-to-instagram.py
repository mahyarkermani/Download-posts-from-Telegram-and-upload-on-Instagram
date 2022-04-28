"""
# Introduction

This module is responsible for liking the comments Blow
the post accounts are collected from the user's following.
This app is a scrapper to do some things on the Instagram website.
This program receives and likes the comments below each post of the last 24 hours from your following

# How does the program work?

This app will receive your Instagram account username and password.
Then it enters your account for the first time and receives and saves
the list of all your followings and then leaves your account.

It will then login to your account again and receive the last 24 hours
of posts from each user (your followings). It then checks to see if the
comment is below the posts and then it likes all the comments below the
post by your account. 
It does this enough to like all the comments below the received posts.
After finishing the work, it rests for 15 minutes and then activates automatically.
It then checks again to see if there is a new post and if there is a comment
below the posts, It likes them. Also, if a new comment is placed below previous posts,
it recognizes them and likes them again. 
Note: Every post whose comments are liked, the post itself is liked


# Abilities

This program is tested only on Windows operating system and works completely and without bugs, on Windows operating system.
so if you are Linux or Mac, etc., please customize the source code.
In future updates, I promise to synchronize the program with other operating systems.

- Displays all your logs in a cmd window in Windows
- If you wish, you can see all the steps and operation of the robot in a browser
- The program performs its activities completely automatically, and after finishing its work, it rests for 15 minutes and then restarts
- After each restart, it will check your recent 24 hour posts and all followins, and if it sees anything new, it will perform the desired operations
- Receives all comments below each post
- Every post whose comments are liked, the post itself is liked
- Various methods are designed for the robot to function properly and your account not to be blocked. So the program works completely and automatically and there is no problem for your Instagram accounts
- If you have a specific idea or option, let me know by email so I can add them to the robot
- Updates are provided to the app on an ongoing basis


# Tested on

Currently, this program has only been tested on Windows 10, and with Python 3, and will be compatible with other operating systems in the future.
So please customize it if needed.

# Introducing the tool

This program is provided in the form of Python source code, and in this section we will introduce
the folders and tools available in the program.
The first folder is plugin, Where the webdriver of the browser is located (to run programs and scraper, we need this software).
In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

- Firefox download link: [Mozilla Pages](https://www.mozilla.org/en-US/firefox/download/thanks/)
- Webdriver download link: [github Pages](https://github.com/mozilla/geckodriver/releases/)

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.
The next folder is the software, where we usually put the software needed in the Windows operating system so that you can install them if needed.


# Prerequisites

This program is written with Python 3.9 but supports Python 3 and all versions.
The required modules of this program are located in the 'prerequisites' file in the plugin folder, and you can install the required modules with the following command:

{python -m pip install --upgrade pip}
{python -m pip install -r plugin\\prerequisites.txt}

In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

- Firefox download link: [Mozilla Pages](https://www.mozilla.org/en-US/firefox/download/thanks/)
- Webdriver download link: [github Pages](https://github.com/mozilla/geckodriver/releases/)

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.


# About the author

This program was written by a young Iranian and this person tries to keep his GitHub programs always up to date.
If would you like to contact me, you can send a message to my personal email:

- **mohammadmahyarkermani@gmail.com**

You can also see my resume at the following link:

{}


# Report bugs

Since this program is written as a scraper and with a small change on Instagram,it may crash,
Please if you have any problems with how the program runs and works, please publish your error in the issue section of GitHub
or send it to my email to fix the bugs of the program as soon as possible. Thank you for your cooperation :)


"""
# Import modules
# Telegram operating
from telethon import TelegramClient
# Instagram operating
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# Display mode
from colorama import Style, Fore, init
from platform import system
import time, datetime, os


def show_log(message:str, status:str="notif"):
    """This function displays various reports in a window that opens in the application.
    - parameters:
        - message: str
            - The report that each function sends of its performance.
        - status: str
            - Message sending status (notif, success or error, default: notif)."""

    try:
        # Identify message status and display output
        init() # Show color correct
        if status.lower() == "notif":
            print (Style.BRIGHT + Fore.BLUE + "[*] " + Style.BRIGHT + Fore.YELLOW + message + Style.RESET_ALL + Fore.RESET)

        elif status.lower() == "success":
            print (Style.BRIGHT + Fore.BLUE + "[+] " + Style.BRIGHT + Fore.GREEN + message + Style.RESET_ALL + Fore.RESET)

        elif status.lower() == "error":
            print (Style.BRIGHT + Fore.BLUE + "[!] " + Style.BRIGHT + Fore.RED + message + Style.RESET_ALL + Fore.RESET)

        # If the message status was unknown 
        else:
            print ("[-] " + message)
    
    # If there is an error in displaying the colored text
    except:
        print ("""[!] There are problems displaying colors.
            Please report your error via email to the developer to resolve this issue:
                Developer Email: mohammadmahyarkermani@gmail.com\n""")
        print ("[*] " + message)

def clear_screen():
    """This module is responsible for cleaning the screen and logs"""

    try:
        # If platform and os was Windows
        if system().lower() == "windows":
            os.system("cls")
    except:
        show_log ("There was a problem cleaning the screen.", status="error")

def config():
    """This function sets the required variables from the config file in the plugin folder, 
    and sets various variables for the performance of other functions.
    This is also responsible for entering and setting up the telegram session."""

    try:
        # Sets the required variables
        global today_month, today_day, today_hour, today_minute
        global _username, _password, channel_id, message_id, client
        global path_geckodriver, website_insta_addr, \
        input_username, input_password, button_submit, notnow, \
        new_post, send_media, _next, share, success_upload, \
        close_post, button_accept_cookies, graphical_mode


        # Set special variables for use function upload_media_instagram
        path_geckodriver = os.path.abspath("plugin\geckodriver.exe")
        website_insta_addr = "https://www.instagram.com/"

        input_username = "input[name='username']"
        input_password = "input[name='password']"

        button_submit = "button[type='submit']"

        notnow = "//button[contains(text(), 'Not Now')]"

        new_post = "svg[aria-label='New Post']"

        send_media = "input[class='tb_sK'][accept='image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime']"

        _next = "//button[contains(text(), 'Next')]"

        share = "//button[contains(text(), 'Share')]"

        success_upload = "//h2[contains(text(), 'Your post has been shared.')]"

        close_post = "svg[aria-label='Close']"

        button_accept_cookies = "//button[contains(text(), 'Allow essential and optional cookies')]"

        session = os.path.abspath(r'plugin\telegram-bot')

        # Set the execution time of the program
        today_time = datetime.datetime.utcnow()
        today_month = today_time.month
        today_day = today_time.day
        today_hour = today_time.hour
        today_minute = today_time.minute

        # Set the variables required for information processing
        print (Style.BRIGHT + Fore.WHITE)

        api_id = int(input("What is your api id (Telegram): "))
        api_hash = input("What is your api hash (Telegram): ")
        channel_id = input("What is your channel id (Telegram): ")
        _username = input("What is your username (Instagram): ")
        _password = input("What is your password (Instagram): ")
        graphical_mode = input("[!] Do you want to see the browser window of all the steps (y/n)? ").lower()

        # Checks if the user has just entered the yes or no value
        # Does the user want to see the graphical environment of the robot performance?
        while True:
            if graphical_mode != "yes" and graphical_mode != "y" and graphical_mode != "no" and graphical_mode != "n":
                graphical_mode = input("Do you want to see the browser window of all the steps? y/n").lower()
            else:
                break

        print (Style.RESET_ALL + Fore.RESET)

        message_id = []

        # Login, create and save Telegram session
        client = TelegramClient(session, api_id, api_hash)

        # Clear screen
        clear_screen()

        # Display log
        show_log("Files were configured successfully.")
    
    # If an error occurs during the program
    except:
        # Display log
        show_log("""There is a problem with the configuration files. 
        Please check the config file in the plugin folder or
        Please report your error via email to the developer to resolve this issue:
            Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def _identify_path(file_path:str):
    """This function finds the extension of the desired file and gives the exact path of the file along with the output extension.
    This function is automatically embedded in other functions.
    - parameters:
        - file_path: str
            - Directory and the file in it (example: media\\mypic) and file without extension"""
    
    try:
        # Set and global some variables for other functions
        global path_file_complete
        # Separate the directory from the file name
        file_path = file_path.split("\\")

        # Get the list of files in the directory
        file_list = os.listdir(file_path[0])

        # Identify and receive the complete file path with the extension in the desired directory
        # The complete path of the file is given with the output extension
        for file in file_list:
            file_data = file.split(".")
            
            if file_data[0] == file_path[1]:
                path_file = str(file)
                path_file_complete = os.path.realpath("media\\" + path_file)
                show_log("New file path detected: " + path_file_complete)
    except:
        show_log ("""[!] There are problems identify path.
        Please report your error via email to the developer to resolve this issue:
            Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

async def download_media_telegram():
    """This function is responsible for downloading posts from the Telegram channel.
    Only posts that are sent to the channel after the start of the program are downloaded,
    new posts are downloaded and the identification and download steps are done automatically.
    Only photos and videos are supported and stored in the media folder."""

    try:
        # Sets the required variables for use other functions
        global result

        # Check the posts in the Telegram channel
        # starting from the last post
        # Only photos and videos are reviewed
        # Only posts that are sent to the channel after starting the program will be downloaded
        async for message in client.iter_messages(channel_id):

            # Identify new posts
            # Calculate post time
            message_time = message.date
            message_time_month = message_time.month
            message_time_day = message_time.day
            message_time_hour = message_time.hour
            message_time_minute = message_time.minute

            # Has it been downloaded before?
            if message.id not in message_id:
                # Identify new posts
                if message_time_month >= today_month and message_time_day >= today_day and message_time_hour >= today_hour and message_time_minute >= today_minute:
                    # Is it a photo or a video?
                    if message.photo or message.video:
                        # Identify path, download, save and display logs
                        show_log(f"New post found. It is being downloaded in the 'media' path called {message.id}, Please wait.")

                        name = f"media\{message.id}"
                        await message.download_media(file=name)
                        message_id.append(message.id)

                        _identify_path(name)

                        show_log(f"The new file was downloaded in the '{path_file_complete}' path.")
                        result = True
                        break
                    # If there was no photo or video
                    else:
                        continue
                # If no new post has been posted on the channel yet
                else:
                    show_log(f"No new posts have been posted on '{channel_id}' Channel yet.")
                    result = False
                    break
            # If this post was previously downloaded
            else:
                continue

    # If an error occurs during the program
    except:
        # Display log
        show_log("""There is a problem with the download function from Telegram, please check the following:
            - Check your channel address in the configuration file in the plugin folder
            - Set another channel address in the configuration file
            - Check your anti filter and internet
            - Your channel must be public
            - You should be able to download media on your Telegram channel
            - Your Telegram account should not be restricted or reported
            - or Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def login_to_instagram():
    """This function enters the Instagram account as a scraper,
    so that other functions have the necessary access to upload the post."""
    
    try:
        # Global and set required variables
        global driver

        # Set some options for browser scraper
        options_browser = Options()
        options_browser.add_argument("--no-sandbox")
        options_browser.add_argument("--disable-crash-reporter")
        options_browser.add_argument("--disable-extensions")
        options_browser.add_argument("--disable-logging")
        options_browser.add_argument("--log-level=3")

        # If selected by the user, the browser display window will not be displayed
        # Otherwise, if the user agrees, a browser window will open graphically and show the robot steps and process in an instant
        if graphical_mode == "no" or graphical_mode == "n":
                options_browser.add_argument("--headless")

        # Load driver, firefox and Instagram website for browser scraper
        load_driver = Service(path_geckodriver)
        # service=load_driver, options=options_browser
        driver = webdriver.Firefox(service=load_driver, options=options_browser)
        driver.delete_all_cookies()
        # driver.maximize_window()
        driver.get(website_insta_addr)

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, button_accept_cookies))).click()
            time.sleep(5)
        except:
            pass

        # Find username and password label in web page
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, input_username)))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, input_password)))

        # Clear username and password label
        # Write username and password account to labels
        username.clear()
        username.send_keys(_username)

        password.clear()
        password.send_keys(_password)


        # Find and click to button submit for login to account
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_submit))).click()

        # Ignore some pop-up and other window in operating
        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, notnow))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, notnow))).click()
        except:
            pass
        
        # Display log
        show_log(f"The app successfully entered the '{_username}' user account on Instagram.")
    
    # If an error occurs during the program
    except:
        # Display log
        show_log("""There was a problem logging to Instagram account. Please check the following:
            - Check your username and password in the config file in the plugin folder
            - Setup another account in the config file and try again with another account
            - Check your anti filter and internet
            - Your account must not have two-step verification
            - Your Instagram account should not be restricted or reported
            - Reinstall the Firefox file
            - Make sure the 'geckodriver.exe' file is in the plugin folder
            - or Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def upload_media_instagram():
    """This module opens the file upload page on the Windows operating system,
    and asks the user to select the media they want to upload to their Instagram account.
    The selected media is then uploaded as a post on the Instagram account."""

    # Find some elements in web page and click on them
    try:
        # In this section, the received post will be uploaded to the Instagram account
        show_log(f"The app is uploading {path_file_complete} posts to your Instagram account, please wait")
        count_try = 0
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, new_post))).click()
        file_uploade = driver.find_element(by=By.CSS_SELECTOR, value=send_media)
        file_uploade.send_keys(path_file_complete)

        # The media upload page opens
        # The user must select the media to upload
        # An alarm sounds to alert the user
        # If the user selects their media, the application will start uploading
        # Otherwise, the application will wait for the user to select it
        while True:
            # If the user selected their media
            try:
                # Upload steps
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, _next))).click()    
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, _next))).click()
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, share))).click()
                
                # Waiting for the upload to complete on the Instagram page and display the post
                while True:
                    try:
                        # If the upload was successful
                            driver.find_element(by=By.XPATH, value=success_upload)
                            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, close_post))).click()
                            # Display log
                            show_log(f"Post '{path_file_complete}' was successfully uploaded to {_username}'s Instagram account.", status="success")
                            break
                    
                    # If not uploaded
                    except:
                        # Display log and try again
                        show_log(f"Post '{path_file_complete}' is uploading to {_username}'s Instagram account, please wait.")
                        time.sleep(10)
                        pass
                
                # If the upload process is complete
                break
            
            # Alert the user to select their media from the window that opens
            except:
                count_try += 1
                if count_try == 3:
                    show_log("""There was a problem uploading the file to your Instagram account, please check the following:
                        - Try again and make sure enter currect username and password
                        - Check your anti filter and internet
                        - Your Instagram account should not be restricted or reported
                        - Reinstall the Firefox file
                        - Setup another account in the config file and try again with another account
                        - Make sure the media folder and the files inside it are in the right place
                        - or Please report your error via email to the developer to resolve this issue:
                                Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

                    break

                time.sleep(20)
    
    # If an error occurs during the program
    except:
        # Display log
        show_log("""There was a problem uploading media to your Instagram account, please check the following:
            - Try again
            - Check your anti filter and internet
            - Your Instagram account should not be restricted or reported
            - Reinstall the Firefox file
            - Setup another account in the config file and try again with another account
            - or Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def start():
    """This module runs the program completely and is responsible for keeping the program active for automatic work."""
    
    try:
        clear_screen()
        # Display log
        show_log("The program is launching, please complete the configuration steps by answering the questions below." + "\n" * 5)
        # Run config function
        config()
        # Run login_to_instagram function
        login_to_instagram()

        # Search, find and upload new posts in Instagram account
        with client:
            # Activity automatically and permanently
            while True:
                # Search and find new posts in Telegram channel
                client.loop.run_until_complete(download_media_telegram())

                # If there was a new post
                if result:
                    upload_media_instagram()
                
                # If there was no new post
                else:
                    # Display log and try again after 1-minute
                    show_log("The program is at rest, after a minute the posts of the desired channel are checked again.")
                    time.sleep(60)
                    continue
    
     # If an error occurs during the program
    except:
        show_log("""There is a problem launching the app, please check the following:
            - Try again
            - Check the logs in the window that opens
            - Check your anti filter and internet
            - Make sure the files in the application folders are correct
            - or Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

if __name__ == "__main__":
    start()
