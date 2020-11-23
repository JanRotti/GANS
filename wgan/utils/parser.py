import argparse

def parameter_parser():

    parser = argparse.ArgumentParser(description = "GPR WGAN")

    parser.add_argument("--epochs",dest = "epochs",type = int,default = 10000, help = "Number of gradient descent iterations. Default is 200.")

    parser.add_argument("--dataDir",dest = "dataDir",type = str,default = "./data", help = "Directory with files to be processed")

    parser.add_argument("--learningRate",dest = "learningRate",type = float,default = 0.00005, help = "Gradient descent learning rate. Default is 0.01.")

    parser.add_argument("--hiddenDim",dest = "hiddenDim",type = int,default = 100, help = "Number of neurons by hidden layer. Default is 128.")				 

    parser.add_argument("--batchSize",dest = "batchSize",type = int,default = 64,help = "Batch size")

    parser.add_argument("--discUpdates",dest = "discUpdates",type = int,default = 5, help = "Number of discriminator update steps per learning step")

    parser.add_argument("--gpWeight",dest = "gpWeight", type = float,default = 10, help = "Weight of gradient penalty")

    parser.add_argument("--imgSize",dest = "imgSize",type = int,default = 128, help = "Img Size to Crop to")
    
    parser.add_argument("--runName",dest = "runName",type = str ,default= "B64", help="Name for output files")
    
    return parser.parse_args()
