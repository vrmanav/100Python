import pandas as pd

data = pd.read_csv("./squirrel_data.csv")


gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])


squirrel_dict = {
    "Fur Color": [
        "Gray",
        "Cinnamon",
        "Black",
    ],
    "Count": [
        gray_count,
        cinnamon_count,
        black_count,
    ],
}

df = pd.DataFrame(squirrel_dict)
df.to_csv("./formatted_data.csv")
