import numpy as np

np.random.seed(1234) # Make it so the same random numbers are generated every time.
data = np.random.rand(12,6)*20 # Generate the data that will go into the table

numRows = len(data) # The number of rows in 'data'
numCols = len(data[0]) # The number of columns in 'data'
decimalPlaces = 2 # Specify the number of decimal places to use for rounding the data in the table.

txt = "" # Initialize the string that will contain the formatted data

for i in range(numRows): # Iterate over every row in the data
    for j in range(numCols): # Iterate over every row in the data
        value = np.round(data[i,j], decimalPlaces) # Round the value in 'data[i,j]' to the specified number of decimal places
        txt += '{}'.format(value) # Append this string to the 'txt' variable

        if j < (numCols - 1): # If we are not on the last column
            txt += ' & ' # Append the Latex formatting for a new column
        else: # If we are on the last column.
            txt += r' \\' # Append the Latex formatting for a new line.
            txt += '\n' # This is not Latex formatting. This makes a new line when we print the 'txt' variable

print(txt) # Print the text that will be copy-and-pasted into the .tex file.