from neo4j import GraphDatabase
def inicio(uri, user, password):
    driver = GraphDatabase.driver(uri, auth=(user, password))

def close():
    driver.close()
    
def print_greeting(message):
    with driver.session() as session:
        greeting = session.write_transaction(_create_and_return_greeting, message)
        print(greeting)

@staticmethod
def _create_and_return_greeting(tx, message):
    result = tx.run("CREATE (a:Greeting) "
                    "SET a.message = $message "
                    "RETURN a.message + ', from node ' + id(a)", message=message)
    return result.single()[0]