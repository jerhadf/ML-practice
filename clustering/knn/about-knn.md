# K nearest neighbors (KNN)

## Overview
* **Simple Algorithm**: KNN is a straightforward ML algorithm for classification & regression. The intuition: examples are classified based on the class of their nearest neighbours - *k* nearest neighbours are used in determining the class.
**Example-based**: It doesn't build a model but memorizes the training dataset.
**Neighbor Voting**: When a new point needs classification, KNN looks at the '*k*' closest points (neighbors) in the training dataset and assigns the most frequent class among these neighbors to the new point.

## Pseudocode

```python
1. Load the training and test datasets.
2. Choose the value of k.
    2.1 k is the number of nearest neighbors to consider. It can be any positive integer.
    2.2 The choice of k depends on the data; generally, larger values of k reduce noise, but create boundaries that are less distinct.
3. Initialize an empty list to store the predictions for the test dataset.
4. For each point in the test dataset, do the following:
    4.1 Initialize an empty list to store the distances to the training points.
    4.2 For each point in the training dataset:
        4.2.1 Calculate the distance between the test point and the current training point. This can be done using various methods like Euclidean distance, Manhattan distance, etc.
        4.2.2 Add the calculated distance and the class of the training point to the distances list as a tuple.
    4.3 Sort the distances list in ascending order based on the distance.
    4.4 Select the first k entries from the sorted distances list.
    4.5 Get the classes of the k entries and find the most frequent class. In case of a tie, one class is randomly selected.
    4.6 Add the most frequent class to the predictions list.
5. **End.** The predictions list now contains the predicted class for each point in the test dataset.
```

## Sources or further reading
* [K-Nearest Neighbour Classifiers - A Tutorial](https://dl.acm.org/doi/10.1145/3459665)
