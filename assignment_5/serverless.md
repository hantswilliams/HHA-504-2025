<!-- Slide number: 1 -->
# Compute -
Serverless Approaches
Hants Williams, PhD, RN

<!-- Slide number: 2 -->
# Architectural Models (deploy)

<!-- Slide number: 3 -->
# Tenancy
Single Tenant versus Multi-tenant
Arch Patterns:

Single Tenet

Multi Tenet

App
App Env

App
Customer 1
Customer 2
Customer 3
Customer 1
Customer 1
Single Tenet

App Env
Single Tenet
Customer 2

App
App Env
Customer 1
Customer 3

<!-- Slide number: 4 -->
# Tenancy
Single Tenant versus Multi-tenant
What is best for healthcare?

![Image](Image.jpg)

<!-- Slide number: 5 -->
# Tenancy
Single Tenant versus Multi-tenant
Arch Patterns:

![Image](Image.jpg)

App
App Env

![Image](Image.jpg)

App
Customer 1
Customer 2
Customer 3
Customer 1
Customer 1

![Image](Image.jpg)

App Env

![Image](Image.jpg)

![Image](Image.jpg)
Customer 2

App
App Env

![Image](Image.jpg)
Customer 1
Customer 3

<!-- Slide number: 6 -->
Arch Patterns

Monolithic vs Cloud

![Image](Image.jpg)
Cloud native/micro vs EDS
https://www.ibm.com/think/topics/application-architecture-types

<!-- Slide number: 7 -->
Arch Patterns 3-tier SaaS:

![Image](Image.jpg)

<!-- Slide number: 8 -->

![Image](Image.jpg)
All clinical Functions

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
VMware VM A Contains Everything
Biggest advantage: Simple management

<!-- Slide number: 9 -->

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Image](Image.jpg)
Backend 1: Labs
Backend 6: Ride share services

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
AWS VM A
GCP VM F
GCP VM D

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
Backend 4: Careplans
Backend 2: Outpatient

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
AWS VM B
GCP VM C
Backend 5: Faxing

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
GCP VM E

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
Backend 3: Pt Education
Biggest advantage: No single point of complete failure

<!-- Slide number: 10 -->

![Image](Image.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)

![Google Shape;3796;p87](GoogleShape3796p87.jpg)
Biggest advantage: Simple management
Biggest advantage: No single point of complete failure

<!-- Slide number: 11 -->
# Uber: 2,000 + microservices
https://www.uber.com/blog/microservice-architecture/

![Screenshot 2023-03-21 at 7.13.53 AM.png](Screenshot20230321at71353AMpng.jpg)

![Screenshot 2023-03-21 at 7.14.09 AM.png](Screenshot20230321at71409AMpng.jpg)

<!-- Slide number: 12 -->
# Spotify: 800 + microservices
https://gotocon.com/dl/goto-berlin-2015/slides/KevinGoldsmith_MicroservicesSpotify.pdf

![Screenshot 2023-03-21 at 7.19.17 AM.png](Screenshot20230321at71917AMpng.jpg)

![Screenshot 2023-03-21 at 7.19.02 AM.png](Screenshot20230321at71902AMpng.jpg)
https://github.com/spotify/apollo

<!-- Slide number: 13 -->
# If you want to learn more…
https://engineering.cerner.com/

![Screenshot 2023-03-21 at 7.22.02 AM.png](Screenshot20230321at72202AMpng.jpg)

<!-- Slide number: 14 -->
# Event Driven / Serverless

<!-- Slide number: 15 -->
https://aws.amazon.com/serverless/videos/video-lambda-intro/

![Screen Shot 2022-03-01 at 11.53.26 AM.png](ScreenShot20220301at115326AMpng.jpg)
AWS Lambda lets you run code without provisioning or managing servers
(e.g., serverless)

