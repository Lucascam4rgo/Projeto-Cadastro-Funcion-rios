from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

