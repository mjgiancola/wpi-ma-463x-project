from data_utils import *
from my_pca import *
from my_lasso import *
from sklearn.model_selection import KFold, cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def best_lda():
    #TODO find best LDA using data
    pass

def getScores_pca(X, Y, num_pred_list, num_cv_folds):
    kfold = KFold(n_splits=num_cv_folds)
    
    scores = []
    for p in num_pred_list:
        print("Evaluating LDA with predictors=%2d" % p)
        my_LDA = LinearDiscriminantAnalysis()
        my_LDA.fit(my_pca(X, p), Y)
	scores.append(cross_val_score(my_LDA, X, Y, cv = kfold).mean())

    return scores

def getScores_lasso(X, Y, alpha_list, num_cv_folds):
    kfold = KFold(n_splits=num_cv_folds)
    
    scores = []
    for a in alpha_list:
        print("Evaluating LDA with alpha=%2d" % a)
        my_LDA = LinearDiscriminantAnalysis()
        my_LDA.fit(my_lasso(X, Y, a), Y)
	scores.append(cross_val_score(my_LDA, X, Y, cv = kfold).mean())

    return scores

if __name__ == '__main__':

    X, Y = get_training()

    num_pred_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 30]
    alpha_list = [.125, .25, .375, .5, .625, .75, .875, 1]

    ten_scores_pca = getScores_pca(X, Y, num_pred_list, 10)
    loocv_scores_pca = getScores_pca(X, Y, num_pred_list, len(X))
    ten_scores_lasso = getScores_lasso(X, Y, alpha_list, 10)
    loocv_scores_lasso = getScores_lasso(X, Y, alpha_list, len(X))

    print("_______________________PCA__________________________________")
    for i in range(len(num_pred_list)):
	p = num_pred_list[i]
	acc1 = ten_scores_pca[i]
	acc2 = loocv_scores_pca[i]
	print("| predictors = %2d | 10-Fold Accuracy: %.3f | LOOCV Accuracy: %.3f |" % (p, acc1, acc2))
    print("____________________________________________________________")

    print("_______________________Lasso________________________________")
    for i in range(len(alpha_list)):
	a = alpha_list[i]
	acc1 = ten_scores_lasso[i]
	acc2 = loocv_scores_lasso[i]
	print("| predictors = %2d | 10-Fold Accuracy: %.3f | LOOCV Accuracy: %.3f |" % (a, acc1, acc2))
    print("____________________________________________________________")
    # TODO Generate graphs of num_pred vs. accuracy


"""
output:
    ____________________________________________________________
    | predictors =  3 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors =  5 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors =  7 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors =  9 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 11 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 13 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 15 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 17 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 19 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 21 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    | predictors = 30 | 10-Fold Accuracy: 0.964 | LOOCV Accuracy: 0.960 |
    ____________________________________________________________
"""
