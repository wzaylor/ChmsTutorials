import numpy as np
import vtk

def example():
    boneSurfaceFileName = 'dat/oks003_MRC_TBB_SKC_LVTIT_01.stl'
    ligamentSurfaceFileName = 'dat/oks003_ACL_AGS_LVTIT.stl'

    boneSurface = loadStlSurface(boneSurfaceFileName)
    ligamentSurface = loadStlSurface(ligamentSurfaceFileName)
    distanceCutOff = 0.5 # This is the cut off distance. This has the same units as the given polydata, so it is usually mm if the .stl files are defined using MR or CT images.

    insertionPointIds = getNearestNeighborNodeIds(ligamentSurface, boneSurface, distanceCutOff)
    visualization(boneSurface, ligamentSurface, insertionPointIds)
    return

def getNearestNeighborNodeIds(sourcePolydata, targetPolydata, tolerance):
    """
    Get a list of the nodeIds on the ``sourcePolydata`` that are within ``tolerance`` of the ``targetPolydata``

    .. NOTE:: This function uses the signed distance between nodes on the ``sourcePolydata`` and ``

    :param sourcePolydata: vtkPolyData object (or similar), The polydata that defines the source geometry. The nodeIds that are returned are from this polydata. Note that only the points from this object are used, so it can also be a vtkUnstructuredGrid object.
    :param targetPolydata: vtkPolyData object, The polydata that defines the target geometry. The nodeIds that are returned are within ``tolerance`` of this polydata.
    :param tolerance: float, The nodeIds of the ``sourcePolydata`` that are returned are within ``tolerance`` of the ``targetPolydata``
    :return: list, A list of nodeIds that relate to the ``sourcePolydata``.
    """
    nodeIds = [] # Initialize an empty list that will be populated with the desired nodeIds
    # Setup the object/variable that is used to conduct the nearest neighbor search
    distFilter = vtk.vtkImplicitPolyDataDistance()
    distFilter.SetInput(targetPolydata)
    x = sourcePolydata.GetNumberOfPoints()
    for pointId in range(sourcePolydata.GetNumberOfPoints()):
        sourcePoint = sourcePolydata.GetPoint(pointId)
        signedDist = distFilter.EvaluateFunction(sourcePoint)
        if signedDist <= tolerance:
            nodeIds.append(pointId)

    return nodeIds

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

def visualization(surface0, surface1, surface1NodeIds):
    """
    Create a visualization that shows the two given surfaces and the points that relate to the given nodeIds.
    :param surface0: vtkPolyData, The polydata object that is being visualized
    :param surface1: vtkPolyData, The polydata object that is being visualized
    :param surface1PointIds: list 1xn, A list of nodeIds from ``surface1``. These points will be part of the visualization, to show a specific subset of points from ``surface1``
    :return:
    """
    # Create a new polydata object that is just the desired points specified in ``surface1NodeIds``
    #--------------------------------
    points = vtk.vtkPoints()
    verts = vtk.vtkCellArray()  # Initialize the variable that is used to store the nodeIds. This is needed to visualize the points
    for i in range(len(surface1NodeIds)):
        points.InsertPoint(i, surface1.GetPoint(surface1NodeIds[i])) # Set the ith point as the coordinates from the corresponding point in ``surface1``.
        verts.InsertNextCell(1)  # Insert a cell into the cellArray that has a length of 1
        verts.InsertCellPoint(i) # Specify the entry for the newly inserted cell. This value is equal to i.

    pointsPolydata = vtk.vtkPolyData() # Initialize the points polydata object
    pointsPolydata.SetPoints(points) # Set the points for the polydata
    pointsPolydata.SetVerts(verts) # Specify the "verts" cellArray as the vertices in the ``surface1`` polydata object.
    #--------------------------------

    # Render the three polydata objects
    #--------------------------------

    # Create the renderer
    ren = vtk.vtkRenderer()

    pointsActor = vtk.vtkActor()
    pointsMapper = vtk.vtkPolyDataMapper()
    pointsMapper.SetInputData(pointsPolydata)
    pointsActor.SetMapper(pointsMapper)
    pointsActor.GetProperty().SetRepresentationToPoints()
    pointsActor.GetProperty().SetColor(1, 1, 0)
    pointsActor.GetProperty().SetPointSize(5)
    pointsActor.GetProperty().SetRenderPointsAsSpheres(True)
    ren.AddActor(pointsActor)

    surface0Actor = vtk.vtkActor()
    surface0Mapper = vtk.vtkPolyDataMapper()
    surface0Mapper.SetInputData(surface0)
    surface0Actor.SetMapper(surface0Mapper)
    surface0Actor.GetProperty().SetOpacity(1) # Make the surface a little transparent so we can better see the points.
    surface0Actor.GetProperty().SetOpacity(1.)
    ren.AddActor(surface0Actor)

    surface1Actor = vtk.vtkActor()
    surface1Mapper = vtk.vtkPolyDataMapper()
    surface1Mapper.SetInputData(surface1)
    surface1Actor.SetMapper(surface1Mapper)
    surface1Actor.GetProperty().SetColor(1, 0, 1) # Make the surface a different color.
    surface1Actor.GetProperty().SetOpacity(0.6)
    ren.AddActor(surface1Actor)

    # Create the window
    renWin = vtk.vtkRenderWindow()
    # Add the renderer to the window
    renWin.AddRenderer(ren)
    # Define an interactor. This controls how the user can interact with
    # things in the window.
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # The default interactor style doesn't work well for a mouse,
    # so we will redefine it as another pre-set style called 'track ball'.
    trackBallStyle = vtk.vtkInteractorStyleTrackballCamera()
    # Set the interactor style as the 'track ball' style defined above.
    iren.SetInteractorStyle(trackBallStyle)

    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()

    # Start the event loop.
    iren.Start()

    return

if __name__ == '__main__':
    example()