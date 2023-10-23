import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('HR_comma_sep.csv')
dum1 = pd.get_dummies(df['sales'])
dum2 = pd.get_dummies(df['salary'])

dum1.drop('IT', axis="columns", inplace=True)
dum2.drop('medium', axis="columns", inplace=True)

df_new = pd.concat([df, dum1, dum2], axis="columns")
df_new.drop(['sales', 'salary'], axis="columns", inplace=True)

x_train, x_test, y_train, y_test = train_test_split(df_new.drop('high', axis="columns"),
                                                    df_new['high'], test_size=0.25)

clf = LogisticRegression()
clf.fit(x_train, y_train)
print(clf.predict(x_test))
print(clf.score(x_test, y_test))
