import importlib, glob, json, os, random
from os.path import basename, isfile, join
from fastapi import FastAPI

__version__ = '0.1.0'

"""
Instantiate our FastAPI app.
"""
def create_app():
    app = FastAPI()

    @app.get('/')
    def welcome():
        return {'msg': "Run commands with commando!"}

    route_files = glob.glob(join('routes', "*.py"))
    modules = [basename(f)[:-3] for f in route_files if isfile(f) and not f.endswith('__init__.py')]
    for module in sorted(modules):
        module_path   = f"routes.{module}"
        router_module = importlib.import_module(module_path)
        app.include_router(router_module.router)

    return app
