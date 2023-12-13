*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***

Crawl Acm
    Set Username  Esimerkki Käyttäjä
    Submit Credentials
    Click Link  Lisää linkki
    Set Link  https://dl.acm.org/doi/10.1145/2380552.2380613
    Submit Link
    Crawl Acm Should Succeed With Article  @article{luukkainen:2012,

*** Keywords ***

Set Link
    [Arguments]  ${link}
    Input Text  Linkki  ${link}

Submit Link
    Click Button  Lähetä

Crawl Acm Should Succeed With Article
    [Arguments]  ${acm-article}
    Article Page Should Be Open
    Page Should Contain  ${acm-article}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Submit Credentials
    Click Button  Kirjaudu sisään
