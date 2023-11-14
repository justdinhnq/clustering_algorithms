# Types of clustering algorithms
When choosing a clustering algorithm, it's crucial to consider whether the algorithm scales to the target dataset and the desired characteristics of the clusters. An algorithm that scales linearly with the size of the target dataset would have its runtime decrease as compared with an algorithm that scales quadratically with the number of examples. Let's denote $n$ as the number of examples, $O(n)$ as the complexity of the linear-scaling algorithm, and $O(n^2)$ as the complexity of the quadratic-scaling algorithm. $O(n^2)$ algorithms are not practical and less effective than $O(n)$ algorithms when the number of examples are in millions. The desired characteristics for forming clusters vary across different categories of clustering techniques. Generally, they convey assumptions about the structure, distribution, and organization of the data, guiding the choice of clustering technique based on the dataset's expected properties.

Clustering techniques are basically categorized into four groups: centroid, density, distribution, and hierarchy.

## 1. Centroid-based Clustering
<p align="center">
<img src="https://developers.google.com/static/machine-learning/clustering/images/CentroidBasedClustering.svg" width="300" height="300">
</p>

**Concept**:

This method identifies clusters by finding the center point, or centroid, of a group of data points. Clusters are formed based on the proximity of data points to the centroid, and each point is assigned to the cluster with the nearest centroid.

**When to apply**:

If you expect the clusters to be compact, well-defined around a central point, and roughly spherical in shape, centroid-based clustering like K-means might be a suitable choice.

**Desired Characteristics**:

- Compactness: The clusters are expected to be tight and well-defined around a central point (centroid)
- Similar Cluster Size: Ideally, clusters should have similar sizes
- Spherical Shape: Centroid-based methods often assume clusters to be spherical, which influences the desired shape of the clusters.

**Pros and Cons**:

Centroid-based algorithms are efficient, effective, and simple but sensitive to initial conditions and outliers. They are efficient because these algorithms can process and cluster data relatively quickly. They are effective because they produce meaningful and accurate clustering results. They are simple because they don't involve complex calculations or intricate procedures. That makes them easy to understand, implement, and use. Centroid-based clustering, such as K-means, has its strengths and weaknesses.

Pros:
- Simplicity and Speed: These methods are computationally efficient and easy to implement, making them suitable for large datasets.
- Scalability: They often perform well on high-dimensional data and can scale to a large number of data points.
- Convergence: The algorithm usually converges quickly to a solution, providing a relatively fast clustering process.
- Well-suited for Balanced Clusters: They work well when clusters are spherical and of similar size.
  
Cons:
- Sensitivity to Initialization: K-means, in particular, is sensitive to the initial placement of centroids, which can result in different clusters.
- Assumes Circular Clusters: K-means assumes that clusters are spherical and equally sized, which may not reflect the true nature of all datasets.
- Outliers Impact Results: The presence of outliers can significantly affect the centroid positions and, consequently, the clustering results.
- Fixed Number of Clusters: The user must specify the number of clusters beforehand, which might not be known in real-world scenarios.

**Conclusion**:

In summary, centroid-based clustering is a powerful and efficient approach, especially for well-behaved datasets. However, it may struggle with more complex data structures and is sensitive to certain parameters and assumptions

## 2. Density-based Clustering
<p align="center">
<img src="https://developers.google.com/static/machine-learning/clustering/images/DensityClustering.svg" width="300" height="300">
</p>

**Concept**:

Density-based clustering focuses on regions of high data density, allowing for the identification of clusters with arbitrary shapes. Clusters are formed where there is a sufficient density of data points, and regions with lower density are considered noise or outliers.

**When to apply**:

If you anticipate clusters with arbitrary shapes, varying levels of density, and robustness to noise, density-based methods like DBSCAN could be more appropriate.

**Desired Characteristics**:

- Adaptability to Shape: Clusters can take on arbitrary shapes rather than being confined to predefined forms.
- Robustness to Noise: Density-based methods are designed to handle noise and outliers gracefully, focusing on regions of high data density.
- Variable Cluster Density: Ability to identify clusters with varying levels of density (dense and sparse regions) within the dataset.

**Pros and Cons**:

Pros:

