# github-actions-workflows-runs-timing-stats
Python tool to generate GHA workflows runs timing stats for GHE edition
Tested and Workfs for GHE

## Requirements
- python >= 3.5
- matplotlib

## Usage
1. Ensure requirements are installed/ working.
2. Follow [this](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to generate a personal access token.
3. Run the script with 

```bash
> python main.py --user="<Your github Username>" --token="<Your generated token>" --repo="<name of the workflow repo>" --owner="<owner of the workflow repo>"
```
4. Profit.
