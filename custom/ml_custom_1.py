import random
import math

def generate_data(dimensions=2, num_clusters=3, num_points_per_cluster=50, centers=None, spread=0.8):
    """
    Generate clustered data.
    
    Parameters:
    - dimensions: The number of dimensions for each data point.
    - num_clusters: The number of clusters to generate.
    - num_points_per_cluster: The number of points to generate for each cluster.
    - centers: List of center coordinates for each cluster. If not provided, random centers will be chosen.
    - spread: Standard deviation for the Gaussian distribution around each cluster center.
    
    Returns:
    List of data points with the specified number of dimensions.
    """
    if centers is None:
        # Generate random centers if not provided
        centers = [[random.randint(1, 6) for _ in range(dimensions)] for _ in range(num_clusters)]
    elif len(centers) != num_clusters:
        raise ValueError("The number of provided centers does not match the number of clusters.")
    
    data = []
    
    for center in centers:
        cluster_data = [
            [random.gauss(center[dim], spread) for dim in range(dimensions)] 
            for _ in range(num_points_per_cluster)
        ]
        data.extend(cluster_data)

    return data

def compute_silhouette_score(data, labels):
    """Compute the silhouette score. Higher is better.
    
    The silhouette score is calculated for each data point, then averaged over all points.
    For each data point:
      a = average distance to other points in the same cluster
      b = minimum average distance to points in a different cluster
    silhouette = (b - a) / max(a, b)
    """
    silhouettes = []
    for i, x in enumerate(data):
        same_cluster = [data[j] for j, label in enumerate(labels) if label == labels[i] and j != i]
        other_cluster = [data[j] for j, label in enumerate(labels) if label != labels[i]]
        
        if not same_cluster or not other_cluster:
            continue

        a = sum(math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2) for y in same_cluster) / len(same_cluster)
        b = min(sum(math.sqrt((x[0]-z[0])**2 + (x[1]-z[1])**2) for z in other_cluster) / len(other_cluster) for label in set(labels) if label != labels[i])
        
        silhouettes.append((b - a) / max(a, b))
    return sum(silhouettes) / len(silhouettes) if silhouettes else 0


def euclidean_distance(point1, point2):
    """Euclidean distance between two equal length lists of numbers"""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


class Cluster:
    def __init__(self, centroid):
        self.centroid = centroid
        self.data_points = []

class ClusteringAlgorithm:
    def __init__(self, max_clusters=3, max_iterations=100):
        self.max_clusters = max_clusters
        self.max_iterations = max_iterations
        
        self.clusters = []

    def fit(self, data):
        # Initialize clusters with random centroids
        for _ in range(self.max_clusters):
            centroid = random.choice(data)
            cluster = Cluster(centroid)
            self.clusters.append(cluster)
            
        for _ in range(self.max_iterations):
            # Initialize clusters for each iteration
            clusters = [Cluster(cluster.centroid) for cluster in self.clusters]
            
            # Assign each data point to the closest cluster
            for point in data:
                distances = [euclidean_distance(point, cluster.centroid) for cluster in self.clusters]
                closest_cluster_index = distances.index(min(distances))
                clusters[closest_cluster_index].data_points.append(point)
            
            # Update cluster centroid
            for i in range(self.max_clusters):
                if clusters[i].data_points:
                    new_centroid = [sum(dim)/len(clusters[i].data_points) for dim in zip(*clusters[i].data_points)]
                    clusters[i].centroid = new_centroid
                    
            self.clusters = clusters         

    # predict --> labels
    def predict(self, data):
        label_predicted = []
        for point in data:
            distances = [euclidean_distance(point, cluster.centroid) for cluster in self.clusters]
            closest_cluster_index = distances.index(min(distances))
            label_predicted.append(closest_cluster_index)
        
        return label_predicted

if __name__ == "__main__":
    data = generate_data(
        dimensions=3, 
        num_clusters=3, 
        num_points_per_cluster=100, 
        centers=[[-2.0, -2.0, 1.0], [2.0, 2.0, 1.0], [0, -2.0, 2.0]]
    )
    
    model = ClusteringAlgorithm(max_clusters=3, max_iterations=20)
    model.fit(data)
    labels_predicted = model.predict(data)

    # Validation
    silhouette_threshold = 0.6
    score = compute_silhouette_score(data, labels_predicted)
    assert score > silhouette_threshold, f"Silhouette score below threshold of {silhouette_threshold}! Score: {score:.3f}"
    print(f"Test Passed with score {score}!")
