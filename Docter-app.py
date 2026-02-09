import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
from datetime import datetime

# ------------------------------------
# 1. ENHANCED DATABASE (List of Dictionaries)
# ------------------------------------
diseases = [
    {
        "name": "Asthma",
        "symptoms": "Shortness of breath, Chest tightness, Wheezing, Coughing, Difficulty breathing at night.",
        "prevention": "Avoid triggers (smoke, dust, pollen), Regular exercise, Maintain healthy weight, Use air purifiers.",
        "medicines": "Inhalers (Albuterol, Salbutamol), Corticosteroids (Fluticasone), Leukotriene modifiers.",
        "advice": "Consult a pulmonologist regularly. Always carry your rescue inhaler. Create an asthma action plan.",
        "severity": "Moderate to Severe",
        "specialist": "Pulmonologist",
        "emergency": "If unable to speak or blue lips, seek immediate help"
    },
    {
        "name": "Diabetes Type 2",
        "symptoms": "Increased thirst, Frequent urination, Extreme hunger, Fatigue, Blurred vision, Slow healing wounds.",
        "prevention": "Balanced diet (low glycemic index), Regular exercise (150 min/week), Maintain BMI < 25, Regular checkups.",
        "medicines": "Metformin, Insulin therapy, SGLT2 inhibitors, DPP-4 inhibitors.",
        "advice": "Monitor blood glucose daily. Regular foot examination. Annual eye checkup. Stay hydrated.",
        "severity": "Chronic",
        "specialist": "Endocrinologist",
        "emergency": "If blood sugar > 300 mg/dL or < 70 mg/dL with confusion"
    },
    {
        "name": "Influenza (Flu)",
        "symptoms": "High fever (100°F+), Body aches, Chills, Fatigue, Dry cough, Sore throat.",
        "prevention": "Annual flu vaccination, Frequent hand washing, Avoid close contact, Boost immunity with Vitamin C.",
        "medicines": "Oseltamivir (Tamiflu), Zanamivir, Paracetamol for fever, Antihistamines.",
        "advice": "Rest for 5-7 days. Drink 2-3 liters of water daily. Isolate to prevent spread.",
        "severity": "Mild to Moderate",
        "specialist": "General Physician",
        "emergency": "Difficulty breathing or chest pain"
    },
    {
        "name": "Hypertension",
        "symptoms": "Headaches, Shortness of breath, Nosebleeds, Flushing, Dizziness (often asymptomatic).",
        "prevention": "DASH diet (low sodium), Regular aerobic exercise, Limit alcohol to 1 drink/day, Stress management.",
        "medicines": "ACE inhibitors (Lisinopril), Beta-blockers (Metoprolol), Calcium channel blockers, Diuretics.",
        "advice": "Monitor BP twice daily. Reduce caffeine. Practice meditation. Limit processed foods.",
        "severity": "Chronic",
        "specialist": "Cardiologist",
        "emergency": "BP > 180/120 mmHg with headache/vision changes"
    },
    {
        "name": "COVID-19",
        "symptoms": "Fever >100.4°F, Dry cough, Loss of taste/smell, Fatigue, Body aches, Sore throat.",
        "prevention": "Vaccination + boosters, N95 masks in crowded places, Social distancing, Ventilation.",
        "medicines": "Paxlovid (if eligible), Molnupiravir, Dexamethasone (severe cases), Symptomatic treatment.",
        "advice": "Isolate for 5 days minimum. Monitor oxygen saturation (should be >94%). Use pulse oximeter.",
        "severity": "Mild to Critical",
        "specialist": "Infectious Disease Specialist",
        "emergency": "Oxygen saturation < 92% or difficulty breathing"
    },
    {
        "name": "Migraine",
        "symptoms": "Throbbing headache (usually one side), Nausea, Vomiting, Sensitivity to light/sound/smell, Aura.",
        "prevention": "Identify triggers (chocolate, cheese, stress), Regular sleep schedule, Stay hydrated, Manage stress.",
        "medicines": "Triptans (Sumatriptan), NSAIDs (Ibuprofen), Anti-nausea drugs, Preventive medications.",
        "advice": "Rest in dark, quiet room. Apply cold compress to forehead. Keep migraine diary.",
        "severity": "Moderate to Severe",
        "specialist": "Neurologist",
        "emergency": "Sudden severe headache or with fever/stiff neck"
    },
    {
        "name": "Seasonal Allergy",
        "symptoms": "Sneezing, Runny/stuffy nose, Itchy eyes/nose/throat, Watery eyes, Postnasal drip.",
        "prevention": "Check pollen forecast, Keep windows closed, Use HEPA filters, Shower after outdoor activities.",
        "medicines": "Antihistamines (Cetirizine, Loratadine), Nasal corticosteroids, Decongestants, Eye drops.",
        "advice": "Start medication before allergy season. Wear sunglasses outside. Use saline nasal rinse.",
        "severity": "Mild to Moderate",
        "specialist": "Allergist",
        "emergency": "Difficulty breathing or throat swelling"
    },
    {
        "name": "Gastroenteritis",
        "symptoms": "Diarrhea, Nausea, Vomiting, Stomach cramps, Low-grade fever, Loss of appetite.",
        "prevention": "Proper hand hygiene, Safe food handling, Drink clean water, Avoid undercooked food.",
        "medicines": "Oral rehydration salts, Anti-diarrheals (Loperamide), Probiotics, Zinc supplements.",
        "advice": "BRAT diet (Bananas, Rice, Applesauce, Toast). Small frequent meals. Rest digestive system.",
        "severity": "Mild to Severe",
        "specialist": "Gastroenterologist",
        "emergency": "Signs of dehydration or blood in stool"
    },
    {
        "name": "Arthritis",
        "symptoms": "Joint pain, Stiffness (worse in morning), Swelling, Reduced range of motion, Redness around joints.",
        "prevention": "Maintain healthy weight, Regular low-impact exercise, Protect joints, Omega-3 supplements.",
        "medicines": "NSAIDs (Naproxen), DMARDs, Corticosteroid injections, Biologic response modifiers.",
        "advice": "Apply heat/cold therapy. Use assistive devices. Practice gentle stretching. Stay active.",
        "severity": "Chronic",
        "specialist": "Rheumatologist",
        "emergency": "Sudden severe joint swelling with fever"
    },
    {
        "name": "Anxiety Disorder",
        "symptoms": "Excessive worry, Restlessness, Fatigue, Difficulty concentrating, Irritability, Sleep problems.",
        "prevention": "Regular exercise, Mindfulness meditation, Limit caffeine/alcohol, Maintain sleep schedule.",
        "medicines": "SSRIs (Sertraline), SNRIs, Benzodiazepines (short-term), Buspirone.",
        "advice": "Practice deep breathing. Challenge negative thoughts. Keep a worry journal. Seek therapy.",
        "severity": "Mild to Severe",
        "specialist": "Psychiatrist/Psychologist",
        "emergency": "Panic attacks with chest pain or suicidal thoughts"
    }
]

