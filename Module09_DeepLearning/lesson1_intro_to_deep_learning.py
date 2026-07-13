import tensorflow as tf

print("=" * 40)
print("Module 09 - Deep Learning")
print("Lesson 1 - Introduction to Deep Learning")
print("=" * 40)

print(f"TensorFlow Version: {tf.__version__}")

print("\nDeep Learning is a subset of Machine Learning.")
print("It uses Artificial Neural Networks (ANNs) with multiple hidden layers.")
print("These layers automatically learn patterns from data.")

print("\nReal-World Applications:")
applications = [
    "Image Recognition",
    "Speech Recognition",
    "Natural Language Processing (ChatGPT)",
    "Self-Driving Cars",
    "Medical Diagnosis"
]

for i, app in enumerate(applications, start=1):
    print(f"{i}. {app}")