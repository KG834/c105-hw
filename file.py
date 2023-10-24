import os, cv2
path = "Images"

images = []

for index in os.listdir(path):
    name, extention = os.path.splitext(index)
    if extention in [".jpg", ".png"]:
        file_name = path + "/" +index
        print(file_name)
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count-1):
    pic = cv2.imread(images[i])
    out.write(pic)
out.release()
print("Done")
