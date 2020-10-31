import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# print("TF Version: ", tf.__version__)
# print("TF-Hub version: ", hub.__version__)
# print("GPU available: ", tf.config.list_physical_devices('GPU'))

def load_image(img_path):
    """ Auxiliar funtion to properly tranform the image to a tensor
    """
    img = plt.imread(img_path).astype(np.float32)[np.newaxis, ...]

    if img.max() > 1.0:
        img = img / 255.0
    if len(img.shape) == 3:
        img = tf.stack([img, img, img], axis=-1)
    
    return img

def save_image(img_path, img):
    """ Auxiliar function to save an image stored in a tensor format 
    """
    plt.imsave(img_path, np.squeeze(img, axis=0))

def load_from_input():
    """ Auxiliar function to get inputs for the model 
    """

    content_img_path = './sample_content_images/' + input("\n Content image name: ")
    style_img_path = './sample_style_images/' + input("\n Style image name: ")
    out_img_path = './output_images/' + input("\n Output image name: ")

    content_img = load_image(content_img_path)
    style_img = load_image(style_img_path)

    # the model works best with style images 256x256
    resize = bool(int(input("\n Resize style image? (0 false - 1 true): \n")))
    if resize:
        x = int(input())
        y = int(input())
        preserve = bool(int(input()))
        
        style_img = tf.image.resize(style_img, size=(x, y), preserve_aspect_ratio=preserve)

    return content_img, style_img, out_img_path


###### MAIN ######

print("*********** Getting images ***********")
content_img, style_img, out_img_path = load_from_input()

# resize the contet image to control the execution time/memory consumption
max_r = 1300 # max size of the biggest axis
content_img = tf.image.resize(content_img, size=(
    max_r, max_r), preserve_aspect_ratio=True)


print("*********** Loading Module ***********")
# module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1') # older version
module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
# module = hub.load('./magenta/') # if the saved_model.pb is downloaded and stored in the ./magenta/

print("*********** Using Model ***********")
outputs = module(tf.constant(content_img), tf.constant(style_img))
stylized_img = outputs[0]

print("*********** Saving Image ***********")
save_image(out_img_path, stylized_img)