<!-- Slide number: 16 -->
ServerLESS with client-server model
Serverless is a model in which application code is executed on-demand in response to triggers that application developers configure ahead of time.
Biggest advantage: COST
Website returns and displays something from function

![Google Shape;4132;p92](GoogleShape4132p92.jpg)

![Google Shape;2779;p70](GoogleShape2779p70.jpg)

![Google Shape;194;p23](GoogleShape194p23.jpg)

![pasted-movie.png](pastedmoviepng.jpg)
Sheets updates a row

Function
You
Database updates a database field

![pasted-movie.png](pastedmoviepng.jpg)

Function is only used when there is a request, vs a VM that may always be on

<!-- Slide number: 17 -->

![pasted-movie.png](pastedmoviepng.jpg)
(BINDING)
(PYTHON)
(TRIGGER)

<!-- Slide number: 18 -->
(TRIGGER)
(FUNCTION)
(BINDING)

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 19 -->
# Serverless Functions versus VMs
Serverless Funcs: no access OS

Serverless Funcs: only provide code (python, JS, go, etc..) that you want to run

Serverless Funcs: on-demand
VMs: access to OS

VMs: need to maintain OS

VMs: always on

<!-- Slide number: 20 -->
# Examples of when we might use them…
1. Processing Patient Data in Real-Time
Input (Trigger): New patient data upload (e.g., wearable device data) to cloud storage.

Output (Binding): Store processed data in a healthcare system’s database or trigger alerts for anomalies.

Example: A Fitbit uploads heart rate data, and the cloud function processes it and stores the results in a patient monitoring database.

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 21 -->
# Examples of when we might use them…
2. Appointment Reminder Notifications

![pasted-movie.png](pastedmoviepng.jpg)
Input (Trigger): Cron job (scheduled trigger) that runs daily to check for upcoming appointments.

Output (Binding): Send SMS, email, or push notification reminders to patients.

Example: A daily serverless function checks for appointments in the next 24 hours and sends a reminder via Twilio SMS or email.

<!-- Slide number: 22 -->
# Examples of when we might use them…
3. Patient Surveys and Feedback Collection

![pasted-movie.png](pastedmoviepng.jpg)
Input (Trigger): Completion of medical appointment or procedure.

Output (Binding): Send feedback survey and store responses in the survey system.

Example: After a patient's surgery, a function triggers an email survey and records the response in a feedback database.

<!-- Slide number: 23 -->

![pasted-movie.png](pastedmoviepng.jpg)

<!-- Slide number: 24 -->
Function costs:

![Screenshot 2024-09-30 at 12.52.22 PM.png](Screenshot20240930at125222PMpng.jpg)

<!-- Slide number: 25 -->
Function memory:

![Screenshot 2024-09-30 at 12.51.09 PM.png](Screenshot20240930at125109PMpng.jpg)

<!-- Slide number: 26 -->
Function runtimes:

![Screenshot 2024-09-30 at 12.51.50 PM.png](Screenshot20240930at125150PMpng.jpg)

<!-- Slide number: 27 -->
Function request time:

![Screenshot 2024-09-30 at 12.50.36 PM.png](Screenshot20240930at125036PMpng.jpg)

<!-- Slide number: 28 -->
# Cron Jobs
Packages: airflow, crontab

![pasted-movie.png](pastedmoviepng.jpg)
Cron Jobs
- Simple: CronTab
- Complex: Airflow / Dags

<!-- Slide number: 29 -->
# Why ?
You want have a task - you don’t want to have to re-launch, or re-do it on a day to day basis

Best thing to do is AUTOMATE

Help run robs periodically without any human intervention, at a set time (automation)

<!-- Slide number: 30 -->
# Examples
You want to re-run script that pulls data from a database, and using pandas / re-format it for reporting purposes every morning at 8:00am

You want to re-run script X that creates a new csv/xls weekly user stats (logins, logouts, etc…) for security purposes every Friday afternoon at 4:45pm EST

