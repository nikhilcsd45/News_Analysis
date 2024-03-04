# from flask import Flask, render_template, request
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# def get_clean_text(url):
#     # Fetching the webpage content
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Extracting news content based on the specific classes where India Today news are printed
#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
    
#     # Combining all extracted text into a single string
#     combined_text = ' '.join([element.get_text() for element in news_content])
    
#     # Cleaning the text using regular expressions and NLTK
#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase
    
#     return clean_text

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     url = request.form['url']
#     clean_text = get_clean_text(url)
    
#     # Tokenize the text
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","clearfix","_next"])
#     combined_text = ' '.join([element.get_text() for element in news_content])
#     sentences = sent_tokenize(combined_text)  # Counting sentences from combined_text
#     words = word_tokenize(clean_text)
    
#     # Remove stopwords
#     stop_words = set(stopwords.words('english'))
#     filtered_words = [word for word in words if word not in stop_words]
    
#     # POS tagging
#     tagged_words = pos_tag(filtered_words)
    
#     # Count POS tags
#     pos_counts = {}
#     for word, tag in tagged_words:
#         if tag in pos_counts:
#             pos_counts[tag] += 1
#         else:
#             pos_counts[tag] = 1
    
#     # Count number of sentences and words
#     num_sentences = len(sentences)
#     num_words = len(filtered_words)
    
#     return render_template('result.html', url=url, pos_counts=pos_counts, num_sentences=num_sentences, num_words=num_words)

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for, flash
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# # Function to insert data into PostgreSQL table
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags):
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags) VALUES (%s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags))
#         connection.commit()

#     except Exception as e:
#         print("Error inserting data into the table:", e)
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","_next"])
#     combined_text = ' '.join([element.get_text() for element in news_content])
    
#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase
    
#     return clean_text

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     if request.method == "POST":
#         url = request.form["Url"]
#         No_of_words = request.form["No_of_words"]
#         No_of_Sentences = request.form["No_of_Sentences"]
#         Post_tags = request.form["Post_tags"]

#         insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags)
#         flash('Data inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", stored_data=stored_data)

# if __name__ == '__main__':
# #     app.run(debug=True)


# from flask import Flask, render_template, request, flash, url_for  # Import url_for
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# # Function to insert data into PostgreSQL table
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags):
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags) VALUES (%s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags))
#         connection.commit()

#     except Exception as e:
#         print("Error inserting data into the table:", e)
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","_next"])
#     combined_text = ' '.join([element.get_text() for element in news_content])
    
#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase
    
#     return clean_text

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = ""
    
#     No_of_sentences = ""
#     Post_tags = ""
#     pos_counts = ""
#     clean_text1 = ""  # Initialize clean_text with an empty string
    
#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         clean_text1=clean_text
        
        
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
        
#         No_of_sentences = len(sent_tokenize(combined_text))
#         words = word_tokenize(clean_text)
#         No_of_words= len(word_tokenize(clean_text))
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
#         tagged_words = pos_tag(filtered_words)
#         pos_counts = {}
#         for words, tag in tagged_words:
#             if tag in pos_counts:
#                 pos_counts[tag] += 1
#             else:
#                 pos_counts[tag] = 1
#         Post_tags = pos_counts

#         insert_data_into_table(url,No_of_words,No_of_sentences,Post_tags)
#         flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text1,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            pos_counts=pos_counts)#, stored_data=stored_data)

# @app.route("/stored_data")
# def stored_data():
#     stored_data = get_all_data_from_table()
#     return render_template("stored_data.html", stored_data=stored_data)

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request, flash, url_for
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# # Function to insert data into PostgreSQL table
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags):
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags) VALUES (%s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags))
#         connection.commit()

#     except Exception as e:
#         print("Error inserting data into the table:", e)
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])
    
#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase
    
#     return clean_text

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0  # Initialize with 0
#     No_of_sentences = 0  # Initialize with 0
#     Post_tags = ""
#     pos_counts = {}
#     clean_text = ""  # Initialize clean_text with an empty string
    
