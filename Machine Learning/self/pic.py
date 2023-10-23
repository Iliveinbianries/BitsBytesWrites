import pickle

file = open('svm', 'rb')
data = pickle.load(file)
print(data)
