'''
Finding files that match a pattern

You're now going to practice using the glob module to find all csv files in the 
workspace. In the next exercise, you'll programmatically load them into DataFrames.

As Dan showed you in the video, the glob module has a function called glob that 
takes a pattern and returns a list of the files in the working directory that match 
that pattern.

For example, if you know the pattern is part_ single digit number .csv, you can 
write the pattern as 'part_?.csv' 
(which would match part_1.csv, part_2.csv, part_3.csv, etc.)

Similarly, you can find all .csv files with '*.csv', or all parts with 'part_*'. 
The ? wildcard represents any 1 character, and the * wildcard represents any number 
of characters.

INSTRUCTIONS
100 XP
Import the glob module along with pandas (as its usual alias pd).
Write a pattern to match all .csv files.
Save all files that match the pattern using the glob() function within the glob 
module. That is, by using glob.glob().
Print the list of file names. This has been done for you.
Read the second file in csv_files (i.e., index 1) into a DataFrame called csv2.
Hit 'Submit Answer' to print the head of csv2. Does it look familiar?
'''
