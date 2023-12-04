*** Settings ***
Library  SeleniumLibrary
# Library  .../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0
${HOME_URL}  http://${SERVER}
# ${article_URL}  http://${SERVER}/login
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

Result Page Should Be Open
    Title Should Be  Lähdeviitteiden tallennussovellus

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Login Should Succeed
    Article Page Should Be Open

Login With Correct Credentials
    Set Username  Roope
    Submit Credentials
    Login Should Succeed

List Page Should Be Open
    Title Should Be  Viitelista

Confirm Page Should Be Open
    Title Should Be  Viite poistettu