from flask import Flask, request, render_template, redirect, flash, jsonify

from surveys import Question, Survey, satisfaction_survey

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secret'

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def survey_welcome_page():
    return render_template('welcome.html', survey = satisfaction_survey)

@app.route('/questions/<int:question_no>')
def display_question(question_no):
    print(f"i am inside questions/0")
    return render_template('question.html', question = satisfaction_survey.questions[question_no])