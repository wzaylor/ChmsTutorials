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

    # The complete path to the .stl file
    stlSurfaceFileName = r'/home/will/Projects/ChmsTutorials/source/Python/3DVisualization/dat/oks003_FMB_AGS_LVTIT.stl'

    # Initialize the object that is used to load the .stl file
    stlFileReader = vtk.vtkSTLReader()
    # Specify the .stl file's name.
    stlFileReader.SetFileName(stlSurfaceFileName)
    # Load the .stl file. Note that this makes changes to the stlFileReader variable, but doesn't output polydata
    stlFileReader.Update()
    # Get the polydata from the 'stlFileReader' variable as a new variable named 'surfacePolyData'.
    surfacePolyData = stlFileReader.GetOutput()

    # Initialize the mapper
    surfaceMapper = vtk.vtkPolyDataMapper()
    # Set the mapper's polydata as spherePolyData
    surfaceMapper.SetInputData(surfacePolyData)

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