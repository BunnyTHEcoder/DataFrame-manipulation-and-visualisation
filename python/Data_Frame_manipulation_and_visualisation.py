import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

print("Welcome to The DataFrame Statistician! \nProgrammed by Srishty M")
df=pd.DataFrame({})

while True:
    print("\nPlease choose from the following options: \n1 – Load data from a file \n2 – View data \n3 – Clean data \n4 – Analyse data \n5 – Visualise data \n6 - Save data to a file \n7 - Quit")
    inp = (input())
    
    if (not inp.isdigit()) or (int(inp) not in range(1,8)):
        print("Invalid selection!")
    else:
        choice=int(inp)
        if (choice == 7):
            print("Quiting")
            #break
            quit()
        if choice==1:
            print("Enter file name: ")
            finame=input()
            pathi=os.path.join(sys.path[0], finame)
            try:
                df = pd.read_csv(pathi)
            except FileNotFoundError:
                msg = "Sorry, the file does not exist."
                print(msg)
            except TypeError:
                print("Unable to load data")
            except:
                print("some error")

            while True:
                print("The columns are as follows. Choose one of them as index")
                print(list(df.columns))
                col=input()
                if col in df.columns:
                    df.set_index(col, inplace=True)
                    break
                elif col==" " or col=="":
                    break

        elif choice==2:
            print(df)

        elif choice==3:
            while True:
                print("\nCleaning data: \n1 - Drop rows with missing values \n2 - Fill missing values \n3 - Drop duplicate rows \n4 - Drop column \n5 - Rename column \n6 - Finish cleaning")
                order=input()
                if (not order.isdigit()) or (int(order) not in range(1,7)):
                    print("Invalid selection!")
                else:
                    c=int(order)
                    if c==1:
                        df.dropna(inplace=True)
                    elif c==2:
                        print("What value do you want to fill in the missing cell?")
                        val=input()
                        if not val.isdigit():
                            print("not a number")
                        else:
                            df.fillna(int(val), inplace=True)
                    elif c==3:
                        df.drop_duplicates(inplace=True)
                    elif c==4:
                        while True:
                            print("Choose a column to drop")
                            print(list(df.columns))
                            colu=input()
                            if colu in df.columns:
                                df.drop(colu,axis='columns', inplace=True)
                                break
                            elif colu==" " or colu=="":
                                break

                    elif c==5:
                        print("Choose a column to rename")
                        coln=input()
                        print("Enter a new name")
                        newn=input()
                        df.rename(columns = {coln:newn}, inplace=True)

                    elif c==6:
                        print("Back to menu")
                        break

        elif choice==4:
            for col in df.columns:
                print(df[col].describe())
                print(df.corr())

        elif choice==5:
            plot_opt=["bar","line","boxplot"]
            while True:
                print("choose on of the following:")
                print(plot_opt)
                grph=input()
                print("choose y-axis")
                print(list(df.columns))
                yl=input()
                if (grph in plot_opt) and (yl in df.columns):
                    if grph=="bar":
                        plt.bar(df.index, df[yl])
                    elif grph=="line":
                        plt.plot(df.index, df[yl])
                    elif grph=="boxplot":
                        plt.boxplot(df[yl])
                    print("What should be the title?")
                    tt=input()
                    if tt != "":
                        plt.title(tt)
                    print("Enter the x-axis label you want")
                    xl=input()
                    if xl !="":
                        plt.xlabel(xl)
                    print("Enter the y-axis label, you want")
                    yl=input()
                    if yl!="":
                        plt.ylabel(yl)
                    plt.show()
                    break
                else:
                    print("wrong input")
            
        elif choice==6:
            print("Enter file name you want to save as")
            filnm=input()
            if filnm!= "" or filnm!=" ":
                if ("." in filnm) and (filnm.split(".")[1]=="csv"):
                    fn=os.path.join(sys.path[0], filnm)
                else:
                    fn=os.path.join(sys.path[0], filnm+".csv")
                
                df.to_csv(fn)
                    







                    

