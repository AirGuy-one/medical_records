from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PatientCreate(BaseModel):
    full_name: str
    birth_date: datetime | None = None


class PatientOut(BaseModel):
    id: UUID
    full_name: str
    birth_date: datetime | None

    model_config = {"from_attributes": True}


class DoctorCreate(BaseModel):
    full_name: str
    specialization: str | None = None


class DoctorOut(BaseModel):
    id: UUID
    full_name: str
    specialization: str | None

    model_config = {"from_attributes": True}


class VisitCreate(BaseModel):
    patient_id: UUID
    doctor_id: UUID


class VisitOut(BaseModel):
    id: UUID
    patient_id: UUID
    doctor_id: UUID
    visit_date: datetime

    model_config = {"from_attributes": True}


class DiagnosisCreate(BaseModel):
    visit_id: UUID
    code: str
    description: str | None = None


class DiagnosisOut(BaseModel):
    id: UUID
    code: str
    description: str | None
    visit_id: UUID

    model_config = {"from_attributes": True}


class PrescriptionCreate(BaseModel):
    visit_id: UUID
    text: str


class PrescriptionOut(BaseModel):
    id: UUID
    text: str
    visit_id: UUID

    model_config = {"from_attributes": True}


class AttachmentCreate(BaseModel):
    visit_id: UUID
    file_path: str


class AttachmentOut(BaseModel):
    id: UUID
    file_path: str
    uploaded_at: datetime
    visit_id: UUID

    model_config = {"from_attributes": True}
