
# ==========================================
# AI TOOLKIT - ENTRY 2
# LLM Reliability & Hallucination Checker
# ==========================================

print("=" * 45)
print("       AI HALLUCINATION CHECKER")
print("=" * 45)

# Step 1: Collect information

ai_tool = input("\nEnter the AI tool name: ")

prompt = input("Enter the prompt you gave the AI: ")

claim = input("Enter the claim made by the AI: ")

# Step 2: Collect verification evidence

print("\n--- FACT VERIFICATION ---")

evidence = input(
    "Enter the evidence or source you checked: "
)

# Step 3: Classify the claim

print("\nSelect the result:")

print("1. Correct")
print("2. Incorrect")
print("3. Unsupported")
print("4. Unverified")

choice = input("Enter your choice (1-4): ")

results = {
    "1": "Correct",
    "2": "Incorrect",
    "3": "Unsupported",
    "4": "Unverified"
}

result = results.get(choice, "Unverified")

# Step 4: Determine hallucination status

if result == "Incorrect" or result == "Unsupported":
    hallucination = "Potential hallucination detected"
else:
    hallucination = "No hallucination established"

# Step 5: Record how the claim was checked

method = input(
    "\nHow did you verify or catch the claim? "
)

# Step 6: Generate investigation report

print("\n" + "=" * 45)
print("       INVESTIGATION REPORT")
print("=" * 45)

print("AI Tool:", ai_tool)

print("Original Prompt:", prompt)

print("AI Claim:", claim)

print("Evidence:", evidence)

print("Verification Result:", result)

print("Hallucination Status:", hallucination)

print("Detection Method:", method)

print("=" * 45)

print("\nInvestigation completed successfully!")
