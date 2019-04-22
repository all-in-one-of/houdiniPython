# 456.py
# File is run when Houdini opens an existing hou file

#########################################################
# Function to create blank geo node
def create_geoNode():

    # Access obj network
    obj = hou.node("/obj")

    # Create geo node
    geo = obj.createNode("geo", node_name="newGeo")


#########################################################
# Function to create camera node
def create_cameraNode():

    # Access obj network
    obj = hou.node("/obj")

    # Create cam node in obj network
    cam = obj.createNode("cam", "cam_1080")

    # Define resolution using dictionary format
    res = {'resx': 1920, 'resy': 1080}
    # Apply resolution to camera
    cam.setParms(res)

    # Turn off camera node display flag
    cam.setDisplayFlag(False)


#########################################################
# Function to create Redshift render ROP & IPR nodes
def create_redshiftNode():

    # Access out network
    out = hou.node("/out")

    # Create Redshift ROP in out network
    redRop = out.createNode("Redshift_ROP")

    # Set ROP gamma to No Gamma
    redRop.setParms({"RS_gammaFileMode": "noGamma"})

    #########################################
    # Create Redshift IPR in out network
    redIPR = out.createNode("Redshift_IPR")

#########################################################
# Collect functions to generate all new nodes at startup
# in new main() function
def main():

    # Check if a node in the obj network starts with "cam..."
    # Wildcard (*) used to check for prefix "cam..."
    if not hou.node('/obj').glob('cam*'):
        create_cameraNode()

    # Check if a node in the obj network starts with "Redshift..."
    # Wildcard (*) used to check for prefix "Redshift..."
    if not hou.node('/out').glob('Redshift*'):
        create_redshiftNode()

#########################################################
# Call main function
main()