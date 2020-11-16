from skimage.io import imread, imsave
from skimage.util import random_noise
from os import listdir
from os.path import isfile, join, splitext

def apply_noise(imge_path, mode):
	dest = "/home/yhetman/Pictures/price-tags/tags-png/"
	fname = splitext(imge_path)[0]
	fname = fname + str(mode) + '.png'
	img = imread(imge_path)/255.0
	if mode is not None:
		gimg = random_noise(img, mode=mode)
		imsave(join(dest, fname), gimg)



def apply_to_all_files(mypath):
	files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
	for file_path in files:
		apply_noise(file_path, "gaussian")
#		apply_noise(file_path, "salt")
#		apply_noise(file_path, "pepper")
#		apply_noise(file_path, "gaussian")



def main():
	dir_path="/home/yhetman/Pictures/price-tags/tags-png/noises/"
	apply_to_all_files(dir_path)


if __name__ == "__main__":
	main()
