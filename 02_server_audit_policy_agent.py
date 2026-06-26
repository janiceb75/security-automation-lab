servers = [ {"Hostname": "WEB01", "OS": "Windows Server 2019"}, 
           {"Hostname": "APP01", "OS": "Windows Server 2008"}, 
           {"Hostname": "LEGACY01", "OS": "Windows Server 2003"}, 
           {"Hostname": "DB01", "OS": "Ubuntu 22.04"} ]

os_policy = { "Windows Server 2003":
              { "status": "Unsupported",
                "severity": "Critical" },
              "Windows Server 2008": 
              { "status": "Unsupported",
                "severity": "High" } }
        
class ServerAuditAgent():
    def __init__(self):
        self.findings = ["Findings :"  ]
        self.supported = ["Supported Servers :"]

    def AuditServers(self,servers):
        for entry in servers:
            if entry["OS"] in os_policy:
                policy_result =  os_policy[entry["OS"]]
                
                serverfinding = {
                    "Hostname":entry["Hostname"],
                    "OS":entry["OS"],
                    "Status":policy_result["status"],
                    "Severity":policy_result["severity"]
                    
                    
                }
                
                self.findings.append(serverfinding)
            else:
                self.supported.append(entry)
        return self.findings, self.supported


janAgent2 = ServerAuditAgent()

print(janAgent2.AuditServers(servers))