#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
        
#         No_of_words = len(word_tokenize(clean_text))  # Calculate the number of words
        
#         No_of_sentences = len(sent_tokenize(clean_text))  # Calculate the number of sentences
        
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
#         tagged_words = pos_tag(filtered_words)
        
#         for word, tag in tagged_words:
#             if tag in pos_counts:
#                 pos_counts[tag] += 1
#             else:
#                 pos_counts[tag] = 1
        
#         Post_tags = pos_counts

#         insert_data_into_table(url, No_of_words, No_of_sentences, Post_tags)
#         flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            pos_counts=pos_counts, stored_data=stored_data)

# @app.route("/stored_data")
# def stored_data():
#     stored_data = get_all_data_from_table()
#     return render_template("stored_data.html", stored_data=stored_data, Pos_counts=Pos_counts)

# if __name__ == '__main__':
#     app.run(debug=True)








# from flask import Flask, render_template, request, flash, url_for, redirect
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# import json
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# ADMIN_PASSWORD = '68564213'  # Password for accessing stored data
# # Updated insert_data_into_table function with improved error handling
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags):
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags) VALUES (%s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags))
#         connection.commit()
#         print("Data inserted successfully.")

#     except psycopg2.Error as e:
#         print("Error inserting data into the table:", e)
#         connection.rollback()  # Rollback in case of error to maintain data integrity

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Other parts of your code remain the same


# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []
#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])
    
#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase
    
#     return clean_text
# @app.route("/", methods=['POST', 'GET'])
# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0
#     No_of_sentences = 0
#     Post_tags = ""  # Changed variable name to Post_tags
#     pos_counts = {}  # Initialize pos_counts as an empty dictionary
#     clean_text = ""

#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         No_of_words = len(word_tokenize(clean_text))
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
#         No_of_sentences = len(sent_tokenize(combined_text))
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
#         tagged_words = pos_tag(filtered_words)
#         post_dic={}
#         for words, tag in tagged_words:
#             if tag in post_dic:
#                 post_dic[tag] += 1
#             else:
#                 post_dic[tag] = 1

#         pos_counts = json.dumps(post_dic)  # Converting part-of-speech dictionary to JSON string
#         Post_tags = pos_counts  # Assigning pos_counts to Post_tags
#         insert_data_into_table(url, No_of_words, No_of_sentences, Post_tags)
#         flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            post_counts=pos_counts, stored_data=stored_data)

# # Route for viewing details (requires password)
# @app.route("/stored_data", methods=['GET', 'POST'])
# def stored_data():
#     if request.method == 'POST':
#         if request.form['password'] == ADMIN_PASSWORD:
#             pos_counts={}
#             data = get_all_data_from_table()  # Retrieving all stored data from the database
#             return render_template("stored_data.html", data=data, pos_counts=pos_counts)  # Rendering the stored data page with retrieved data
#         else:
#             flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
#             return redirect(url_for('password'))  # Redirecting to password entry page

#     return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# # Route for entering the password
# @app.route("/password", methods=['GET', 'POST'])
# def password():
#     return render_template("password.html")  # Rendering the password entry page


# # @app.route("/stored_data")
# # def stored_data():
# #     stored_data = get_all_data_from_table()
# #     pos_counts= {}  # Define pos_counts here as well
# #     return render_template("stored_data.html", stored_data=stored_data, pos_counts=pos_counts)

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request, flash, url_for, redirect
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# import json

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '6856',
#     'host': 'localhost',
#     'port': '5432'
# }

# ADMIN_PASSWORD = '6856'  # Password for accessing stored data

# # Updated insert_data_into_table function with improved error handling
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags):
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags) VALUES (%s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags))
#         connection.commit()
#         print("Data inserted successfully.")

#     except psycopg2.Error as e:
#         print("Error inserting data into the table:", e)
#         connection.rollback()  # Rollback in case of error to maintain data integrity

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])

#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase

