from flask import Flask, render_template

app = Flask(__name__)

# function binding
@app.route("/")
def home():
    return "Hello Flak"

@app.route("/c4e")
def c4e():
    return "Hello C4E, hihi"

@app.route("/me")
def me():
    return "NSK"

@app.route("/hi/<name>")
def hi_name(name):
    return "Hi " + name

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    s = a + b
    return str(s)

@app.route("/posts/<int:index>")
def posts(index):
    titles=[
        "Troi hom nay dep qua",
        "Hom nay troi mua",
        "Hom nay troi nang"
    ]
    contents = [
        "Di ra ngoai thoi",
        "Mang theo o",
        "Khong ra ngoai",
    ]
    d = contents[index]
    t = titles[index]
    return render_template("post.html", title=t, content=d)
@app.route("/movie")
def movie():
    return render_template("movie.html", name="Deadpool", img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzaJcyYD4HoTS-qRgGosmrpEc5frKcY6seDKS6zd0JSooZ_lLg")
@app.route("/movies")
def movies():
    # movie_titles = [
    #     "Deadpool",
    #     "Black Window",
    #     "Captain American",
    #     "Adam Warlock",
    # ]
    movie_list = [
        {
            "title": "Deadpool"
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsYEdRhG6jUx_X12p77R9fi1PdnwT5BJDYbnD5YOd_nLFYdL4QFQ"
        },
         {
            "title": "Black Window"
            "image": "https://fanfest.com/wp-content/uploads/2018/07/black-widow-620x450.jpg"
        },
         {
            "title": "Captain American"
            "image": "https://images-na.ssl-images-amazon.com/images/I/71cmLZFzM2L._SL1500_.jpg"
        }



    ]
    return render_template("movies.html", movies=movie_list)

if __name__ == "__main__":
    app.run(debug=True)