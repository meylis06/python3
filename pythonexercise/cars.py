cars=("Lamborghini", "Ferrari", "Porsche", "Bugatti", "BMW")
X= list(cars)
X.append("Mercedes")
cars= tuple(X)
print(cars)
X.pop(0)
cars= tuple(X)
print(cars)