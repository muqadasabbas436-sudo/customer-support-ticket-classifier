# Customer Support Ticket Classifier - Built by Muqadas Abbas
import csv

def classify_ticket(message):
    message = message.lower()
    if "late" in message or "failed" in message or "damaged" in message:
        return "Complaint"
    else:
        return "Inquiry"

# Read and classify from CSV
with open('Tickets.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ticket = row['message']
        category = classify_ticket(ticket)
        print(f"Ticket: {ticket} -> Category: {category}")
