*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page And Sign In

*** Test Cases ***

Search With Correct Cite
    Set Search Cite  esimerkkikirjoittaja:2023
    Submit Search Cite
    Cite Search Should Succeed With Article  @article{esimerkkikirjoittaja:2023,

Search Book With Correct Cite
    Set Search Cite  esimerkkikirjailija:2023
    Submit Search Cite
    Cite Search Should Succeed With Book  @book{esimerkkikirjailija:2023,

Search Mastersthesis With Correct Cite
    Set Search Cite  esimerkkigraduilija:2023
    Submit Search Cite
    Cite Search Should Succeed With Mastersthesis  @mastersthesis{esimerkkigraduilija:2023,

Search With Correct Tag
    Set Search Tag  tagi
    Submit Search Tag
    Tag Search Should Succeed With Article  @article{luukkainen:2012,

Delete Acm Crawl
    Click Link  Muokkaa tai poista viitteitä
    Click Link  Poista
    Set Delete  Poista
    Delete Should Succeed With Message  Viite on poistettu.

Delete Article
    Click Link  Muokkaa tai poista viitteitä
    Click Link  Poista
    Set Delete  Poista
    Delete Should Succeed With Message  Viite on poistettu.

Delete Book
    Click Link  Muokkaa tai poista viitteitä
    Click Link  Poista
    Set Delete  Poista
    Delete Should Succeed With Message  Viite on poistettu.

Delete Mastersthesis
    Click Link  Muokkaa tai poista viitteitä
    Click Link  Poista
    Set Delete  Poista
    Delete Should Succeed With Message  Viite on poistettu.



*** Keywords ***

Go To Starting Page And Sign In
    Go To Starting Page
    Set Username  Esimerkki Käyttäjä
    Submit Credentials

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

Cite Search Should Succeed With Mastersthesis
    [Arguments]  ${mastersthesis}
    Result Page Should Be Open
    Page Should Contain  ${mastersthesis}

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
