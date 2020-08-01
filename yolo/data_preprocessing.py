import numpy as np
import os
import glob
import tensorflow as tf
import PIL.Image

DATA_LIST = glob.glob('data\\*.jpg')
IMG_SIZE = 256

def get_file_name(path):
    return path.split('\\')[1]

def make_dir(keyword):
    dir = "data\\" + keyword + "\\"
    if not os.path.exists(dir):
        os.makedirs(dir)
        print("--> ", dir)
    return dir

def resize(crp_img):
    image = PIL.Image.open(crp_img)
    resized = image.resize((IMG_SIZE,IMG_SIZE))
    dir = make_dir("resized")
    resized.save(dir + crp_img.split('\\')[2], "JPEG", quality=100)
    return resized

def write_tf(tf_img, keyword):
    dir = make_dir(keyword)
    enc = tf.io.encode_jpeg(tf_img, quality = 100)
    tf.io.write_file(dir+get_file_name(org_img), enc)

def crop(org_img):
    image_string = tf.io.read_file(org_img)
    image = tf.image.decode_jpeg(image_string, channels = 3)
    cropped = tf.image.central_crop(image, 0.55)
    #cropped = tf.image.resize_with_crop_or_pad(image, 150,128)
    write_tf(cropped, "cropped")


for org_img in DATA_LIST:
    crop(org_img)
    crp_img = "data\\cropped\\" +get_file_name(org_img)
    resize(crp_img)

