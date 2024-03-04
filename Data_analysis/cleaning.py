
from flask import Flask, render_template, request, flash, url_for, redirect
import psycopg2
import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import nltk
import json
import yake

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Set the secret key

# PostgreSQL database configuration
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '68564213',
    'host': 'localhost',
    'port': '5432'
}

ADMIN_PASSWORD = '68564213'  # Password for accessing stored data

# Updated insert_data_into_table function with improved error handling
def insert_data_into_table(url, num_words, num_sentences, pos_counts, keywords_frequency, image_count, headings_used):
    connection = None  # Initialize connection variable
    cursor = None  # Initialize cursor variable
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        table_name = 'url_text'
        query = f"INSERT INTO {table_name} (url, num_words, num_sentences, pos_counts, keywords_frequency, image_count, headings_used) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(query, (url, num_words, num_sentences, pos_counts, json.dumps(keywords_frequency), image_count, json.dumps(headings_used)))
        connection.commit()
        print("Data inserted successfully.")

    except psycopg2.Error as e:
        print("Error inserting data into the table:", e)
        if connection:
            connection.rollback()  # Rollback in case of error to maintain data integrity

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Function to retrieve all data from PostgreSQL table
def get_all_data_from_table():
    connection = None  # Initialize connection variable
    cursor = None  # Initialize cursor variable
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        table_name = 'url_text'
        query = f"SELECT * FROM {table_name}"

        cursor.execute(query)
        data = cursor.fetchall()

        return data

    except Exception as e:
        print("Error retrieving data from the table:", e)
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Function to clean text from HTML content
def get_clean_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
    combined_text = ' '.join([element.get_text() for element in news_content])

    clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
    clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
    clean_text = clean_text.lower()  # Convert text to lowercase

    return clean_text

# Function to count images in the text
def count_images_in_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_tags = soup.find_all('img')  # Find all image tags within the combined text
    image_count = len(image_tags)  # Count the number of image tags

    return image_count

# Function to extract headings from the URL
def extract_headings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize a dictionary to store headings
    headings_used = {'h1': [], 'h2': [], 'h3': [], 'h4': [], 'h5': [], 'h6': []}

    # Extract text from h1, h2, h3, h4, h5, and h6 tags
    for tag in headings_used.keys():
        headings = soup.find_all(tag)
        for heading in headings:
            headings_used[tag].append(heading.get_text())

    return headings_used

@app.route("/", methods=['POST', 'GET'])
def portal():
    url = ""
    num_words = 0
    num_sentences = 0
    pos_counts = ""  # Initialize pos_counts as an empty dictionary
    clean_text = ""
    keywords_frequency = {}  # Initialize keywords_frequency as an empty dictionary
    image_count = 0  # Initialize image count
    headings_used = {}  # Initialize headings dictionary

    if request.method == "POST":
        url = request.form["Url"]
        clean_text = get_clean_text(url)
        num_words = len(word_tokenize(clean_text))
        
        # Extract text from URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
        combined_text = ' '.join([element.get_text() for element in news_content])
        
        # Count number of sentences
        num_sentences = len(sent_tokenize(combined_text))
        
        # Tokenize words and filter out stopwords
        words = word_tokenize(clean_text)
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]
        
        # Tag filtered words with parts of speech
        tagged_words = pos_tag(filtered_words)
        pos_dic = {}
        for word, tag in tagged_words:
            if tag in pos_dic:
                pos_dic[tag] += 1
            else:
                pos_dic[tag] = 1
        
        # Convert part-of-speech dictionary to JSON string
        pos_counts = json.dumps(pos_dic)
        
        # Extract SEO keywords
        keyword_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, dedupFunc='seqm')

        keywords = keyword_extractor.extract_keywords(clean_text)
        # Since we want to also include single and double-word phrases, we create additional extractors
        keyword_extractor_2 = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc='seqm')
        keyword_extractor_1 = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, dedupFunc='seqm')

        # Extract keywords of 2 words
        keywords_2 = keyword_extractor_2.extract_keywords(clean_text)

        # Extract keywords of 1 word
        keywords_1 = keyword_extractor_1.extract_keywords(clean_text)

        # Combine all keywords
        keywords += keywords_2 + keywords_1
        
        keywords_frequency = {}
        
        # Count frequency of each keyword using pos_dic
        for keyword, _ in keywords:
            keywords_frequency[keyword] = clean_text.lower().count(keyword.lower())

        # Sort the keywords by frequency in descending order
        sorted_frequency = {k: v for k, v in sorted(keywords_frequency.items(), key=lambda item: item[1], reverse=True)}
        
        # Store sorted keywords and frequencies in keywords_frequency
        keywords_frequency = sorted_frequency

        # Count images in text
        image_count = count_images_in_text(url)

        # Extract headings from URL
        headings_used = extract_headings(url)

        insert_data_into_table(url, num_words, num_sentences, pos_counts, keywords_frequency, image_count, headings_used)
        #flash('Data analyzed and inserted successfully!')

    stored_data = get_all_data_from_table()
    return render_template("index.html", url=url, cleaned_text=clean_text,
                           num_words=num_words, num_sentences=num_sentences,
                           pos_counts=pos_counts, keywords_frequency=keywords_frequency,
                           image_count=image_count, headings_used=headings_used,
                           stored_data=stored_data)

# Route for viewing details (requires password)
@app.route("/stored_data", methods=['GET', 'POST'])
def stored_data():
    if request.method == 'POST':
        if request.form['password'] == ADMIN_PASSWORD:
            pos_counts={}
            keywords_frequency={}
            image_count = 0
            headings_used = {}
            data = get_all_data_from_table()  # Retrieving all stored data from the database
            return render_template("stored_data.html", data=data, pos_counts=pos_counts,
                                   keywords_frequency=keywords_frequency, image_count=image_count,
                                   headings_used=headings_used)  # Rendering the stored data page with retrieved data
        else:
            flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
            return redirect(url_for('password'))  # Redirecting to password entry page

    return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# Route for entering the password
@app.route("/password", methods=['GET', 'POST'])
def password():
    return render_template("password.html")  # Rendering the password entry page

if __name__ == '__main__':
    app.run(debug=True)
