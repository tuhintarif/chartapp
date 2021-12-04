## 1. Setup environment

Can use either pipenv or pip.

### pipenv

Note: Prerequisites: Must have pipenv installed. first. Command to install:

> *pip install pipenv* or *brew install pipenv*

After installation is finished, run below command to create virtual environment.

> *pipenv shell* 

### pip

> *pip install virtualenv*

After installation is complete, go to the path you want to install in your system and run below:

> *virtualenv [name_of_your_folder]*

Then, cd to Scripts folder and run below:

> *activate.bat*

Your virtual environment should be activated. You can now safely return to your folder and execute the next step.


## 2. Install all require packages using pipenv or pip
> *pipenv install -r requirements.txt*

### OR

> *pip install -r requirements.txt* <br />
> *pip3 install -r requirements.txt*


## 3. Database migration and seeding

Prerequisites: Step 1 and 2 must be initiated before proceeding Step 3. 

Once all packages have been installed, run below command to proceed with database migration process:

> *python manage.py makemigrations*

then, run

> *python manage.py migrate*

## 4. Run server

> *python manage.py runserver*

# Congratulations! You made it!


# Home page will be displayed without data

![Optional Text](../main/images/homepage_without_data.png)


# Home page will be displayed with data

![Optional Text](../main/images/homepage_with_data.png)


