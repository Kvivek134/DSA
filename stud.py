class Student:

    def setData(self):
        self.name = input("Enter Student Name: ")
        self.rollno = int(input("Enter Roll No: "))
        self.dsa = int(input("Enter DSA Marks: "))
        self.dbms = int(input("Enter DBMS Marks: "))
        self.react = int(input("Enter React Marks: "))

    def getData(self):
        print("\n----- Student Result -----")
        print("Name:", self.name)
        print("Roll No:", self.rollno)

        # Check Pass / Fail
        if self.dsa >= 40 and self.dbms >= 40 and self.react >= 40:
            total = self.dsa + self.dbms + self.react
            percentage = total / 3

            print("DSA:", self.dsa)
            print("DBMS:", self.dbms)
            print("React:", self.react)
            print("Percentage:", percentage, "%")
            print("Result: PASS")

        else:
            print("DSA:", self.dsa if self.dsa >= 40 else "-")
            print("DBMS:", self.dbms if self.dbms >= 40 else "-")
            print("React:", self.react if self.react >= 40 else "-")
            print("Percentage: -")
            print("Result: FAIL")
s1 = Student()
s1.setData()

# Display result
s1.getData()
