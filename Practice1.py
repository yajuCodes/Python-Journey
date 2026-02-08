# Write a program to count vowels in a string.

text = input ("Enter a string:")

vowels = "AEIOUaeiou"
count = 0

for ch in text :
    if ch in vowels :
        count += 1
print("Number of vowels:", count)
print("My python journey begins")