import mesa 
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import IsingModel



# define and set up agent visualization
def ising_draw(agent):
    if agent is None:
        return
    portrayal = {"Shape": "rect", "Filled": "true", "w": 0.8, "h": 0.8, "Layer": 0}

    if agent.state == 1:
        portrayal["Color"] = "#ccc2c9"# whitish pink

    else:
        portrayal["Color"] = "#7a0c58"# dark pink

    return portrayal


# set up how and what we're calling for the gui
canvas_element = CanvasGrid(ising_draw, 100, 100, 500, 500)


# set up how the visualization will look
model_params = {        
    "beta": mesa.visualization.Slider(
         name="Parameter beta", value=0.21, min_value=0, max_value=1, step=0.01
    ),
    "height": 100,
    "width": 100,
    "hot_configuration":mesa.visualization.Choice(
        name = "Hot configuration",
        value = False,
        choices = [True, False]
    )
    
}

# call the various visualization elements
# model, grid
# features a name for the model and our relevant input parameter values
server = ModularServer(
    IsingModel,
    [canvas_element ],
    "Ising Spin Model",
    model_params
)
