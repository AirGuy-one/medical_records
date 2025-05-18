from uuid import UUID

from sqlalchemy.orm import Session

import models, schemas


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


def create_diagnosis(db: Session, diagnosis_in: schemas.DiagnosisCreate) -> models.Diagnosis:
    db_obj = models.Diagnosis(**diagnosis_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_prescription(db: Session, prescription_in: schemas.PrescriptionCreate) -> models.Prescription:
    db_obj = models.Prescription(**prescription_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_attachment(db: Session, attachment_in: schemas.AttachmentCreate) -> models.Attachment:
    db_obj = models.Attachment(**attachment_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_history_by_patient(db: Session, patient_id: UUID) -> list[models.Visit]:
    return db.query(models.Visit).filter_by(patient_id=patient_id).all()
