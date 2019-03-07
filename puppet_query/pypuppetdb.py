from pypuppetdb import connect
db = connect("puppetdb02-esxi.com")

nodes = db.nodes()
for node in nodes:
	print(node)