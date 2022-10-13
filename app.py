from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_form_fields():
    """This function updates the questions html to show the appropriate inputs
    needed based on the story text"""

    prompts = silly_story.prompts
    return render_template("questions.html", prompts = prompts)

@app.get("/story")
def show_story():
    """This function collects the form data. Using data, it generates and
    displays the story on the results.html"""

    inputs = {}

    for prompt in silly_story.prompts:
        response = request.args[prompt]
        inputs[prompt] = response

    story = silly_story.generate(inputs)

    return render_template("results.html", story = story)

# inputs = {prompt: request.args[prompt] for prompt in silly_story.prompts}
