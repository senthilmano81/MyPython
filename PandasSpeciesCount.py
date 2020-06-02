import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

print(df.head())
print(df.shape)

keys = df['Species'].value_counts().keys().tolist()
count = df['Species'].value_counts().tolist()
print(keys)
print(count)
