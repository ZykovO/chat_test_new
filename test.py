from datetime import date, datetime, time
from typing import Union
from pydantic import BaseModel, constr
from fastapi import Form

class Ticket_new(BaseModel):
    internal_ticket_number : int
    external_ticket_number : str
    ticket_type : str
    ticket_text : str
    shop : str
    shop_city : str
    ticket_deadline : Union[datetime,str] = 'нет'
    time_to_deadline : int = 0
    performer_id : int
    message : str = None
class Ticket(BaseModel):
    internal_ticket_number : int
    external_ticket_number : str
    ticket_type : str
    ticket_text : str
    shop : str
    shop_city : str
    ticket_deadline : Union[datetime,str] = 'нет'
    time_to_deadline : int = 0
    performer_id : int
    message : str = None

class Comment(BaseModel):
    performer_id : int
    internal_ticket_number : int
    id : int
    text : str
    autor : str
    time : datetime

class Contractor(BaseModel):
    id : int
    name : str
    city : str
    region : str
    edrpou : str
    status : bool

class Performer(BaseModel):
    id : int
    contractor_id : int
    name : str
    notusedname : str
    phonenumber : str
    position : str
    id_employees_asu : int
    is_active : bool