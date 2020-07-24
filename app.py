from flask import Flask, request, render_template, redirect, flash, jsonify, session

from surveys import Question, Survey, satisfaction_survey

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def survey_welcome_page():
    '''Welcomes the user to the survey. Contains a start survey button'''

    return render_template('welcome.html', survey = satisfaction_survey)


@app.route('/questions/<int:question_no>', methods=["POST"])
def create_responseList(question_no):
    '''creates response list in session for each user'''

    session['response'] = []
    return redirect('/questions/0')



@app.route('/questions/<int:question_no>')
def display_question(question_no):
    '''Prompts the user to answer each question contained in the survey instance'''

    ##question_number = question_no

    print(f"i am inside questions/0")
    if question_no == 0:
        session['question_number'] = 0
    elif question_no != session['question_number'] :
        flash("You’re trying to access an invalid question")
        question_no = session['question_number']

    session['question_number'] = question_no
    return render_template('question.html', question = satisfaction_survey.questions[question_no],  question_number = session['question_number'])


@app.route('/answers', methods=['POST'])
def collect_answers():
    '''Collects the user's response to the survey question by appending their answer into the responses list. Redirects the user to the next question'''

    session['response'].append(request.form['choice'])
    session['question_number'] += 1
    next_question = session['question_number']

    if next_question < len(satisfaction_survey.questions):
        return redirect(f'/questions/{next_question}')
    else :
        return render_template('/thank-you.html')