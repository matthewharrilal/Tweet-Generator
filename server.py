from flask import Flask
app = Flask(__name__)
import histogram_exercises
import dictionary_words
# import tweetGenTutorials
import creating_randomness
import ClassDictogram as d

@app.route('/')
def generate_word():
    return d.Dictogram.generate_sentence_from_markov_chain(10)



if __name__ == '__main__':
    # Turn this on in debug mode to get detailled information about request related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)