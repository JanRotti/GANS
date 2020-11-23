import numpy as np
import os
import sys
import matplotlib.pyplot as plt

# Preprocessing
import glob
from PIL import Image, ImageOps
import random

# model dependencies
import torch
import torch.nn as nn
import torchvision
from models import Generator

def loadModel(directory = ''):
