from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError

from models import BuildName
from utils import load_data, topo_sort

app = FastAPI()


@app.post("/get_tasks", response_model=List[str])
def get_tasks(build_name: BuildName):
    """
    Endpoint to get the list of tasks in topological order for a given build.
    """
    tasks, builds = load_data()
    try:
        return topo_sort(build_name.build, tasks, builds)
    except KeyError:
        raise HTTPException(
            status_code=400, detail="Build or task not found in yaml files")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc.errors()), status_code=400)
