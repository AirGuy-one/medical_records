from uuid import UUID

from sqlalchemy.orm import Session

import models
import schemas


def create_patient(db: Session, patient_in: schemas.PatientCreate) -> models.Patient:
    db_obj = models.Patient(**patient_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_doctor(db: Session, doctor_in: schemas.DoctorCreate) -> models.Doctor:
    db_obj = models.Doctor(**doctor_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_visit(db: Session, visit_in: schemas.VisitCreate) -> models.Visit:
    db_obj = models.Visit(**visit_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_diagnosis(db: Session, visit_id: UUID, data: schemas.DiagnosisCreate) -> models.Diagnosis:
    db_obj = models.Diagnosis(**data.dict(), visit_id=visit_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_prescription(db: Session, visit_id: UUID, data: schemas.PrescriptionCreate) -> models.Prescription:
    db_obj = models.Prescription(**data.dict(), visit_id=visit_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_attachment(db: Session, visit_id: UUID, file_path: str) -> models.Attachment:
    db_obj = models.Attachment(visit_id=visit_id, file_path=file_path)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_history_by_patient(db: Session, patient_id: UUID) -> list[models.Visit]:
    return db.query(models.Visit).filter_by(patient_id=patient_id).all()
