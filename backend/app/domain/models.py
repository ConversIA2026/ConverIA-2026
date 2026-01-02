# Definición del sistema de tipos del dominio , buscando modularidad y separación de responsabilidades.

from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from domain.states import ConversationState, UserState

#! Contratos del dominio (entities)
@dataclass
class Message:
    sender: str
    content: str
    timestamp: datetime | None = None 

@dataclass
class Conversation:
    id: str
    messages: List[Message] = field(default_factory=list)
    state: ConversationState = ConversationState.OPEN
    timestamp: datetime | None = None
    
@dataclass
class User:
    email: str
    name: str    
    password: str
    state: UserState = UserState.ACTIVE
    conversations: List[Conversation] = field(default_factory=list)
    created_at: datetime | None = None
    
@dataclass
class Business:
    id: str
    name: str
    users: List[User] = field(default_factory=list)
    created_at: datetime | None = None

@dataclass
class Appointment:
    id: str
    business_id: str
    user_id: str
    scheduled_at: datetime
    created_at: datetime | None = None
    
@dataclass
class Service:
    id: str
    business_id: str
    name: str
    description: str | None = None
    price: float | None = None
    created_at: datetime | None = None
    
@dataclass
class Settings:
    business_id: str
    notifications_enabled: bool = True
    theme: str | None = None
    created_at: datetime | None = None
    
@dataclass
class Notification:
    id: str
    user_id: str
    message: str
    read: bool = False
    created_at: datetime | None = None