# Basically,
The program uses Selenium Webdriver to go on SpeedTest and run a test. If the desired internet speed (defined by a constant) is not reached, it uses selenium once again to log into twitter and post a complaint. Originally posting under @AdemSikayet. For security, this repo can't directly post under that same account, but you can change the .env file for any twitter account you want.

# Selenium is not a built-in library in Python
If you're getting errors, make sure you have Selenium Webdriver downloaded.
