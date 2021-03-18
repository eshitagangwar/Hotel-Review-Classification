# Hotel-Review-Classification
# Overview
In this assignment we will write a  classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative. We will be using the word tokens as features for classification.

# Data
A set of training and development data is available as a compressed ZIP archive on Blackboard. The uncompressed archive contains the following files:

A top-level directory with two sub-directories, one for positive reviews and another for negative reviews (plus license and readme files which you won’t need for the exercise).

Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews.

Each of these subdirectories contains four subdirectories, called “folds”.

Each of the folds contains 80 text files with English text (one review per file).

The submission script will train your model on part of the training data, and report results on the remainder of the training data (reserved as development data; see below). The grading script will train your model on all of the training data, and test the model on unseen data in a similar format. The directory structure and file names of the test data will be masked so that they do not reveal the labels of the individual test files.
