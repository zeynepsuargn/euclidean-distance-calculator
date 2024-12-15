import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaları içeren liste
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafelerin saklanacağı liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayın
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulun
min_distance = min(distances)

# Sonuçları yazdırın
print("Noktalar:", points)
print("Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
