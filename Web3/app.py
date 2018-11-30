from flask import Flask, render_template, request
import mlab
from register import Register
from gmail import GMail, Message

app = Flask(__name__)
mlab.connect()

# @app.route("/add_movie", methods=["GET", "POST"])
# def add_movie():
#     if request.method == "GET":
#         return render_template("add_movie.html")
#     elif request.method == "POST":
#         form = request.form
#         t = form["title"]
#         img = form["image"]
#         y = form["year"]
#         # print(t, img, y)

#         m = Movie(title=t, image=img, year=y)
#         m.save()
#         return "Gotcha!!!!!!"
@app.route("/add_register", methods=["GET", "POST"])
def add_register():
    if request.method == "GET":
        return render_template("add_register.html")
    elif request.method == "POST":
        form = request.form
        user = form["username"]
        pas = form["password"]
        em = form["email"]

        exist_user = Register.objects(username=user).first()
        if exist_user != None:
            return "User already exists!"
        else:
            m = Register(username=user, password=pas, email=em)
            m.save() 

        
        gmail = GMail("khains0000@gmail.com", "sykhai123")
        template = "Ban da tao tai khoan thanh cong"
        message = Message("Dang ky tai khoan", to=em, html= template)
        gmail.send(message)
      
        return "Gotcha!!!!!!"


if __name__ == "__main__":
    app.run(debug=True)

