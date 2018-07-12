'''
Iterating and concatenating all matches

Now that you have a list of filenames to load, you can load all the files into a list
of DataFrames that can then be concatenated.

You'll start with an empty list called frames. Your job is to use a for loop to 
iterate through each of the filenames, read each filename into a DataFrame, and 
then append it to the frames list.

You can then concatenate this list of DataFrames using pd.concat(). Go for it!

INSTRUCTIONS
100 XP
Write a for loop to iterate though csv_files:
In each iteration of the loop, read csv into a DataFrame called df.
After creating df, append it to the list frames using the .append() method.
Concatenate frames into a single DataFrame called uber.
Hit 'Submit Answer' to see the head and shape of the concatenated DataFrame!
'''
