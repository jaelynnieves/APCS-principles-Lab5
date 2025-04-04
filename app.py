from flask import Flask, request, render_template, redirect
from age_picker import AgePicker

app = Flask(__name__)

age_picker = AgePicker(0, 0, 0, 0, 0)

@app.route('/')
def home():
    return "LETS GUESS YOUR AGEEEEEE!!!!!" 

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    answers = ['Youtube', 'Tiktok', 'Instagram', 'Myspace', 'Facebook']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected'] 
        if selected == answers[0]:
            age_picker.add('toddler')
        if selected == answers[1]:
            age_picker.add('child')
        if selected == answers[2]:
            age_picker.add('teen')
        if selected == answers[3]:
            age_picker.add('adult')
        if selected == answers[4]:
            age_picker.add('elderly')
        
        return redirect('/question/2')
    
@app.route('/question/2', methods = ['GET', "POST"])
def second_question():
    answers = ['Ms.Rachel', 'Taylor Swift', 'Rihanna', 'New kids on the Block', 'Elvis Presley']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            age_picker.add('toddler')
        if selected == answers[1]:
            age_picker.add('child')
        if selected == answers[2]:
            age_picker.add('teen')
        if selected == answers[3]:
            age_picker.add('adult')
        if selected == answers[4]:
            age_picker.add('elderly')

    return redirect('/question/3')
    

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    answers = ['Bluey', 'Pj mask', 'Gravity Falls', 'Full house', 'The Brady Brunch']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form.get['selected']
        if selected == answers[0]:
            age_picker.add('toddler')
        if selected == answers[1]:
            age_picker.add('child')
        if selected == answers[2]:
            age_picker.add('teen')
        if selected == answers[3]:
            age_picker.add('adult')
        if selected == answers[4]:
            age_picker.add('elderly')
   
    return redirect('/age')
    
@app.route('/age')
def get_age():
    return 'YOU AREEEEEE' + age_picker.sort() + '!' + 'Congratulations or not...'

if __name__ == "__main__":
    app.run()