from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC

X, y = make_classification(n_samples=50, n_features=2, n_informative=2,
                           n_clusters_per_class=1, random_state=0)

lin_svm = SVC(kernel='linear', C=10).fit(X, y)
lin_svm.decision_function([[1, 0]])
