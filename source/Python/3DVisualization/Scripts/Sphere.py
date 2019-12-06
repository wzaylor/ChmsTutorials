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

    # Initialize the source
    sphere = vtk.vtkSphereSource()
    # Set the center to the desired coordinates
    sphere.SetCenter(1., 4., 6.)
    # Set the radius to the desired value
    sphere.SetRadius(1.2)
    # Update the source to apply changes
    sphere.Update()
    # Generate the polydata from the source
    spherePolyData = sphere.GetOutput()

    # Initialize the mapper
    sphereMapper = vtk.vtkPolyDataMapper()
    # Set the mapper's polydata as spherePolyData
    sphereMapper.SetInputData(spherePolyData)

    # Initialize the actor
    sphereActor = vtk.vtkActor()
    # Set the actor's mapper as sphereMapper
    sphereActor.SetMapper(sphereMapper)
    # Add the actor to the renderer
    ren.AddActor(sphereActor)

    # Define the axes actor.
    axes = vtk.vtkAxesActor()
    # Add the axes actor to the window.
    ren.AddActor(axes)

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