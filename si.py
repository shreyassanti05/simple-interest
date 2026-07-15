# Simple Interest Calculator

print("==================================")
print("    Simple Interest Calculator")
print("==================================")

# Input
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display Results
print("\n========== Result ==========")
print(f"Principal Amount : {principal}")
print(f"Rate of Interest : {rate}%")
print(f"Time             : {time} years")
print(f"Simple Interest  : {simple_interest:.2f}")
print(f"Total Amount     : {principal + simple_interest:.2f}")
print("============================")