# Store original disease names for reset
all_disease_names = [d["name"] for d in diseases]

# Search history
search_history = []

def show_disease_info():
    selected_disease_name = disease_combo.get()
    
    if not selected_disease_name:
        messagebox.showwarning("Selection Missing", "Please select a disease first!")
        return

    user_name = entry_name.get().strip()
    if not user_name:
        messagebox.showwarning("Input Missing", "Please enter your name.")
        return
    
    user_age = entry_age.get().strip()
    if user_age and not user_age.isdigit():
        messagebox.showwarning("Invalid Input", "Age must be a number.")
        return
    
    # Add to search history with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    search_history.append({
        "timestamp": timestamp,
        "user": user_name,
        "disease": selected_disease_name,
        "age": user_age if user_age else "Not specified"
    })
    
    # Update history display
    update_history_display()

    # Find disease data
    found_data = None
    for item in diseases:
        if item["name"] == selected_disease_name:
            found_data = item
            break
    
    if found_data:
        # Update the UI with disease info
        lbl_result_symptoms.config(text=found_data["symptoms"])
        lbl_result_prevention.config(text=found_data["prevention"])
        lbl_result_medicines.config(text=found_data["medicines"])
        lbl_result_advice.config(text=found_data["advice"])
        lbl_result_severity.config(text=found_data["severity"])
        lbl_result_specialist.config(text=found_data["specialist"])
        lbl_result_emergency.config(text=found_data["emergency"])
        
        # Update status with user info
        age_text = f", Age: {user_age}" if user_age else ""
        lbl_status.config(
            text=f"Showing details for: {selected_disease_name} (Patient: {user_name}{age_text})", 
            fg="#2ecc71"
        )
        
        # Update risk indicator based on age
        if user_age:
            age = int(user_age)
            if age > 60 and found_data["severity"] in ["Chronic", "Moderate to Severe"]:
                lbl_risk.config(text="⚠️ Higher Risk (Age > 60)", fg="#e74c3c", bg="#fadbd8")
            elif age < 10 and found_data["name"] in ["Influenza (Flu)", "COVID-19"]:
                lbl_risk.config(text="⚠️ Monitor Closely", fg="#f39c12", bg="#fef5e7")
            else:
                lbl_risk.config(text="✅ Standard Care", fg="#27ae60", bg="#d5f4e6")
    else:
        messagebox.showerror("Error", "Disease data not found!")

