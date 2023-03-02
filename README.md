# Directory Listing App
GUI that allows users to navigate through directories and view their contents in the sorted fashion

## Prerequisites
To have a functioning Directory Listing App, please have Python 3.6 or above installed on your operating system. No additional third-party libraries are required. The app supports execution on Windows, Linux, and Mac.
To run the app, double click the directory_listing.py file, or open the file using your IDE of choice and run from the therein. Changing the file name shouldn’t affect the app’s performance.

## Features
Initially, the app window will appear as shown below. It can be maximized by clicking the Maximize button or resized by dragging the sides to your liking.

The app automatically shows the absolute path of the directory in which it has been executed. This current working directory is always anchored in the bottom left.

Once inside the Search Box, type the required file/folder name and press Enter. The matching function is not case-sensitive. If the required file is not found, the app with prompt “no such file”. This prompt will disappear after 2 seconds.

If the double-clicked file is not a directory, the app with prompt “not a directory”, highlighting the row red. This prompt will disappear after 2 seconds.
 
To go back in the directory structure, double-click two dots.
