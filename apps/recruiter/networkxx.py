import cv2

# Load the image
image = cv2.imread('/home/tinsae/Desktop/AHF_Fintech/apps/recruiter/graph.png')

# Flip the image horizontally
flipped_horizontal = cv2.flip(image, 1)

# Flip the image vertically
flipped_vertical = cv2.flip(image, 0)

# Rotate the image 180 degrees to preserve character direction
# rotated_180 = cv2.rotate(image, cv2.)

# Display the original and flipped images
cv2.imshow('Rotated 180 Degrees', flipped_vertical)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()