import lux
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/college.csv")
df.intent = ["AverageCost","SATAverage"]