#     return clean_text

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0
#     No_of_sentences = 0
#     pos_counts = ""  # Initialize pos_counts as an empty dictionary
#     clean_text = ""
    

#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         No_of_words = len(word_tokenize(clean_text))
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
#         No_of_sentences = len(sent_tokenize(combined_text))
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
#         tagged_words = pos_tag(filtered_words)
#         post_dic={}
#         for words, tag in tagged_words:
#             if tag in post_dic:
#                 post_dic[tag] += 1
#             else:
#                 post_dic[tag] = 1

#         pos_counts = json.dumps(post_dic)  # Converting part-of-speech dictionary to JSON string

#         insert_data_into_table(url, No_of_words, No_of_sentences, pos_counts)
#         flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            post_counts=pos_counts, stored_data=stored_data)

# # Route for viewing details (requires password)
# @app.route("/stored_data", methods=['GET', 'POST'])
# def stored_data():
#     if request.method == 'POST':
#         if request.form['password'] == ADMIN_PASSWORD:
           
#             data = get_all_data_from_table()  # Retrieving all stored data from the database
#             return render_template("stored_data.html", data=data)  # Rendering the stored data page with retrieved data
#         else:
#             flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
#             return redirect(url_for('password'))  # Redirecting to password entry page

#     return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# # Route for entering the password
# @app.route("/password", methods=['GET', 'POST'])
# def password():
#     return render_template("password.html")  # Rendering the password entry page

# if __name__ == '__main__':
#     app.run(debug=True)









# from flask import Flask, render_template, request, flash, url_for, redirect
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# import json


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# ADMIN_PASSWORD = '68564213'  # Password for accessing stored data

# # Updated insert_data_into_table function with improved error handling
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags,Keywords_frequency):
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags,Keywords_frequency) VALUES (%s, %s, %s, %s,%s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags,Keywords_frequency))
#         connection.commit()
#         print("Data inserted successfully.")

#     except psycopg2.Error as e:
#         print("Error inserting data into the table:", e)
#         if connection:
#             connection.rollback()  # Rollback in case of error to maintain data integrity

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])

#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase

#     return clean_text

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0
#     No_of_sentences = 0
#     pos_counts = ""  # Initialize pos_counts as an empty dictionary
#     clean_text = ""
#     Keywords_frequency=""
#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         No_of_words = len(word_tokenize(clean_text))
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
#         No_of_sentences = len(sent_tokenize(combined_text))
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
#         tagged_words = pos_tag(filtered_words)
#         post_dic={}
#         for words, tag in tagged_words:
#             if tag in post_dic:
#                 post_dic[tag] += 1
#             else:
#                 post_dic[tag] = 1

#         pos_counts = json.dumps(post_dic)  # Converting part-of-speech dictionary to JSON string
# #keyword
        
#     import yake
#     # Sample news article text
#     news_article =clean_text
#     # Initialize YAKE keyword extractor
#     # Parameters: lan = Language (default='en'), n = Number of keywords to extract (default=3)
#     #             dedupLim = Degree of deduplication (default=0.9), dedupFunc = Deduplication function (default='seqm')
#     keyword_extractor = yake.KeywordExtractor()

#     # Extract keywords from the news article
#     keywords = keyword_extractor.extract_keywords(news_article)

#     # Find the maximum score
#     if keywords:
#         max_score = max(score for _, score in keywords)
#     else:
#         max_score=0
#     # Normalize scores to the range [0, 1]
#     normalized_keywords = [(keyword, score / max_score) for keyword, score in keywords]
#     Keywords_frequency_str={}
#     # Print the normalized keywords and their scores
#     for keyword, score in normalized_keywords[-10:]:
#         Keywords_frequency_str[keyword]= round(score,2)
#     Keywords_frequency = json.dumps(Keywords_frequency_str) 
# #keyword
#     insert_data_into_table(url, No_of_words, No_of_sentences, pos_counts,Keywords_frequency)
#     #flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            post_counts=pos_counts,Keywords_frequency1=Keywords_frequency, stored_data=stored_data)

