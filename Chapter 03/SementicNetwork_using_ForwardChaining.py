#Experiment 16: Semantic Network Using Forward Chaining
#Description: This program represents knowledge using a Semantic Network in the form of a Python dictionary. 
#It displays relationships between objects such as Dog, Cat, and Animal.

# Semantic Network

semantic_network = {
    "Dog": {
        "is_a": "Animal",
        "has": "Tail",
        "can": "Bark"
    },
    "Cat": {
        "is_a": "Animal",
        "has": "Tail",
        "can": "Meow"
    },
    "Animal": {
        "needs": "Food",
        "can": "Move"
    }
}

# Display Semantic Network
for object, relations in semantic_network.items():
    for relation, value in relations.items():
        print(object, "----", relation, "---->", value)