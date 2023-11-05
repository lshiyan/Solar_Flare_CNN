from PIL import Image
from torchvision import transforms

solar_Images=[f for f in os.listdir("img") if f.endswith(".jpg")]

transformed_Images=[]
for imageFilePath in solar_Images:
    image=Image.to_grayscale(Image.open("img\\"+imageFilePath))
    tensor_Transform = transforms.ToTensor()
    transformed_Image=tensor_Transform(image)
    transformed_Images.append(transformed_Image)

print(transformed_Images[1])