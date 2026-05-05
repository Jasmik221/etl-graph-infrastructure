// 1. Show full graph
MATCH (a)-[r]->(b)
RETURN a, r, b
LIMIT 50;

// 2. Count nodes
MATCH (n:Node)
RETURN count(n) AS total_nodes;

// 3. Count relationships
MATCH ()-[r:CONNECTED_TO]->()
RETURN count(r) AS total_relationships;

// 4. Count nodes by type
MATCH (n:Node)
RETURN n.type AS node_type, count(*) AS count
ORDER BY count DESC;

// 5. Most connected nodes
MATCH (n:Node)--()
RETURN n.name AS node, n.type AS type, count(*) AS degree
ORDER BY degree DESC;

// 6. Relationship statistics
MATCH ()-[r:CONNECTED_TO]->()
RETURN r.type AS connection_type,
       count(*) AS count,
       avg(r.length) AS average_length;

// 7. Shortest path from main source to selected client
MATCH p = shortestPath(
  (a:Node {id: 1})-[*..10]->(b:Node {id: 20})
)
RETURN p;

// 8. Neighbors of selected node
MATCH (n:Node {id: 13})--(neighbor)
RETURN n, neighbor;