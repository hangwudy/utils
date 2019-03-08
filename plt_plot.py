import matplotlib.pyplot as plt
import cv2
import numpy as np

img1 = cv2.imread("car_door_1.png")
img2 = cv2.imread("car_door_2.png")

scale = 400

img1 = cv2.resize(img1, (scale,scale))
img2 = cv2.resize(img2, (scale,scale))

img3 = np.hstack((img1, img2))
# text = "Text"
# cv2.putText(img1, text, (10, 25), cv2.FONT_HERSHEY_COMPLEX,
#                 1.0, (255, 255, 255), 1)

# cv2.imshow("Output", img3)
# cv2.waitKey()
# cv2.destroyAllWindows()


img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
_, ax = plt.subplots(1,1)

text_on_image = "Predicted latitude: 12\nPredicted longitude: 25"
text_on_image2 = "Prediction: (12, 25)\nGround Truth: (13, 25)"

ax.text(0, 1, text_on_image2,
        size='small',
        horizontalalignment='left',
        verticalalignment='top',
        # family='serif',
        bbox={'facecolor': 'white', 'alpha':0.5, 'pad':2},
        # rotation=45,
        color='white',
        transform=ax.transAxes)

ax.axis('off')
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_frame_on(False)
plt.imshow(img3)
plt.savefig("test.pdf", dpi=500,transparent=True,bbox_inches='tight',pad_inches=0)
# plt.show()

"""
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img1 = cv2.resize(img1, (400,400))
img2 = cv2.resize(img2, (400,400))

figsize = (20,10)
_, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
ax1.axis('off')
ax2.axis('off')
title = "Title"
# ax1.set_title(title)

ax1.imshow(img1)
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)
ax1.set_frame_on(False)

ax2.imshow(img2)
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_yaxis().set_visible(False)
ax2.set_frame_on(False)

plt.savefig("test.eps", dpi=500,transparent=True,bbox_inches='tight',pad_inches=0)
plt.show()
"""