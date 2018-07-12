*** Settings ***
Library                AppiumLibrary
Test Teardown          Close Application

*** Variable ***
${REMOTE_URL}          http://localhost:4723/wd/hub
${APP_PACKAGE}         livio.pack.lang.en_US
${APP_ACTIVITY}        livio.pack.lang.en_US.DictionaryView
${PLATFORM_NAME}       Android
${PLATFORM_VERSION}    5.1
${DEVICE_NAME}         Pixel API 22
${NO_RESET}            True
${el1}                 accessibility_id=Search
${el2}                 id=livio.pack.lang.en_US:id/search_src_text

*** Test Case ***
First Test
    Set Up And Open Application
    Action 1
    Action 2

*** Keywords ***
Set Up And Open Application
    Open Application               ${REMOTE_URL}                          platformName=${PLATFORM_NAME}
    ...                            platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}
    ...                            appPackage=${APP_PACKAGE}              appActivity=${APP_ACTIVITY}
    ...                            noReset=${NO_RESET}

Action 1
    Click Element                  ${el1}

Action 2
    Input Text                     ${el2}                                 doctor
    Press Keycode                  66