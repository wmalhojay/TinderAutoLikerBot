***********************************************
*                                             *
*             Tinder Auto Liker               *
*                                             *
***********************************************

# Tinder Automation with Selenium

This Python script automates the process of logging into Tinder using Facebook credentials and automatically liking profiles. It utilizes Selenium WebDriver to interact with the Tinder web interface.

## Prerequisites

- Python 3.x
- Selenium WebDriver for Python (`pip install selenium`)

## Usage

1. Replace `EmailCredential` and `PassWordCredential` with your Facebook login credentials.
2. Make sure you have the latest version of Chrome WebDriver installed and in your system's PATH.
3. Run the script. It will:
   - Open Chrome and navigate to Tinder.
   - Click through initial dialogs (e.g., consent and login).
   - Log in via Facebook.
   - Automatically like profiles for approximately 99 iterations.
   - Handle location and notification dialogs.

## Notes

- Adjust the waiting times (`time.sleep()`) as necessary for your network and system speed.
- Ensure your Facebook account is verified and allowed to log in through this script.