def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    disease_combo.set('')  # Clear selection
    gender_var.set("Male")
    
    # Reset combobox to all diseases
    disease_combo['values'] = all_disease_names
    
    # Clear results
    lbl_result_symptoms.config(text="-")
    lbl_result_prevention.config(text="-")
    lbl_result_medicines.config(text="-")
    lbl_result_advice.config(text="-")
    lbl_result_severity.config(text="-")
    lbl_result_specialist.config(text="-")
    lbl_result_emergency.config(text="-")
    
    lbl_status.config(text="Form cleared. Select a disease to begin.", fg="#7f8c8d")
    lbl_risk.config(text="Risk Level: Not assessed", fg="#95a5a6", bg="#f0f4f8")

def get_search_suggestions(search_term):
    """Get matching suggestions for search term"""
    suggestions = []
    search_term = search_term.lower().strip()
    
    if not search_term:
        return []
    
    for disease in diseases:
        # Check in disease name
        if search_term in disease["name"].lower():
            suggestions.append(disease["name"])
            continue
        
        # Check in symptoms
        if search_term in disease["symptoms"].lower():
            suggestions.append(disease["name"])
            continue
        
        # Check in specialist
        if search_term in disease["specialist"].lower():
            suggestions.append(disease["name"])
            continue
        
        # Check in medicines
        if search_term in disease["medicines"].lower():
            suggestions.append(disease["name"])
            continue
        
        # Check in severity
        if search_term in disease["severity"].lower():
            suggestions.append(disease["name"])
            continue
    
    # Remove duplicates while preserving order
    seen = set()
    unique_suggestions = []
    for suggestion in suggestions:
        if suggestion not in seen:
            seen.add(suggestion)
            unique_suggestions.append(suggestion)
    
    return unique_suggestions

def update_suggestions(event=None):
    """Update suggestion list based on current search text"""
    search_term = entry_search.get().strip()
    
    if search_term:
        suggestions = get_search_suggestions(search_term)
        if suggestions:
            # Show suggestions in a listbox
            suggestion_listbox.delete(0, tk.END)
            for suggestion in suggestions[:5]:  # Show max 5 suggestions
                suggestion_listbox.insert(tk.END, suggestion)
            
            # Position the listbox below the search entry
            x = entry_search.winfo_rootx() - root.winfo_rootx()
            y = entry_search.winfo_rooty() - root.winfo_rooty() + entry_search.winfo_height()
            suggestion_listbox.place(x=x, y=y, width=entry_search.winfo_width())
            suggestion_listbox.lift()
        else:
            suggestion_listbox.place_forget()
    else:
        suggestion_listbox.place_forget()

def on_suggestion_select(event):
    """When a suggestion is selected, populate search and disease dropdown"""
    if suggestion_listbox.curselection():
        selected = suggestion_listbox.get(suggestion_listbox.curselection())
        entry_search.delete(0, tk.END)
        entry_search.insert(0, selected)
        suggestion_listbox.place_forget()
        
        # Also update the disease dropdown
        search_disease_from_suggestion(selected)

