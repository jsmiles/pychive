# pychive
A python tool to archive portions of database tables. 

# Main Code
If you just want to get going then checkout `pychive.py`. Following these steps:
* Generate an input file. The program expects a file called `archiveList.txt` in the same directory as `pychive.py`. 
* The input file should contain two things a table name and date of archive in this shape 'tableName,Date'
* Run `pychive.py`
* Thats it, the tables you have input have been archived to new tables following this pattern: __testTable__ becomes __testTable_Archive_TodaysDate__

# Example
Aside from the main program I have included in this repo sufficient files to help you run a test example.
* `testgen.py` will generate an `example.db` and insert some test data into three tables
* `archiveList.txt` is an example input list, detailing two tables and a date for each. This can be run as is and will archive half of two tables data. Or you can just copy the format for your own project. 
* `validation.py` can be run after you run the `pychive.py` or even before. It will output a table list twice and in between the data in each table. This is very helpful when debugging your own project. However, it also serves the purpose of illustrating that __pychive__ works if you follow along with the example. 

# Health Warnings
In short there are many limitations to __pychive__, a few of them are listed below:
* Not public facing, this approach if used in a web form would leave you open to sql injection attacks etc.
* This code comes with no warranty and you use it entirely at your own risk. I accept no responsibility.
* It is setup to work with SQLite. The approach should work with other databases but I have not had time to develop this functionality. 
* This relies on f strings so only python version 3.6 and above will work.

