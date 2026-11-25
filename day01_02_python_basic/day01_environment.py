import sys
import platform

print("Hello SAP AI Journey!")
name = "Sagar"
skills = [
    "SAP",
    "BTP",
    "Python",
    "AI",
    "Agentic AI"
]
print(f"Developer: {name}")
print("My target: SAP Enterprise AI Architect")

for skill in skills:
    print(skill)

print("AI Agent Engineering - Day 1")
print("---------------------------")
print(f"Python version: {sys.version}")
print(f"Operating system: {platform.system()}")
print(f"Machine: {platform.machine()}")
print("Environment check: SUCCESS")
