import pandas as pd
import csv
from sklearn.feature_extraction.text import CountVectorizer
filepath_dict = {'positive': "data/sentiment_analysis/positive.txt",
                 'negative': "data/sentiment_analysis/negative.txt",
}


# filepath_dict = {'yelp':   'data/sentiment_analysis/yelp_labelled.txt',
#                  'amazon': 'data/sentiment_analysis/amazon_cells_labelled.txt',
#                  'imdb':   'data/sentiment_analysis/imdb_labelled.txt'
#                  }
df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
print(df.iloc[0])

sentences = ['Today is the absolute worst day', 'Today is the greatest day ever.']

# with open('positive.csv', newline='') as f:
#     reader = csv.reader(f)
#     positiveList = list(reader)
# with open('negative.csv', newline='') as f:
#     reader = csv.reader(f)
#     negativeList = list(reader)
# from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences)
#print(vectorizer.vocabulary_)
print(vectorizer.transform(sentences).toarray())
from sklearn.model_selection import train_test_split

df_yelp = df[df['source'] == 'positive']

sentences = df_yelp['sentence'].values
y = df_yelp['label'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
print(X_train)
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)

print("Accuracy:", score)
for source in df['source'].unique():
    df_source = df[df['source'] == source]
    sentences = df_source['sentence'].values
    y = df_source['label'].values

    sentences_train, sentences_test, y_train, y_test = train_test_split(
        sentences, y, test_size=0.25, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(sentences_train)
    X_train = vectorizer.transform(sentences_train)
    X_test  = vectorizer.transform(sentences_test)

    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    score = classifier.score(X_test, y_test)
    print('Accuracy for {} data: {:.4f}'.format(source, score))
from keras.models import Sequential
from keras import layers

input_dim = X_train.shape[1]  # Number of features

model = Sequential()
model.add(layers.Dense(10, input_dim=input_dim, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))