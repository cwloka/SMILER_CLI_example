import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os
import psych_metrics as psm

# some hardcoded relative paths which should work if you run with default output paths specified in the YAML file and run this code from its directory
salmappath = '../images/maps/'
stimulipath = '../images/stimuli/'
targetpath = '../images/targmap/'
distpath = '../images/distmap/'

# get the list of models which were run
models = [os.path.split(os.path.split(x)[0])[1] for x in glob(salmappath + '*/')]

# we want scores per image, so get the names of the images to separate out the score plots
imgs = [os.path.splitext(os.path.basename(x))[0] for x in glob(stimulipath + '*.png')]

scores = {} # initialize a score dictionary for human inspection

for img in imgs:
    scores[img] = {} # initialize the score dictionary for this image
    score_array = np.zeros([len(models),4]) # we also want to store scores in an array for easy plotting; we have four metrics

    # now loop through the models and calculate the scores. If doing this on a large dataset it would be more efficient to import the target and distractor maps in the image loop, and the saliency map at the start of the model loop, but on this small dataset we will simply pass the map paths and keep the cv2 dependency contained to psych_metrics
    targmap = targetpath + img + '.png'
    distmap = distpath + img + '.png'
    for idx, model in enumerate(models):
        salmap = salmappath + model + '/' + img + '.png'

        scores[img][model] = {}

        scores[img][model]["avgrat_d"] = psm.avgrat_dist(salmap, targmap, distmap, dilate=2)
        scores[img][model]["avgrat_b"] = psm.avgrat_bg(salmap, targmap, distmap, dilate=2)
        scores[img][model]["maxrat_d"] = psm.maxrat_dist(salmap, targmap, distmap, dilate=2)
        scores[img][model]["maxrat_b"] = psm.maxrat_bg(salmap, targmap, distmap, dilate=2)

        # this is not the neatest way to do this, but it is hopefully clear what values are going where
        score_array[idx,0] = scores[img][model]["avgrat_d"]
        score_array[idx,1] = scores[img][model]["maxrat_d"]
        score_array[idx,2] = scores[img][model]["avgrat_b"]
        score_array[idx,3] = scores[img][model]["maxrat_b"]

    # now that we've calculated the scores for this image, create a plot of those scores
    fig, ax = plt.subplots()
    width = 0.2
    x = np.arange(len(models))

    ax.bar(x, score_array[:,0], width, color = '#000080', label='Average T-D Ratio')
    ax.bar(x + width, score_array[:,1], width, color = '#0F52BA', label='Maximum T-D Ratio')
    ax.bar(x + (2*width), score_array[:,2], width, color = '#6593F5', label='Average T-B Ratio')
    ax.bar(x + (3*width), score_array[:,3], width, color = '#73C2FB', label='Maximum T-B Ratio')

    ax.set_ylabel('Ratio Score')
    #ax.set_ylim(0,5)
    ax.set_xticks(x + (3/2)*width)
    ax.set_xticklabels(models)
    ax.set_xlabel('Model')
    ax.set_title('Scores for ' + img)
    ax.legend()
    ax.axhline(1, linestyle='-', color='r') # add a line highlighting equal saliency between target and distractor

    fig.savefig('../' + img + '_scores.png', bbox_inches='tight')
    plt.close(fig)