def search_disease_from_suggestion(disease_name):
    """Search for a disease when selected from suggestions"""
    matching_diseases = []
    for disease in diseases:
        if disease["name"] == disease_name:
            matching_diseases.append(disease["name"])
            break
    
    if matching_diseases:
        disease_combo['values'] = matching_diseases
        disease_combo.set(disease_name)
        lbl_status.config(text=f"Selected: {disease_name}", fg="#3498db")

def search_disease(event=None):
    search_term = entry_search.get().strip().lower()
    if not search_term:
        return
    
    matching_diseases = []
    for disease in diseases:
        if (search_term in disease["name"].lower() or 
            search_term in disease["symptoms"].lower() or
            search_term in disease["specialist"].lower()):
            matching_diseases.append(disease["name"])
    
    if matching_diseases:
        disease_combo['values'] = matching_diseases
        disease_combo.set(matching_diseases[0])
        lbl_status.config(text=f"Found {len(matching_diseases)} matching disease(s)", fg="#3498db")
        suggestion_listbox.place_forget()  # Hide suggestions after search
    else:
        messagebox.showinfo("No Results", f"No diseases found matching '{search_term}'")
        # Reset to full list
        disease_combo['values'] = all_disease_names
        disease_combo.current(0)

def reset_search():
    disease_combo['values'] = all_disease_names
    disease_combo.current(0)
    entry_search.delete(0, tk.END)
    suggestion_listbox.place_forget()
    lbl_status.config(text="Search reset to all diseases", fg="#7f8c8d")

def update_history_display():
    # Show last 3 searches
    history_text = ""
    for i, record in enumerate(reversed(search_history[-3:])):
        history_text += f"{record['timestamp']}: {record['user']} → {record['disease']}\n"
    
    if history_text:
        lbl_history.config(text=history_text)
    else:
        lbl_history.config(text="No search history yet")

def show_about():
    messagebox.showinfo("About Disease Info System",
                       "Disease Information System v2.0\n\n"
                       "Features:\n"
                       "• 10+ disease profiles\n"
                       "• Search functionality\n"
                       "• Risk assessment\n"
                       "• Search history\n"
                       "• Emergency guidelines\n\n"
                       "For educational purposes only.\n"
                       "Always consult a healthcare professional.")

# ------------------------------------
# 3. MODERN GUI SETUP
# ------------------------------------
root = tk.Tk()
root.title("KIU HealthMate Pro - Disease Information System")
root.geometry("800x900")
root.configure(bg="#f8f9fa")
root.resizable(True, True)

# Custom fonts
header_font = Font(family="Segoe UI", size=22, weight="bold")
sub_header_font = Font(family="Segoe UI", size=14, weight="bold")
normal_font = Font(family="Segoe UI", size=11)
label_font = Font(family="Segoe UI", size=10, weight="bold")
small_font = Font(family="Segoe UI", size=9)

# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=normal_font, padding=6)
style.configure('TCombobox', font=normal_font)

# --- Header with gradient effect ---
header_frame = tk.Frame(root, bg="#3498db", height=80)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

lbl_title = tk.Label(header_frame, 
                    text="🏥 KIU HealthMate Pro", 
                    font=header_font, 
                    bg="#3498db", 
                    fg="white")
lbl_title.pack(pady=20)

# --- Search Bar with Suggestions ---
search_frame = tk.Frame(root, bg="#f8f9fa", padx=20, pady=10)
search_frame.pack(fill=tk.X)

tk.Label(search_frame, text="Quick Search:", font=label_font, bg="#f8f9fa").pack(side=tk.LEFT, padx=(0, 10))
entry_search = tk.Entry(search_frame, font=normal_font, width=25, relief=tk.SOLID, bd=1)
entry_search.pack(side=tk.LEFT, padx=5)
entry_search.bind('<KeyRelease>', update_suggestions)
entry_search.bind('<Return>', search_disease)  # Press Enter to search

btn_search = tk.Button(search_frame, text="🔍 Search", font=small_font, bg="#3498db", fg="white",
                      command=search_disease, cursor="hand2", relief=tk.FLAT, padx=15)
btn_search.pack(side=tk.LEFT, padx=5)

