import cmd, json
import requests
class github_activity(cmd.Cmd):
    intro = "Welcome to the GitUser Activity cli Tools"
    prompt ="github-activity>> "
    
    def do_user(self,arg):
        if arg.strip():
            url = f'https://api.github.com/users/{arg}/events'
            getting_content = requests.get(url)
            contents = getting_content.json()
            allPushed = []
            allIssues = []
            allPR = []
            allStarred = []
            for event in contents:
                match event['type']:
                    case "PushEvent":
                        allPushed.append(event)
                    case "WatchEvent":
                        allStarred.append(event)
                    case "IssuesEvent":
                        allIssues.append(event)
                    case "PullRequestsEvent":
                        allPR.append(event)
                    case _:
                        continue
            if len(allIssues) == 0 or len(allPR) == 0 or len(allStarred) == 0 or len(allPushed) == 0 :
                if len(allIssues) ==0:
                    pass
                else:
                    firstIssue = allIssues[0]
                    actionIssues = firstIssue['payload']['action']
                    repoIssues = firstIssue['repo']['name']
                if len(allPR) ==0:
                    pass
                else:
                    firstPR = allIssues[0]
                    actionPR = firstPR['payload']['action']
                    repoPR = firstPR['repo']['name']
                if len(allStarred) ==0:
                    pass
                else:
                    firstStarred = allStarred[0]
                    actionStarred = firstStarred['payload']['action']
                    repoStarred = firstStarred['repo']['name']
                if len(allPushed) ==0:
                    pass
                else:
                    firstPushed = allPushed[0]
                    commitSize = firstPushed['payload']['size']
                    repoPushed = firstPushed['repo']['name']
                    
            
    def do_exit(self,line):
        return True

if __name__ == '__main__':
    github_activity().cmdloop()