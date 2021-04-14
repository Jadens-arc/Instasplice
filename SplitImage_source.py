from PIL import Image
import os


def splitImage(n, path=None, image=None):
    if image == None:
        image = Image.open(path)
    width, height = image.size
    images = []
    left = 0
    for i in range(n):
        images.append(image.crop((left, 0, left + (width / n), height)))
        left += width / n

    return images


def saveImages(images, name, filetype):
    for index, image in enumerate(images):
        image.save(f'output/{name}{index}.{filetype}')


def makeImageDivisible(path=None, image=None):
    if image == None:
        image = Image.open(path)
    width, height = image.size
    leftOver = width % height
    print(leftOver)
    return image.crop((leftOver / 2, 0, width - (leftOver / 2), height))


def autosplit(path, save=True):
    croppedImage = makeImageDivisible(path=path)
    width, height = croppedImage.size
    ratio = width / height
    images = splitImage(int(ratio), image=croppedImage)

    if save:
        pathInfo = path.split('.')
        pathInfo[0] = pathInfo[0].split('/')[-1]
        saveImages(images, pathInfo[0], pathInfo[1])

    return images

if __name__ == '__main__':
    images = os.listdir('input')
    for image in images:
        if image == '.gitignore':
            continue
        autosplit(f'input/{image}')
