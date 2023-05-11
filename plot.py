import plotly.express as px

x, y = [], []
with open(input("Enter result.txt path"), "r") as file:
    for i in file.readlines():
        print(i)
        x.append(float(i.split("|")[1]))
        y.append(float(i.split("|")[-1]))

fig = px.scatter(x=x, y=y)
fig.show()
