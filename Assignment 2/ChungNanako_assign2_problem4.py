# Nanako Chung
# September 25th, 2016
# M/W 2-3:15 Intro to Comp Sci
# Problem #4: Data Size Converter

# prompt user to enter file size in KB, convert it to floating number, then print
kilobytes = input("Enter a file size, in kilobytes (KB): ")
float_kilobytes = float(kilobytes)
print()
print(kilobytes, "KB", "...")
print()

# convert kilobytes to bits using floating numbers and formatting
kilobytes_to_bits = float(8192*float_kilobytes)
fkilobytes_to_bits = format(kilobytes_to_bits, ",.2f")
fbits = format(fkilobytes_to_bits, ">27")
print("... in bits", fbits, "bits")

#convert bits to bytes using floating numbers and formatting
bits_to_bytes = float(kilobytes_to_bits/8)
fbits_to_bytes = format(bits_to_bytes, ",.2f")
fbytes = format(fbits_to_bytes, ">26")
print("... in bytes", fbytes, "bytes")

# convert kilobytes to megabytes using floating numbers and formatting
kilobytes_to_megabytes = float(float_kilobytes/1024)
fkilobytes_to_megabytes = format(kilobytes_to_megabytes, ",.2f")
fmegabytes = format(fkilobytes_to_megabytes, ">22")
print("... in megabytes", fmegabytes, "MB")

# convert megabytes to gigabytes using floating numbers and formatting
megabytes_to_gigabytes = float(kilobytes_to_megabytes/1024)
fmegabytes_to_gigabytes = format(megabytes_to_gigabytes, ",.2f")
fgigabytes = format(fmegabytes_to_gigabytes, ">22")
print("... in gigabytes", fgigabytes, "GB")

# at least five ways to "crash" the program are:
# 1. a syntax error; when i was working with the formatted variables, sometimes i would forget to put the "f" in front and Python would print the wrong thing!
# 2. run-time error; when i was working on converting kilobytes to bits, i sometimes received a runtime error as a result of multiplying a floating number and a string.
# 3. logic error; when i ran the code, a strange long repetitive number came up after converting kilobytes to bits. this was because i forgot to conver the kilobytes into a floating number, and so the string repeated itself several times instead of actually computing it
# 4. logic error; when i fixed the previous problem in #3, i got a result saying "inf". this was because i did not convert the new formatted values into floating numbers.
# 5. syntax error; sometimes i would put quotes around variables, converting them into a string rather than showing the value of the variable.
