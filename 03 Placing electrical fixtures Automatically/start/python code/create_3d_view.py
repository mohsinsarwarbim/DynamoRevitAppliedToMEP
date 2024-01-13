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
import Autodesk.Revit.DB as DB
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

all_views = DB.FilteredElementCollector(doc) \
			  .OfClass(DB.View3D) \
			  .WhereElementIsNotElementType() \
			  .ToElements()

view_name = "_dynamo_raybounce_analysis"
view_exist = view_name  in [view.Name for view in all_views]

if view_exist:
	OUT = [view for view in all_views if view.Name == view_name]
else:
	# Create 3D view
	TransactionManager.Instance.EnsureInTransaction(doc)
	
	default_3dview_type = doc.GetDefaultElementTypeId(DB.ElementTypeGroup.ViewType3D)
	nview = DB.View3D.CreateIsometric(doc, default_3dview_type)
	nview.Name = view_name
	nview.CropBoxActive = False
	nview.CropBoxVisible = False
	if nview.CanToggleBetweenPerspectiveAndIsometric():
		nview.ToggleToIsometric()
		#nview.ToggleToPerspective() 
	TransactionManager.Instance.TransactionTaskDone()       
	OUT = nview