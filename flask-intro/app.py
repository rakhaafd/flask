from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey2025"

@app.route("/")
def my_index():
    # variable parsing
    val = '40%'

    # looping parsing
    language = ['Python', 'Javascript', 'Bash Script']

    # conditioning parsing
    wife = "Wonjian" #Park Gyu
    return render_template("index.html", value=val, lang=language, girl=wife)

@app.route("/contact")
def my_contact():
    return render_template("contact.html")

@app.route("/about")
def my_about():
    return render_template("about.html")

#parsing to link http://127.0.0.1:5000/parsing/1000 (int)
@app.route("/parsing/<int:value>")
def go_parsing(value):
    return "the value is : {}".format(value)

#parsing to link http://127.0.0.1:5000/parsing/tes (string)
@app.route("/parsing2/<string:val2>")
def go_parsing2(val2):
    return "the value is : {}".format(val2)

#parsing to link http://127.0.0.1:5000/argumentparse?value=40 (argument)
@app.route("/argumentparse")
def go_argument():
    data = request.args.get("value")
    return "value in argument is: {}".format(data)

#parsing value from url to set value session
@app.route("/page/<int:value>")
def session_1(value):
    session["my_value"] = value
    return "Success set value!"

@app.route('/page/see')
def view_session_1():
    try: #try & except is same with if else
        data = session["my_value"]
        return "Values set is = {}".format(data)
    except:
        return "You dont have value session anymore"

# http://127.0.0.1:5000/page/500: add value in here (500)
# then, see in here http://127.0.0.1:5000/page/see
#output: Values set is = 500

#how to logout?/destroy session
@app.route("/page/logout")
def logout_session_1():
    session.pop("my_value")
    return "Success Logout/Delete Section"
#after this, if you go to /see route, u can see return except. bcs the data already gone

if __name__ == "__main__":
    app.run(debug=True)