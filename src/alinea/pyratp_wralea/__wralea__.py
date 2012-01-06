
# This file has been generated at Thu Jan 05 10:33:01 2012

from openalea.core import *


__name__ = 'PyRATP'

__editable__ = True
__description__ = ''
__license__ = 'CeCILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = []
__version__ = '0.9.0'
__authors__ = ''
__institutes__ = None
__icon__ = 'icon.png'


__all__ = ['ratp_can2riri', 'ExtractLight_ExtractLight', 'ratp_read_grid', 'ratp_read_skyvault', 'ratp_DoAll', 'ratp_fill_grid', 'ratp_DoIrradiation', 'Plot3DRATP_Plot3DRATP', 'ratp_read_vgx', 'ratp_ExtractTime', 'ratp_extract_leaves', 'ratp_read_vegetation', 'ratp_read_micrometeo', 'ExtractVar_ExtractVar', 'RATP2VTK_RATP2VTK']



ratp_can2riri = Factory(name='can2riri',
                authors=' (wralea authors)',
                description='can2riri',
                category='simulation, ecophysiology',
                nodemodule='ratp',
                nodeclass='can2riri',
                inputs=[{'interface': IFileStr(filter="*.can", save=False), 'name': 'filename', 'value': None, 'desc': '3D can file'}],
                outputs=[{'interface': IInt, 'name': 'entity', 'desc': ''}, {'interface': IFloat, 'name': 'x', 'desc': ''}, {'interface': IFloat, 'name': 'y', 'desc': ''}, {'interface': IFloat, 'name': 'z', 'desc': ''}, {'interface': IFloat, 'name': 's', 'desc': ''}, {'interface': IFloat, 'name': 'n', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




ExtractLight_ExtractLight = Factory(name='ExtractLight',
                authors=' (wralea authors)',
                description='Extract PAR from RATP output',
                category='data processing',
                nodemodule='ExtractLight',
                nodeclass='ExtractLight',
                inputs=[{'interface': None, 'name': 'Elt2Voxel', 'value': None, 'desc': ''}, {'interface': None, 'name': 'RATPOutput', 'value': None, 'desc': ''}, {'interface': IInt, 'name': 'Day', 'value': None, 'desc': ''}, {'interface': IInt, 'name': 'Hour', 'value': None, 'desc': ''}, {'interface': IInt, 'name': 'Variable', 'value': None, 'desc': 'Numero colonne de la variable choisie'}],
                outputs=[{'interface': None, 'name': 'PAR', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_read_grid = Factory(name='read grid',
                authors=' (wralea authors)',
                description='Build a RATP Grid',
                category='simulation, ecophysiology',
                nodemodule='ratp',
                nodeclass='read_grid',
                inputs=[{'interface': IFileStr(filter="*.grd", save=False), 'name': 'filename', 'value': None, 'desc': '3d Grid file'}],
                outputs=[{'interface': None, 'name': 'grid', 'desc': 'No output for the moment'}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_read_skyvault = Factory(name='read_skyvault',
                authors=' (wralea authors)',
                description='read the skyvault file',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='read_skyvault',
                inputs=[{'interface': IFileStr(filter="*.skv", save=False), 'name': 'filename', 'value': None, 'desc': 'Skywvault file'}],
                outputs=[{'interface': None, 'name': 'grid', 'desc': 'No output for the moment'}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_DoAll = Factory(name='do_all',
                authors=' (wralea authors)',
                description='run RATP',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='DoAll',
                inputs=[{'interface': ISequence, 'name': 'inputs', 'value': None, 'desc': ''}],
                outputs=[{'name': 'time_spatial', 'desc': 'time evolution for each voxel'}, {'name': 'tree', 'desc': 'time evolution for each voxel'}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_fill_grid = Factory(name='fill grid',
                authors=' (wralea authors)',
                description='fill a RATP Grid with vegetation',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='fill_grid',
                inputs=[{'interface': IInt, 'name': 'entity', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 'x', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 'y', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 'z', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 's', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 'n', 'value': None, 'desc': ''}, {'interface': None, 'name': 'grid', 'value': None, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'grid', 'desc': 'No output for the moment'}, {'interface': None, 'name': 'Elt2Voxels', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_DoIrradiation = Factory(name='ratp_radiation',
                authors=' (wralea authors)',
                description='run RATP - irradiation calculation only',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='DoIrradiation',
                inputs=[{'interface': ISequence, 'name': 'inputs', 'value': None, 'desc': ''}],
                outputs=[{'interface': None, 'name': 'RATP_Output', 'desc': 'No output for the moment'}],
                widgetmodule=None,
                widgetclass=None,
               )




Plot3DRATP_Plot3DRATP = Factory(name='Plot3DRATP',
                authors=' (wralea authors)',
                description='',
                category='visualisation',
                nodemodule='Plot3DRATP',
                nodeclass='Plot3DRATP',
                inputs=[{'interface': ISequence, 'name': 'Scene', 'value': None, 'desc': ''}, {'interface': ISequence, 'name': 'Color', 'value': None, 'desc': ''}],
                outputs=[{'interface': ISequence, 'name': 'Scene', 'desc': 'Colored Scene  '}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_read_vgx = Factory(name='plant from vegestar',
                authors=' (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='read_vgx',
                inputs=[{'interface': IFileStr(filter="*.vgx", save=False), 'name': 'filename', 'value': None, 'desc': 'Vegestar 3d Grid file'}],
                outputs=[{'interface': IInt, 'name': 'entity', 'desc': ''}, {'interface': IFloat, 'name': 'x', 'desc': ''}, {'interface': IFloat, 'name': 'y', 'desc': ''}, {'interface': IFloat, 'name': 'z', 'desc': ''}, {'interface': IFloat, 'name': 's', 'desc': ''}, {'interface': IFloat, 'name': 'n', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_ExtractTime = Factory(name='extract time',
                authors=' (wralea authors)',
                description='',
                category='Mtg, light',
                nodemodule='ratp',
                nodeclass='ExtractTime',
                inputs=None,
                outputs=None,
                widgetmodule=None,
                widgetclass=None,
               )




ratp_extract_leaves = Factory(name='extract leaves',
                authors=' (wralea authors)',
                description='',
                category='Mtg, light',
                nodemodule='ratp',
                nodeclass='extract_leaves',
                inputs=[{'name': 'mtg', 'desc': 'MTG file'}, {'interface': 'IFloat', 'name': 'scaling factor', 'value': 100}, {'interface': 'IFloat', 'name': 'nitrogen', 'value': 2.0}],
                outputs=[{'name': 'leaves_id', 'desc': 'vertex id for leaves '}, {'name': 'entity', 'desc': 'the vegetation type'}, {'name': 'X', 'desc': 'X coordinate'}, {'name': 'Y', 'desc': 'Y coordinate'}, {'name': 'Z', 'desc': 'Z coordinate'}, {'name': 'leaf area', 'desc': 'leaf area'}, {'name': 'leaf nitrogen', 'desc': 'leaf nitrogen'}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_read_vegetation = Factory(name='read_vegetation',
                authors=' (wralea authors)',
                description='read the vegetation files',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='read_vegetation',
                inputs=[{'interface': IFileStr(filter="*.vfn", save=False), 'name': 'filename', 'value': None, 'desc': 'Vegetation file'}],
                outputs=[{'interface': None, 'name': 'grid', 'desc': 'No output for the moment'}],
                widgetmodule=None,
                widgetclass=None,
               )




ratp_read_micrometeo = Factory(name='read_micrometeo',
                authors=' (wralea authors)',
                description='read the micrometeo files',
                category='Unclassified',
                nodemodule='ratp',
                nodeclass='read_micrometeo',
                inputs=[{'interface': IFileStr(filter="*.mto", save=False), 'name': 'filename', 'value': None, 'desc': 'Micrometeo file'}],
                outputs=[{'interface': None, 'name': 'grid', 'desc': 'No output for the moment'}],
                widgetmodule=None,
                widgetclass=None,
               )




ExtractVar_ExtractVar = Factory(name='ExtractVar',
                authors=' (wralea authors)',
                description='',
                category='data i/o',
                nodemodule='ExtractVar',
                nodeclass='ExtractVar',
                inputs=[{'interface': ISlice, 'name': 'IN1', 'value': None, 'desc': 'dfgd'}, {'interface': None, 'name': 'IN2', 'value': None, 'desc': 'dgdg'}],
                outputs=[{'interface': IInt, 'name': 'Column', 'desc': 'dfgfd'}, {'interface': IStr, 'name': 'Name', 'desc': 'dfgdfg'}],
                widgetmodule=None,
                widgetclass=None,
               )




RATP2VTK_RATP2VTK = Factory(name='RATP2VTK',
                authors=' (wralea authors)',
                description='Paraview file',
                category='data i/o',
                nodemodule='RATP2VTK',
                nodeclass='RATP2VTK',
                inputs=[{'interface': ISequence, 'name': 'Scene', 'value': None, 'desc': ''}, {'interface': ISequence, 'name': 'Variable', 'value': None, 'desc': ''}, {'interface': IStr, 'name': 'VariableName', 'value': 'Variable', 'desc': ''}],
                outputs=[{'interface': None, 'name': 'VTK File', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