btn_reset = tk.Button(search_frame, text="Reset", font=small_font, bg="#95a5a6", fg="white",
                     command=reset_search, cursor="hand2", relief=tk.FLAT, padx=15)
btn_reset.pack(side=tk.LEFT, padx=5)

# Suggestion Listbox
suggestion_listbox = tk.Listbox(root, font=normal_font, height=5, bg="white", 
                                selectbackground="#3498db", selectforeground="white",
                                relief=tk.SOLID, bd=1)
suggestion_listbox.bind('<ButtonRelease-1>', on_suggestion_select)
suggestion_listbox.bind('<Return>', on_suggestion_select)

# --- Main Content Frame ---
main_container = tk.Frame(root, bg="#ecf0f1")
main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Left Panel (Input)
left_panel = tk.Frame(main_container, bg="white", bd=1, relief=tk.RIDGE, padx=20, pady=20)
left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))

# Right Panel (Output)
right_panel = tk.Frame(main_container, bg="white", bd=1, relief=tk.RIDGE, padx=20, pady=20)
right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# --- Left Panel Content ---
tk.Label(left_panel, text="👤 Patient Information", font=sub_header_font, bg="white", fg="#2c3e50").pack(anchor="w", pady=(0, 15))

# Patient Details Grid
input_grid = tk.Frame(left_panel, bg="white")
input_grid.pack(fill=tk.X)

# Name
tk.Label(input_grid, text="Full Name:", font=label_font, bg="white").grid(row=0, column=0, sticky="w", pady=8)
entry_name = tk.Entry(input_grid, font=normal_font, width=25, relief=tk.SOLID, bd=1)
entry_name.grid(row=0, column=1, padx=10, pady=8)

# Age
tk.Label(input_grid, text="Age:", font=label_font, bg="white").grid(row=1, column=0, sticky="w", pady=8)
entry_age = tk.Entry(input_grid, font=normal_font, width=10, relief=tk.SOLID, bd=1)
entry_age.grid(row=1, column=1, sticky="w", padx=10, pady=8)

# Gender
tk.Label(input_grid, text="Gender:", font=label_font, bg="white").grid(row=2, column=0, sticky="w", pady=8)
gender_frame = tk.Frame(input_grid, bg="white")
gender_frame.grid(row=2, column=1, sticky="w", padx=10)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", 
               bg="white", font=normal_font, selectcolor="#d6eaf8").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", 
               bg="white", font=normal_font, selectcolor="#fadbd8").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", 
               bg="white", font=normal_font, selectcolor="#fef9e7").pack(side=tk.LEFT)

# Disease Selection
tk.Label(left_panel, text="🩺 Select Disease", font=sub_header_font, bg="white", fg="#2c3e50").pack(anchor="w", pady=(20, 10))

disease_combo = ttk.Combobox(left_panel, values=all_disease_names, font=normal_font, state="readonly", width=28)
disease_combo.pack(pady=(0, 10))
disease_combo.current(0)

# Action Buttons
btn_frame = tk.Frame(left_panel, bg="white")
btn_frame.pack(pady=20)

btn_submit = tk.Button(btn_frame, text="📋 Get Details", font=label_font, bg="#27ae60", fg="white",
                      command=show_disease_info, cursor="hand2", relief=tk.RAISED, padx=20, pady=8)
btn_submit.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(btn_frame, text="🗑️ Clear", font=label_font, bg="#e74c3c", fg="white",
                     command=clear_form, cursor="hand2", relief=tk.RAISED, padx=20, pady=8)
btn_clear.pack(side=tk.LEFT, padx=5)

btn_about = tk.Button(left_panel, text="ℹ️ About", font=small_font, bg="#7f8c8d", fg="white",
                     command=show_about, cursor="hand2", relief=tk.FLAT)
btn_about.pack(pady=(10, 0))

# Status and Risk
lbl_status = tk.Label(left_panel, text="Enter details and select a disease", font=small_font, bg="white", fg="#7f8c8d")
lbl_status.pack(pady=(20, 5))

lbl_risk = tk.Label(left_panel, text="Risk Level: Not assessed", font=label_font, bg="#f0f4f8", 
                   relief=tk.SOLID, bd=1, padx=10, pady=5)
