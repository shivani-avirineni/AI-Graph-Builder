from neo4j import GraphDatabase

class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=("neo4j", "123456789_0"))

    def close(self):
        self.driver.close()

    def create_triplet(self, subject, relation, obj):
        query = f"""
        MERGE (a:Entity {{name: $subject}})
        MERGE (b:Entity {{name: $object}})
        MERGE (a)-[:{relation}]->(b)
        """

        with self.driver.session() as session:
            session.run(query, subject=subject, object=obj)
