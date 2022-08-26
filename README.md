# wallstreetbets-data-collection
Aggregates r/wallstreetbets and stock market information for data analysis.

# About
Hello! This program is for analysing the discussion activities in the WallStreetBets Reddit.

Before running the program, the following external libraries are needed:\
-praw\
-dotenv\
-requests\
-pandas\
-seaborn\
-matplotlib

No dataset downloads are necessary.

All the necessary data analysis tools are set up in main.py.

Before running the program:\
1.) Update CURRENT_MONTH to the current month\
2.) Uncomment or comment the lines of codes at the end of the main function, if desired.
The first set of code is for getting the price history on a given stock. The second set
of code is for knowing what the most commonly used words are in WallStreetBets. It is
purely for entertainment purposes, and will take an extremely long time to run.\
3.) test.py is a remnant of our testing, you do not need to be concerned with that file.

That is all, You can now run main.py to begin an analysis on WallStreetBets!

