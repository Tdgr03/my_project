import csv

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# CSV dosyasını oku ve noktaları oluştur
points = []
with open("coordinates.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Başlık satırını atla
    for row in reader:
        x, y = map(int, row)
        points.append(Point(x, y))

print("Okunan noktalar:", points)
