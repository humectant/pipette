from typing import Any

from celery import group, chord
from fastapi import APIRouter

from app.tasks.util import noop

router = APIRouter()


@router.post("/chain", status_code=201)
def run_chain() -> Any:
    """
    Run a simple Celery chain. Runs its tasks in a series.
    """
    chain = noop.s(1) | noop.s(2) | noop.s(3)
    res = chain()
    print(f"res: {res}")
    results = res.get()  # blocking
    print(f"results: {results}")
    return results


@router.post("/group", status_code=201)
def run_group() -> Any:
    """
    Run a simple Celery group. Runs its tasks in parallel.
    """
    workflow = (
        group([noop.s(i) for i in range(5)])
    )
    res = workflow()
    print(f"res: {res}")
    results = res.get()  # blocking
    print(f"results: {results}")
    return results


@router.post("/chord", status_code=201)
def run_chord() -> Any:
    """
    Run a simple Celery chord. Runs its tasks in parallel and then calls a final task.
    Chords require a backend and results be ignored.
    'you should avoid using chords as much as possible' - official Celery documentation
    """
    workflow = chord(
        [noop.s(i) for i in range(5)], noop.s(999)
    )
    res = workflow()
    print(f"res: {res}")
    results = res.get()  # blocking
    print(f"results: {results}")
    return results