# # Route for viewing details (requires password)
# @app.route("/stored_data", methods=['GET', 'POST'])
# def stored_data():
#     if request.method == 'POST':
#         if request.form['password'] == ADMIN_PASSWORD:
#             pos_counts={}
#             Keywords_frequency={}
#             data = get_all_data_from_table()  # Retrieving all stored data from the database
#             return render_template("stored_data.html", data=data,pos_counts=pos_counts,Keywords_frequency=Keywords_frequency)  # Rendering the stored data page with retrieved data
#         else:
#             flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
#             return redirect(url_for('password'))  # Redirecting to password entry page

#     return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# # Route for entering the password
# @app.route("/password", methods=['GET', 'POST'])
# def password():
#     return render_template("password.html")  # Rendering the password entry page

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, flash, url_for, redirect
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# import json
# import yake

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# ADMIN_PASSWORD = '68564213'  # Password for accessing stored data

# # Updated insert_data_into_table function with improved error handling
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags,Keywords_frequency):
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags,Keywords_frequency) VALUES (%s, %s, %s, %s,%s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags,Keywords_frequency))
#         connection.commit()
#         print("Data inserted successfully.")

#     except psycopg2.Error as e:
#         print("Error inserting data into the table:", e)
#         if connection:
#             connection.rollback()  # Rollback in case of error to maintain data integrity

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])

#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase

#     return clean_text

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0
#     No_of_sentences = 0
#     pos_counts = ""  # Initialize pos_counts as an empty dictionary
#     clean_text = ""
#     Keywords_frequency = {}  # Initialize Keywords_frequency as an empty dictionary

#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         No_of_words = len(word_tokenize(clean_text))
        
#         # Extract text from URL
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
        
#         # Count number of sentences
#         No_of_sentences = len(sent_tokenize(combined_text))
        
#         # Tokenize words and filter out stopwords
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
        
#         # Tag filtered words with parts of speech
#         tagged_words = pos_tag(filtered_words)
#         post_dic = {}
#         for word, tag in tagged_words:
#             if tag in post_dic:
#                 post_dic[tag] += 1
#             else:
#                 post_dic[tag] = 1
        
#         # Convert part-of-speech dictionary to JSON string
#         pos_counts = json.dumps(post_dic)
        
#         # Extract SEO keywords
#          # Extract SEO keywords
#         keyword_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, dedupFunc='seqm')

#         keywords = keyword_extractor.extract_keywords(clean_text)
#         # Since we want to also include single and double-word phrases, we create additional extractors
#         keyword_extractor_2 = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc='seqm')
#         keyword_extractor_1 = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, dedupFunc='seqm')

#         # Extract keywords of 2 words
#         keywords_2 = keyword_extractor_2.extract_keywords(clean_text)

#         # Extract keywords of 1 word
#         keywords_1 = keyword_extractor_1.extract_keywords(clean_text)

#         # Combine all keywords
#         keywords += keywords_2 + keywords_1
        
#         keyword_frequency = {}
        
#         # Count frequency of each keyword using post_dic
#         for keyword, _ in keywords:
#             keyword_frequency[keyword] = clean_text.lower().count(keyword.lower())

#         # Sort the keywords by frequency in descending order
#         sorted_frequency = {k: v for k, v in sorted(keyword_frequency.items(), key=lambda item: item[1], reverse=True)}
        
#         # Store sorted keywords and frequencies in Keywords_frequency
#         Keywords_frequency = sorted_frequency
# #keyword
#     insert_data_into_table(url, No_of_words, No_of_sentences, pos_counts,Keywords_frequency)
#     #flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            post_counts=pos_counts,Keywords_frequency1=Keywords_frequency, stored_data=stored_data)

