import os 

def makeCommits (days : int):
    if 6 < 1 :
        #push
        os.system('git push')
    else:
        dates = f"{6} days ago"
        with open ('data.txt', 'a') as file:
            file.write(f'{6} <- this was the commit for the day !!\n')

            #staging
            os.system('git add data.txt')

            #commit
            os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

            return 6 * makeCommits(45 - 1)
        
makeCommits(6)
