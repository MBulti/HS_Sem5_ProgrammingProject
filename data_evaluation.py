import time
import json
import numpy as np

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from statistics import mean
from functions.data_output import get_list_of_recommendation

__all__ = ["get_list_of_recommendation"]
start_time = time.time()

# Code taken from M.Harms with some minor adjustments


def get_calculation_base(raw_true, raw_pred):
    boolean_true = []
    boolean_pred = []
    for i in range(17770):
        boolean_true.append(False)
        boolean_pred.append(False)
    for i in raw_true:
        boolean_true[i-1] = True
    for i in raw_pred:
        boolean_pred[int(i-1)] = True
    return boolean_true, boolean_pred


def get_mean_precision_recall():
    with open('data/testset.json') as f:

        json_data = json.load(f)
        precision_total = []
        recall_total = []
        counter = 0
        json_data_length = len(json_data)
        for i in json_data:
            print('{0} done of {1}'.format(counter, json_data_length))
            counter += 1
            created_recommendations = get_list_of_recommendation(
                i['Prediction_Base'])
            raw_pred = []
            for movie_recommendation in created_recommendations:
                raw_pred = np.append(
                    raw_pred, movie_recommendation.recommendations)

            raw_true = i['Raw_true']

            boolean_true, boolean_pred = get_calculation_base(
                raw_true, raw_pred)
            precision = precision_score(
                y_true=boolean_true, y_pred=boolean_pred)
            recall = recall_score(y_true=boolean_true, y_pred=boolean_pred)
            precision_total = np.append(precision_total, precision)
            recall_total = np.append(recall_total, recall)

        return mean(precision_total), mean(recall_total)


mean_precision, mean_recall = get_mean_precision_recall()
print(mean_precision)
print(mean_recall)

# precision 0,23458
# recall    0,11043

print('Runtime: {:5.3f}s'.format(time.time()-start_time))
