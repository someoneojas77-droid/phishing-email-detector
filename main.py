from model import detect_phishing_ml

print("===== Phishing Email Detector =====")

email = input("Enter email text:\n")

result = detect_phishing_ml(email)

print("\nResult:", result)