import numpy as np

def calculate(list):
    #Check if list contains 9 numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #Convert list to numpy array
    MVSD = np.array(list).reshape(3,3)
    #All calls for the needed calculations (mean, variance, std dev, max, min, sum)
    meanCalc = meanIterations(MVSD)
    varCalc = varIterations(MVSD)
    sdCalc = sdIterations(MVSD)
    maxCal = maxIterations(MVSD)
    minCalc = minIterations(MVSD)
    sumCalc = sumIterations(MVSD)

    #Putting all calculation variables into dictionary
    calculations = {'mean': meanCalc,
                    'variance': varCalc,
                    'standard deviation': sdCalc,
                    'max': maxCal,
                    'min': minCalc,
                    'sum': sumCalc,
                    }
    #Returning dictionary with calculations
    return calculations

def meanIterations(meanarray):
    #Does all mean calculations and returns them in list format
    axis0 = np.mean(meanarray, axis = 0).tolist()
    axis1 = np.mean(meanarray, axis = 1).tolist()
    whole = float(np.mean(meanarray))

    allMeans = [axis0,axis1,whole]
    return allMeans

def varIterations(vararray):
    #Does all variance calculations and returns them in list format
    axis0 = np.var(vararray, axis = 0).tolist()
    axis1 = np.var(vararray, axis = 1).tolist()
    whole = float(np.var(vararray))

    allVars = [axis0,axis1,whole]
    return allVars

def sdIterations(sdarray):
    #Does all standard deviation calculations and returns them in list format
    axis0 = np.std(sdarray, axis = 0).tolist()
    axis1 = np.std(sdarray, axis = 1).tolist()
    whole = float(np.std(sdarray))

    allSDs = [axis0,axis1,whole]
    return allSDs

def maxIterations(maxarray):
    #Does all max calculations and returns them in list format
    axis0 = np.max(maxarray, axis = 0).tolist()
    axis1 = np.max(maxarray, axis = 1).tolist()
    whole = float(np.max(maxarray))

    allMaxs = [axis0,axis1,whole]
    return allMaxs

def minIterations(minarray):
    #Does all min calculations and returns them in list format
    axis0 = np.min(minarray, axis = 0).tolist()
    axis1 = np.min(minarray, axis = 1).tolist()
    whole = float(np.min(minarray))

    allMins = [axis0,axis1,whole]
    return allMins

def sumIterations(sumarray):
    #Does all sum calculations and returns them in list format
    axis0 = np.sum(sumarray, axis = 0).tolist()
    axis1 = np.sum(sumarray, axis = 1).tolist()
    whole = float(np.sum(sumarray))

    allSums = [axis0,axis1,whole]
    return allSums