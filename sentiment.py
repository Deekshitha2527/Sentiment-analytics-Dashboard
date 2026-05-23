from textblob import TextBlob

def get_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        return "Positive", polarity

    elif polarity < -0.2:
        return "Negative", polarity

    else:
        return "Neutral", polarity