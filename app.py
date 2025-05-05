from flask import Flask, render_template, request, redirect, url_for, session, send_file
import io
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session handling

# In-memory users database { username: password }
users = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user in users and users[user] == pwd:
            session['logged_in'] = True
            session['username'] = user
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid Credentials ❌")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_user = request.form['username']
        new_pwd = request.form['password']
        confirm_pwd = request.form['confirm_password']

        if new_user in users:
            return render_template('signup.html', error="Username already exists ❗")
        if new_pwd != confirm_pwd:
            return render_template('signup.html', error="Passwords do not match ❗")

        users[new_user] = new_pwd
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    word_count = None
    if request.method == 'POST':
        text = request.form['text_area']
        words = text.split()
        word_count = {}
        for word in words:
            word = word.lower().strip(",.?!")
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        session['word_count'] = word_count
    return render_template('home.html', word_count=word_count)

@app.route('/download')
def download_csv():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    word_count = session.get('word_count', {})
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Word', 'Count'])
    for word, count in word_count.items():
        cw.writerow([word, count])

    output = io.BytesIO()
    output.write(si.getvalue().encode('utf-8'))
    output.seek(0)

    return send_file(output,
                     mimetype='text/csv',
                     download_name='word_count.csv',
                     as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
