from flask import render_template, request, redirect, url_for
from app import app
post = {
    'username': '',
    'usercity': '',
    'userhobby': '',
    'userage': '',
}

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        usercity = request.form.get('usercity')
        userhobby = request.form.get('userhobby')
        userage = request.form.get('userage')

        # Проверка на пустые значения
        if (username and usercity) and (userhobby and userage):
            post['username'] = username
            post['usercity'] = usercity
            post['userhobby'] = userhobby
            post['userage'] = userage
            return redirect(url_for('index'))
            # Передача данных в шаблон
    return render_template('blog.html',**post)
