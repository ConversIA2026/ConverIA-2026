# Se define estados específicos del dominio, como estados de usuario, estados de conversación, etc.
# Transiciones y validaciones asociadas a dichos estados.

from enum import Enum

# Estados explícitos para conversaciones y usuarios
class ConversationState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    PENDING = "pending"
    
class UserState(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
