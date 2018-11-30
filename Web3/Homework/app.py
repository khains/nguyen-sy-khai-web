from flask import Flask, render_template, request
import mlab
from bike import Bike

app = Flask(__name__)
mlab.connect()

@app.route("/new_bike", methods = ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike.html")
    if request.method == "POST":
        form = request.form
        m = form["model"]
        f = form["fee"]
        img = form["image"]
        y = form["year"]
        # print(m, f, img, y)
        b = Bike(model=m, fee=f, image=img, year=y)
        b.save()
        return "OK"



if __name__ == "__main__":
    app.run(debug=True)

