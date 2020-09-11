import numpy as np
import vtk

def example():
    # Define the variables needed before setting up and performing a nearest neighbor search.
    sourcePoint = np.array([0., 0., 0.]) # The point that is used in the nearest neighbor search
    targetSurfaceFileName = 'dat/oks003_FMB_AGS_LVTIT.stl' # The name of the .stl file that defines the surface
    targetSurface = loadStlSurface(targetSurfaceFileName) # The vtkPolyData object defined by the .stl file.

    # Setup the object/variable that is used to conduct the distance calculation
    distFilter = vtk.vtkImplicitPolyDataDistance()
    distFilter.SetInput(targetSurface)

    # Perform the distance calculation.
    signedDist = distFilter.EvaluateFunction(sourcePoint) # Get the signed distance between 'sourcePoint' and 'targetSurface'.
    print(f"Distance between 'sourcePoint' and 'targetSurface'. Negative distances are inside the surface: {signedDist}") # Print the point's coordinates so this function does something mildly interesting.

    return

def loadStlSurface(fileName):
    """
    This function loads a .stl file and returns vtkPolyData.
    :param fileName: string, The name of the .stl file that is being loaded.
    :return: vtkPolyData, The geometry that was in the .stl file.
    """
    reader = vtk.vtkSTLReader()
    reader.SetFileName(fileName)
    reader.Update()
    polyData = reader.GetOutput()
    return polyData


if __name__ == '__main__':
    example()