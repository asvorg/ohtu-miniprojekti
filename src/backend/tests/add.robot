*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***

Add Article
    Set Username  Esimerkki Käyttäjä
    Submit Credentials
    Click Link  Lisää artikkeli
    Set Author  Esimerkkikirjoittaja
    Set Title  Esimerkki
    Set Year  2023
    Set Article  Esimerkkiartikkeli
    Submit Article
    Adding Article Should Succeed With Article  @article{esimerkkikirjoittaja:2023,

Add Book
    Set Username  Esimerkki Käyttäjä
    Submit Credentials
    Click Link  Lisää kirja
    Set Author  Esimerkkikirjailija
    Set Editor  Esimerkki editori
    Set Title  Esimerkki otsikko
    Set Publisher  Esimerkki julkaisija
    Set Year  2023
    Submit Article
    Adding Book Should Succeed With Book  @book{esimerkkikirjailija:2023,

Add Tag
    Set Username  Esimerkki Käyttäjä
    Submit Credentials
    Click Link  Muokkaa tai poista viitteitä
    CLick Link  Muokkaa
    Set Tag  tagi
    Submit Tag
    Adding Tag Should Succeed


*** Keywords ***

Set Author
    [Arguments]  ${author}
    Input Text  Kirjoittaja  ${author}

Set Editor
    [Arguments]  ${editor}
    Input Text  Editori  ${editor}

Set Title
    [Arguments]  ${title}
    Input Text  Otsikko  ${title}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  Julkaisija  ${publisher}


Set Year
    [Arguments]  ${year}
    Input Text  Julkaisuvuosi  ${year}

Set Article
    [Arguments]  ${article}
    Input Text  Artikkeli  ${article}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Submit Credentials
    Click Button  Kirjaudu sisään

Set Search Cite
    [Arguments]  ${cite}
    Input Text  citeKey  ${cite}

Set Tag
    [Arguments]  ${tag}
    Input Text  Tagit  ${tag}

Set Search Tag
    [Arguments]  ${tag}
    Input Text  tag  ${tag}

Set Delete  
    [Arguments]  ${poista}
    SeleniumLibrary.Submit Form

Submit Search Cite
    Click Button  Etsi

Submit Article
    Click Button  Lähetä

Submit Tag
    Click Button  Tallenna

Submit Search Tag
    Click Button  id=2

Cite Search Should Succeed With Article
    [Arguments]  ${article}
    Result Page Should Be Open
    Page Should Contain  ${article}

Cite Search Should Succeed With Book
    [Arguments]  ${book}
    Result Page Should Be Open
    Page Should Contain  ${book}

Tag Search Should Succeed With Article
    [Arguments]  ${article}
    Result Page Should Be Open
    Page Should Contain  ${article}

Delete Should Succeed With Message
    [Arguments]  ${message}
    Confirm Page Should Be Open
    Page Should Contain  ${message}

Adding Article Should Succeed With Article
    [Arguments]  ${article}
    Article Page Should Be Open
    Page Should Contain  ${article}

Adding Book Should Succeed With Book
    [Arguments]  ${book}
    Article Page Should Be Open
    Page Should Contain  ${book}

Adding Tag Should Succeed
    List Page Should Be Open
