def plot_loss_and_accuracy(losses, accs):
    """ Plot a visual graph showing the evolution of both, loss and accuracy, relating to the epochs
        
    Keywords arguments:
    losses -- losses of the model
    accs -- accuracy of the model
    """
  fig, ax_tuple = plt.subplots(1, 2, figsize=(16,6))
  fig.suptitle('Loss and accuracy')

  for i, (y_label, y_values) in enumerate(zip(['BCE loss','Accuracy'],[losses, accs])):
    ax_tuple[i].plot(range(len(y_values)),  y_values, label='train')
    ax_tuple[i].set_xlabel('epochs')
    ax_tuple[i].set_ylabel(y_label)
    ax_tuple[i].legend()