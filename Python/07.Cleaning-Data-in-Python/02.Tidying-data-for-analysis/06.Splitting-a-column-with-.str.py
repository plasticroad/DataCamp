'''
Splitting a column with .str

The dataset you saw in the video, consisting of case counts of tuberculosis by 
country, year, gender, and age group, has been pre-loaded into a DataFrame as tb.

In this exercise, you're going to tidy the 'm014' column, which represents males 
aged 0-14 years of age. In order to parse this value, you need to extract the first 
letter into a new column for gender, and the rest into a column for age_group. 
Here, since you can parse values by position, you can take advantage of pandas' 
vectorized string slicing by using the str attribute of columns of type object.

Begin by printing the columns of tb in the IPython Shell using its .columns 
attribute, and take note of the problematic column.

INSTRUCTIONS
100 XP
Melt tb keeping 'country' and 'year' fixed.
Create a 'gender' column by slicing the first letter of the variable column of 
tb_melt.
Create an 'age_group' column by slicing the rest of the variable column of tb_melt.
Print the head of tb_melt. This has been done for you, so hit 'Submit Answer' to 
see the results!
'''
