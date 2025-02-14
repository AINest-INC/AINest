# github_api.py
import requests

def get_repository_info(owner, repo, github_token):
    """Gets information about a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        github_token (str): Your GitHub personal access token.

    Returns:
        dict: The repository information if successful, None otherwise.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting repository info: {response.status_code} - {response.text}")
        return None

def list_repository_issues(owner, repo, github_token):
    """Lists issues in a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        github_token (str): Your GitHub personal access token.

    Returns:
        list: A list of issues if successful, None otherwise.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error listing repository issues: {response.status_code} - {response.text}")
        return None

if __name__ == '__main__':
    # Example usage:
    github_token = "YOUR_GITHUB_TOKEN"
    owner = "octocat"
    repo = "Spoon-Knife"
    repo_info = get_repository_info(owner, repo, github_token)
    if repo_info:
        print("Repository Info:")
        print(repo_info)

    issues = list_repository_issues(owner, repo, github_token)
    if issues:
        print("\nRepository Issues:")
        for issue in issues:
            print(f"- {issue['title']}")
