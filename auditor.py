import requests
import sys

def fetch_github_repos(username):
    print(f"Fetching repositories for {username}...")
    
    api_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"\n✅ Success! Found {len(repos)} public repositories:\n")
        print("-" * 40)
        
        for repo in repos:
            name = repo.get("name")
            url = repo.get("html_url")
            desc = repo.get("description", "No description provided.")
            
            print(f"📦 Repository: {name}")
            print(f"🔗 URL: {url}")
            print(f"📝 Description: {desc}")
            print("-" * 40)
            
    elif response.status_code == 404:
        print(f"❌ Error: The user '{username}' was not found on GitHub.")
    else:
        print(f"⚠️ Failed to fetch data. Status Code: {response.status_code}")

if __name__ == "__main__":
    # Check if the user provided exactly 1 argument after the script name
    if len(sys.argv) < 2:
        print("❌ Error: You must provide a username.")
        print("💡 Usage: python auditor.py <github_username>")
        sys.exit(1) # This tells the operating system the script failed
        
    # sys.argv[0] is the script name ('auditor.py'). sys.argv[1] is the username.
    target_user = sys.argv[1]
    
    fetch_github_repos(target_user)