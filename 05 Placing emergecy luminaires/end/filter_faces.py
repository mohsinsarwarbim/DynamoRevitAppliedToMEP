__author__= "sm.mohsinsarwar@gmail.xom"
import sys
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.ExtensibleStorage import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('System')
from System.Collections.Generic import *

doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

locations = IN[0]
surfaces = IN[1]

list_faces = []
for i, points in enumerate(locations):
	auxiliar_list_points=[]
	for point in points:
		faces = surfaces[i]
		for face in faces:
			does_intersect = Geometry.DoesIntersect(point, face)
			if does_intersect:
				auxiliar_list_points.append(face)
				break
	list_faces.append(auxiliar_list_points)
				

OUT = list_faces