def getinput():

    name=str(input("Enter student name:"))
    marks=int(input("Enter marks (0-100):"))

    while marks<0 or marks>100:
        print("invalid marks!Enter marks between 0 to 100.")
        marks = int(input("Enter marks (0-100):"))

    return name,marks

def grade(m):

    if m>=90 and m<=100:
        Grade="A"
        Message="Outstanding! 🌟 Keep shining! 🎉"

    elif m>=80 and m<=89:
        Grade = "B"
        Message = "Very Good! 👍 Keep it up! 🔥"

    elif m>=70 and m<=79:
        Grade = "C"
        Message = "Good effort! 😃 Keep improving! 💪"

    elif m>=60 and m<=69:
        Grade = "D"
        Message = "Nice try! ✨ Keep practicing! 📚"

    else:
        Grade = "F"
        Message = "Don’t give up! 🌱 Work harder and you’ll succeed! 💡"


    return Grade,Message

def Result(name,marks,Grade,Message):

    print("RESULT OF",name.upper(),":")
    print("MARKS:",marks,"/100")
    print("Grade:",Grade)
    print("Message:",Message)


def main():
    name,marks=getinput()
    Grade, Message=grade(marks)
    Result(name,marks,Grade,Message)

main()
