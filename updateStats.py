readList=[[i, [int(a) for a in open(i.lower()+".txt").read().split()]] for i in ["Easy", "Medium", "Hard"]];open("stats.txt","w").write("".join([f"{(difficulty:=info[0])} Difficulty{(n:=chr(10))}------------------------------------------------------------------------------{n}Runs Documented: {(Length:=len(times:=info[1]))}{n}Fastest Time: {min(times)}{n}Average Time: {(total:=sum(times))/Length}{n}Total Time Spent Playing {difficulty} Difficulty:{n}{(timeFunc:=(lambda x: ''.join(['{} day{} '.format((days:=(x//i)),('' if days==1 else 's')) if j==0 else '{}{}{} '.format((unit:=((x%[86400,3600,60,1][j-1])//i)), [' hour', ' minute', ' second'][j-1], ('' if unit==1 else 's')) for j,i in enumerate([86400,3600,60,1])])))(total)}{n}{n}" for info in readList])+f"Total Time On Minesweeper: {timeFunc(sum([sum(i[1]) for i in readList]))}")
