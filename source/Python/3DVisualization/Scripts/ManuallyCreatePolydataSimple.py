import vtk

def example():
    # Create the renderer
    ren = vtk.vtkRenderer()
    # Create the window
    renWin = vtk.vtkRenderWindow()
    # Add the renderer to the window
    renWin.AddRenderer(ren)
    # Define an interactor. This controls how the user can interact with
    # things in the window.
    iren = vtk.vtkRenderWindowInteractor()
    # Set the window defined above as the window that the interactor
    # will work on.
    iren.SetRenderWindow(renWin)

    # Initialize the points object
    nodes = vtk.vtkPoints()
    # Manually add the node coordinates. Note the nodeIDs start at 0 instead of 1.
    nodes.InsertPoint(0, 1.0201, 0.0040, 0.0072)
    nodes.InsertPoint(1, 1.0305, 1.0057, 0.0099)
    nodes.InsertPoint(2, 1.3103, 1.0007, 1.0099)
    nodes.InsertPoint(3, -0.5000, 1.0000, 1.0099)

    # Initialize the elements object
    elements = vtk.vtkCellArray()
    # Create the object that stores the list of nodeIDs
    elementIdList0 = vtk.vtkIdList()
    # Insert the nodeIDs in the appropriate order.
    elementIdList0.InsertNextId(0)
    elementIdList0.InsertNextId(1)
    elementIdList0.InsertNextId(2)

    # Create the object that stores the list of nodeIDs
    elementIdList1 = vtk.vtkIdList()
    # Insert the nodeIDs in the appropriate order.
    elementIdList1.InsertNextId(0)
    elementIdList1.InsertNextId(1)
    elementIdList1.InsertNextId(3)

    # Insert the elementIdLists into 'elements'
    elements.InsertNextCell(elementIdList0)
    elements.InsertNextCell(elementIdList1)

    # Initialize the polydata variable
    polydata = vtk.vtkPolyData()
    # Specify that the variable 'nodes' as the points in the polydata
    polydata.SetPoints(nodes)
    # Similarly, specify that the variable 'elements' as the polys in polydata
    polydata.SetPolys(elements)

    # Initialize the mapper
    surfaceMapper = vtk.vtkPolyDataMapper()
    # Set the mapper's polydata as spherePolyData
    surfaceMapper.SetInputData(polydata)

    # Initialize the actor
    surfaceActor = vtk.vtkActor()
    # Set the actor's mapper as sphereMapper
    surfaceActor.SetMapper(surfaceMapper)
    # Add the actor to the renderer
    ren.AddActor(surfaceActor)

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

if __name__=='__main__':
    example()