<!-- Slide number: 31 -->
# Cron expression
It helps you to specify/define at what time and intervals you want to run the job.

The syntax has 6–7 fields in it:-

![Image](Image.jpg)

<!-- Slide number: 32 -->
Special Characters used in the expression:-

	* (any) ::: Job executes at every time unit.
	- (range) ::: Range of the time unit.
	, (values) ::: Multiple value of time unit.
	/ (increments) ::: Specify incremental values of the time unit.
	? (“no specific value”) ::: Useful when you need to specify something in one of the two fields in which the character is allowed, but not the other. For example, if I want my trigger to fire on a particular day of the month (say, the 10th), but don’t care what day of the week that happens to be, I would put “10” in the day-of-month field, and “?” in the day-of-week field.
	# (occurrence) ::: It is used to specify the “N-th” occurrence of a weekday of the month, for example, “3rd Friday of the month” can be indicated as “6#3“
	L (last) — it has different meanings when used in various fields. For example, if it’s applied in the <day-of-month> field, then it means last day of the month, i.e. “31st for January” and so on as per the calendar month. In the <day-of-week>, it specifies the “last day of a week” like “6L“, which denotes the “last Friday”.

<!-- Slide number: 33 -->
# Helper
https://crontab.guru/

![Screen Shot 2022-09-28 at 5.14.11 PM.png](ScreenShot20220928at51411PMpng.jpg)

![Screen Shot 2022-09-28 at 5.13.42 PM.png](ScreenShot20220928at51342PMpng.jpg)

<!-- Slide number: 34 -->
# Initial setup
Ubuntu / Linux
1. Should already be installed by default; can confirm by running ‘crontab -h’

2. Make sure have the simplest text editor selected by default; can run ‘select-editor’ in the terminal and select ‘nano’ - if no nano, can first install using ‘sudo apt-get install nano’

<!-- Slide number: 35 -->
# Important commands
Crontab
Look at existing jobs: crontab -e

Stop/comment out jobs: place a # in front of a line

Restart the service: sudo service cron reload

Status check: systemctl status cron

<!-- Slide number: 36 -->
# Running directly via python file
1.0 get the location of where python3 is installed: (should give output of /usr/bin/python3 )

which python3

1.1. open crontab file, you need to fire this command:

crontab -e

1.2 Each line in crontab is an entry with an expression and a command to run:

* * * * * /usr/bin/python3 /ubuntu/users/documents/pythonfile.py
* * * * * python3 /location/to/python/file/pythonfile.py

<!-- Slide number: 37 -->
# Creating a bash file to run
A Bash script is a plain text file which contains a series of commands.

These commands are a mixture of commands we would normally type ouselves on the command line (such as ls or cp for example) and commands we could type on the command line
nano myscript.sh

![Screen Shot 2022-09-28 at 5.29.06 PM.png](ScreenShot20220928at52906PMpng.jpg)
chmod +x myscript.sh
./myscript.sh

<!-- Slide number: 38 -->
# Creating a bash file to run
.sh file   [script file]
#!/bin/sh
python3 /location/to/python/file/pythonfile.py
python app.py

<!-- Slide number: 39 -->
# Creating a bash file to run
.sh file
1.1. open crontab file, you need to fire this command:

crontab -e

1.2 Each line in crontab is an entry with an expression and a command to run:

* * * * * /location/to/sh/file/server.sh

NOTE:
- you may need to make you .sh file runnable by first performing chmod -x server.sh

<!-- Slide number: 40 -->
# Import notes from class…
Output errors
- If you are doing any print, console statements in your file that you are automating, you must have another file (aka log file) that will capture and store that information

- To begin with only python, we will use the same approach for when we were launching a flask app and running it in the background

- At the end of the crontab expression, you can add this:
      * * * * * /usr/bin/python3 /ubuntu/users/documents/pythonfile.py > log.txt 2>&1 &