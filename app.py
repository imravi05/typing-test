from flask import Flask, render_template, request
import time
import random

app = Flask(__name__)

# A list of words to generate random text
word_list = [
    "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog",
    "hello", "world", "typing", "speed", "test", "is", "fun", "to", "try",
    "practice", "improve", "your", "typing", "skills", "writing", "code",
    "is", "a", "great", "way", "to", "learn", "new", "things"
]

# Function to generate random text
def generate_random_text(num_words=10):
    return ' '.join(random.choices(word_list, k=num_words))

@app.route('/', methods=['GET', 'POST'])
def index():
    # Generate random text for the user to type
    random_text = generate_random_text(15)  # Generate 15 words of random text

    current_time = time.time()

    if request.method == 'POST':
        # Get the typed text and starting time from the form
        typed_text = request.form['typed_text']
        start_time = float(request.form['start_time'])
        end_time = time.time()

        # Calculate the time taken and words per minute (WPM)
        time_taken = end_time - start_time
        words_count = len(typed_text.split())
        wpm = (words_count / time_taken) * 60 if time_taken > 0 else 0

        return render_template('index.html', wpm=wpm, typed_text=typed_text, time_taken=time_taken, random_text=random_text, current_time=current_time)

    return render_template('index.html', random_text=random_text, wpm=None, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
