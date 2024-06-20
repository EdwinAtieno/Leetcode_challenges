/**
 * @param {number} startNodeid id of the start node
 * @param {number[]} fromIds ids of the linked nodes (link start)
 * @param {number[]} toIds ids of the linked nodes (link end)
 * @param {number} Endpoint node id, or node id of before closing the loop
 *
 * the goal of this exercise is to find the endpoint node of a simple network or find the loop if there is one
 * in this simple network, each node is linked to at mpst one outgoing node in a one way forward direction
 *
 * implememt the function compute(startNodeid, fromIds, toIds) that return the last node id of the network found when starting from the
 * node with id startNodeid and following the links of the network
 *
 */

function compute(startNodeid, fromIds, toIds){
    const graph = new Graph();
    const nodes = new Map();
    for (let i = 0; i < fromIds.length; i++) {
        const fromId = fromIds[i];
        const toId = toIds[i];
        if (!nodes.has(fromId)) {
            nodes.set(fromId, new Node(fromId));
        }
        if (!nodes.has(toId)) {
            nodes.set(toId, new Node(toId));
        }
        graph.addEdge(nodes.get(fromId), nodes.get(toId));
    }
    const startNode = nodes.get(startNodeid);
    const path = graph.findPath(startNode);
    return path;
}


function computes(startNodeid, fromIds, toIds){
    let node = startNodeid;
    let nextNode = toIds[fromIds.indexOf(node)];
    while(nextNode !== undefined){
        node = nextNode;
        nextNode = toIds[fromIds.indexOf(node)];
    }
    return node;
}