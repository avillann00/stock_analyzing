# import required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import io

# plot the data
def plot_data(df):
    # check to make sure its not empty
    if df.empty:
        return None

    head = df.head()

    # set the style
    sns.set(style="whitegrid")

    # create a figure and axes
    fig, ax = plt.subplots(1, 2, figsize=(14, 7))

    # plot the day change
    sns.barplot(x='Ticker', y='Percent Day Change', data=head, ax=ax[0])
    ax[0].set_title('Percent Day Change for Each Ticker')
    ax[0].set_ylabel('Percent Day Change')
    ax[0].set_xlabel('Ticker')
    ax[0].tick_params(axis='x', rotation=45)

    # plot the month change
    sns.barplot(x='Ticker', y='Percent Month Change', data=head, ax=ax[1])
    ax[1].set_title('Percent Month Change for Each Ticker')
    ax[1].set_ylabel('Percent Month Change')
    ax[1].set_xlabel('Ticker')
    ax[1].tick_params(axis='x', rotation=45)

    # adjust layout
    plt.tight_layout()

    # turn it into a .png file
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # return the graph
    return buf
