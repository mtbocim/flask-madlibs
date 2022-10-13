from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import STORY_FORMATS

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

current_story = "I am here!"

@app.get("/")
def show_story_list():
    #do something with STORY_FORMATS
    return render_template("stories.html", STORY_FORMATS=STORY_FORMATS)

@app.get("/form")
def show_form_fields():
    """This function updates the questions html to show the appropriate inputs
    needed based on the story text"""
    global current_story
    current_story = request.args["stories"]
    print(current_story)
    response = STORY_FORMATS[current_story]
    prompts = response.prompts
    return render_template("questions.html", prompts = prompts)

@app.get("/story")
def show_story():
    """This function collects the form data. Using data, it generates and
    displays the story on the results.html"""
    print("current story = ", current_story)
    story = STORY_FORMATS[current_story]
    inputs = {}
    for prompt in story.prompts:
        value = request.args[prompt]
        inputs[prompt] = value
    
    story = story.generate(inputs)

    return render_template("results.html", story = story)
    
# inputs = {prompt: request.args[prompt] for prompt in silly_story.prompts}
