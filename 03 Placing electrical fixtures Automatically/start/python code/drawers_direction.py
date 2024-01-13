__author__ = 'Mohsin Sarwar, sm.mohsinsarwar@gmail.com'
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

electrical_fixtures = [UnwrapElement(elem) for elem in IN[0]]

vectors = []
for elem in electrical_fixtures:
	transform = elem.GetTotalTransform()
	yaxis = transform.BasisY
	reverse_yaxis = yaxis.Negate()
	vectors.append(reverse_yaxis)

#convert revit vector to dynamo vector
vectors = [vec.ToVector() for vec in vectors]

OUT = vectors