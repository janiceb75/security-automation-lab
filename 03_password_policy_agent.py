class PasswordAuditAgent:
    """Audits user accounts for password policy violations."""

    def __init__(self):
        self.findings = []
        self.high_findings = 0
        self.med_findings = 0
        self.summary_report = {}

    def audit_passwords(self, users, password_policy):
        """Evaluate users against the organization's password policy and generate security findings."""

        for user in users:

            if user["password_age"] > password_policy["max_password_age"]:
                self.findings.append(
                    {
                        "username": user["username"],
                        "finding": "Password expired",
                        "severity": "Medium",
                    }
                )
                self.med_findings += 1
            if user["mfa_enabled"] != password_policy["mfa_required"]:
                self.findings.append(
                    {
                        "username": user["username"],
                        "finding": "MFA not enabled",
                        "severity": "High",
                    }
                )
                self.high_findings += 1
            if user["password_reused"] != password_policy["password_reuse_allowed"]:
                self.findings.append(
                    {
                        "username": user["username"],
                        "finding": "Password Reused",
                        "severity": "High",
                    }
                )
                self.high_findings += 1
        self.summary_report = {
            "Total findings:": len(self.findings),
            "High Findings:": self.high_findings,
            "Medium Findings:": self.med_findings,
        }
        return self.findings, self.summary_report


password_policy = {
    "max_password_age": 30,
    "mfa_required": True,
    "password_reuse_allowed": False,
}

users = [
    {
        "username": "jsmith",
        "password_age": 45,
        "mfa_enabled": True,
        "password_reused": False,
    },
    {
        "username": "agarcia",
        "password_age": 10,
        "mfa_enabled": False,
        "password_reused": False,
    },
    {
        "username": "mbrown",
        "password_age": 90,
        "mfa_enabled": False,
        "password_reused": True,
    },
    {
        "username": "kwilson",
        "password_age": 5,
        "mfa_enabled": True,
        "password_reused": False,
    },
]

JanPasswordAgent = PasswordAuditAgent()


print(JanPasswordAgent.audit_passwords(users, password_policy))
print()
print()
print(JanPasswordAgent.summary_report)
