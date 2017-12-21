#Nanako Chung (worked with Anusha Chintalapati)
#September 29th, 2016
#M/W Intro to Comp Programming
#Problem #3: Birthday Analyzer

#ask user for start and birth date
print("Instructions: Enter the start date and birthdate for an employee to determine their age at the start of employment.")
start_date=int(input("Enter start date MMDDYYYY: "))
birth_date=int(input("Enter birth date MMDDYYYY: "))

#extract ones place
startones=start_date%10
birthones=birth_date%10

#extract tens place
starttens=int((start_date%100)/10)
birthtens=int((birth_date%100)/10)

#entract hundreds
starthuns=int((start_date%1000)/100)
birthhuns=int((birth_date%1000)/100)

#extract thousands
startthou=int((start_date%10000)/1000)
birththou=int((birth_date%10000)/1000)

#extract ten thousands
starttenthou=int((start_date%100000)/10000)
birthtenthou=int((birth_date%100000)/10000)

#extract hundred thousands
starthunthou=int((start_date%1000000)/100000)
birthhunthou=int((birth_date%1000000)/100000)

#extract millions
startmil=int((start_date%10000000)/1000000)
birthmil=int((birth_date%10000000)/1000000)

#extract ten millions
starttenmil=int((start_date%1000000000)/100000000)
birthtenmil=int((birth_date%1000000000)/100000000)

#get the exact month
smonthten=str(starttenmil)
smonthone=str(startmil)
startmonth=smonthten+smonthone

bmonthten=str(birthtenmil)
bmonthone=str(birthmil)
birthmonth=bmonthten+bmonthone

#get exact day
sdayten=str(starthunthou)
sdayone=str(starttenthou)
startday=sdayten+sdayone

bdayten=str(birthhunthou)
bdayone=str(birthtenthou)
birthday=bdayten+bdayone

#get exact year
syearthou=str(startthou)
syearhun=str(starthuns)
syearten=str(starttens)
syearone=str(startones)
startyear=syearthou+syearhun+syearten+syearone

byearthou=str(birththou)
byearhun=str(birthhuns)
byearten=str(birthtens)
byearone=str(birthones)
birthyear=byearthou+byearhun+byearten+byearone

# list month
if birthmonth == "01":
    m="January"
elif birthmonth == "02":
    m="February"
elif birthmonth == "03":
    m="March"
elif birthmonth == "04":
    m="April"
elif birthmonth == "05":
    m="May"
elif birthmonth == "06":
    m="June"
elif birthmonth == "07":
    m="July"
elif birthmonth == "08":
    m="August"
elif birthmonth == "09":
    m="September"
elif birthmonth == "10":
    m="October"
elif birthmonth == "11":
    m="November"
elif birthmonth == "12":
    m="December"
else:
    m="Invalid month."
    
#list day with the proper grammar
if birthday == "01":
    d = "1" + "st"
elif birthday == "02":
    d = "2" + "nd"
elif birthday == "03":
    d = "3" + "rd"
elif birthday == "04":
    d = "4" + "th"
elif birthday == "05":
    d = "5" + "th"
elif birthday == "06":
    d = "6" + "th"
elif birthday == "07":
    d = "7" + "th"
elif birthday == "08":
    d = "8" + "th"
elif birthday == "09":
    d = "9" + "th"
elif birthday == "10" or "11" or "12" or "13" or "14" or "15" or "16" or "17" or "18" or "19" or "20" or "24" or "25" or "26" or "27" or "28" or "29" or "30":
    d = birthday + "th"
elif birthday == "21" or "31":
    d = birthday + "st"
elif birthday == "22":
    d = birthday + "nd"
elif birthday == "23":
    d = birthday + "rd"
else:
    d = "Invalid day."

print("The contestant was born on", " ", m, " ", d, ",", " ", birthyear, sep="")

#convert strings to integers
numberbirthyear = int(birthyear)
numberbirthmonth = int(birthmonth)
numberbirthday = int(birthday)

numberstartyear = int(startyear)
numberstartmonth = int(startmonth)
numberstartday = int(startday)

#determine if age is eligible by using if statements
if (numberstartyear - numberbirthyear)>21:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif (numberstartyear - numberbirthyear)==21:
    if numberstartmonth>numberbirthmonth:
        print("ELIGIBLE: The contestant will be 21 by the time taping begins")
    elif numberstartmonth==numberbirthmonth:
        if numberstartday==numberbirthday:
            print("ELIGIBLE: The contestant will be 21 by the time taping begins")
        elif numberstartday<numberbirthday:
            print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")      
        else:
            print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")      
    else:
        print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
else:
    print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
