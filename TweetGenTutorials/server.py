from flask import Flask
app = Flask(__name__)
import histogram_exercises
import dictionary_words
# import tweetGenTutorials
import creating_randomness

@app.route('/example')
def generate_word():
    return dictionary_words.random_sentence(dictionary_words.split_file)




if __name__ == '__main__':
    # Turn this on in debug mode to get detailled information about request related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)