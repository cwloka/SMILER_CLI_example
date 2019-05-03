import numpy as np
import cv2
import random
import skimage.morphology as morph

# Find the ratio of the average target saliency value and the average distractor saliency value
def avgrat_dist(salmap, targmap, distmap, dilate = 0, add_eps=False):
    if isinstance(salmap, str):
        salmap = cv2.imread(salmap, cv2.IMREAD_GRAYSCALE) # we only want the grayscale version, since saliency maps should all be grayscale
    if isinstance(targmap, str):
        targmap = cv2.imread(targmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for target and black for non-target
    if isinstance(distmap, str):
        distmap = cv2.imread(distmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for distractors and black for non-distractors

    if add_eps:
        randimg = [random.uniform(0,1/100000) for _ in range(salmap.size)]
        randimg = np.reshape(randimg, salmap.shape)
        salmap = salmap + randimg

    targmap_copy = targmap.copy()
    distmap_copy = distmap.copy()

    # dilate the target and distractor maps to allow for saliency bleed
    if dilate > 0:
        targmap_copy = morph.dilation(targmap_copy.astype(np.uint8), morph.disk(dilate))
        distmap_copy = morph.dilation(distmap_copy.astype(np.uint8), morph.disk(dilate))

    # convert the target and distractor masks into arrays with 0 and 1 for values
    targmap_normalized = targmap_copy / 255
    distmap_normalized = distmap_copy / 255

    avgt = np.sum(np.multiply(salmap,targmap_normalized)) / np.sum(targmap_normalized)
    avgd = np.sum(np.multiply(salmap, distmap_normalized)) / np.sum(distmap_normalized)

    if avgd > 0:
        score = avgt/avgd
    else:
        score = -1

    return score

# Find the ratio of the average target saliency value and the average background saliency value
def avgrat_bg(salmap, targmap, distmap, dilate = 0, add_eps=False):
    if isinstance(salmap, str):
        salmap = cv2.imread(salmap, cv2.IMREAD_GRAYSCALE) # we only want the grayscale version, since saliency maps should all be grayscale
    if isinstance(targmap, str):
        targmap = cv2.imread(targmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for target and black for non-target
    if isinstance(distmap, str):
        distmap = cv2.imread(distmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for distractors and black for non-distractors

    if add_eps:
        randimg = [random.uniform(0,1/100000) for _ in range(salmap.size)]
        randimg = np.reshape(randimg, salmap.shape)
        salmap = salmap + randimg

    targmap_copy = targmap.copy()
    distmap_copy = distmap.copy()

    # dilate the target and distractor maps to allow for saliency bleed
    if dilate > 0:
        targmap_copy = morph.dilation(targmap_copy.astype(np.uint8), morph.disk(dilate))
        distmap_copy = morph.dilation(distmap_copy.astype(np.uint8), morph.disk(dilate))

    # convert the target and distractor masks into arrays with 0 and 1 for values
    targmap_normalized = targmap_copy / 255
    distmap_normalized = distmap_copy / 255

    # convert the target and distractor masks into arrays with 0 and 1 for values
    salmap_normalized = salmap/255
    bgmap_normalized = 1 - np.logical_or(targmap_normalized>0.5, distmap_normalized>0.5)

    avgt = np.sum(np.multiply(salmap_normalized,targmap_normalized)) / np.sum(targmap_normalized)
    avgb = np.sum(np.multiply(salmap_normalized, bgmap_normalized)) / np.sum(bgmap_normalized)

    if avgb > 0:
        score = avgt/avgb
    else:
        score = -1

    return score

# Find the ratio of the maximum target saliency value and the maximum distractor saliency value
def maxrat_dist(salmap, targmap, distmap, dilate = 0, add_eps = False):
    if isinstance(salmap, str):
        salmap = cv2.imread(salmap, cv2.IMREAD_GRAYSCALE) # we only want the grayscale version, since saliency maps should all be grayscale
    if isinstance(targmap, str):
        targmap = cv2.imread(targmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for target and black for non-target
    if isinstance(distmap, str):
        distmap = cv2.imread(distmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for distractors and black for non-distractors

    if add_eps:
        randimg = [random.uniform(0,1/100000) for _ in range(salmap.size)]
        randimg = np.reshape(randimg, salmap.shape)
        salmap = salmap + randimg

    targmap_copy = targmap.copy()
    distmap_copy = distmap.copy()

    # dilate the target and distractor maps to allow for saliency bleed
    if dilate > 0:
        targmap_copy = morph.dilation(targmap_copy.astype(np.uint8), morph.disk(dilate))
        distmap_copy = morph.dilation(distmap_copy.astype(np.uint8), morph.disk(dilate))


    # convert the target and distractor masks into arrays with 0 and 1 for values
    targmap_normalized = targmap_copy / 255
    distmap_normalized = distmap_copy / 255
    salmap_normalized = salmap/255

    maxt = np.max(np.multiply(salmap_normalized, targmap_normalized))
    maxd = np.max(np.multiply(salmap_normalized, distmap_normalized))

    if maxd > 0:
        score = maxt/maxd
    else:
        score = -1

    return score

# Find the ratio of the maximum target saliency value and the maximum background saliency value
def maxrat_bg(salmap, targmap, distmap, dilate = 0, add_eps=False):
    if isinstance(salmap, str):
        salmap = cv2.imread(salmap, cv2.IMREAD_GRAYSCALE) # we only want the grayscale version, since saliency maps should all be grayscale
    if isinstance(targmap, str):
        targmap = cv2.imread(targmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for target and black for non-target
    if isinstance(distmap, str):
        distmap = cv2.imread(distmap, cv2.IMREAD_GRAYSCALE) # assume that this is a grayscale binary map with white for distractors and black for non-distractors

    if add_eps:
        randimg = [random.uniform(0,1/100000) for _ in range(salmap.size)]
        randimg = np.reshape(randimg, salmap.shape)
        salmap = salmap + randimg

    targmap_copy = targmap.copy()
    distmap_copy = distmap.copy()

    # dilate the target and distractor maps to allow for saliency bleed
    if dilate > 0:
        targmap_copy = morph.dilation(targmap_copy.astype(np.uint8), morph.disk(dilate))
        distmap_copy = morph.dilation(distmap_copy.astype(np.uint8), morph.disk(dilate))

    # convert the target and distractor masks into arrays with 0 and 1 for values
    targmap_normalized = targmap_copy / 255
    distmap_normalized = distmap_copy / 255
    salmap_normalized = salmap / 255
    bgmap_normalized = 1 - np.logical_or(targmap_normalized>0.5, distmap_normalized>0.5)

    maxt = np.max(np.multiply(salmap_normalized, targmap_normalized))
    maxb = np.max(np.multiply(salmap_normalized, bgmap_normalized))


    if maxt > 0:
        score = maxb/maxt
    else:
        score = -1

    return score
