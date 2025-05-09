import struct
from array import array

def read_idx_images(filename):
    with open(filename, 'rb') as f:
        magic, num_images, rows, cols = struct.unpack(">IIII", f.read(16))
        assert magic == 2051, "Invalid image file magic number"
        image_data = array("B", f.read())  # Read as unsigned bytes
        images = []
        for i in range(num_images):
            start = i * rows * cols
            end = start + rows * cols
            img = [image_data[start + j] for j in range(rows * cols)]
            img_2d = [img[j * cols:(j + 1) * cols] for j in range(rows)]
            images.append(img_2d)
        return images

def read_idx_labels(filename):
    with open(filename, 'rb') as f:
        magic, num_labels = struct.unpack(">II", f.read(8))
        assert magic == 2049, "Invalid label file magic number"
        label_data = array("B", f.read())
        labels = list(label_data)
        return labels

# ✅ Corrected paths — use raw strings (r"...") or forward slashes
image_path = r"C:\Users\lzelk\OneDrive\Documents\GitHub\MachineLearning\NumberRecognization\t10k-images.idx3-ubyte"
label_path = r"C:\Users\lzelk\OneDrive\Documents\GitHub\MachineLearning\NumberRecognization\t10k-labels.idx1-ubyte"

train_images = read_idx_images(image_path)
train_labels = read_idx_labels(label_path)

# Print basic info
print(len(train_images))           # Should print 10000 for test set
print(len(train_images[0]))        # Should print 28
print(len(train_images[0][0]))     # Should print 28
print(train_labels[0])             # First label
import struct
from array import array

def read_idx_images(filename):
    with open(filename, 'rb') as f:
        magic, num_images, rows, cols = struct.unpack(">IIII", f.read(16))
        assert magic == 2051, "Invalid image file magic number"
        image_data = array("B", f.read())
        images = []
        for i in range(num_images):
            start = i * rows * cols
            end = start + rows * cols
            img = [image_data[start + j] for j in range(rows * cols)]
            img_2d = [img[j * cols:(j + 1) * cols] for j in range(rows)]
            images.append(img_2d)
        return images

def read_idx_labels(filename):
    with open(filename, 'rb') as f:
        magic, num_labels = struct.unpack(">II", f.read(8))
        assert magic == 2049, "Invalid label file magic number"
        label_data = array("B", f.read())
        return list(label_data)

def print_ascii_image(image):
    shades = ' .:-=+*#%@'
    for row in image:
        line = ''.join(shades[pixel * len(shades) // 256] for pixel in row)
        print(line)

# === File Paths ===


# === Load Data ===
class Data:
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels
    def LoadData():
        image_path = r"C:\Users\lzelk\OneDrive\Documents\GitHub\MachineLearning\NumberRecognization\t10k-images.idx3-ubyte"
        label_path = r"C:\Users\lzelk\OneDrive\Documents\GitHub\MachineLearning\NumberRecognization\t10k-labels.idx1-ubyte"
        images = read_idx_images(image_path)
        labels = read_idx_labels(label_path)
        return images,labels

    # === Show First Image ===
    def GetImage(i,images,labels):
        first_image = images[i]
        first_label = labels[i]
        grayscale_values = [pixel for row in first_image for pixel in row]
        return grayscale_values,first_label
    def GetImageAndLabel():
        Image = Data.LoadData()[0]
        Label= Data.LoadData()[1]
        Data.GetImage(1,Image,Label)

