import cv2
#C:\Users\신재현\EpitechSummerTeamProject
# python code to see which z cluster each pixel belongs to
from sklearn.cluster import KMeans


class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def dominantColors(self):
        # static method
        # read image
        print(self.IMAGE)
        img = cv2.imread(self.IMAGE)
        # convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        # save image after operations
        self.IMAGE = img
        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)
        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
 #hexadecimal
        # save labels
        self.LABELS = kmeans.labels_

        # returning after converting to integer from float
        return self.COLORS.astype(int)


