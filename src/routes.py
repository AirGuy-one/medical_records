from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from database import get_db
from repositories import (
    create_patient,
    create_doctor,
    create_visit,
    create_diagnosis,
    create_prescription,
    create_attachment,
    get_history_by_patient,
)

router = APIRouter()


@router.post("/patients/", response_model=schemas.PatientOut)
def api_create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)


@router.post("/doctors/", response_model=schemas.DoctorOut)
def api_create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return create_doctor(db, doctor)


@router.post("/visits/", response_model=schemas.VisitOut)
def api_create_visit(visit: schemas.VisitCreate, db: Session = Depends(get_db)):
    return create_visit(db, visit)


@router.post("/visits/{visit_id}/diagnoses", response_model=schemas.DiagnosisOut)
def api_create_diagnosis(visit_id: UUID, diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db)):
    return create_diagnosis(db, diagnosis)


@router.post("/visits/{visit_id}/prescriptions", response_model=schemas.PrescriptionOut)
def api_create_prescription(visit_id: UUID, prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    return create_prescription(db, prescription)


@router.post("/visits/{visit_id}/attachments", response_model=schemas.AttachmentOut)
def api_create_attachment(visit_id: UUID, attachment: schemas.AttachmentCreate, db: Session = Depends(get_db)):
    return create_attachment(db, attachment)


@router.get("/patients/{patient_id}/history", response_model=list[schemas.VisitOut])
def api_get_history_by_patient(patient_id: UUID, db: Session = Depends(get_db)):
    return get_history_by_patient(db, patient_id)
