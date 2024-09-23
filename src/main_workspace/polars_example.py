from lib import calculate2

# shows lib calc2 function and saves a scatter plot using polars
if __name__ == "__main__":
    stats = calculate2(
        "src/main_workspace/data/hw1_q3_test_data.csv",
        "src/main_workspace/outputs/polars_",
    )
    print(stats)