- Adaptability to Cluster Shapes: Density-based methods can identify clusters of arbitrary shapes, making them suitable for complex data structures.
- Robust to Noise: These algorithms are less sensitive to noise and outliers, as they focus on regions of high data density.
- Automatic Cluster Detection: DBSCAN can automatically determine the number of clusters based on the density of the data, eliminating the need for users to pre-specify the cluster count.
- Handles Varying Cluster Densities: Density-based clustering can accommodate clusters with varying densities, making it effective in datasets with unevenly distributed data points.
  
Cons:

- Difficulty with Varying Density Levels: While density-based methods can handle varying densities, they may struggle when clusters have significantly different density levels.
- Sensitive to Parameter Settings: The performance of density-based algorithms can be influenced by the choice of parameters, such as the radius and minimum points required to form a cluster.
- Memory and Computational Requirements: Some density-based algorithms may be computationally expensive and memory-intensive, particularly in high-dimensional or large datasets.
- Not Suitable for Spherical Clusters: They may not perform well on datasets with well-defined spherical clusters, as it is designed to identify clusters of arbitrary shapes.

**Conclusion**:

In summary, density-based clustering is a valuable approach for certain types of datasets, particularly those with complex shapes and varying cluster densities. However, users need to be mindful of parameter tuning and potential computational requirements.


## 3. Distribution-based Clustering
<p align="center">
<img src="https://developers.google.com/static/machine-learning/clustering/images/DistributionClustering.svg" width="300" height="300">
</p>

**Concept**:

Distribution-based clustering, also known as model-based clustering, assumes that the data points are generated from a mixture of probability distributions. Clusters are formed based on the probability distribution models and data points are assigned to the cluster with the highest probability.

**When to apply**:

If the data is expected to follow a specific statistical distribution, and you want to model clusters as probability distributions, distribution-based methods might be suitable. 

**Desired Characteristics**:

- Statistical Significance: Assumes that the data follows a particular statistical distribution, and clusters are formed based on deviations from this distribution.
- Probabilistic Representation: Models clusters as the probability distributions, indicating a probabilistic view of the data
- Variable Cluster Shapes: Can accommodate clusters with different shapes based on the underlying distribution of the data.

**Pros and Cons**:

Pros:

- Flexibility in Cluster Shapes: Distribution-based clustering allows for flexibility in defining cluster shapes. It can accommodate clusters with different shapes and sizes, making it suitable for datasets with complex patterns.
- Probabilistic Assignment: It provides probabilistic assignments of data points to clusters based on the underlying distribution models, offering a measure of uncertainty in cluster assignments.
- Handles Overlapping Clusters: Distribution-based methods can handle overlapping clusters by modeling the mixture of distributions, and capturing areas of data overlap.
- Well-suited for Complex Distributions: Effective for datasets with intricate distribution patterns, as it can model complex probability distributions
  
Cons:

- Sensitive to Model Assumptions: Performance is highly dependent on the correctness of the assumed distribution models. If the data does not conform to the chosen distributions, the results may be inaccurate.
- Computational Complexity: Fitting complex distribution models to large datasets can be computationally expensive, especially in high-dimensional spaces.
- Difficulty in Model Selection: Choosing the appropriate number of clusters and the right distribution model can be challenging and may require domain knowledge or trial-and-error.
- Prone to Initialization Issues: Like other clustering methods, distribution-based clustering can be sensitive to initial parameter values, affecting the stability of the results.

**Conclusion**:

In summary, distribution-based clustering offers flexibility in handling various cluster shapes and is effective for datasets with complex distribution patterns. However, it requires careful consideration of model assumptions, and parameter tuning, and can be computationally demanding.

## 4. Hierarchical Clustering
<p align="center">
<img src="https://developers.google.com/static/machine-learning/clustering/images/HierarchicalClustering.svg" width="500" height="500">
</p>

**Concept**:



**When to apply**:

If you suspect a hierarchical organization in your data, where clusters have nested relationships and exist at different scales, hierarchy-based methods like agglomerative clustering could be beneficial.

**Desired Characteristics**:

- Nested Structure: Implies that the dataset has a hierarchical organization, where clusters can be grouped into larger structures and exhibit nested relationships.
- Flexibility in Scale: Suggests that clusters may exist at various scales within the dataset.
- Visual Representation: Provides a visual representation of the relationships between clusters, indicating a need for a comprehensive understanding of the dataset's structure

**Pros and Cons**:


Pros:

  
Cons:


**Conclusion**:



Note: Source of images from [google](https://developers.google.com/machine-learning/clustering/clustering-algorithms)
