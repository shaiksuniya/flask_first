from flask import Flask

FAI=Flask(__name__)

@FAI.route('/sonu')

def sonu():
    return "<marquee><center><h1>MY NAME IS SONU MONKEY</h1></center></marquee>"

@FAI.route('/renu')
def renu():
    return "<marquee><center><h2>Renu my kidney poindi</h2></center></marquee>"


if __name__=='__main__':
    FAI.run(debug=True)
