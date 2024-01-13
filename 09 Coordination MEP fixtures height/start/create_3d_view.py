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
              .OfClass(DB.View) \
              .WhereElementIsNotElementType() \
              .ToElements()
try:
	TransactionManager.Instance.EnsureInTransaction(doc)
	
	default_3dview_type = doc.GetDefaultElementTypeId(DB.ElementTypeGroup.ViewType3D)
	nview = DB.View3D.CreateIsometric(doc, default_3dview_type)
	nview.Name = "dynamo_raybounce_analysis"
	nview.CropBoxActive = False
	nview.CropBoxVisible = False
	if nview.CanToggleBetweenPerspectiveAndIsometric():
	    nview.ToggleToIsometric()
	    #nview.ToggleToPerspective() 
	    
	TransactionManager.Instance.TransactionTaskDone()
	            
	OUT = nview
except Exception as e:
	OUT = [view for view in all_views if view.Name=="dynamo_raybounce_analysis"]
