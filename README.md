Sometimes customer share "show tech", "show runn" or other files with some characters such as "<--- More --->" and other non printable characters.

You can use the attached script to clean those files, it will create a new file with same name and .clean suffix after removing the unwanted data.

Sample:

rajatsh$ python3 clean_files.py

Enter input file path: tech.log

Enter output file path (press Enter for default '<input>.clean'):

Cleaned file written to: tech.log.clean

 

 

 rajatsh$ ls -lh tech.log*

-rw-r--r--@ 1 rajatsh  staff   1.5M Nov 20 18:08 tech.log

-rw-r--r--  1 rajatsh  staff   1.4M Nov 20 18:08 tech.log.clean
