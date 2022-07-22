from mxa import Mxisoagent

def board_to_mxc():
    mxa = Mxisoagent()
    mxa.initiator()
    mxa.signOn()
    mxa.download_merchants()
    mxa.resave(filename = "merchants.csv")
    return print("All contents of the csv have successfully pumped over to Mxconnect")

if __name__ == '__main__':
    board_to_mxc()
