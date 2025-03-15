from flask import Flask, render_template, request
import db_scripts as db

app = Flask(__name__)

@app.route("/")
def index():
    # get all quiz and send them back to the client
    quiz_list = db.getAllQuiz()
    return render_template("start.html", quiz_list=quiz_list)


@app.route("/test", methods = ["GET", "POST"])
def test():
    # get  
    quiz_id = request.form.get("quiz_id")
    questions = db.getQuestionsByQuizId(quiz_id)
    print(questions)
    return render_template("test.html", questions=questions)



@app.route("/result", methods = ["GET", "POST"])
def result():
   total = 0
   right = 0
   return render_template("result.html", total=total, right=right)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 