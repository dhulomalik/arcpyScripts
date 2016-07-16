import numpy as np
import arcpy
import pythonaddins

class Calculate(object):
    """Implementation for ThreePointProblem_addin.calculatebtn (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        # Input points
        x1 = float(xy1tool.x1) # Point 1
        y1 = float(xy1tool.y1)
        z1 = float(z1cmb.text)
        x2 = float(xy2tool.x2) # Point 2
        y2 = float(xy2tool.y2)
        z2 = float(z2cmb.text)
        x3 = float(xy3tool.x3) # Point 3
        y3 = float(xy3tool.y3)
        z3 = float(z3cmb.text)

        # Plane equation
        A = (y1*z2) + (z1*y3) + (y2*z3) - (z2*y3) - (z3*y1) - (z1*y2)
        B = (z2*x3) + (z3*x1) + (z1*x2) - (x1*z2) - (z1*x3) - (x2*z3)
        C = (x1*y2) + (y1*x3) + (x2*y3) - (y2*x3) - (y3*x1) - (y1*x2)
        D = (z1*y2*x3) + (z2*y3*x1) + (z3*y1*x2) - (x1*y2*z3) - (y1*z2*x3) - (z1*x2*y3)
        E = np.sqrt(A**2 + B**2 + C**2)

        AZ = np.arctan(A/B) * (180/np.pi) # Preliminary azimuth for dip trend
        dip = np.arcsin(-np.cos((np.pi/2) + np.arccos(C/E))) * (180/np.pi) # True dip

        # Test for quadrant
        alpha = A/E
        beta = B/E

        # Place dip-direction in proper quadrant
        if alpha > 0 and beta > 0:
          DD = AZ
        elif alpha > 0 and beta < 0:
          DD = 180 + AZ
        elif alpha < 0 and beta < 0:
          DD = 180 + AZ
        elif alpha < 0 and beta > 0:
          DD = 360 + AZ

        # Right-hand rule strike
        if DD - 90 < 0:
          RHR = 360 + (DD - 90)
        else:
          RHR = DD - 90

        # Centroid coordinates
        Cx = (x1+x2+x3)/3
        Cy = (y1+y2+y3)/3
        Cz = (z1+z2+z3)/3

        # Insert centroid point
        cursor = arcpy.InsertCursor(pointlayercmb.layername) # Feature class must already exist
        row = cursor.newRow()
        row.Shape = arcpy.Point(Cx,Cy,Cz)

        # Populate table
        row.X = Cx
        row.Y = Cy
        row.Z = Cz
        row.DD = DD
        row.dip = dip
        row.RHR = RHR
        cursor.insertRow(row)
        del cursor, row

        # Refresh MXD
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

        # Refresh elevations
        z1cmb.refresh()
        z2cmb.refresh()
        z3cmb.refresh()

class Elevation1(object):
    """Implementation for ThreePointProblem_addin.z1cmb (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWW'
        self.width = 'WWWWW'
    def onEditChange(self, text):
        self.text = text
    def refresh(self):
        self.value = " "

class Elevation2(object):
    """Implementation for ThreePointProblem_addin.z2cmb (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWW'
        self.width = 'WWWWW'
    def onEditChange(self, text):
        self.text = text
    def refresh(self):
        self.value = " "

class Elevation3(object):
    """Implementation for ThreePointProblem_addin.z3cmb (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWW'
        self.width = 'WWWWW'
    def onEditChange(self, text):
        self.text = text
    def refresh(self):
        self.value = " "

class PointLayer(object):
    """Implementation for ThreePointProblem_addin.pointlayercmb (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = False
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWW'
        self.width = 'WWWWWWWWW'
        self.mxd = arcpy.mapping.MapDocument('Current')
        layers = arcpy.mapping.ListLayers(self.mxd)
        for layer in layers:
            pointlayercmb.items.append(layer.name)
    def onSelChange(self, selection):
        self.layername = selection

class SelectPoint1(object):
    """Implementation for ThreePointProblem_addin.xy1tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
    def onMouseDownMap(self, x, y, button, shift):
        self.x1 = x
        self.y1 = y
        print "Point 1: " + str(x) + ", " + str(y)

class SelectPoint2(object):
    """Implementation for ThreePointProblem_addin.xy2tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
    def onMouseDownMap(self, x, y, button, shift):
        self.x2 = x
        self.y2 = y
        print "Point 2: " + str(x) + ", " + str(y)

class SelectPoint3(object):
    """Implementation for ThreePointProblem_addin.xy3tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
    def onMouseDownMap(self, x, y, button, shift):
        self.x3 = x
        self.y3 = y
        print "Point 3: " + str(self.x3) + ", " + str(y)

class UpdateLayers(object):
    """Implementation for ThreePointProblem_addin.layersext (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
    def itemAdded(self, new_item):
        pointlayercmb.items.append(new_item.name)
        pointlayercmb.refresh()
    def itemDeleted(self, deleted_item):
        pointlayercmb.items.remove(deleted_item.name)
        pointlayercmb.refresh()
