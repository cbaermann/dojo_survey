from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('dojo_survey.html')

@app.route('/users', methods=['POST'])
def process_form():
    return render_template("dojo_info.html", name=request.form["name"], loc=request.form["location"], lang=request.form["language"], com=request.form["message"])


if __name__ == '__main__':
    app.run(debug=True)