# # Route for viewing details (requires password)
# @app.route("/stored_data", methods=['GET', 'POST'])
# def stored_data():
#     if request.method == 'POST':
#         if request.form['password'] == ADMIN_PASSWORD:
#             pos_counts={}
#             Keywords_frequency={}
#             data = get_all_data_from_table()  # Retrieving all stored data from the database
#             return render_template("stored_data.html", data=data,pos_counts=pos_counts,Keywords_frequency=Keywords_frequency)  # Rendering the stored data page with retrieved data
#         else:
#             flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
#             return redirect(url_for('password'))  # Redirecting to password entry page

#     return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# # Route for entering the password
# @app.route("/password", methods=['GET', 'POST'])
# def password():
#     return render_template("password.html")  # Rendering the password entry page

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, flash, url_for, redirect
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# import json
# import yake

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# ADMIN_PASSWORD = '68564213'  # Password for accessing stored data

# # Updated insert_data_into_table function with improved error handling
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags, Keywords_frequency, image_count):
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags, Keywords_frequency, image_count) VALUES (%s, %s, %s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags, Keywords_frequency, image_count))
#         connection.commit()
#         print("Data inserted successfully.")

#     except psycopg2.Error as e:
#         print("Error inserting data into the table:", e)
#         if connection:
#             connection.rollback()  # Rollback in case of error to maintain data integrity

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])

#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase

#     return clean_text

# # Function to count images in the text
# def count_images_in_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     image_tags = soup.find_all('img')  # Find all image tags within the combined text
#     image_count = len(image_tags)  # Count the number of image tags

#     return image_count

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0
#     No_of_sentences = 0
#     pos_counts = ""  # Initialize pos_counts as an empty dictionary
#     clean_text = ""
#     Keywords_frequency = {}  # Initialize Keywords_frequency as an empty dictionary
#     image_count = 0  # Initialize image count

#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         No_of_words = len(word_tokenize(clean_text))
        
#         # Extract text from URL
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
        
#         # Count number of sentences
#         No_of_sentences = len(sent_tokenize(combined_text))
        
#         # Tokenize words and filter out stopwords
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
        
#         # Tag filtered words with parts of speech
#         tagged_words = pos_tag(filtered_words)
#         post_dic = {}
#         for word, tag in tagged_words:
#             if tag in post_dic:
#                 post_dic[tag] += 1
#             else:
#                 post_dic[tag] = 1
        
#         # Convert part-of-speech dictionary to JSON string
#         pos_counts = json.dumps(post_dic)
        
#         # Extract SEO keywords
#         keyword_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, dedupFunc='seqm')

#         keywords = keyword_extractor.extract_keywords(clean_text)
#         # Since we want to also include single and double-word phrases, we create additional extractors
#         keyword_extractor_2 = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc='seqm')
#         keyword_extractor_1 = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, dedupFunc='seqm')

#         # Extract keywords of 2 words
#         keywords_2 = keyword_extractor_2.extract_keywords(clean_text)

#         # Extract keywords of 1 word
#         keywords_1 = keyword_extractor_1.extract_keywords(clean_text)

#         # Combine all keywords
#         keywords += keywords_2 + keywords_1
        
#         keyword_frequency = {}
        
#         # Count frequency of each keyword using post_dic
#         for keyword, _ in keywords:
#             keyword_frequency[keyword] = clean_text.lower().count(keyword.lower())

#         # Sort the keywords by frequency in descending order
#         sorted_frequency = {k: v for k, v in sorted(keyword_frequency.items(), key=lambda item: item[1], reverse=True)}
        
#         # Store sorted keywords and frequencies in Keywords_frequency
#         Keywords_frequency = sorted_frequency

#         # Count images in text
#         image_count = count_images_in_text(url)

#     insert_data_into_table(url, No_of_words, No_of_sentences, pos_counts, Keywords_frequency, image_count)
#     # flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            post_counts=pos_counts, Keywords_frequency1=Keywords_frequency,
#                            image_count=image_count, stored_data=stored_data)

