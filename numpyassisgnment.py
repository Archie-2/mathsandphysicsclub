import time
import numpy as np
import matplotlib.pyplot as plt

### Function Definitions ###

# Load data from file
def load_data(data_path):
    """
    Load data from a file into a NumPy array.
    Assumes the file contains rows of x, y coordinates separated by a comma.
    """
    return np.loadtxt(data_path, delimiter=',')

# Initialize centers
def initialise_centers(data, K, init_centers=None):
    """
    Initialize cluster centers. If no initial centers are provided,
    select K random points from the data as initial centers.
    """
    if init_centers is None:
        return data[np.random.choice(data.shape[0], K, replace=False)]
    return init_centers

# Initialize labels
def initialise_labels(data):
    """
    Initialize labels for each data point. Defaults to a 1D array of ones.
    """
    return np.ones(data.shape[0], dtype=int)

# Calculate distances from data points to centers
def calculate_distances(data, centers):
    """
    Compute the Euclidean distance from each data point to all cluster centers.
    """
    return np.linalg.norm(data[:, np.newaxis, :] - centers, axis=2)

# Update labels based on nearest center
def update_labels(distances):
    """
    Assign each data point to the nearest cluster center based on distances.
    """
    return np.argmin(distances, axis=1)

# Update centers based on the mean of assigned points
def update_centers(data, labels, K):
    """
    Compute new cluster centers as the mean of all data points assigned to each cluster.
    """
    return np.array([data[labels == k].mean(axis=0) if np.any(labels == k) else np.zeros(data.shape[1]) for k in range(K)])

# Check if labels have changed
def check_termination(labels1, labels2):
    """
    Check if the labels have converged (i.e., no changes between iterations).
    """
    return np.array_equal(labels1, labels2)

# K-means clustering
def kmeans(data_path, K, init_centers=None):
    """
    Perform K-means clustering on the given dataset.
    """
    data = load_data(data_path)  # Load data
    centers = initialise_centers(data, K, init_centers)  # Initialize centers
    labels = initialise_labels(data)  # Initialize labels

    start_time = time.time()  # Start timing

    while True:
        distances = calculate_distances(data, centers)  # Compute distances
        labels_new = update_labels(distances)  # Assign labels
        centers = update_centers(data, labels_new, K)  # Update centers

        if check_termination(labels, labels_new):  # Check convergence
            break
        else:
            labels = labels_new

    end_time = time.time()  # End timing

    return centers, labels, end_time - start_time  # Return results

# Visualization
def visualise(data_path, labels, centers):
    """
    Visualize the clustering result.
    """
    data = load_data(data_path)  # Load data
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')  # Data points
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)  # Centers
    plt.title('K-means clustering')  # Plot title
    plt.xlabel('Longitude')  # X-axis label
    plt.ylabel('Latitude')  # Y-axis label
    plt.savefig('kmeans.png')  # Save the plot
    plt.show()  # Display the plot

    return plt

### Main Execution ###

if __name__ == "__main__":
    # Specify the data file path
    data_path = "C:\\Users\\dircr\\Downloads\\spice_locations.txt"
    # Specify the number of clusters
    K = 2
    # Set initial centers (optional)
    init_centers = None

    # Perform K-means clustering
    centers, labels, time_taken = kmeans(data_path, K, init_centers)

    # Output results
    print('Final centers:\n', centers)
    print('Time taken for the algorithm to converge:', time_taken)

    # Visualize results
    visualise(data_path, labels, centers)
