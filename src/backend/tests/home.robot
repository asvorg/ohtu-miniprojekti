*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Go To Starting Page
    Starting Page Should Be Open

Login With Correct Credentials
    Set Username  kalle
    Submit Credentials
    Login Should Succeed



*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Submit Credentials
    Click Button  Kirjaudu sisään

Login Should Succeed
    Article Page Should Be Open