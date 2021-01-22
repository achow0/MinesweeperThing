def test(x):
    return "s"*(1-(x==1))

def timeFunc(x):
    out=""
    for j,i in enumerate([86400, 3600, 60, 1]):
        if j==0:
            days=x//i
            out+=f"{days} day{test(days)} "
        else:
            unit=(x%[86400, 3600, 60, 1][j-1])//i
            out+=f"{unit} {['hour', 'minute', 'second'][j-1]}{test(unit)} "
    return out

fout=open("stats.txt","w")

readList=[]
for i in ["Easy", "Medium", "Hard"]:
    fin=open(f"{i.lower()}.txt")
    splitList=fin.read().splitlines()
    intSplitList=[int(a) for a in splitList]
    readList.append([i, intSplitList])

for info in readList:
    difficulty=info[0]
    times=info[1]
    fout.write(f"{difficulty} Difficulty\n")
    fout.write(f"{'-'*78}\n")
    Length=len(times)
    total=sum(times)
    fout.write(f"Runs Documented: {Length}\n")
    fout.write(f"Fastest Time: {min(times)}\n")
    fout.write(f"Average Time: {total/Length}\n")
    fout.write(f"Total Time Spent Playing {difficulty} Difficulty: \n")
    fout.write(timeFunc(total)+"\n")

totalForEachDifficulty=[sum(i[1]) for i in readList]
finalTime=sum(totalForEachDifficulty)
fout.write(f"Total Time On Minesweeper: {timeFunc(finalTime)}")
