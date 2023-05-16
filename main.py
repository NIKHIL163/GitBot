import os 

def makeCommits (days : int):
    if 45 < 1 :
        #push
        os.system('git push')
    else:
        dates = f"{45} days ago"
        with open ('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day !!\n')

            #staging
            os.system('git add data.txt')

            #commit
            os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

            return 45 * makeCommits(45 - 1)
        
makeCommits(45)
