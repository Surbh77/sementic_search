import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# A list to store data (simulate a database)
data = []

@app.route('/api/resource', methods=['POST'])
def create_resource():
    try:
        def calculate_similarity(sentence1, sentence2):
            # Tokenize the sentences
            words = set(word_tokenize(sentence1) + word_tokenize(sentence2))

            # Create TF-IDF vectors for the sentences
            tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
            tfidf_matrix = tfidf_vectorizer.fit_transform([sentence1, sentence2])

            # Calculate the cosine similarity between the TF-IDF vectors
            similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

            return similarity[0][0]

        # Iterate through your DataFrame and calculate similarity
        
        request_data = request.get_json()

        # print(request.get_json())
        if 'text1' in request_data and 'text2' in request_data:
            text1 = request_data['text1']
            text2 = request_data['text2']
            # for index, row in df.iterrows():
            #     sentence1 = row['text1']
            #     sentence2 = row['text2']
            similarity = calculate_similarity(text1, text2)
                # similarities.append(similarity)

        return jsonify({"similarity score": round(similarity,2)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
