#/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime,timedelta
import json
class GithubApi():
    def __init__(self, credentials: dict):
        self.auth = HTTPBasicAuth(credentials['username'], credentials['password'])

    def get_request(self, uri: str):
        resp = requests.get(f'https://git.renre.com/api/v3/{uri}', auth=self.auth).json()
        return resp
    
class GithubRepo():
    def __init__(self, api, owner, repo):
        self.owner = owner
        self.repo = repo
        self.api = api

    def workflows(self):
        resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/workflows')
        #print("workflows resp",resp)

        return resp.get('workflows', [])

    def workflow_runs(self, workflow_id: int):
        pages=1
        items_per_page=30
        workflows_list=[]
        
        for page_number in range (1,pages+1):
            #print("Getting Page numer #", page_number, " for a total of ", items_per_page, " items per page")
            resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/workflows/{workflow_id}/runs?status=success&per_page={items_per_page}&page={ page_number}')     
            workflows_list=workflows_list+resp.get('workflow_runs', [])
        
        return workflows_list

    def workflow_run_timings(self, run_id: int):
        
        resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/runs/{run_id}')
        #resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/runs/122569')
        
        #print(json.dumps(resp, indent=2))
        #exit(1)
        
        start_at=datetime.strptime(resp['run_started_at'], "%Y-%m-%dT%H:%M:%SZ")
        end_at=datetime.strptime(resp['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
               
        #TODO: Filter by sucessful status only?

        # Calculate the time difference
        time_difference_seconds = (end_at - start_at).total_seconds()
        time_difference_minutes = time_difference_seconds / 60
        time_difference = timedelta(seconds=time_difference_seconds)
        print("workflow_run_timings: URL %s at date %s and took %s (%s), attempt #%s Status %s Conclusion %s" % (
            resp['html_url'], str(start_at), str(time_difference_minutes),str(time_difference),(resp['run_attempt']),resp['status'],resp['conclusion'] ))
        return [start_at.strftime("%Y-%m-%d"), time_difference_minutes]
        #return resp

