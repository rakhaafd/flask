from flask import Flask, render_template, url_for, redirect, request, session, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey2025"

@app.route("/", methods=["POST", "GET"])
def index():
    if "email" in session:
        return redirect(url_for('success_req'))
    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        if email == "admin@gmail.com" and password == "pass":
            session['email'] = email
            session['password'] = password
            return redirect(url_for('success_req'))
        else:
            return redirect(url_for('index'))
        
    return render_template("index.html")

@app.route("/success")
def success_req():
    if "email" not in session:
        flash("You must login first", "error")
        return redirect(url_for('index'))
    
    value = f"Welcome {session['email']} !"
    return render_template("success.html", value=value)

@app.route("/about")
def about():
    if "email" not in session:
        flash("You must login first", "error")
        return redirect(url_for('index'))
    
    return render_template("about.html")

@app.route("/contact")
def contact():
    if "email" not in session:
        flash("You must login first", "error")
        return redirect(url_for('index'))
    
    return render_template("contact.html")

@app.route('/logout')
def logout_account():
    if "email" in session:
        session.pop("email")
        session.pop("password")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/table')
def show_table():
    if "email" not in session:
        flash("You must login first", "error")
        return redirect(url_for('index'))
    
    my_social_media = {
        "Instagram" : ["@rakhaafd", "@rakuu.bash"],
        "Github" : ["rakhaafd"],
        "Youtube" : ["rakuubash"],
        "Linkedin" : ["Rakha Fausta"]
    }
    return render_template("table.html", socialmed=my_social_media)

@app.route("/redirect-about")
def redirect_about():
    return redirect(url_for("about"))

@app.route("/redirect-contact")
def redirect_contact():
    return redirect(url_for("contact"))

@app.route("/redirect-index")
def redirect_index():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)