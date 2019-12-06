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