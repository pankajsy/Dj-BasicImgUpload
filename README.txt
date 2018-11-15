NYU APPLICATION SECURITY COURSE
LOCAL SERVER DOCUMENTATION

1. LAMP Stack:
Since the web app was developed using Ubuntu 14.04 and Django Python framework make sure LAMP Stack is setup on your local computer i.e Linux, MySQL, php, Apache are running properly.

2.Download the zipped project:
You can either download the attached project zip file or clone the project from the git repository

The web app is source controlled, so you can pull the code using the following link
https://pankajsy@bitbucket.org/pankajsy/appsecurity.git
Make a directory and change to that directory. This is where you will clone the repository
mkdir <folder_name>
Cd <folder_name>
Git clone the repository from Bitbucket
git clone "https link to appsecurity git repository"


All the Appsec files are downloaded in the desired folder. appsecurity in the following case on :

The folder appsecurity/ is where one will initiate git.

3. Setup the virtual environment
(It's a good practice to setup the virtual environment) It creates isolated Python environments where all the necessary packages required for the django project setup is required
The following document helps in setting up the virtual env.
http://docs.python-guide.org/en/latest/dev/virtualenvs/

It creates virtualenv folder at home location.Create a virtual environment named with our project(eg: appsecurity) inside virtualenv folder and switch to it as follows
source ~/virtualenv/(path to appsecurity env)/bin/activate
After you switch, the command line will manifest a line as follows:

Indication of (appsecurity) confirms you are in Appsecurity virtual environment.

NOTE: Always switch to virtual environment before executing any command in Appsecurity else it will error out as follows:


This is because all the required packages for Appsecurity reside in the virtual environment.

4. Creating App Security database

Django uses different types of databases for its projects like MySql, Sqlite3 etc.
I used MySql provided with an advantage of creating a private profile (Username, Password) and added security

For sqlite3:
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}



For MySql Setup
Given that you have setup the mysql server properly access mysql through shell using following command
mysql -u root -p
We do the following steps after logging as root as per following specifications:
User-Password is for demo purpose
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'dbname',
       'USER': 'user',
       'PASSWORD': 'password',
   }
}

a: Create user in MySql
https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql
 'USER': user,
 'PASSWORD': password,
b: Create db in MySql
https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial
 'NAME': dbname,
c: Grant all access to created user in Mysql

5. pip install -r requirements.txt from the repository
NOTE:  Make sure you are in the virtual env.

This command installs all the required packages in the switched virtual environment.
Make sure all the packages are installed properly.

Sometimes the command errors out with some packages. However it may still install rest of the packages properly. In that case just comment out the package causing error and run the command again.  The output must look like following, with (requirements already satisfed ...) prefix for every package.

 Install the package you commented out previously, using pip install <package name>


6. Then run migrations using the following commands
python manage.py makemigrations (if there are changes in models.py files)
Followed by python manage.py migrate


Migrations running without errors …

7. python manage.py runserver
python manage.py runsever 0.0.0.0:8000  (If you want to start the server to specific port)


If everything goes well and smooth you'll find that the local server has started up and pointing to your localhost address.





