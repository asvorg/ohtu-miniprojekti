*** Settings ***
Library  SeleniumLibrary
# Library  .../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0
${HOME_URL}  http://${SERVER}
# ${LOGIN_URL}  http://${SERVER}/login
# ${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    # jos käytät Firefoxia ja Geckodriveriä käytä seuraavaa riviä sitä alemman sijaan
    # ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Starting Page Should Be Open
    Title Should Be  Kirjautuminen

Login Page Should Be Open
    Title Should Be  Login

Article Page Should Be Open
    Title Should Be  Artikkelit

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Starting Page
    Go To  ${HOME_URL}
