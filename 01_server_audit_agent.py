class ServerAuditAgent:
    def __init__(self):
        self.memory = []
        self.unsupported_count = 0
        
        
    def serverClass(self):
        for server_name, server_type in servers.items():
            if server_type == "Windows Server 2003":
                status = "Unsupported"
                
                serverlist= (f' {server_name} = {status}')
                self.memory.append(serverlist)
                self.unsupported_count += 1
                
            elif server_type == "Windows Server 2008":
                status = "Unsupported"
            
                serverlist= (f' {server_name} = {status}')
                self.memory.append(serverlist)
                self.unsupported_count += 1
                
            else:
                status = "Supported"
                serverlist= (f' {server_name} = {status}')
                self.memory.append(serverlist)
        
        return self.memory
    


janserver=ServerAuditAgent()

servers = {
    "WEB01": "Windows Server 2019",
    "APP01": "Windows Server 2008",
    "DB01": "Ubuntu 22.04",
    "LEGACY01": "Windows Server 2003"
}

print(janserver.serverClass())
print(f'Unsupported Servers = {janserver.unsupported_count}')