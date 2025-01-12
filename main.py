import cmd
import requests
class github_activity(cmd.Cmd):
    intro = "Welcome to the GitUser Activity cli Tools"
    prompt ="github-activity>> "
    
    def do_user(self,arg):
        url = 'https://randomuser.me/api/' # Where we're sending our API Call
        params = {'nat': 'us'}
        response = requests.get(url, params=params)
        print(response)

if __name__ == '__main__':
    github_activity().cmdloop()