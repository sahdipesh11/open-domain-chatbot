from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, \
    QPushButton
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)
        self.setWindowTitle("Chatbot") # Add window title

        # Add chat area widget.
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320) # Parameters: x, y, w, h
        self.chat_area.setReadOnly(True) # Make it read only.

        # Add input field widget.
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>") # Append takes string input.
        self.input_field.clear() # Clear input field.

        # Get response and show it in the chat area with gray background.
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(
            f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")

app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())

