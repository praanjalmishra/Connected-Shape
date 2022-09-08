import math
import json

class Shape:
    """
    A class used to represent Shape object

    ...

    Attributes
    ----------
    shape : str
        Type of shape to represent
    color : str
        color of the shape
    dimension : int
        dimension of the shape

    Methods
    -------
    compute_area(shape, dimension)
        Computes the area of the shape
    """
    def __init__(self, shape, color, dimension):
        self.shape = shape
        self.color = color
        self.dimension = dimension
    
    def __repr__(self):
        return f'{self.shape}, {self.color}, {self.dimension}'
    
    def compute_area(self, shape, dimension):
        if shape == 'circle':
            area = math.pi*(dimension*dimension)
            return area
        else:
            area = dimension*dimension
            return area

class ConnectedShape(Shape):
    """
    A class used to represent COnnected Shape object

    ...

    Attributes
    ----------
    connected_shape : list
        List of all connected shape in the configuration
    number : int
        number of connected shapes 
    connected_shape_info : dict
        Dictionary of all connected shape information. Like Identifier, Shape, Color and Dimension of particular shape.
    connected_area : int
        Total sum area of all connected shapes in the configuration 

    Methods
    -------
    add_shape(shape)
        Add a new shape to the configuration
    display_shape()
        Display all attributes of the shape in the configuration
    area_shape(given_identifier)
        Computes the area of the given shape in the configuration
    display_area_shape(given_identifier)
        Returns the area of the given shape in the configuration
    sum_area()
        Computes the area of all connected shape in the configuration
    update_color(given_identifier, color)
        Modify color of a given shape in the configuration
    update_dimension(self, given_identifier, dimension)
        Modify dimension of a given shape in the configuration
    dump_to_json()
        Dump all shape attributes to a JSON file
    """
    
    def __init__(self):
        self.connected_shape = []
        self.number = 0
        self.connected_shape_info = {}
        self.connected_area = 0

    def __repr__(self):
        return f"Connected shape configuration with {self.number} different shapes"
    
    # the add_shape function adds a shape to the configuration. It takes one input parameter
    # that input parameter must be the shape, color and dimension of the shape
    def add_shape(self, shape):
        
        # This identifiers will be assigned to every shape that gets connected to the configuration.
        # There are 20 identifiers
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1',
                        'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
        self.connected_shape.append(str(shape).split(', ')) ## returns list of lists
        self.number += 1
        
        self.connected_shape_info = {'identifier': [], 'shape': [], 'color': [], 'dimension': []}
        for index, i in enumerate(self.connected_shape):
            self.connected_shape_info['identifier'].append(self.identifier[index])
            self.connected_shape_info['shape'].append(i[0])
            self.connected_shape_info['color'].append(i[1])
            self.connected_shape_info['dimension'].append(i[2])
        return print("Shape added to the configuration".format())
          
    def display_shape(self):
            for i in self.connected_shape_info.items():
                print(i)
                             
    def area_shape(self, given_identifier):
        for index, value in enumerate(self.connected_shape_info['identifier']):
                if value == given_identifier:
                    dimension = int(self.connected_shape_info['dimension'][index])
                    shape = self.connected_shape_info['shape'][index]
                    area_shape = self.compute_area(shape, dimension)
                    return area_shape
                    
    def display_area_shape(self, given_identifier):
        area_shape = self.area_shape(given_identifier)
        print("Area = {:.2f}".format(area_shape))
        
    def sum_area(self):
        for value in self.connected_shape_info['identifier']:
            self.connected_area = self.connected_area + self.area_shape(value)
        print("Computed area sum = {:.2f}".format(self.connected_area))           
        
    def update_color(self, given_identifier, color):
        
        if given_identifier not in self.connected_shape_info['identifier']:
            print("Given shape is not connected, Cannot update the color.")
            
        else: 
            for index, value in enumerate(self.connected_shape_info['identifier']):
                if value == given_identifier:
                    self.connected_shape_info['color'][index] = color
                    
    def update_dimension(self, given_identifier, dimension):
        
        if given_identifier not in self.connected_shape_info['identifier']:
            print("given shape is not connected, Cannot update the dimension.")
            
        else: 
            for index, value in enumerate(self.connected_shape_info['identifier']):
                if value == given_identifier:
                    self.connected_shape_info['dimension'][index] = dimension
                    
    def dump_to_json(self):
        json_object = json.dumps(self.connected_shape_info, indent=4)  
        with open("connected_shape_config.json", "w") as file:
            file.write(json_object)
            
        print("Successfully dumped connected config to json file")