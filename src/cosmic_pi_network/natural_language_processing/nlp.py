import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLP:
    def __init__(self):
        pass

    def tokenize_text(self, text):
        tokens = word_tokenize(text)
        return tokens

    def remove_stopwords(self, tokens):
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return filtered_tokens

    def lemmatize_tokens(self, tokens):
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized_tokens

    def sentiment_analysis(self, text):
        from nltk.sentiment import SentimentIntensityAnalyzer
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        return sentiment

# Example usage
nlp = NLP()
text = "This is a sample text."
tokens = nlp.tokenize_text(text)
filtered_tokens = nlp.remove_stopwords(tokens)
lemmatized_tokens = nlp.lemmatize_tokens(filtered_tokens)
sentiment = nlp.sentiment_analysis(text)
print("Sentiment:", sentiment)
