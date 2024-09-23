import pandas as pd
import matplotlib.pyplot as plt
import polars as pl


def calculate(file_path, path_of_image=None):
    """returns list of tuples for mean, std, and median of mushroom data"""
    raw_training = pd.read_csv(file_path)
    df_train_x = raw_training.iloc[:, :-1]
    mean = ("mean\n", df_train_x[["stem-height", "stem-width"]].mean())
    median = ("median\n", df_train_x[["stem-height", "stem-width"]].median())
    std = ("std\n", df_train_x[["stem-height", "stem-width"]].std())
    df_train_x.plot.scatter("stem-width", "stem-height")
    if path_of_image:
        plt.savefig(path_of_image + "scatter_plot.png")
        plt.close(path_of_image + "scatter_plot.png")
    return [mean, median, std]


def calculate2(file_path, path_of_image=None):
    """returns a dict with mean, std, and median of mushroom data"""
    # Read CSV file using Polars
    raw_training = pl.read_csv(file_path)
    # Select all columns except the last one
    df_train_x = raw_training.select(pl.exclude("class"))
    df_train_select = df_train_x.select("stem-height", "stem-width")
    # Calculate mean, median, and standard deviation
    stats = {}
    stats["mean"] = df_train_select.mean()
    stats["median"] = df_train_select.median()
    stats["std"] = df_train_select.std()
    # Create scatter plot
    plt.figure()
    plt.scatter(df_train_select["stem-width"], df_train_select["stem-height"])
    plt.xlabel("stem-width")
    plt.ylabel("stem-height")

    if path_of_image:
        plt.savefig(path_of_image + "scatter_plot.png")
        plt.close()

    return stats
