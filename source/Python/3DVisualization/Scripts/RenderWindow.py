import vtk

def example():
    # Create the renderer
    ren = vtk.vtkRenderer()
    # Create the window
    renWin = vtk.vtkRenderWindow()
    # Add the renderer to the window
    renWin.AddRenderer(ren)
    # Define an interactor. This controls how the user can interact with objects in the window.
    iren = vtk.vtkRenderWindowInteractor()
    # Set the window defined above as the window that the interactor will work on.
    iren.SetRenderWindow(renWin)

    # This allows the interactor to initialize itself.
    # It needs to be called before an event loop.
    iren.Initialize()

    # Start the event loop.
    iren.Start()
    return

if __name__=='__main__':
    example()