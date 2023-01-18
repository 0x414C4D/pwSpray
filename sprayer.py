import requests 
import HttpNtlmAuth
import sys
import getopt

userfile = ''
fqdn = ''
password = ''
attackurl = ''

def usage():
    return True

def startSpray(userfile, fqdn, password, attackurl):
    return True

def main(argv):
    
    global userfile
    global fqdn
    global password
    global attackurl
    
    #Empty command line options print usage and exits
    if not len(sys.argv[1:]):
        usage()
        sys.exit(0)
        
    #Read commad line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:u:f:p:a", 
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
        exit(0)
        
    if (len(userfile) and len(fqdn) and len(password) and len(attackurl)):
        startSpray(userfile, fqdn, password, attackurl)
        sys.exit(0)
    else:
        usage()
        sys.exit(0)

    
