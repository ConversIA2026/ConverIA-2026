from app.domain.models import Conversation, Message
from app.domain.states import ConversationState


# Aquí van las funciones y clases relacionadas con la gestión de conversaciones
def receive_message(conversation: Conversation, sender: str, content: str, timestamp: str) -> Conversation:
    """El servicio NO crea conversaciones, opera sobre entidades existentes y valida su estado
    siendo implícitamente una FSM
    """
    if conversation.state != ConversationState.OPEN:
        raise ValueError("Cannot receive messages in a closed or pending conversation.")
    
    message = Message(sender=sender, content=content, timestamp=timestamp)
    conversation.messages.append(message)
    
    return conversation
