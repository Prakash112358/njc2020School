

#Task 1.3 & 1.4 NJC Exercise:

#Steps for both tasks inclusive: [6 marks]

#1) Open up a python file called "main.py" add in flask framework DONE
#2) Load the homepage ("/" decorator) and let user access it DONE
#3) This homepage is coded in home.html and it has 3 components [2 inputs + Search button]
#a) Asks where you want to search - name of school or department
#b) Asks key you want to search 
#c) Search Button
#4) Now, back to python once button pressed, obtain key(s) & what to search (dept or name of school) from the html page
#5) In python establish connection with SQL and select respective information for the dept or the school name provided (Since school name is not exact match, make use of a possible function from google to return all partial match for schoolname)
#6) Upon searching store these values in a tuple and load another HTML file ("/display" decorator) and let user access it
#7) This HTML file has access to the tuple of information (use JINJA to access & get values) and formats them in tables neatly and shows in webpage

from  flask import *
import sqlite3


# Instantiate a flask  object and assign it  app
app = Flask(__name__)

# The decorator "/" brings to home page --> execute fxn  below it
@app.route('/') #decorator for home page

def home():
    return  render_template("index.html")

# The decorator "/calculate" brings the  calculate page  --> port/calculate
@app.route('/search', methods = ["POST"]) # data posted returned as py dictionary
def search():
    
    data =  request.form
    dept = data["searchPlace1"]
    sch = data["searchPlace2"]
    search_result1 = "None"

    conn2 = sqlite3.connect("school123.db", check_same_thread=False)

    search_result1 = conn2.execute("SELECT SCHOOL.name, STAFF.name, Department, Contact, Address FROM STAFF,SCHOOL WHERE SCHOOL.name LIKE ('%' || ? || '%') AND STAFF.Department = ?", (sch,dept))


    lst1 = []
    for row in search_result1:
        lst1.append(row)
    print(lst1)
    conn2.commit()
    conn2.close()
    return render_template("results.html", lst1 = lst1)



if  __name__ == '__main__':

    app.run(debug =  True, use_reloader = True)
