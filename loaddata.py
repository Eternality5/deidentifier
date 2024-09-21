import subprocess

# This is a simple script for quickly loading the survey questions into the database,
# it was written in python to limit the number of project dependencies.
command = 'python3 deidentifier/manage.py loaddata '
question_groups = ['question_group_1.json', 'question_group_2.json', 'question_group_3.json']
for question_group in question_groups:
    subprocess.Popen(command + question_group, shell=True)
