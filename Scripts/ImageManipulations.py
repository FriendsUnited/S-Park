import os
import cv2
import urllib.request
import numpy as np


try:
    from PIL import Image
except ImportError:
    import Image


FolderName = "/home/elysian/Documents/opencv_workspace/Negatives/"
ParentFolder = "/home/elysian/Documents/opencv_workspace/"

def renameImages():
    i = 1
    try:
        for filename in os.listdir(FolderName):
            extension = os.path.splitext(filename)[1]
            if extension == ".png" or ".jfif" or ".jpg" or ".jpeg" or ".webp":
                dst = str(i) + extension
                src = FolderName + filename
                dst = FolderName + dst

                os.rename(src, dst)
                i += 1
    except Exception as e:
        print(e)


def convertImages():
    i = 1
    newName = str(i) + ".bmp"
    # fileName = str(i) + ".png"
    for filename in os.listdir(FolderName):
        basename = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]
        if extension == ".png" or ".jfif" or ".jpg" or ".jpeg" or ".webp":
            newName = str(basename) + ".bmp"
            Image.open(filename).save(newName)


def downloadRawImages():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  
            
def Resizing():
    i =3000
    for filename in os.listdir(FolderName):
        try:
            extension = os.path.splitext(filename)[1]
            newFileName = FolderName + filename
            img = cv2.imread(newFileName,cv2.IMREAD_GRAYSCALE)
           
            resized_image = cv2.resize(img, (50, 50))
            #NewImage = FolderName + str(i) + extension
            cv2.imwrite(filename,resized_image)
            i+=1
        except:
            pass


def convertToGrayScale():
   
    for filename in os.listdir(FolderName):
        try :
            newFileName = FolderName + filename
            img = cv2.imread(newFileName,cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(filename,img)
        except :
            pass
            
            
def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

if __name__ == "__main__":
    # renameImages()
    # downloadRawImages()
    #  gnResizing()
    # convertImages()
    #convertToGrayScale()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
