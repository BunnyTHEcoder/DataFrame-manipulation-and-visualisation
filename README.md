# DataFrame-manipulation-and-visualisation
Design and implement a data analysis program in Python using pandas as detailed in the instructions below. 
Menu option 1 - load data from a file
Menu option 2 - View data
Menu option 3 - Clean data
Cleaning option 1 - Drop rows with missing values
Cleaning option 2 - Fill missing values
Cleaning option 3 - Drop duplicate rows
Cleaning option 4 - Drop column
Cleaning option 5 - Rename column
Cleaning option 6 - Finish cleaning
Menu option 4 - Analyse data
Menu option 5 - Visualise data
Menu option 6 - Save data to a file
Sample Output
It should be clear which parts below are user input (not printed, but entered by the user).
The output below is not intended to be exhaustive/complete, but you can discern how the
program should run fairly clearly from what is demonstrated here. E.g., you can see that all
invalid inputs are handled and that unless blank entries are meaningful (e.g., quitting the menu
option or skipping an entry), invalid inputs lead to a repeat of the input.
Welcome to the DataFrame Statistician!
Programmed by Ada Lovelace
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> Python is fun
Invalid selection!
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 2
No data to display.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 5
No data loaded.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 3
No data loaded.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 1
Enter the filename: no such file
File not found.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 1
Enter the filename: nothinginit.txt
Unable to load data.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 1
Enter the filename: sampledata.csv
Data has been loaded successfully.
Which column do you want to set as index? (leave blank for none)
day
min_temp
max_temp
rainfall
humidity
>>> non-existent-name
Invalid selection!
>>> day
day set as index.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 2
 min_temp max_temp rainfall humidity
day
1 11.0 23.0 3.0 55
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
5 NaN NaN NaN 50
6 12.0 22.0 NaN 60
7 13.0 23.0 0.0 65
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 4
min_temp
--------
number of values (n): 8
 minimum: 9.00
 maximum: 13.00
 mean: 10.88
 median: 11.00
 standard deviation: 1.73
 std. err. of mean: 0.61
max_temp
--------
number of values (n): 8
 minimum: 18.00
 maximum: 25.00
 mean: 21.50
 median: 22.50
 standard deviation: 2.51
 std. err. of mean: 0.89
rainfall
--------
number of values (n): 7
 minimum: 0.00
 maximum: 36.00
 mean: 10.86
 median: 3.00
 standard deviation: 13.33
 std. err. of mean: 5.04
humidity
--------
number of values (n): 9
 minimum: 50.00
 maximum: 85.00
 mean: 65.56
 median: 60.00
 standard deviation: 12.86
 std. err. of mean: 4.29
 min_temp max_temp rainfall humidity
min_temp 1.000000 0.907388 -0.821597 -0.759879
max_temp 0.907388 1.000000 -0.910239 -0.907222
rainfall -0.821597 -0.910239 1.000000 0.876242
humidity -0.759879 -0.907222 0.876242 1.000000
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 3
Cleaning...
 min_temp max_temp rainfall humidity
day
1 11.0 23.0 3.0 55
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
5 NaN NaN NaN 50
6 12.0 22.0 NaN 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 0
Invalid selection!
 min_temp max_temp rainfall humidity
day
1 11.0 23.0 3.0 55
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
5 NaN NaN NaN 50
6 12.0 22.0 NaN 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 1
Enter the threshold for dropping rows: 2
 min_temp max_temp rainfall humidity
day
1 11.0 23.0 3.0 55
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
6 12.0 22.0 NaN 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 2
Enter the replacement value: zero
Please enter a valid number.
Enter the replacement value: 0
 min_temp max_temp rainfall humidity
day
1 11.0 23.0 3.0 55
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
6 12.0 22.0 0.0 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 3
2 rows dropped.
 min_temp max_temp rainfall humidity
day
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
6 12.0 22.0 0.0 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 5
Which column do you want to rename?
min_temp
max_temp
rainfall
humidity
>>> something else
Invalid selection!
>>> rainfall
Enter the new name: min_temp
Column name must be unique and non-blank.
Enter the new name: rain
rainfall renamed to rain.
 min_temp max_temp rain humidity
day
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
6 12.0 22.0 0.0 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 4
Which column do you want to drop? (leave blank for none)
min_temp
max_temp
rain
humidity
>>>
No column dropped.
 min_temp max_temp rain humidity
day
1 11.0 23.0 3.0 55
2 13.0 25.0 0.0 60
3 9.0 19.0 17.0 80
4 9.0 18.0 36.0 85
6 12.0 22.0 0.0 60
7 13.0 23.0 0.0 65
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 4
Which column do you want to drop? (leave blank for none)
min_temp
max_temp
rain
humidity
>>> humidity
humidity dropped.
 min_temp max_temp rain
day
1 11.0 23.0 3.0
2 13.0 25.0 0.0
3 9.0 19.0 17.0
4 9.0 18.0 36.0
6 12.0 22.0 0.0
7 13.0 23.0 0.0
Cleaning data:
 1 - Drop rows with missing values
 2 - Fill missing values
 3 - Drop duplicate rows
 4 - Drop column
 5 - Rename column
 6 - Finish cleaning
>>> 6
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 5
Please choose from the following kinds: line, bar, box
>>> pie
Invalid selection!
>>> line
Do you want to use subplots? (y/n)
>>> n
Please enter the title for the plot (leave blank for no title).
>>> First
Please enter the x-axis label (leave blank for no label).
>>> Day
Please enter the y-axis label (leave blank for no label).
>>>
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 5
Please choose from the following kinds: line, bar, box
>>> bar
Do you want to use subplots? (y/n)
>>> y
Please enter the title for the plot (leave blank for no title).
>>> Second
Please enter the x-axis label (leave blank for no label).
>>> This is the day
Please enter the y-axis label (leave blank for no label).
>>> Value
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 5
Please choose from the following kinds: line, bar, box
>>> box
Do you want to use subplots? (y/n)
>>> why
Invalid selection!
>>> n
Please enter the title for the plot (leave blank for no title).
>>> Third
Please enter the x-axis label (leave blank for no label).
>>>
Please enter the y-axis label (leave blank for no label).
>>>
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 6
Enter the filename, including extension:
Cancelling save operation.
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 6
Enter the filename, including extension: newthing.txt
Data saved to newthing.txt
Please choose from the following options:
 1 – Load data from a file
 2 – View data
 3 – Clean data
 4 – Analyse data
 5 – Visualise data
 6 - Save data to a file
 7 - Quit
>>> 7
Goodbye