lbl_risk.pack(pady=10, fill=tk.X)

# Search History
tk.Label(left_panel, text="📜 Recent Searches", font=label_font, bg="white", fg="#34495e").pack(anchor="w", pady=(20, 5))
lbl_history = tk.Label(left_panel, text="No search history yet", font=small_font, bg="#f8f9fa", 
                      relief=tk.SUNKEN, bd=1, height=4, anchor="nw", justify="left", padx=10, pady=5)
lbl_history.pack(fill=tk.X)

# --- Right Panel Content ---
tk.Label(right_panel, text="📊 Disease Information", font=sub_header_font, bg="white", fg="#2c3e50").pack(anchor="w", pady=(0, 15))

# Disease Info Display
info_frame = tk.Frame(right_panel, bg="white")
info_frame.pack(fill=tk.BOTH, expand=True)

# Create info sections with icons
def create_info_section(parent, icon, title, row):
    # Title frame
    title_frame = tk.Frame(parent, bg="white")
    title_frame.grid(row=row, column=0, columnspan=2, sticky="w", pady=(15, 5))
    
    tk.Label(title_frame, text=icon, font=("Segoe UI", 12), bg="white").pack(side=tk.LEFT, padx=(0, 5))
    tk.Label(title_frame, text=title, font=label_font, bg="white", fg="#2980b9").pack(side=tk.LEFT)
    
    # Content label
    content = tk.Label(parent, text="-", font=normal_font, bg="white", wraplength=400, 
                      justify="left", anchor="w", padx=20)
    content.grid(row=row+1, column=0, columnspan=2, sticky="w", pady=(0, 10))
    
    # Separator
    separator = tk.Frame(parent, height=1, bg="#ecf0f1")
    separator.grid(row=row+2, column=0, columnspan=2, sticky="ew", pady=5)
    
    return content

# Create all sections
lbl_result_symptoms = create_info_section(info_frame, "🤒", "Symptoms", 0)
lbl_result_prevention = create_info_section(info_frame, "🛡️", "Prevention", 3)
lbl_result_medicines = create_info_section(info_frame, "💊", "Medications", 6)
lbl_result_advice = create_info_section(info_frame, "👨‍⚕️", "Medical Advice", 9)

# Additional info in a separate frame
extra_frame = tk.Frame(right_panel, bg="white", relief=tk.GROOVE, bd=1)
extra_frame.pack(fill=tk.X, pady=(20, 0))

tk.Label(extra_frame, text="Additional Information", font=label_font, bg="#f8f9fa", 
        fg="#2c3e50").pack(fill=tk.X, pady=5)

# Grid for extra info
extra_grid = tk.Frame(extra_frame, bg="white", padx=10, pady=10)
extra_grid.pack()

# Severity
tk.Label(extra_grid, text="Severity Level:", font=label_font, bg="white").grid(row=0, column=0, sticky="w", pady=5)
lbl_result_severity = tk.Label(extra_grid, text="-", font=normal_font, bg="white")
lbl_result_severity.grid(row=0, column=1, sticky="w", padx=10, pady=5)

# Specialist
tk.Label(extra_grid, text="Consult:", font=label_font, bg="white").grid(row=1, column=0, sticky="w", pady=5)
lbl_result_specialist = tk.Label(extra_grid, text="-", font=normal_font, bg="white")
lbl_result_specialist.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Emergency
tk.Label(extra_grid, text="🚨 Emergency Signs:", font=label_font, bg="white", fg="#e74c3c").grid(row=2, column=0, sticky="w", pady=5)
lbl_result_emergency = tk.Label(extra_grid, text="-", font=normal_font, bg="white", fg="#e74c3c", wraplength=300)
lbl_result_emergency.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Footer
footer = tk.Label(root, text="⚠️ Disclaimer: This is for informational purposes only. Always consult a healthcare professional for medical advice.",
                 font=small_font, bg="#f8f9fa", fg="#7f8c8d", pady=10)
footer.pack(fill=tk.X, side=tk.BOTTOM)

# Hide suggestion listbox initially
suggestion_listbox.place_forget()

# Start the application
root.mainloop()
