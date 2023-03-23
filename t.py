import os
#nothing for you bruh
# Set the expected GitHub repository link

EXPECTED_GITHUB_LINK = "https://github.com/TEAM-RXN/MR-XERX"

# Get the current working directory

cwd = os.getcwd()

# Check if the current working directory matches the expected GitHub repository link

if not cwd.startswith(EXPECTED_GITHUB_LINK):

    print("Error: The code is not running from the expected GitHub repository link.")

    exit()

else:

    print("Success: The code is running from the expected GitHub repository link.")

