from typing import Optional

class AppError(Exception):
    status_code = 400
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        if status_code:
            self.status_code = status_code
        self.message = message

    def to_dict(self):
        return {"error": self.message}