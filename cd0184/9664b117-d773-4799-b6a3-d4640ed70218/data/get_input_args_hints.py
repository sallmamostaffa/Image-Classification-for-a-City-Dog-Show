#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Salma Mostafa
# DATE CREATED: 4-7-2024                           
# REVISED DATE: 
# PURPOSE: Retrieve command line inputs from user using the Argparse Python module
##
import argparse

def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these arguments. If the user fails to 
    provide some or all of the arguments, then the default values are used.
    
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    
    Returns:
     - parse_args() - data structure that stores the command line arguments object  
    """
    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser()
    
    # Argument 1: Folder of pet images
    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='path to the folder of pet images')
    
    # Argument 2: CNN Model Architecture
    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture to use for image classification')
    
    # Argument 3: File containing dog names
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that contains names of dog breeds')
    
    # Return parsed arguments
    return parser.parse_args()