# # Route for viewing details (requires password)
# @app.route("/stored_data", methods=['GET', 'POST'])
# def stored_data():
#     if request.method == 'POST':
#         if request.form['password'] == ADMIN_PASSWORD:
#             pos_counts={}
#             Keywords_frequency={}
#             image_count = 0
#             data = get_all_data_from_table()  # Retrieving all stored data from the database
#             return render_template("stored_data.html", data=data, pos_counts=pos_counts,
#                                    Keywords_frequency=Keywords_frequency, image_count=image_count)  # Rendering the stored data page with retrieved data
#         else:
#             flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
#             return redirect(url_for('password'))  # Redirecting to password entry page

#     return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# # Route for entering the password
# @app.route("/password", methods=['GET', 'POST'])
# def password():
#     return render_template("password.html")  # Rendering the password entry page

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, flash, url_for, redirect
# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# import re
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# import nltk
# import json
# import yake

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'  # Set the secret key

# # PostgreSQL database configuration
# db_config = {
#     'dbname': 'postgres',
#     'user': 'postgres',
#     'password': '68564213',
#     'host': 'localhost',
#     'port': '5432'
# }

# ADMIN_PASSWORD = '68564213'  # Password for accessing stored data

# # Updated insert_data_into_table function with improved error handling
# def insert_data_into_table(url, No_of_words, No_of_Sentences, Post_tags, Keywords_frequency, image_count, headings_used):
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"INSERT INTO {table_name} (url, No_of_words, No_of_Sentences, Post_tags, Keywords_frequency, image_count, headings_used) VALUES (%s, %s, %s, %s, %s, %s, %s)"

#         cursor.execute(query, (url, No_of_words, No_of_Sentences, Post_tags, Keywords_frequency, image_count, json.dumps(headings_used)))
#         connection.commit()
#         print("Data inserted successfully.")

#     except psycopg2.Error as e:
#         print("Error inserting data into the table:", e)
#         if connection:
#             connection.rollback()  # Rollback in case of error to maintain data integrity

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to retrieve all data from PostgreSQL table
# def get_all_data_from_table():
#     connection = None  # Initialize connection variable
#     cursor = None  # Initialize cursor variable
#     try:
#         connection = psycopg2.connect(**db_config)
#         cursor = connection.cursor()

#         table_name = 'url_text'
#         query = f"SELECT * FROM {table_name}"

#         cursor.execute(query)
#         data = cursor.fetchall()

#         return data

#     except Exception as e:
#         print("Error retrieving data from the table:", e)
#         return []

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()

# # Function to clean text from HTML content
# def get_clean_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#     combined_text = ' '.join([element.get_text() for element in news_content])

#     clean_text = re.sub(r'<.*?>', '', combined_text)  # Remove HTML tags
#     clean_text = re.sub(r'[^a-zA-Z\s]', '', clean_text)  # Remove non-alphabetic characters
#     clean_text = clean_text.lower()  # Convert text to lowercase

#     return clean_text

# # Function to count images in the text
# def count_images_in_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     image_tags = soup.find_all('img')  # Find all image tags within the combined text
#     image_count = len(image_tags)  # Count the number of image tags

#     return image_count

# # Function to extract headings from the URL
# def extract_headings(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Initialize a dictionary to store headings
#     headings_used = {'h1': [], 'h2': [], 'h3': [], 'h4': [], 'h5': [], 'h6': []}

#     # Extract text from h1, h2, h3, h4, h5, and h6 tags
#     for tag in headings_used.keys():
#         headings = soup.find_all(tag)
#         for heading in headings:
#             headings_used[tag].append(heading.get_text())

#     return headings_used

# @app.route("/", methods=['POST', 'GET'])
# def portal():
#     url = ""
#     No_of_words = 0
#     No_of_sentences = 0
#     pos_counts = ""  # Initialize pos_counts as an empty dictionary
#     clean_text = ""
#     Keywords_frequency = {}  # Initialize Keywords_frequency as an empty dictionary
#     image_count = 0  # Initialize image count
#     headings_used = {}  # Initialize headings dictionary

#     if request.method == "POST":
#         url = request.form["Url"]
#         clean_text = get_clean_text(url)
#         No_of_words = len(word_tokenize(clean_text))
        
