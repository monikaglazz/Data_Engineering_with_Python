# 1

# in one step, create a new file and pass the print function into the file
echo "print('This is my first Python script')" > my_first_python_script.py

# check file location 
ls

# check file content 
cat my_first_python_script.py

# execute Python script file directly from command line  
python my_first_python_script.py

# 2

# Add scikit-learn to the requirements.txt file
echo "scikit-learn" > requirements.txt

# Preview file content
cat requirements.txt

# Install the required dependencies
pip install -r requirements.txt

# Verify that Scikit-Learn is now installed
pip list


# 3
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed ...
# |  |  |  |  |
# *  *  *  *  * command-to-be-executed

# Verify that there are no CRON jobs currently scheduled
crontab -l 

# Create Python file hello_world.py
echo "print('hello world')" > hello_world.py

# Preview Python file 
cat hello_world.py

# Add as job that runs every minute on the minute to crontab
echo "* * * * * python hello_world.py" | crontab

# Verify that the CRON job has been added
crontab -l

# 4

# Preview both Python script and requirements text file
cat create_model.py
cat requirements.txt

# Pip install Python dependencies in requirements file
pip install -r requirements.txt

# Run Python script on command line
python create_model.py

# Add CRON job that runs create_model.py every minute
echo "* * * * * python create_model.py" | crontab

# Verify that the CRON job has been scheduled via CRONTAB
crontab -l
