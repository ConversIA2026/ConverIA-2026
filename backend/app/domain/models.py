# Definición del sistema de tipos del dominio , buscando modularidad y separación de responsabilidades.

from dataclasses import dataclass, field
from typing import List
from domain.states import ConversationState, UserState


@dataclass
class Message:
    sender: str
    content: str
    timestamp: str 

@dataclass
class Conversation:
    id: str
    messages: List[Message] = field(default_factory=list)
    state: ConversationState = ConversationState.OPEN
    
@dataclass
class User:
    user_id: str
    username: str
    state: UserState = UserState.ACTIVE
    conversations: List[Conversation] = field(default_factory=list)