#         # Extract text from URL
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         news_content = soup.find_all('div', class_=["news-content", "story-highlights", "description", "story-kicker","container","at_row","_next","clearfix"])
#         combined_text = ' '.join([element.get_text() for element in news_content])
        
#         # Count number of sentences
#         No_of_sentences = len(sent_tokenize(combined_text))
        
#         # Tokenize words and filter out stopwords
#         words = word_tokenize(clean_text)
#         stop_words = set(stopwords.words('english'))
#         filtered_words = [word for word in words if word not in stop_words]
        
#         # Tag filtered words with parts of speech
#         tagged_words = pos_tag(filtered_words)
#         post_dic = {}
#         for word, tag in tagged_words:
#             if tag in post_dic:
#                 post_dic[tag] += 1
#             else:
#                 post_dic[tag] = 1
        
#         # Convert part-of-speech dictionary to JSON string
#         pos_counts = json.dumps(post_dic)
        
#         # Extract SEO keywords
#          # Extract SEO keywords
#         keyword_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, dedupFunc='seqm')

#         keywords = keyword_extractor.extract_keywords(clean_text)
#         # Since we want to also include single and double-word phrases, we create additional extractors
#         keyword_extractor_2 = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc='seqm')
#         keyword_extractor_1 = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, dedupFunc='seqm')

#         # Extract keywords of 2 words
#         keywords_2 = keyword_extractor_2.extract_keywords(clean_text)

#         # Extract keywords of 1 word
#         keywords_1 = keyword_extractor_1.extract_keywords(clean_text)

#         # Combine all keywords
#         keywords += keywords_2 + keywords_1
        
#         keywords_frequency = {}
        
#         # Count frequency of each keyword using post_dic
#         for keyword, _ in keywords:
#             keywords_frequency[keyword] = clean_text.lower().count(keyword.lower())

#         # Sort the keywords by frequency in descending order
#         sorted_frequency = {k: v for k, v in sorted(keywords_frequency.items(), key=lambda item: item[1], reverse=True)}
        
#         # Store sorted keywords and frequencies in Keywords_frequency
#         Keywords_frequency = sorted_frequency

#         # Count images in text
#         image_count = count_images_in_text(url)

#         # Extract headings from URL
#         headings_used = extract_headings(url)

#     insert_data_into_table(url, No_of_words, No_of_sentences, pos_counts, Keywords_frequency, image_count, headings_used)
#     #flash('Data analyzed and inserted successfully!')

#     stored_data = get_all_data_from_table()
#     return render_template("index.html", url=url, cleaned_text=clean_text,
#                            num_words=No_of_words, num_sentences=No_of_sentences,
#                            post_counts=pos_counts, Keywords_frequency=Keywords_frequency,
#                            image_count=image_count, headings_used=headings_used,
#                            stored_data=stored_data)

# # Route for viewing details (requires password)
# @app.route("/stored_data", methods=['GET', 'POST'])
# def stored_data():
#     if request.method == 'POST':
#         if request.form['password'] == ADMIN_PASSWORD:
#             pos_counts={}
#             Keywords_frequency={}
#             image_count = 0
#             headings_used = {}
#             data = get_all_data_from_table()  # Retrieving all stored data from the database
#             return render_template("stored_data.html", data=data, pos_counts=pos_counts,
#                                    Keywords_frequency=Keywords_frequency, image_count=image_count,
#                                    headings_used=headings_used)  # Rendering the stored data page with retrieved data
#         else:
#             flash('Incorrect password!', 'error')  # Flashing an error message if password is incorrect
#             return redirect(url_for('password'))  # Redirecting to password entry page

#     return redirect(url_for('password'))  # Redirecting to password entry page if accessed directly

# # Route for entering the password
# @app.route("/password", methods=['GET', 'POST'])
# def password():
#     return render_template("password.html")  # Rendering the password entry page

# if __name__ == '__main__':
#     app.run(debug=True)

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
