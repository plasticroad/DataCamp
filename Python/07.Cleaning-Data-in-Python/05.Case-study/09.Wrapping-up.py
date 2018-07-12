'''
Wrapping up

Now that you have a clean and tidy dataset, you can do a bit of visualization and 
aggregation. In this exercise, you'll begin by creating a histogram of the 
life_expectancy column. You should not get any values under 0 and you should see 
something reasonable on the higher end of the life_expectancy age range.

Your next task is to investigate how average life expectancy changed over the years.
To do this, you need to subset the data by each year, get the 
life_expectancy column from each subset, and take an average of the values. 
You can achieve this using the .groupby() method. This .groupby() method is 
covered in greater depth in Manipulating DataFrames with pandas.

Finally, you can save your tidy and summarized DataFrame to a file using
the .to_csv() method.

Matplotlib and pandas have been pre-imported as plt and pd. Go for it!

INSTRUCTIONS
100 XP
Create a histogram of the life_expectancy column using the .plot() method of 
gapminder. Specify kind='hist'.
Group gapminder by 'year' and aggregate 'life_expectancy' by the mean. 
To do this:
Use the .groupby() method on gapminder with 'year' as the argument. Then 
select 'life_expectancy' and chain the .mean() method to it.
Print the head and tail of gapminder_agg. This has been done for you.
Create a line plot of average life expectancy per year by using the .plot() method 
(without any arguments) on gapminder_agg.
Save gapminder and gapminder_agg to csv files called 'gapminder.csv' and 
'gapminder_agg.csv', respectively, using the .to_csv() method.
'''
