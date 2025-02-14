# github_integration.py
from github_api import get_repository_info, list_repository_issues

def analyze_repository(owner, repo, github_token):
    """Analyzes a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.
        github_token (str): Your GitHub personal access token.

    Returns:
        dict: A dictionary containing analysis results.
    """
    repo_info = get_repository_info(owner, repo, github_token)
    issues = list_repository_issues(owner, repo, github_token)

    analysis_results = {
        "repository_name": repo_info["name"] if repo_info else "N/A",
        "description": repo_info["description"] if repo_info else "N/A",
        "open_issues_count": repo_info["open_issues_count"] if repo_info else 0,
        "total_issues": len(issues) if issues else 0
    }

    return analysis_results

if __name__ == '__main__':
    # Example usage:
    github_token = "YOUR_GITHUB_TOKEN"
    owner = "octocat"
    repo = "Spoon-Knife"
    analysis = analyze_repository(owner, repo, github_token)
    print("Repository Analysis:")
    print(analysis)
