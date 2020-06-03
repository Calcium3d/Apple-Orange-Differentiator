from sklearn import tree
# the first number is the weight and second one is whether it is rough or not. 0 is smooth and 1 is rough
features = [[140, 0], [130, 0], [150, 1], [170, 1]]
# 0 are apples and 1 are oranges
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[135, 0]]))