
# Ques 1
The act of choosing, altering, and converting raw data into features that may be utilised in supervised learning is known as feature engineering. To make machine learning operate successfully on new jobs, better features may need to be designed and trained.

Feature engineering in ML is divided into four stages: feature creation, transformations, feature extraction, and feature selection. Feature engineering is the process of producing, transforming, extracting, and selecting features, also known as variables, that are most favourable to the development of an accurate ML algorithm.

# Ques 2
Feature Selection is the process of automatically or manually selecting the features that contribute the most to your prediction variable or output of interest. Irrelevant characteristics in your data might reduce model accuracy and cause your model to train based on irrelevant features.

There are three different kinds of feature selection:

Methods for wrapping (forward, backward, and stepwise selection)
Methods for filtering (ANOVA, Pearson correlation, variance thresholding)
Methods embedded (Lasso, Ridge, Decision Tree).

# Ques 3
The following are the primary distinctions between the filter and wrapper approaches for feature selection: Filter techniques assess the utility of features based on their correlation with the dependent variable, whereas wrapper approaches assess the usefulness of a subset of features by training a model on it.

When using univariate approaches, the filter method has the shortest running time; however, it does not account feature interdependence and tends to each feature independently. The wrapper technique offers the advantages of improved generalisation and robust interaction with the feature selection classifier.





# Ques 4
When creating a predictive model, feature selection is the process of minimising the number of input variables. It is preferable to limit the number of input variables in order to reduce modelling computational costs and, in certain situations, increase model performance.



The primary underlying premise of feature extraction is to reduce raw data to a simplified and comprehensible representation that captures the data's essential qualities or patterns. This procedure entails selecting or developing a collection of informative characteristics capable of efficiently representing the data while removing unnecessary or superfluous information. The idea is to extract characteristics that will help subsequent machine learning or data analysis activities perform better.

Principal Component Analysis (PCA)
Independent Component Analysis 
Recursive Feature Elimination

# ques 5
Text classification is the problem of assigning categories to text data according to its content. The most important part of text classification is feature engineering: the process of creating features for a machine learning model from raw text data.

# Ques 6
Cosine similarity is a statistic that measures how similar papers are regardless of size. The cosine similarity is useful because, even if two comparable documents are separated by the Euclidean distance (because to their size), they may still be orientated closer together.

The cosine of the angle between two n-dimensional vectors in an n-dimensional space called cosine similarity. It is the dot product of the two vectors divided by the product of the lengths (or magnitudes) of the two vectors.



# Ques 7
As a result, the Hamming distance between two vectors is the amount of bits that must be changed to transform one into the other. Example Calculate the distance between vectors 01101010 and 11011011. Because they vary in four locations, the Hamming distance d(01101010,11011011) equals four.

Jaccard Index:
The Jaccard index measures the similarity between two sets by dividing the size of their intersection by the size of their union.
For Feature 1 and Feature 2:
Intersection: {1, 0, 0, 0, 0, 0, 1, 1}
Union: {1, 0, 0, 0, 1, 0, 1, 1}

Jaccard Index = Intersection / Union
= 8 / 8
= 1.0

For Feature 1 and Feature 3:
Intersection: {1, 0, 0, 0, 1, 0, 0, 1}
Union: {1, 1, 0, 0, 1, 0, 1, 1}
Jaccard Index = Intersection / Union
= 8 / 8
= 1.0


# Ques  8
High dimension occurs when the variable number p exceeds the sample size n, i.e. p>n, instances. High-dimensional data is defined as data with n samples and p characteristics, where p is more than n.

Data like as tomographic imaging, ECG, and MEG are examples. Microarray gene expression data is one example of high dimensional data.


# Ques 9
PCA is a technique for identifying a smaller number of uncorrelated variables known as principle components from a larger set of data. The method is commonly used to highlight variance and capture significant patterns in a data collection.

Physical quantities can be represented using vectors. Vectors are most typically employed in physics to describe displacement, velocity, and acceleration. Vectors are arrows that represent a combination of magnitude and direction.

An embedding is a low-dimensional, learnt continuous vector representation of discrete variables into which high-dimensional vectors can be translated in the context of machine learning. In general, embeddings improve the efficiency and usability of ML models and may be utilised with other models as well.

# Ques 10
SFFS (sequential floating forward selection) begins with an empty set. SFFS takes backward steps after each advance step as long as the goal function grows. The sequence of floating backward selection (SFBS) begins with the entire collection.

The Jaccard coefficient is a measure of the proportion of overlap between sets defined as: (5.1), where W1 and W2 are two sets, in our case the ego networks' 1-year intervals. The Jaccard coefficient can range between 0 and 1, with 0 indicating no overlap and 1 representing total overlap.
