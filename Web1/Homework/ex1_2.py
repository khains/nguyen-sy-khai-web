from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!"

@app.route("/about-me")
def about_me():
    return render_template("about_me.html")

@app.route("/school")
def school():
    return redirect("http://techkids.vn ", code = 302)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    z = height / 100
    bmi = weight / (z*z)
    if bmi < 16:
        return "BMI= " + str(bmi) + ": Severely underweight"
    elif bmi < 18.5:
        return "BMI= " + str(bmi) + ": Underweight"
    elif bmi < 25:
        return "BMI= " + str(bmi) + ": Normal"
    elif bmi < 30:
        return "BMI= " + str(bmi) + ": Overweight" 
    else:
        return "BMI= " + str(bmi) + ": Obese"


@app.route("/user/<user_name>")
def user_name(user_name):
    users = {
	"huy" :         {
			"name" : "Nguyen Quang Huy",
			"age" : 29
       },
    "tuananh" : {
			"name" : "Huynh Tuan Anh",
			"age" : 22
       }
    }
    for k in users.keys():

        if user_name in k:
            a = users[user_name]
            return render_template("user_names.html", name = a["name"], age = a["age"])
        else:
            return "User not found"




if __name__ == "__main__":
    app.run(debug = True)