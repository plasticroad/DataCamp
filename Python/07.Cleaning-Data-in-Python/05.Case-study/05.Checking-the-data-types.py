'''
Checking the data types

Now that your data is in the proper shape, you need to ensure that the columns are 
of the proper data type. That is, you need to ensure that country is of type object, 
year is of type int64, and life_expectancy is of type float64.

The tidy DataFrame has been pre-loaded as gapminder. Explore it in the 
IPython Shell using the .info() method. Notice that the column 'year' is of 
type object. This is incorrect, so you'll need to use the pd.to_numeric() function 
to convert it to a numeric data type.

NumPy and pandas have been pre-imported as np and pd.

INSTRUCTIONS
100 XP
Convert the year column of gapminder using pd.to_numeric().
Assert that the country column is of type np.object. This has been done for you.
Assert that the year column is of type np.int64.
Assert that the life_expectancy column is of type np.float64.
'''
