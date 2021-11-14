from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def home():
    return render_template('base.html', madlibs=story.prompts)

@app.route('/madlibs')
def generate_madlib():
    n = request.args.get('noun')
    return render_template('madlib.html', noun=n)