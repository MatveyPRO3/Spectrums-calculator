import plotly.express as px

x, y = [], []
with open("result.txt", "r") as file:
    for i in file.readlines():
        x.append(i.split("|")[1])
        y.append(i.split("|")[-1])

fig = px.scatter(x=x, y=y)
fig.show()
