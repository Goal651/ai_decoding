import cv2
from pyzbar.pyzbar import decode

img = cv2.imread("image.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Increase contrast
gray = cv2.equalizeHist(gray)

# Optionally threshold
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

barcodes = decode(thresh)

for b in barcodes:
    print(b.type, b.data.decode('utf-8'))

if not barcodes:
    print("No PDF417 barcode found.")
