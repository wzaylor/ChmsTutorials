clear; clc;

rng(1234); % Make it so the same random numbers are generated every time.
data = rand(12,6)*20.; % Generate the data that will go into the table

[numRows, numCols] = size(data); % The number of rows and columns in 'data'
decimalPlaces = 2; % Specify the number of decimal places to use for rounding the data in the table.

txt = ""; % Initialize the string that will contain the formatted data

for i = 1:numRows
    for j = 1:numCols
        value = round(data(i,j), decimalPlaces); % Round the value in 'data[i,j]' to the specified number of decimal places
        txt = txt + string(value); % Append this string to the 'txt' variable
        
        if j < numCols % If we are not on the last column
            txt = txt + ' & '; % Append the Latex formatting for a new column
        else % If we are on the last column.
            txt = txt + ' \\\\'; % Append the Latex formatting for a new line.
            txt = txt + '\n'; %This is not Latex formatting. This makes a new line when we print the 'txt' variable
        end
    end
end

txt = compose(txt); % Enforce the '\n', and other characters in 'txt'
disp(txt) % Print the text that will be copy-and-pasted into the .tex file.