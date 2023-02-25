import os
import openai
from flask import Flask, request

app = Flask(__name__)
openai.api_key = "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"

# Add CSS styles
style = """
    body {
        margin: 0;
        padding: 0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 16px;
        line-height: 1.4;
    }
    
    header {
        background-color: #000;
        color: #fff;
        padding: 20px;
        text-align: center;
    }
    
    h1 {
        font-size: 36px;
        margin: 0;
        padding: 20px;
    }
    
    form {
        margin: 0 auto;
        max-width: 600px;
        padding: 20px;
    }
    
    label {
        display: block;
        font-size: 20px;
        margin-bottom: 10px;
    }
    
    input[type="text"] {
        border: none;
        border-bottom: 2px solid #ccc;
        font-size: 20px;
        padding: 10px;
        width: 100%;
    }
    
    input[type="submit"] {
        background-color: #000;
        color: #fff;
        border: none;
        font-size: 20px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    
    p {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 16px;
        text-align: center;
        margin-top: 40px;
    }
"""
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form['input']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Correct this to standard English: " + input_text,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        corrected_text = response.choices[0].text.strip()
        return f'''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Correct Text</title>
                    <style>{style}</style>
                </head>
                <body>
                    <header>
                        <h1>Correct Text</h1>
                    </header>
                    <main>
                        <form method="post">
                            <label for="input">Enter text to be corrected:</label>
                            <input type="text" id="input" name="input">
                            <input type="submit" value="Submit">
                        </form>
                        <p style="font-family: sans-serif; text-align: center;">Corrected text:</p>
                        <p style="font-family: sans-serif; text-align: center;">{corrected_text}</p>
                    </main>
                </body>
            </html>
        '''
    else:
        return (
            '<h1>Please enter the statement you would like to correct</h1>'
            '<form method="post">'
            '<label for="input">Input:</label>'
            '<input type="text" id="input" name="input"><br><br>'
            '<input type="submit" value="Submit">'
            '</form>'
        )
