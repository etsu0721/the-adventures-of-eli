from diagrams import Diagram, Cluster
from diagrams.generic.device import Mobile
from diagrams.custom import Custom

graph_attr = {
    'fontsize': '32',
    'bgcolor': 'transparent',
}

with Diagram('The Adventures of Eli - Data Pipeline', filename='data_pipeline', outformat='jpg', direction='LR', graph_attr=graph_attr):
    
    with Cluster('Extract'):
        wsp = Mobile('Water Sports Tracker'),
        gaia = Mobile('Gaia GPS')
        iCloud = Custom('iCloud', './my_resources/iCloud-icon.jpeg')
    
    with Cluster('Transformation'):
        unconverted_gpx_folder = Custom('Unconverted GPX', './my_resources/folder-icon.png') 
        gpx_to_json_scr = Custom('Batch GPX to JSON', './my_resources/python-script-icon.png')
        converted_gpx_folder = Custom('Converted GPX', './my_resources/folder-icon.png') 
        unenhanced_json_folder = Custom('Unenhanced JSON', './my_resources/folder-icon.png')
        enhance_json_scr = Custom('Enhance JSON', './my_resources/python-script-icon.png')
        enhanced_json_folder = Custom('Enhanced JSON', './my_resources/folder-icon.png')

    with Cluster('Load'):
        tableau = Custom('Tableau', './my_resources/tableau-icon.png')

    wsp >> iCloud 
    gaia >> iCloud 
    iCloud >> unconverted_gpx_folder 
    unconverted_gpx_folder >> gpx_to_json_scr 
    gpx_to_json_scr >> [
        converted_gpx_folder,
        unenhanced_json_folder
    ] 
    unenhanced_json_folder >> enhance_json_scr >> enhanced_json_folder
    enhanced_json_folder - tableau