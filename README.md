# <b>Program flow: Version 2</b>

## <b>Program</b>
 * (NEW BRANCH FOR THIS) web scrape to populate a real time showing of available surveys
 * Store a list of available surveys the Census Bureau has
 * Print the list available surveys the Census Bureau has
 * Ask the user for input, typing the name of the survey they want to use

## <b>User:</b>
 * inputs the name of the survey they would like to use

## <b>Program</b>
 * Prints back the name of the survey they would like to use

# <b>Program flow: Version 1</b>

## <b>User:</b>
 * inputs 'yes' or 'no'

## <b>Program:</b>
 * If 'yes': navigate to webpage
 * If 'no': exit program
 * If other: instruct user to input 'yes' or 'no'

# <b>Program flow: Eventual Final Product</b>

## <b>Program:</b>
  * Introduction statement
  
## <b>User:</b>
  * selects data they want to download from the Census
    ***Could use selenium, webbrowser, or requests modules***
    
## <b>Program:</b>
  * Navigates to webpage
  * Downloads file
  * Transfers downloaded file to working folder
  * Reads all headers in CSV or Excel file
  * Prints all variable names from headers in nice way for user to see
  
## <b>User:</b>
  * Selects what data they want to keep from the list
  
## <b>Program:</b>
  * Outputs redacted Excel file to a directory that makes sense
  * Prints directory to user where new Excel file is located
  * Name the variables you are concerned with
