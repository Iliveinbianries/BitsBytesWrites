# What is Machine Unlearning?

Machine unlearning is the task of updating machine learning (ML) models after partial deletion of training data on which the model had been trained, so that the model reflects the remaining data. Its need arises in many database applications that train their data on ML models while allowing data deletions. 

# Importance of Machine Unlearning

Let's take an online store for example. The store maintains a database of customer data & their ratings of products to train a model that could predict customer preferences. Suppose some users request their accounts to be deleted from the database, then how should ML model unlearn the deleted data? One possible way is to retrain ML model on the remaining data from scratch. But this approach is expensive in terms of both computational power and time consumption. Is it possible to remove all influence of a subset of training data when it's requested to delete it, but avoid the full cost of retraining from scratch? Many machine unlearning methodologies have been proposed to make this possible. Some of them are:

## Machine Unlearning methods for linear models - 

Several unlearning methods have been proposed for various linear ML models. Fisher unlearning & Influence unlearning have proven good results in terms of efficiency & accuracy for logistic regression models.

### 1. Fisher Unlearning

Fisher unlearning method updates the model using remaining data to perform corrective Newton step i.e. uses Newton step to unlearn deleted data.

### 2. Influence Unlearning

Influence Unlearning method computes the influence of deleted data on the parameters of trained ML model & then updates parameters to remove that influence. 

## Federated Unlearning -

Federated learning enables numerous computers or servers to jointly train a model without sharing data, so that privacy individual data sources is not compromised. Federated unlearning enables individual devices or servers to selectively remove specific data or features from their local models, while still contributing to the overall
federated model.

### 1. Class Unlearning

To eliminate particular classes or categories of data from a machine learning model, the approach of class unlearning is used in federated unlearning. The majority of the time, this process is carried out locally, with each client or device being in charge of determining and deleting the pertinent classes of data from their local models. After that,the locally modified models are transmitted to the main server, where they are combined to produce a new global model without the deleted classes.

### 2. Client Unlearning

Client unlearning often entails determining which client-specific information or parameters need to be altered or eliminated, and then updating the local models to take these changes into account.

# Challenges

One of the challenges of machine unlearning is that it can be difficult to determine which data to unlearn and how much to unlearn. It is also important to ensure that unlearning does not negatively affect the model’s performance or introduce new biases. In addition, unlearning can be computationally expensive, particularly for large models or
datasets.