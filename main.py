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
            if len(contents) != 0 and getting_content.status_code == 200:
                allPushed = []
                allIssues = []
                allPR = []
                allStarred = []
                firstPR = None
                firstIssue = None
                firstPushed = None
                firstStarred = None
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
                        firstPR = allPR[0]
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
                
                if firstIssue:
                    print (f"{actionIssues} a issue in {repoIssues}")
                else:
                    print (f"User has no recent issue")
                
                if firstPushed:
                    print(f"User {arg} pushed {commitSize} commits to {repoPushed}")
                else:
                    print('User not pushed on the last days')
                    
                if firstPR:
                    print (f"{actionPR} a PullRequest in {repoPR}")
                else:
                    print (f"User has no recent PullRequest")
                
                if firstStarred:
                    print (f"{actionStarred} {repoStarred}")
                else:
                    print (f"User has not starred a repo on the last day")
            else:
                print(f"User {arg} has not a Github Account")    
                
    def do_exit(self,line):
        return True

if __name__ == '__main__':
    github_activity().cmdloop()