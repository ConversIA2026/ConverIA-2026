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