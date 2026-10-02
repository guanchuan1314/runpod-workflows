import pathlib, runpy, sys
folder = pathlib.Path(__file__).resolve().parent
sys.argv = [str(folder.parent / 'model-tools/install_models.py'), '--manifest', str(folder / 'models.json'), *sys.argv[1:]]
runpy.run_path(str(folder.parent / 'model-tools/install_models.py'), run_name='__main__')
