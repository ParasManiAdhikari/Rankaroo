from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items_to_rank = ['Item 1', 'Item 2', 'Item 3']

@app.route('/')
def index():
    return render_template('index.html', items=items_to_rank)

@app.route('/submit_rankings', methods=['POST'])
def submit_rankings():
    # Process submitted rankings here
    # You can access the rankings from request.form

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
