# Smart Study Planner - Basemera Hilda 
import os
FILE_NAME = "study_log.txt"
sessions = []

def classify_session(d):
    if d < 30: return "Short"
    elif d <= 90: return "Medium"
    else: return "Long"

def add_session():
    print("\n--- Add a Study Session ---")
    subject = input("Enter subject name: ").strip()
    topic = input("Enter topic: ").strip()
    date_label = input("Enter date/day: ").strip()
    while True:
        try:
            duration = float(input("Enter duration in minutes: "))
            if duration <=0:
                print("Must be positive")
                continue
            break
        except:
            print("Enter a number")
    sessions.append({"subject":subject,"topic":topic,"date":date_label,"duration":duration})
    print(f"Added! Type: {classify_session(duration)}")

def view_sessions():
    if not sessions:
        print("\nNo sessions")
        return
    print(f"\n{'Subject':<12} {'Topic':<12} {'Date':<10} {'Mins':<6} Type")
    print("-"*55)
    for s in sessions:
        print(f"{s['subject']:<12} {s['topic']:<12} {s['date']:<10} {s['duration']:<6} {classify_session(s['duration'])}")

def search_by_subject():
    q=input("\nEnter subject to search: ").strip().lower()
    found=[s for s in sessions if s['subject'].lower()==q]
    if not found:
        print(f"No sessions for '{q}'")
        return
    total=sum(s['duration'] for s in found)
    print(f"Found {len(found)} - Total {total} mins")
    for s in found:
        print(f" - {s['date']} | {s['topic']} | {s['duration']} mins")

def study_statistics():
    if not sessions:
        print("\nNo data")
        return
    total=sum(s['duration'] for s in sessions)
    print(f"\nTotal: {total/60:.2f} hrs")
    per={}
    for s in sessions:
        per[s['subject']]=per.get(s['subject'],0)+s['duration']
    for k,v in per.items():
        print(f" - {k}: {v/60:.2f} hrs")
    print(f"Weakest: {min(per,key=per.get)}")
    longest=max(sessions,key=lambda x:x['duration'])
    print(f"Longest: {longest['subject']} {longest['duration']} mins")

def save_sessions():
    with open(FILE_NAME,"w") as f:
        for s in sessions:
            f.write(f"{s['subject']},{s['topic']},{s['date']},{s['duration']}\n")
    print("Saved!")

def load_sessions():
    if not os.path.exists(FILE_NAME): return
    try:
        with open(FILE_NAME,"r") as f:
            for line in f:
                a,b,c,d=line.strip().split(",")
                sessions.append({"subject":a,"topic":b,"date":c,"duration":float(d)})
    except: pass

def main():
    load_sessions()
    while True:
        print("\n1.Add 2.View 3.Search 4.Stats 5.Save & Exit")
        ch=input("Choice: ")
        if ch=="1": add_session()
        elif ch=="2": view_sessions()
        elif ch=="3": search_by_subject()
        elif ch=="4": study_statistics()
        elif ch=="5": save_sessions(); break
        else: print("Invalid 1-5")

if __name__=="__main__":
    main()
