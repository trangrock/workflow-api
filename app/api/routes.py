from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.api.models import Workflow
from app.db.models import get_db, Workflow as WorkflowData, Component as ComponentData

router = APIRouter()

# Endpoint to create new workflow and add data into the database
@router.post("/workflow/")
async def create_workflow(workflow: Workflow, db: Session = Depends(get_db)):
    try:
        # Create SQLAlchemy models for the workflow and its components
        db_workflow = WorkflowData(name = workflow.name)
        db_components = [ComponentData(type=c.type, settings=c.settings) for c in workflow.components]

        # Add components to the workflow
        db_workflow.components = db_components

        # Add the workflow to the database session and commit changes
        db.add(db_workflow)
        db.commit()
        db.refresh(db_workflow)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "Workflow created successfully", "workflow": db_workflow}


# Endpoint to query all workflows from the database
@router.get("/workflow/", response_model=List[Workflow])
async def get_all_workflows(db: Session = Depends(get_db)):
    results = []
    try:
        data = db.query(WorkflowData).all()
        results = [item.__dict__ for item in data]  # Convert SQLAlchemy ORM objects to dicts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return results


# Endpoint to query a workflow by id from the database
@router.get("/workflow/{workflow_id}", response_model=Workflow)
async def get_workflow(workflow_id: int, db: Session = Depends(get_db)):
    results = []
    try:
        data = db.query(WorkflowData).filter(WorkflowData.id == workflow_id).first()
        if not data:
            return {"message": "No workflow with this id was found"}
        else:
            results = data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return results
