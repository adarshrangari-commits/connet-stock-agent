import json
import os

LEADS_FILE = "leads.json"

def load_leads():
    if not os.path.exists(LEADS_FILE):
        return []
    try:
        with open(LEADS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # fallback for newline-separated JSON
        leads = []
        with open(LEADS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    leads.append(json.loads(line))
                except:
                    pass
        return leads

def save_leads(leads):
    with open(LEADS_FILE, "w") as f:
        json.dump(leads, f, indent=2)

def capture_lead():
    name = input("Enter your name: ").strip() or None
    phone = input("Enter your phone: ").strip() or None
    city = input("Enter your city: ").strip() or None
    interest = input("Enter your interest (stocks, SIP, pre-IPO, etc.): ").strip() or None
    score = 50

    lead = {"name": name, "phone": phone, "city": city, "interest": interest, "score": score}

    leads = load_leads()
    leads.append(lead)
    save_leads(leads)

    print("\n✅ Lead captured successfully!")
    print(lead)

if __name__ == "__main__":
    capture_lead()
