import webbrowser #ask system to open the urls in browser 
import requests #checking for websites response

#websites listed belowe in dictionary form
websites = {
    "gmail": "add the website here",
    "git-hub":"add the website here",
    "linkedin": "add the website here "

}

#opening the websites 
def launch_websites(websites):
    for website, url in websites.items():
        try:
            webbrowser.open(url)
            print(f"opening the {website}:{url}")
        except webbrowser.Error as error:
            print(f"Could not open {website}:{url}")


 #checking for webites if they are reachable 
def check_website(websites):
    for website, url in websites.items():
        try:
            response = requests.get(url, timeout=5)
            response_code = response.status_code

            if response_code ==200:
                print(f"opening {website}")
            elif response_code ==403:
                print(f"forbidden {website}")
            else:
                print(f"{website} status code {response_code}")


        except requests.exceptions.RequestException as error:
            print(f"{website} request failed {error}")

check_website(websites) #calling the function 
launch_websites(websites) #calling the function 





    

    
    
    


    