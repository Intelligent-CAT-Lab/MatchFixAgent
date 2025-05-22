class Conversation:
    def __init__(self) -> None:
        self.messages = []

    def add_message(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})


class Session:
    def __init__(self, session_id: str) -> None:
        self.session_id = session_id


class MCPConfig:
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file


class Model:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
