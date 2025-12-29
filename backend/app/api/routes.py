# Traductor entre HTTP y el dominio
# Estará recibiendo requests, llamando servicios del dominio y devolviendo respuestas HTTP (endpoints).

from fastapi import APIRouter, HTTPException  # type: ignore
from pydantic import BaseModel # type: ignore
from app.domain.models import Conversation
from app.services.conversation import receive_message
from app.storage.memory import get_conversation, save_conversation

router = APIRouter()

# BaseModel para validar la request
class MessageRequest(BaseModel):
    conversation_id: str
    sender: str
    content: str
    timestamp: str
    
@router.post("/messages")
def post_message(payload: MessageRequest):
    conversation = get_conversation(payload.conversation_id)
    
    if not conversation:
        # carga el estado actual de la respectiva conversación
        conversation = Conversation(id=payload.conversation_id)
        
    try:
        conversation = receive_message(
            conversation,
            sender=payload.sender,
            content=payload.content
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    save_conversation(conversation)

    return {
        "conversation_id": conversation.id,
        "messages": len(conversation.messages),
        "state": conversation.state
    }
