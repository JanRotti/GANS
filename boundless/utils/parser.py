import argparse

def parameter_parser():

    parser = argparse.ArgumentParser(description = "GPR WGAN")

    parser.add_argument("--epochs",dest = "epochs",type = int, default = 10000, help = "Number of gradient descent iterations. Default is 200.")

    parser.add_argument("--dataDir",dest = "dataDir",type = str, default = "./data", help = "Directory with files to be processed")
    
    parser.add_argument("--maskRatio",dest = "maskRatio",type = float, default = 0.25, help = "Ratio of images to be reconstructed")

    parser.add_argument("--learningRate",dest = "learningRate",type = float,default = 0.0001, help = "Gradient descent learning rate. Default is 0.0001.")			 

    parser.add_argument("--batchSize",dest = "batchSize",type = int, default = 64,help = "Batch size")

    parser.add_argument("--advLambda",dest = "advLambda", type = float,default = 10, help = "Weight of adversarial Loss")

    parser.add_argument("--imgSize",dest = "imgSize",type = int,default = 128, help = "Img Size to Crop to")
    
    parser.add_argument("--runName",dest = "runName",type = str ,default= "full", help="Name for output files")
    
    return parser.parse_args()
