# STEPS TO MAKE OUR OWN VIRTUAL ENVIRONMENT

# Command to make virtual environment ---> python -m venv myenv (myenv cab be any name (kuchbhi))

# THIS ENVIRONMENT ALSO CONTAINS PYTHON FOR US , IT HAS TO BE ACTIVATED---- 

# activation of virtual environment           .\myenv\Scripts\activate

"""

whenever you need to open project on someone's else pc
1. Create your own virtual Environment
2. Run the command 
         pip install -r requirements.txt  (this downloads all the libraries we used for our project ---)


"""
"""

To make our requirements file :
    pip freeze > requirements.txt

After Activation : 

    install required libraries using pip install
    
    1. Install mysql connector for python

            pip install mysql-connector-python 

    2. pip list 

            shows the list of installed libraries with their versions                 
       
"""

import mysql.connector as db
print('Sucess !!!!')

