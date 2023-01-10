from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/c3f99fbb923b8cf304f8')
    all_post = response.json()
    return render_template("index.html", blog_post=all_post)


@app.route('/post/<blog_id>')
def blog(blog_id):
    print(blog_id)
    response = requests.get('https://api.npoint.io/c3f99fbb923b8cf304f8')
    all_post = response.json()
    spec_item = 0
    for item in all_post:
        if item['id'] == int(blog_id):
            spec_item = item
    print(spec_item)
    return render_template("post.html", blog_info=spec_item)


if __name__ == "__main__":
    app.run(debug=True)
