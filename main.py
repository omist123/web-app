from flask import Flask, render_template, request, url_for,redirect
from flask_mail import Mail, Message
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['TESTING'] = False
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'owenmistretta@gmail.com'
app.config['MAIL_PASSWORD'] = 'gqkdncjkhuyklmcb'
app.config['MAIL_DEFAULT_SENDER'] = 'owenmistretta@gmail.com'
app.config['MAIL_MAX_EMAILS'] = 5
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = True

#gqkdncjkhuyklmcb
mail = Mail(app)
@app.route('/feedback', methods = ['POST','GET'])
def email():
    if request.method == 'POST':
        msg = Message('User Email!', recipients=['owenmistretta@gmail.com'])
        msg.body = request.form['content']
        mail.send(msg)
        return render_template('feedback.html')
        
        
       
    else: 
        return render_template('feedback.html')


@app.route('/home')
def home():
    return render_template('why.html')

@app.route('/projects')
def proj():
    return render_template('projects.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')



if __name__ == '__main__': # runs app with debugging turned on
   
   app.run(debug = True)