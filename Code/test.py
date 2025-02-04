import win32com.client


pathToGraphic = r"C:\Users\monon\OneDrive\Desktop\Basketball\Boys\vs Oregon 010925\FINAL.psd"
#Layer to change
layer_name = "homeScore"
# The text to change 
new_text = "5"


#Done in win32com.client
def win():

    # sets app to the connection/phisical 
    app = win32com.client.Dispatch("Photoshop.Application")

    #Opens it on the desktop
    app.Open(pathToGraphic)

    # Opens it for changing 
    doc = app.ActiveDocument

    # checking if the layer to change is in the layers
    #for layer in doc.ArtLayers:
    #   if layer.Name == layer_name:
    #      # Assigns the layer to text layer variable
    #     text_layer = layer

    # This is a better way to get to the layer 
    text_layer = doc.ArtLayers[layer_name]

    text_layer = text_layer.TextItem
    # font = Arial, weight = Bold, size = 135px
    # Change text size 
    text_layer.size = 135

    text_layer.Contents = new_text

    # Change position
    text_layer.Position = (100, 100)

    print(text_layer)

    # Saves the doc
    doc.Save()
    # Closes the doc with no saving 
    #doc.Close(2)

    #Quits the app loop 
    #app.Quit()

if __name__ == "__main__":
    win()
