import numbers
import sklearn.ensemble as skl_ensemble
import sklearn.preprocessing as skl_preprocessing

from Orange.classification import SklLearner, SklModel

__all__ = ["RandomForestLearner"]


class RandomForestClassifier(SklModel):
    pass


class RandomForestLearner(SklLearner):
    __wraps__ = skl_ensemble.RandomForestClassifier
    __returns__ = RandomForestClassifier

    def __init__(self, n_estimators=10, max_features="auto",
                 random_state=None, max_depth=3, max_leaf_nodes=5,
                 preprocessors=None):
        super().__init__(preprocessors=preprocessors)
        self.params = vars()
