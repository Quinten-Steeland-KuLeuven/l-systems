from flask import Flask


app = Flask(__name__)

file1 = open("History.txt","r")
for line in file1:
	None

listline = line.split("\t")


imageopen= open("./Images/mostRecent.svg", 'r')

imagescript = ""
for line in imageopen:
	
	imagescript += line
	
@app.route("/")
def table():
	print('something')
	return "<!DOCTYPE html><html><head><meta charset=\"UTF-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" /><meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\" /><style>table, th, td { border: 1px solid black}</style></head><body><h1>L-SYSTEMS</h1><table><tr><th>Date</th><th>Variables</th><th>Constants</th><th>Axiom</th><th>Rules</th><th >Translations</th><th>Iterations</th><th>l-system</th></tr><tr><td>"+listline[0]+"</td><td>"+listline[1]+"</td><td>"+listline[2]+"</td><td>"+listline[3]+"</td><td>"+listline[4]+"</td><td>"+listline[5]+"</td><td>"+listline[6]+"</td><td>"+listline[7]+"</td></tr></table><h2>Drawing</h2>"+imagescript+"</body></html>"
	
