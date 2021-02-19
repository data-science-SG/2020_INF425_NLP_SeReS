def plot_conf_mat(y_test, y_preds, norm="false"):
    """ Plot a visual confusion matrix with the respective values (normalized or don't)

    Keywords arguments:
    y_test -- test labels
    y_preds -- prevision labels
    norm -- normalize confusion matrix (default false)
    """
    fig, ax = plt.subplots(figsize=(3, 3))
    ax = sns.heatmap(confusion_matrix(y_test, y_preds, normalize=norm),
                    annot=True,
                    cbar=False)
    plt.xlabel("True label")
    plt.ylabel("Predicted label")