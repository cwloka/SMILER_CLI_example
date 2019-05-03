# SMILER CLI Example: Singleton Target Detection

This is an example application which showcases the use of SMILER using the command line interface (CLI). Note that although this example is designed to showcase an interesting and non-standard exploration of the properties of saliency algorithms, it is nevertheless a toy example with only a very small number of test images. Any conclusions or judgements about algorithm performance are therefore tentative at best.

This example was written by Calden Wloka, and most recently tested under SMILER version 1.1.0

## Running instructions

This readme assumes that the user has already successfully downloaded and configured SMILER. If SMILER is not set up on your system, instructions and content can be found on the [GitHub repository](https://github.com/TsotsosLab/SMILER).

To run the experiment specification file included in this example, execute the command:

`smiler run -e [path/to/example/folder]/smiler_psych.yaml`

## Experiment description

This experiment examines the ability of saliency models to find singleton targets in psychophysical search arrays. It uses four example images, each one representing a different form of singleton target. For more background on why we feel psychophysical experimentation is an underexplored but important area of saliency modeling research, see the following paper:

Neil D.B. Bruce, Calden Wloka, Nick Frosst, Shafin Rahman, and John Tsotsos (2015) On computational modeling of visual saliency: Examining what’s right, and what’s left. Vision Research 116:95-112 [Link](https://www.sciencedirect.com/science/article/pii/S0042698915000267)

Images were created using the Psychophysical Image Generator (PIG) tool, which can be found [here](http://jtl.lassonde.yorku.ca/PIG/).

Model performance is evaluated by calculating the ratio of maximum target salience versus maximum distractor salience, as well as taking the ratio of the average target salience versus average distractor salience.

## Experiment file descriptions

This example organizes files into two subfolders: `images` and `analysis`.

The `images` folder contains `stimuli` which provides the input images for the experiment, `distmap` which provides the binary distractor masks, and `targmap` which provides the binary target masks. If map logging is turned on, this folder will also contain a `maps` folder after the experiment is run which contains the output of the different saliency algorithms.

The `analysis` folder contains all the files necessary to perform the model evaluation after conducting an experimental run specified by the YAML files.
