secrets = {
    "dev": {
        "database_username": "dev_user",
        "database_password": "dev_pass_123",
        "api_key": "dev-APIKEY-xyz",
        "smtp_server": "smtp.dev.example.com",
        "smtp_password": "dev_smtp_pass"
    },
    "staging": {
        "database_username": "staging_user",
        "database_password": "staging_pass_456",
        "api_key": "staging-APIKEY-abc",
        "smtp_server": "smtp.staging.example.com",
        "smtp_password": "staging_smtp_pass"
    },
    "uat": {
        "database_username": "uat_user",
        "database_password": "uat_pass_789",
        "api_key": "uat-APIKEY-def",
        "smtp_server": "smtp.uat.example.com",
        "smtp_password": "uat_smtp_pass"
    },
    "prod": {
        "database_username": "prod_user",
        "database_password": "prod_pass_secure",
        "api_key": "prod-APIKEY-123456",
        "smtp_server": "smtp.example.com",
        "smtp_password": "prod_smtp_pass"
    }
}
def getinfo(a):
    dic = secrets.get(a,'nothing')
    return dic

getinfo('api_key')
getinfo('dev').get("api_key")
getinfo('prod')