import math

def euclideanDistance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: Birinci nokta (x1, y1) şeklinde bir demet.
    point2: İkinci nokta (x2, y2) şeklinde bir demet.

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]  # Örnek noktalar listesi

distances = []
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

min_distance = min(distances)

print("Noktalar:", points)
print("Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)