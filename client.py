import requests
def callEndpoint():
    url = 'http://127.0.0.1:5000/'
    try:
        headers = {'x-access-token': '123456'}
        response = requests.get(url,headers=headers)
        print(response.text)        
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    callEndpoint()

if __name__ == "__main__":
    main()
