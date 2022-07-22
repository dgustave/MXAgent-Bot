from mxa import Mxisoagent 


if __name__ == '__main__':
    mxa = Mxisoagent()
    mxa.initiator()
    mxa.signOn()
    mxa.resave()
    print("All contents of the csv have successfully pumped over to Mxconnect")