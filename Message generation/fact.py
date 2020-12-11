# from subprocess import Popen
# import requests
# from bs4 import BeautifulSoup

# def get_text(url):
#     rs = requests.get(url)
#     root = BeautifulSoup(rs.content, 'html.parser')
#     text_out = str(root) 
#     text = text_out[31000:34000]
#     return text

# url = "https://fungenerators.com/random/facts"
# text = get_text(url)
# # text_out = str(text) 
# # text = text_out[31000:34000]

# spliting = text.split('>')
# for i in range(len(spliting)):
#     if spliting[i] == '\n<h2 class="wow fadeInUp animated" data-wow-delay=".6s"':
#         number = i+1
#         break

# fact = spliting[number].split('<')
# fact = fact[0]

# print(fact)

def get_fact(my_word):
    category_main = ['Animal', 'Plants', 'Scientists', 'Authors', 'Biography', 'National Parks', 'Periodic Table', 'US States', 'Holidays', 'Dogs', 'Space', 'US History', 'Countries', 'Wonders of the World', 'Health', 'Music Instruments', 'Sports', 'Seas', 'History', 'World History', 'US National Landmarks', 'Geography', 'Viruses', 'Food', 'Nutrition', 'Ancient Civilizations', 'Rocks', '13 Colonies', 'Artists', 'Weather', 'Rivers', 'Dinosaurs', 'Human Body', 'Games', 'Cats', 'Geology', 'Energy', 'Vegetables', 'Civil War', 'Cities', 'Science', 'Technology', 'Environmental Science', 'Religion', 'Minerals', 'Weather Instruments', 'Chemistry', 'Fiction', 'US Geography', 'Business', 'Transportation', 'Cultures', 'US Government', 'Hybrid Animals', 'Extinct Animals', 'Earth Systems', 'Astrological Instruments', 'Europe', 'Manmade Disasters', 'Rome', 'Biology', 'Museums', 'Music', 'Rain Forests', 'Social Studies', 'Deepest Places', 'Movies', 'Organisms', 'Mythology', 'Prehistoric', 'Mexico', 'Volcanoes', 'Canada', 'Literature', 'Marine Parks', 'Oceans', 'Careers', 'Numbers']

    category_main_for_found = ['Animal', 'Plant', 'Scientist', 'Author', 'Biography', 'National Park', 'Periodic Table', 'US State', 'Holiday', 'Dog', 'Space', 'US History', 'Countrie', 'Wonder of the World', 'Health', 'Music Instruments', 'Sport', 'Sea', 'History', 'World History', 'US National Landmark', 'Geography', 'Viruse', 'Food', 'Nutrition', 'Ancient Civilization', 'Rock', '13 Colonies', 'Artist', 'Weather', 'River', 'Dinosaur', 'Human Body', 'Game', 'Cat', 'Geology', 'Energy', 'Vegetable', 'Civil War', 'Cities', 'Science', 'Technology', 'Environmental Science', 'Religion', 'Mineral', 'Weather Instruments', 'Chemistry', 'Fiction', 'US Geography', 'Business', 'Transportation', 'Culture', 'US Government', 'Hybrid Animal', 'Extinct Animal', 'Earth System', 'Astrological Instrument', 'Europe', 'Manmade Disaster', 'Rome', 'Biology', 'Museums', 'Music', 'Rain Forest', 'Social Study', 'Deepest Place', 'Movie', 'Organism', 'Mythology', 'Prehistoric', 'Mexico', 'Volcanoes', 'Canada', 'Literature', 'Marine Park', 'Ocean', 'Career', 'Number']


    category_lev2 = [
    ['Caribou', 'Magellanic penguin', 'Weasel', 'Quokka', 'Arthropods', 'Killer Whale', 'Alpaca', 'Cormorant', 'Chameleon', 'Spectacled Bear', 'European plaice', 'Greaterstick-nest rat', 'Macaroni penguin', 'Sand lizard', 'Golden oriole', "Wilsons bird of paradise", 'Lumpfish', 'Bowhead whale', 'Firefly', 'Zebu', 'Hornet', 'Dingo', 'Peacock Butterfly', 'Cow', 'Quail', 'African penguin', 'Arctic fox', 'Haddock', 'Kiang', 'Blackbird', 'Galapagos tortoise', 'Fisher', 
    'Javan rhinoceros', 'Goliath frog', 'Banded palm civet', 'Marbled cat', 'Hake', 'Nautilus', 'Pied-billed grebe', 'Warthog', 'Dolphin', 'Crab-eating fox', 'Collared peccary',
    'African golden cat', 'Small-eyed snake', 'Jerboa', 'Amazon horned frog', 'Seal', 'Blobfish', 'Lapwing', 'Tarsier', 'Hummingbird', 'Bongo', 'Common nighthawk', 'Tuco-tuco', 
    'Frogfish', 'Saiga', 'Himalayan snowcock', 'Mole', 'Aardvark', 'Hermit crab', 'Box turtle', 'Ruff', 'Bumblebee', 'Gemsbok', 'Yak', 'Nyala', 'Goliath beetle', 'Chinese crocodile lizard', 
    'Donkey', 'Tentacled snake', 'African tree toad', 'Grant’s gazelle', 'Mealybugs', 'Killer bees', 'Common redpoll', 'Glass frog', 'Flea', 'Kakapo', 'Snow monkey', 'Barn owl', 'Mosquito', 
    'Menhaden', 'Angel shark', 'Prairie skink', 'California condor', 'Tsetse fly', 'Green honeycreeper', 'Flat-headed cat', 'Common buzzard', 'Cod', 'Weakfish', 'Kangaroo rat', 'Broad-headed snake',
    'Galago', 'Llama', 'Osprey', 'Emperor penguin', 'Kangaroo', 'European nightjar', 'Naked MoleRat', 'Giant white-tailed rat', 'Squirrel monkey', 'House wren', 'Monitor lizard', 'Andean cat', 'Gopher',
    'Desert tortoise', 'Yellowhammer', 'Cricket', 'Gerenuk', 'Potto', 'Pine siskin','Iguana', 'Dog-faced water snake', 'Goat', 'Tripod fish', 'Rhinoceros', 'Octopus', 'Giant otter', 'Pseudoscorpions',
    'Leeches', 'Dark-eyed junco', 'Mudpuppy', 'Liberian mongoose', 'Keel-billed toucan', 'Jackrabbit', 'Basking shark', ' Oxpecker', 'Sculpin', 'Barracuda', 'Amargosa toad', 'Cassowary', 'Butterfly fish',
    'Kingfisher', 'Jellyfish', 'Common frog', 'Common raven', 'Lion', 'Legless lizard', 'Common lancehead', 'Polar Bear', 'Lobster', 'Magpie', 'Snail kite', 'Emperor tamarin', 'Moray eel', 'Owl',
    'False water rat', 'Amazon river dolphin', 'Ibis', 'Tayra', 'Seahorse', 'Monte Iberia eleuth', 'Blacknose shark', 'Gray mouse lemur', 'Dwarf lantern shark', 'Banded sea krait',
    'Rough-skinned newt', 'Heron', 'Red-naped snake', 'Bald Eagle', 'Finch', 'Goose', 'Vampire squid', 'Great White Shark', 'Aldabra giant tortoise', 'Mantis shrimp',
    'Agile frog', 'Rock hyrax', 'Darkling beetles', 'Sloth', 'Red-eyed tree frog', 'King crab', 'Kinkajou', 'Barnacle', 'Ticks', 'Sea squirt', 'Clownfish', 'Puerto Rican coqui', 'Hawk',
    'Atlantic canary', 'Leaf-tailed gecko', 'Grouse', 'Coral', 'Fruit fly', 'Tarantula', 'Mountain viscacha', 'Cookiecutter shark', 'Gila monster', 'Boomslang', 'Clouded leopard', 
    'Striped rocket frog', 'Falcon', 'Starfish', 'Regent honeyeater', 'Black tip shark', 'Lake sturgeon', 'Vole', 'Mona monkey', 'Moorhen', 'Colocolo', 'Green bee-eater', 'Fin whale', 
    'Bilby', 'Ladybug', 'Sitatunga', 'Guanaco', 'Red-sided garter snake', 'Skink', 'Gray catbird', 'Horse', 'Web-spinners', 'Chinese mountain cat', 'Alligator', 'Mouflon', 'Amazon milk frog', 
    'Eastern cottontail', 'Water buffalo', 'Slow worm', 'Electric Eel', 'Midwife toad', 'Black bear', 'Beaver', 'Spotted handfish', 'Koi fish', 'Crab spider', 'Jackal', 'Eastern wood-pewee', 
    'Lemming', 'Indian eagle-owl', 'Cotton-top tamarin', 'Goral', 'Binturong', 'Nutria', 'Eastern bluebird', 'Ermine', 'Malayan tiger Facts',' Tuatara', 'Ferret', 'Fennec fox', 'Wolverine',
    'Sunbirds', "Commersons dolphin", 'Least bittern', 'Meerkat', 'Pilot whale', 'Numbat', 'Beluga whale', 'Grey seal', 'Frill-necked lizard', 'Brown antechinus', 'Mallard duck', 'Springbok',
    'Gaur', 'Steenbok', 'Tegu', 'Northern mockingbird', 'Mule', 'Corsac fox', 'Angelfish', 'Porpoise', 'Black-bellied whistling duck', 'Sea snakes', 'Eastern meadowlark', 'Capuchin monkey', 
    'Yellow-lfish', 'Porpoise', 'Black-bellied whistling duck', 'Sea snakes', 'Eastern meadowlark', 'Capuchin monrmit thrush', 'Lemur', 'Kodkod', 'Erect-crested penguin', 'Muntjac', 'Bush rat',
    'Armadillo', 'Eastern hognose snakkey', 'Yellow-Bellied Marmot', 'Margay', 'Mule deer', 'Booby', 'Bat', 'Thorny skate', 'Lemon shark',  "Darwins frog", 'Massasauga', 'Jaguar', 'Rosy-faced lovebird', 
    'Nightingale', 'Crab-eating macaque', 'Guinea fowl Oncilla', 'Hermit thrush', 'Lemur', 'Kodkod', 'Erect-crested penguin', 'Muntjac', 'Bush rat', 'Armadus', 'Pygmy hog', 'Pig', 'Dwarf crocodile', 
    'Ant', "Przewalskis horse", 'Fat-tailed dunnart', 'Albatross', 'Ruby-cillo', 'Eastern hognose snake', 'Jaguarondi', 'European starling', 'Manta ray', 'Giant squid', 'Wombaundhog', 'Walleye', 
    'Lionfish', 'Gray brocket deer', 'Rabbit', 'Crab', 'Leopard seal', 'Marco Polo sheep', 'Emu', 't', 'Python', 'Tomato frog', "Darwins frog", 'Massasauga', 'Jaguar', 'Rosy-faced lovebird', 'Nightine', 
    'Markhor', 'African clawless otter', 'American marten', 'Frigatebird', 'Centipedes', 'Whippoorwill', 'Grass snagale', 'Crab-eating macaque', 'Guinea fowl', 'Horned viper', 'Cape sugarbird', 'Minke whale',
    "Mako shark", 'Little red kaluta', 'Pigeon', 'Warbling vireo', "Dalls sheep", 'Brown-headed cowbird', 'Walrus', 'S monkey', 'Dragonfly', 'Blue tit', 'Platypus', 'Pygmy hog', 'Pig', 'Dwarf crocodile',
    'Ant', 'Przewal marlin', 'African linsang', 'Sea lamprey', 'Ringtail', 'Caiman lizard', 'Bobcat', 'Wrasse', 'Saw shark', "Javelinaskis horse", 'Fat-tailed dunnart', 'Albatross', 'Ruby-crowned kinglet', 
    'Fire-bellied toad', "Stone Flamingo", 'Hen harrier', 'Green toad', 'Marsh frog', 'Blue jay', 'Fur seal', 'Corn snakes', 'Piranhas', 'Grey remarten', 'Narwhal', 'Olingo', 'Bottlenose dolphin', 'Groundhog',
    'Walleye', 'Lionfish', 'Gray brocket deer', 'Rabbit', 'Crab', 'Leopard seal', 'Marco Polo sheep', 'Emu', 'Rainbow trout', 'Eurasian harvest mouse', 'Woolly monkey', 'Eyelash viper', 'Sparrow', 'Great kiskadee', 
    'Markhor', 'African clawless otter', 'American marten', 'Frigatebird', 'Centipedes', 'Whippoorwill', 'Grass snake', 'Monkfish','Hyena', 'Western brown snake', 'Nurse shark', 'Siberian ibex', 'Egyptian vulture', 
    'Mako shark', 'Little red kaluta', 'Pigeon', 'Warbling vireo', "Dalls sheep", 'Brown-headed cowbird', 'Walrus', 'Sable', 'Sheep', 'Fishing cat', 'Arctic hare', 'Quoll', 'Hamerkop', 'Common tenrec', 'Sawflies', 
    'Blue marlin', 'African linsang', 'Sea lamprey', 'Ringtail', 'Caiman lizard', 'Bobcat', 'Wrasse', 'Saw shark', 'Javelina', 'Moths', 'Leopard tortoise', 'Russian desman', 'Grizzly Bear', 'Sambar deer', 'Hispid cotton rat',
    'Flamingo', 'Hen harrier', 'Green toad', 'Marsh frog', 'Blue jay', 'Fur seal', 'Corn snakes', 'Piranhas', 'Grey reef shark', 'Mountain yellow-legged frog Facts', 'Camel', 'Remora', 'Olm', 'Speartooth shark',
    'Guinea pig', 'Right whale', 'Long-tailed planigale', 'Puffer fish', 'Oribi', 'Avocet', 'Click beetles', 'Bearded dragon', 'Sociable weaver', 'Turkey', "Kemps Ridley turtle", 'Arctic wolf', 'Sugar glider',
    'Mauritius kestrel', 'Gerbil', 'Tiger swallowtail', 'Kouprey', 'Black widow', 'Shoebill', "Wallaces flying frog", 'African wild dog', 'Black skimmer', 'Bar jack', 'Sea cucumber', 'Sei whale', 'Spider monkey',
    'Mudskipper', 'Leopard', 'Short-eared dog', 'Humpback whale', 'Seagull', 'King snake', 'Anteater', 'Spring peeper', 'Woodpecker', 'Okapi', 'Masked palm civet', 'Mayfly', 'Dung beetle', 'Galapagos penguin', 
    'Cuban tree frog', 'Big-eyed bugs', 'Horned marsupial frog', 'Perentie', 'Antelope', 'Oyster', 'Visayan warty pig', 'Guppy', 'Small-scaled burrowing asp', 'Moor frog', 'Secretarybird', 'Aphids', 'Mongoose',
    'Curl snake', 'African clawed frog', 'Swift', 'Horn shark', 'Leopard cat', 'Asian elephant', 'Asian golden cat', 'Red-billed chough','Giant clam', 'Woodlouse', 'Ocelot', 'Common genet', 'Wildebeest', 'Shrew', 
    'Bandicoot', 'Barn swallow', 'Black racer', 'Sea urchin', 'Musk ox', 'Red panda', 'Mullet', 'Little penguin', 'White-footed mouse', 'Langur', 'Wild turkey', 'Marsh rice rat', 'Aardwolf', 'Water moccasin', 'Black mamba',
    'Loggerhead shrike', 'Mulga snake', 'Scarlet macaw', 'Chinese white dolphin', 'Gar', 'Kori bustard', 'Black turnstone', 'House fly', 'Sand diver', 'Giraffe', 'Whale shark', 'Pademelon Facts', 'Blue whale', 'Hamster', 
    'Viviparous lizard', "Russells viper", 'Vaquita', 'Atlantic halibut', 'Atlantic puffin', 'Daddy longlegs', 'Agouti', 'Tasmanian Devil', 'Hooded seal', "Pallass cat", 'Asian giant hornet', 'Bay cat', 'Rubber eel',
    'Greater roadrunner', 'Porcupine', 'Elephant', 'Dusky shark', 'African buffalo', 'Dugong', 'Pheasant', 'Black-speckled palm viper', 'Capybara', 'Western fox snake', "Thomsons gazelle", 'Long-eared owl', 'Bowfin', 
    'Nilgai', 'Penguin', 'Parasitic jaeger', 'African Civet', 'Komodo Dragon', 'Chipmunk', 'Peregrine falcon', 'Crane', 'Elk', 'Gentoo penguin', 'Millipedes', 'Cicadas', 'Muskrat', 'Saw-shelled turtle', 'Anaconda', 'Sea Turtle',
    'Ring-tailed coati', 'Coral snake', 'Hare', 'Blue-winged leafbird', 'Scarab beetles', 'Chimpanzee', 'Bonnet macaque', 'Flying lizards (draco)', "Dwyers snake", 'Bull shark', 'Woma python', 'Horseshoe crab', 'Raccoon dog',
    'Asian palm civet', 'Canada goose', 'Skeleton shrimp', 'Honey badger', 'Panther', 'Tapir', 'Ryukyu flying-fox', 'Axolotl', 'Pangolin', 'Chamois', 'Salmon', 'Brown-headed nuthatch', 'Stonefish', 'Wyoming toad', 'Wild boar', 
    'Parakeet', 'Impala', 'Bushpig', 'Cuttlefish', 'Red-breasted sapsucker', 'Caracal', 'Albacore', 'Goanna', 'Hammerhead shark', 'Spiny crayfish', 'Dumbo octopus', 'Grey partridge', 'Agama', 'Panamanian golden frog', 'Green lacewings',
    'Night monkey', 'Spot prawn', 'Stingray', 'Flounder', 'Saola', 'Cuckoo', 'Hedgehog', 'Dormouse', 'Silver arowana', 'Manatee', 'Camel spider', 'Boa constrictor', 'Earwigs', 'Chinchilla', 'Black-footed cat', 'Humboldt penguin', 'Spectacled caiman',
    'Asiatic black bear', 'Earthworm', 'Yellow warbler', 'Mandarin duck', 'Common myna', 'Pelican', 'Slug', 'Aye-aye', 'Oryx', 'Echidna', 'Moloch', 'Loon', 'American bullfrog', 'Walking sticks', 'Baboon', 'Rose-breasted grosbeak', 
    'Scorpion', 'Catfish', 'Dusky dolphin', 'Cheetah', ' Tree kangaroo', 'Common Toad', 'Banded cat-eyed snake', 'Honey bee', 'Wildcat', 'Hoopoe', 'Iriomote cat', 'Gharial', 'Pronghorn', 'Himalayan tahr', 'Wolf', 'Tawny frogmouth',
    'Raccoon', 'Gray rat snake', 'Sperm whale', 'Skunk', 'Deep sea hatchetfish', 'Elephant trunk snake', 'Orangutan', 'Kiwi', 'Common linnet', 'Common adder', 'Goby', 'Blue monkey', 'Indian palm squirrel', 'Sulcata tortoise', 
    'Sea Anemone', 'Fossa', 'Hippopotamus', 'Mandrill', 'Crested caracara', 'Pygmy marmoset', 'Snail', 'Bison', 'Tiger', 'Chinstrap penguin', 'Armadillo lizard', 'Ovenbird', 'Caiman', 'Yellow-headed jawfish', 'Bushbuck', 'Towhee', 
    'Rhea', 'Hoatzin', 'Eagle', 'Coyote', 'Velvet scoter', 'Sand Cat', 'Cedar waxwing', "Clarks nutcracker", 'Lynx', 'Common kusimanse', 'Crocodile', 'Northern goshawk', 'Giant African snail', 'Spiny bush viper', 'Lake whitefish',
    'Serval', 'Rainbow bee-eater', 'Peacock', 'Harpy eagle', 'Assassin bug', 'Golden mole', 'Chicken', 'Green vine snake (Oxybelis fulgidus)', 'African wild ass', 'Common sandpiper', 'Cuscus', 'Leafhoppers', 'Boreal toad', 'Indian rhinoceros', 
    'Cacomistle', 'Bactrian camel', 'Herring', 'Alewife', 'Mink', 'European polecat', 'Tiger shark', 'Spinner dolphin', 'Gorilla', 'Loris', 'Cichlid', 'Pine snake', 'Sand dollars', 'Gibbon', 'Yosemite toad', 'Fox', 'Zebra duiker', 
    'Chuckwalla', 'Elephant seal', 'Panda', 'Black stilt', 'Sun Bear', 'Emperor goose', 'Moose', 'Diana monkey', 'Indri', 'Rusty-spotted cat', 'Glass lizard', 'Toucan', 'Little stint', 'Salamander', 'Blue-gray gnatcatcher', 'Opossum',
    'Hartebeest', 'Babirusa', 'Kudu', 'Hercules beetle', 'Parrot', 'Adelie penguin', 'Alligator snapping turtle', 'Giant sea bass', 'Dhole', 'Northern bobwhite', 'Zebra', "Brydes whale", 'Indian star tortoise', 'Desert bighorn sheep',
    'Badger', 'Mackerel', 'Giant tube worms', 'Cobra', 'Froghopper', 'Tuna', 'Stink bug', 'King penguin', 'Bush dog', 'Coati', 'Gopher snake', 'Scissor-tailed flycatcher', 'Golden lion tamarin', 'Ostrich', 'Flying fish', 'Gecko', 'Bonobo',
    'Green anole', 'Elephant shrew', 'Flying squirrel', 'Blesbok', 'Tailed Frog', 'Rattlesnake', 'Koala', 'Red-tailed monkey', 'Prairie dog', 'Termite', 'Northern cardinal', 'Cockroach', 'Praying Mantis', 'Grasshopper', 'T-Rex Facts'],

    ['Hakea', 'Indian paintbrush', 'Common ragweed', 'Wild ginger', 'Jasmine', 'Chrysanthemum', 'Africa tulip tree', 'Alligator weed', 'American pokeweed', 'Dandelion', 'Geranium', 'Lychee', 'Sagebrush', 'Lupine', 'Carnation', 
    'Casuarina', 'Comfrey', 'Fire moss', 'Common heather', 'Plum', 'Tansy', 'Starfruit', 'Saltbush', 'Sorrel', 'Celery', 'Horsetail', 'Moss', 'Hellebore', 'Leek', 'Mopane', 'Joshua tree', 'Willow tree', 'Black-eyed Susan', 'Chives',
    'Box elder', 'Canola', 'Kiwifruit', 'Great Valley gumweed', 'Madrone tree', 'Star anise', 'Sorghum', 'Leafy spurge', 'Lemon-scented gum', 'Kapok tree', 'Kale', 'Cranberry', 'Thyme', 'Winter savory', 'White baneberry', 'Teasel', 'Spruce',
    'Giant hogweed', 'Acacia', 'Oak tree', 'Mamoncillo', 'Lemongrass', 'Sassafras', 'Lavender', 'Welwitschia', 'Cucumbertree', 'Elephant garlic', 'Common hop', 'Elderberry', 'Magnolia tree', 'Great yellow gentian', 'Mesquite tree', 
    'White snakeroot', 'Sweet potato', 'Lemon', 'Mariposa lily', 'Longan', 'Kohlrabi', 'Fuchsia', 'Yarrow', 'Agrimony', 'Barnyard grass', 'Allegheny woodrat', 'African Blackwood', 'Gympie gympie', 'Aspen', 'Orchid', 'Philodendron', 'Ombu tree',
    'Sumac', 'Opium poppy', 'Mango', 'Diesel tree', 'Iris', 'Eastern cottonwood', 'Hemlock', 'Poplar tree', 'Peony', 'Salsify', 'Zucchini', 'Wolfberry', 'Maple tree', 'Morning glory', 'Lords-and-ladies', 'Manzanita', 'Japanese cheesewood',
    'Ash tree', 'Baseball plant', 'Buttonbush', 'Bushmaster', 'Bay tree', 'Pear', 'Cucumber', 'Rose', 'Sandalwood', 'Orange hawkweed', 'Tamarisk (salt cedar)', 'Petunia', 'Lily', "Dutchmans pipe", 'Macadamia', 'Juneberry', 'Honey locust', 
    'Rice', 'Catalpa', 'Amaryllis', 'Allspice', 'Anise', 'Oleander', 'Red ironbark', 'Mistletoe', 'Monkey flowers', 'Mustard', 'Cauliflower', 'Chaste tree', 'Chinaberry', 'Cane toad', 'Coneflowers', 'Radish', 'Cumin', 'Tomato', 'Snowball tree', 
    'Sweet flag', 'Yucca', 'Pomelo', 'Fern', 'Elephant grass', 'Maracuja', 'Meadow foxtail', 'Laburnum', 'Beech', 'Cheatgrass', 'Curuba', 'Bearberry', 'Chicory', 'Peach', 'Tibouchina', 'Rambutan', 'Mullein', 'Raspberry', 'Cycads', 'Dragon blood tree',
    'Coontail', 'Great egret', 'Ebony tree', 'Figwort', 'Strawberry', 'Deadly nightshade', 'Tulip', 'Bladderwort', 'Firethorn', 'Aster', 'Artichoke', 'Coconut tree', 'Indian jujube', 'Marula', 'Milkweed', 'Privet', 'Chamomile', 'Cornflower (Centaurea)',
    'Durian', 'Camellia', 'Cotton', 'Pumpkin', 'Velvet tree', 'Swiss chard', 'Penstemon', 'Sycamore tree', 'Daffodil', 'Green pitcher plant', 'Coyote brush', 'Inland taipan', 'Foxglove', 'Aloe vera', 'Eggplant', 'Potato', 'Forget-me-not', 'Jerusalem artichoke',
    'Buckwheat', 'Chickpea', 'Corn', 'Lily of the valley', 'Poinsettia', 'Mulberry', 'Quinoa', 'Cinnamon', 'Dactylis', 'Fava bean', 'Feijoa', 'Cowslip', 'Sage', 'Wisteria', 'Tupelo', 'Turnip', 'Yaupon', 'Grape', 'Jade plant', 'Elodea', 'Killdeer', 'Hackberry tree',
    'Barley', 'Lime', 'Poison Ivy', 'Kudzu', 'Loquat', 'Common myrtle', 'Coriander', 'Carnivorous plants', 'Lima bean', 'Shallot', 'Pigweed', 'Rhododendron', 'Melon', "Dogs mercury", 'Freesia', 'Gooseberry', 'Flax', 'Spinach', 'Air potato', 'Black cohosh', 'Bilberry', 
    'Christmas fern', 'Mediterranean cypress', 'Lacebark', 'Ginseng', 'Rabbitfish', 'Hawthorn', 'Cashew tree', 'Linden', 'Pineapple', 'Medusahead', 'Medlar', 'Common spicebush', 'Dill', 'Bamboo', 'Teak', 'Titan arum', 'Snowberry', 'Silk tree', 'Mint', 'Greek valerian', 
    'Gladiolus', 'Lettuce', 'Guava', 'Basil', 'Camphor tree', 'Bleeding heart', 'Black currant', 'Common smilax', 'Onion', 'Monkey puzzle', 'Goumi', 'Rock ptarmigan', 'Tiger snake', 'Honeysuckle', 'Hibiscus', 'Mimosa (Mimosa pudica)', 'Pine', 'Old World climbing fern',
    'Parsnip', 'Goldenrod', 'Fennel', 'Avocado', 'Broadleaf plantain', 'Aronia', 'Camel thorn', 'Alfalfa', 'Orange', 'Hemp agrimony', 'King protea', 'Persimmon', 'Licorice', 'Beetroot', 'Carrotwood', 'Borage', 'Cantaloupe', 'Dogwood', 'Redbud tree', 'Resurrection plant', 
    'Grevillea', 'Whimbrel', 'Larch', 'Lungwort', 'Soybean', 'Olive', 'Oxalis', 'Quince', 'Henna', 'Lentils', 'Apple', 'Common centaury', 'Bael', 'Clove tree', 'Cassava', 'Papaya', 'Meadowsweet', 'Kiwano', 'Purple loosestrife', 'Primrose', 'Cabbage', 'Catnip', 'Crowberry',
    'Dogbane', 'Harebell', 'Snowdrop', 'Telegraph plant', 'Zinnia', 'Butterfly weed', 'American hornbeam', 'Marigold', 'Begonia', 'Lotus', 'Parrot feather', 'Rowan', 'Mahogany', 'Marsh mallow', 'Birch tree', 'Common gorse', 'Burdock', 'Cocklebur', 'Cattail', 'Oregano', 'Red fescue',
    'Mangosteen', 'Senna', 'Teff', 'Cherry', 'Hyssop', "Culvers root", 'Ephedra', 'Hazelnut', 'Viola', 'Balsa tree', 'Banksia', 'Caper', 'American sweetgum', 'Pea', 'Carob tree', 'Fig', 'Princess tree', 'Soapberry', 'Myristica fragrans (nutmeg)', 'Millet', 'Carrot', 'Common storkbill',
    'Coca', 'Common sneezeweed', 'Elm', 'Walnut tree', 'Water primrose', 'Waratah', 'Tarragon', 'Wormwood', 'Chestnut tree', 'Rosary pea', 'Eelgrass', 'Lingoberry', 'Hickory', 'Angel trumpet', 'Banana', 'Daikon', 'Castor bean', 'Asparagus', 'Peanuts', 'Garlic', 'Eucalyptus',
    'Scotch broom', 'Toyon', 'Rhubarb', 'Passiflora', 'Common nettle', 'Curry plant', 'Cotoneaster', 'Coreopsis', 'Hemp', 'Wheat', 'Boxwood', 'African lovegrass', 'Butter-and-eggs', 'Black cherry', 'Giant sequoia', 'Senegal date palm', 'Evening primrose', 'Pigface', 
    'Japanese knotweed', 'Black bat flower', 'Cactus', 'Glasswort', 'Galangal', 'Cedar', 'Sunflower', 'Jumping cholla', 'Rosemary', 'Willowherb', 'Valerian', 'Witch hazel', "St Johns wort", 'Daisy', 'Fenugreek', 'Jojoba', 'Feverfew', 'Jimson weed', 'Blueberry', 
    'Canada fleabane', 'Bok choi', 'Collard greens', 'Caraway', 'Green beans', 'Skunkvine', 'Purple saxifrage', 'Reindeer lichen', 'Jewelweed', 'Buttercup', 'Crocus', 'Baobab', 'Parsley', 'Photosynthesis Facts'],


    ['Dian Fossey', 'Stephen Hawking', 'Sigmund Freud', 'William Herschel', 'Thomas Hunt Morgan', 'Nikola Tesla', 'Wernher Von Braun', 'Robert Bunsen', 'Wolfgang Ernst Pauli', 'Rudolf Virchow', 'Robert Brown', 'Tycho Brahe', 'Michael Faraday', 'William Harvey', 'William Smith', 'Maria Goeppert-Mayer', 'Thomas Midgley Jr.', 'Rene Descartes', 'Thomas Willis', 'Otto Hahn', 'William Bayliss', 'William Buckland', 'John Logie Baird', 'Percy Lavon Julian', 'Neil Armstrong', 'Neil Degrasse Tyson', 'Prafulla Chandra Ray', 'Thomas Alva Edison', 'William Thomson', 'Rachel Carson', 'Zora Neale Hurston', 'Tim Noakes', 'Robert Bosch', 'Timothy John Berners-Lee', 'Robert Boyle', 'Ukichiro Nakaya', 'Robert Goddard', 'Pierre-Simon Laplace', 'Wilbur And Orville Wright', 'Wilhelm Conrad Roentgen', 'Rosalind Franklin', 'Joseph Lister', 'Salim Ali', 'Sally Ride', 'Justus Von Liebig', 'Noam Chomsky', 'Wilhelm Wundt', 'Srinivasa Ramanujan', 'Steven Chu', 'Mohammad Abdus Salam', 'Robert Koch', 'John Von Neumann', 'Theodosius Dobzhansky', 'Walther Wilhelm Georg Bothe', 'Rudolf Christian Karl Diesel', 'Joseph Banks', 'Werner Heisenberg', 'Thomas Kuhn', 'Jean Piaget', 'Louis Agassiz', 'Leonhard Euler', 'Rita Levi-Montalcini', 'Max Planck', 'John Archibald Wheeler', 'J. Robert Oppenheimer', 'Konrad Lorenz', 'Sven Wingqvist', 'Vladimir Vernadsky', 'Muhammad Ibn Musa Al-Khwarizmi', 'Christiaan Huygens', 'Jonas Salk', 'Jane Goodall', 'Marie Curie', 'Gottfried Leibniz', 'Lise Meitner', 'Thomas Newcomen', 'Max Born', 'Wilhelm Ostwald', 'J. Hans D. Jensen', 'Louis Pasteur', 'J.J. Thomson', 'Katharine Burr Blodgett', 'Charles Babbage', 'Paul Dirac', 'Arnold Orville Beckman', 'Niels Bohr', 'Paul Ehrlich', 'Svante Arrhenius', 'Robert Hooke', 'Pierre Curie', 'James Watson', 'Thomas Burnet', 'Leonardo Da Vinci', 'Linus Pauling', 'Randy Pausch', 'Samuel Morse', 'Sheldon Lee Glashow', 'Omar Khayyam', 'Karl F. Herzfeld', 'Willard Frank Libby', 'John Dalton', 'Dorothy Hodgkin', 'James Chadwick', 'The Wright Brothers', 'Luther Burbank', 'Michio Kaku', 'Arthur Eddington', 'Virginia Apgar', 'Charles Sherrington', 'Harriet Quimby', 'Walter Schottky', 'Agnes Arber', 'Prokop Divis', 'Lester R. Brown', 'Clyde Tombaugh', 'Mary Anning', 'Jean-Baptiste Lamarck', 'Daniel Bernoulli', 'Alberto Santos Dumont', 'Gottlieb Daimler', 'Karl Landsteiner', 'Carolus Linnaeus', 'Otto Haxel', 'Trofim Lysenko', 'Alessandro Volta', 'Homi Jehangir Bhabha', 'Ernst Mayr', 'Humphry Davy', 'Charles Darwin', 'James Clerk Maxwell', 'Charles Lyell', 'Peter Debye', 'William Hopkins', 'Edward Teller', 'Francis Galton', 'John Ray', 'Frank Hornby', 'Ronald Ross',
    'Johannes Kepler', 'Leo Szilard', 'Hedy Lamarr', 'Christiane Nusslein-Volhard', 'George Gamow', 'Niccolo Leoniceno', 'Nicholas Culpeper', 'George Washington Carver', 'Joseph Priestley', 'Claude Levi-Strauss', 'Alfred Wegener', 'Emile Berliner', 'Henry David Thoreau', 'K. Eric Drexler', 'Andre Marie Ampere', 'Richard Feynman', 'Jim Al Khalili', 'David Bohm', 'Max Delbruck', 'Ernesto Illy', 'Antonio Meucci', 'Grace Murray Hopper', 'Ernest Haeckel', 'Gregor Mendel', 'Max Von Laue', 'John Bardeen', 'C.V. Raman', 'Ludwig Boltzmann', 'Ernst Mach', 'Jagadish Chandra Bose', 'John Locke', 'Bill Nye', 'Gustav Kirchoff', 'Pearl Kendrick', 'Alexander Fleming', 'Ernst Werner Von Siemens', 'Kristian Birkeland',
    'Lynn Margulis', 'Alexander Graham Bell', 'Hans Christian Oersted', 'Avicenna', 'Thabit Ibn Qurra', 'Abu Nasr Al-Farabi', 'Mae Carol Jemison', 'William John Swainson', 'Leland Clark', 'Georg Ohm', 'Marcello Malpighi', 'Edwin Herbert Land', 'Murray Gell-Mann', 'Ivan Pavlov', 'William Ramsay', 'Beatrix Potter', 'Maria Gaetana Agnesi', 'Franz Boas', 'B. F. Skinner', 'Benjamin Cabrera', 'Ahmed Zewail', 'Maria Mitchell', 'Hendrik Antoon Lorentz', 'Claude Bernard', 'Nicolaus Copernicus', 'Ramon Barba', 'Albert Abraham Michelson', 'Carl Bosch', 'Descartes', 'Gerty Theresa Cori', 'Henry Ford', 'Carl Sagan', 'Louis De Broglie', 'Abdul Qadeer Khan', 'Andreas Vesalius', 'Henry Moseley', 'Jocelyn Bell Burnell', 'Ernest Rutherford', 'Dmitrti Mendeleev', 'Hermann Von Helmholtz', 'Michael E. Brown', 'Arnold Sommerfeld', 'Erwin Schrodinger', 'Kip S. Thorne', 'Luigi Galvani', 'E.O. Wilson', 'Edmond Halley', 'Gustav Ludwig Hertz', 'Erwin Chargaff', 'Ibn Battuta', 'Euclid', 'Edward Jenner', 'Mihalio Petrovic Alas', 'Evangelista Torricelli', 'Irene Joliot-Curie', 'James Hutton', 'Galileo Galilei', 'Ada Lovelace',
    'James Prescott Joule', 'Adalbert Czerny', 'Alfred Binet', 'Isaac Newton', 'Elizabeth Blackwell', 'Frederick Gowland Hopkins', 'Blaise Pascal', 'Frederick Sanger', 'Benjamin Franklin', 'Alfred Nobel', 'Henry Bessemer', 'Benjamin Thompson', 'Leonardo of Pisa', 'George-Louis Leclerc, Comte De Buffon', 'Henry Cavendish', 'Bernado Houssay', 'Albert Einstein', 'Gertrude Elion', 'Amedeo Avogadro', 'Aristotle', 'Enrico Fermi', 'Carl Friedrich Gauss', 'Albrecht von Haller', 'Antony Hewish', 'Bernhard Riemann', 'Lucretius', 'Antoine Lavoisier', 'Emmy Noether', 'Guglielmo Marconi', 'Antoine van Leeuwenhoek',
    'Andrew Wiles', 'John Napier', 'Ibn Rushd', 'James Dwight Dana', 'Archimedes', 'Lee De Forest', 'Alexander von Humboldt', 'Hans Selye', 'Theodor Schwann', 'Charles-Augustin de Coulomb', 'Edwin Hubble',
    'Leon Foucault', 'Alfred Blalock', 'Heinrich Hertz', 'Jan Baptista Van Helmont', 'Clarence Birdseye', 'Emil von Behring', 'Al-Battani', 'Emil Fischer', 'Henri Becquerel', 'Emil Kraepelin', 'Friedrich Wohler', 'Anders Celsius', 'Fritz Haber', 'Angel Alcala', 'Aldo Leopold', 'Ernst Ising', 'Alan Turing', 'Alexander Bain', 'John Needham', 'Barbara McClintock', 'Alexandre Brongniart', 'George Beadle', 'George Gaylord Simpson', 'Frederick Soddy', 'Jean Andre Deluc', 'Mario Molina', 'Democritus', 'HermannRorschach', 'Keisuke Ito', 'Arrturi Virtanen', 'Alfred Kinsey', 'Pythagoras', 'Friedrich August Kekule', 'Shintaro Hirase Facts'],

    ['Friedrich Wilhelm Von Steuben', 'Ernest Hemingway', 'Robert Munsch', 'Rudyard Kipling', 'Nathaniel Hawthorne', 'Czeslaw Milosz', 'Anne Rice', 'Maya Angelou', 'Jules Verne', 'D. H. Lawrence', 'Lord Byron', 'Anne Frank', 'Nora Roberts', 'Jack Kerouac', 'Mary Shelley', 'Salman Rushdie', 'Dan Brown', 'Stephen King', 'C.S. Lewis', 'Mary Higgins Clark', 'Jeff Kinney', 'Christopher Hitchens', 'Dr. Seuss', 'Gary Paulsen', 'Stephen Hawking', 'Agatha Christie', 'Tennessee Williams', 'Aldous Huxley', 'Germaine Greer', 'Christopher Paolini', 'Beatrix Potter', 'R. L. Stine', 'Jack London', 'Leo Tolstoy', 'Isaac Asimov', 'Elbert Hubbard',
    'Euripides', 'Robert Frost', 'Danielle Steel', 'Ellen G. White', 'J. R. R. Tolkien', 'Franz Kafka', 'Harper Lee', 'William Shakespeare', 'Michael Ende', 'Roald Dahl', 'Frank McCourt', 'E.M. Forster', 'Enid Blyton', 'Edgar Allan Poe', 'Holly Black', 'George Orwell', 'Laura Ingalls Wilder', 'Washington Irving', 'Lucy Maud Montgomery', 'Mario Puzo', 'Barbara Cartland', 'Richard Scarry', 'J.D. Salinger', 'William S. Burroughs', 'Chinua Achebe', 'Allen Ginsberg', 'Jane Austen', 'Antoine De Saint-Exupery', 'Dashiell Hammett', 'John Grisham', 'Beverly Cleary', 'Kenneth Grahame', 'Astrid Lindgren', 'Roger Hargreaves', 'David Baldacci', 'David Foster Wallace', 'A.A. Milne', 'AynRand', 'Hans Christian Andersen', 'Fernando Pessoa', "Flannery OConnor", 'Truman Capote', 'Edith Wharton', 'Virginia Woolf', 'Walt Whitman', 'Chuck Palahniuk', 'Arthur Miller', 'Mark Twain', 'NapoleonHill', 'F. Scott Fitzgerald', 'Nicholas Sparks', 'Anais Nin', 'Edward Stratemeyer', 'Daphne du Maurier', 'Louisa May Alcott', 'Edward Lear', 'Patricia Cornwell', 'Arthur C. Clarke', 'John Steinbeck', 'Judy Blume', 'Hunter S. Thompson', 'J. K. Rowling', 'James Patterson', 'Sidney Sheldon', 'Oscar Wilde', 'George Eliot', 'Debbie Macomber', 'George Bernard Shaw', 'Kurt Vonnegut', 'Don DeLillo', 'Tom Clancy', 'Elie Wiesel', 'Geoffrey Chaucer', 'Voltaire', 'Alan Moore', 'Albert Camus', 'Eric Carle', 'Douglas Adams', 'Dante Alighieri', 'Cormac McCarthy', 'Charles Dickens', 'Jackie Collins', 'Ian Fleming', 'Sir Francis Drake', 'Joseph Conrad', 'Dav Pilkey', 'Lewis Carroll', 'Alexander Mccall Smith', 'Anton Chekhov', 'H. G. Wells', 'Gabriel Garcia Marquez', 'Dean Koontz', 'Jean de Brunhoff', 'Dale Carnegie', 'Walter Farley', 'Arundhati Roy', 'Michelangelo Buonarroti', 'Homer', 'L. Frank Baum', 'Clive Cussler', 'Marc Brown', 'Christopher Marlowe', 'Emily Dickinson', 'Daniel Defoe', 'Lynne Reid Banks', 'Johnny Gruelle', 'Hugh Lofting', 'George R. R. Martin', 'Herman Melville', 'Doris Lessing Facts'], 

    ['Jackie Robinson', 'Adam Levine', 'Daniel Boone', 'Bradley Cooper', 'Tupac Shakur', 'Abraham Lincoln', 'Barack Obama', 'Thomas Edison', 'Whitey Bulger', 'Michelle Knight', 'Idris Elba', 'Daniel Craig',
    'Cesar Chavez', 'Arnold Schwarzenegger', 'Al Capone', 'George Washington Carver', 'Louis Armstrong',
    'Selena Quintanilla', 'Calvin Coolidge', 'Eazy-E', 'Mark Zuckerberg', 'Matt Damon', 'Martin Luther King Jr.', 'Tom Hardy', 'Melania Knauss (Trump)', 'Fidel Castro', 'Charles Manson', 'Rachel McAdams', 'Deborah Sampson', 'Adam Sandler', 'Robin Williams', 'Queen Elizabeth', 'Kate Winslet', 'Jimmy Carter', 'Eddie Murphy', 'Tina Turner', 'Sojourner Truth', 'Emma Stone', 'Matthew McConaughey', 'Joseph Pulitzer', 'Junipero Serra', 'James Brown', 'Pablo Escobar', 'Hillary Clinton', 'Dwight D Eisenhower', 'Christina Ricci', 'Clint Eastwood', 'Andrew Jackson', 'Mao Zedong', 'Amy Winehouse', 'Mark Wahlberg',
    'Anna Kendrick', 'Winston Churchill', 'Florence Nightingale', 'Betty White', 'Thurgood Marshall', 'Miguel Hidalgo', 'Freddie Mercury', 'Robert Frost', 'Shirley Chisholm', 'Bruce Jenner', 'Harrison Ford', 'Will Smith', 'Bartolomeu Dias', 'Morgan Freeman', 'Bernie Sanders', 'Molly Pitcher', 'Donald Trump', 'Sybil Ludington', 'James Dean', 'Amelia Earhart', 'Olaudah Equiano', 'Reese Witherspoon', 'MarcoRubio', 'Alan Rickman', 'Ted Cruz', 'Sam Houston', 'Amanda Knox', 'Denzel Washington', 'Diana Ross',
    'Ted Bundy', 'Meryl Streep', 'Jesse Owens', 'Jane Addams', 'Grover Cleveland', 'Ida B Wells', 'Harriet Tubman', 'Francisco Pizarro', 'Socrates', 'Susan B. Anthony', 'Charles Perrault', 'Nellie Bly', 'Nicolaus Copernicus', 'Steve Jobs', 'Robert E. Lee', 'Jodi Arias', 'Amerigo Vespucci', 'Sean Penn', 'Suge Knight', 'Teddy Roosevelt', 'Roberto Clemente', 'Juan Ponce de Leon', 'Abigail Adams', 'Buddy Holly', 'Howard Hughes', 'Michael Oher', 'Christopher Columbus', 'Marco Polo', 'Carly Fiorina', 'Paul Revere', 'President John F. Kennedy', 'Alice Paul', 'Lizzie Borden', 'Duke Ellington', 'Oprah Winfrey',
    'Chevy Chase', 'Jeffrey Dahmer', 'Henry Hudson', 'Ferdinand Magellan', 'Alexander Hamilton', 'Christian Longo', 'Jacques Cartier', 'Jon Stewart', 'Hitler Facts'],

    ['Morrocoy National Park', 'Glacier Bay National Park', 'Kings Canyon National Park', 'Voyageurs National Park', 'Nikko National Park', 'Karijini National Park', 'Canaima National Park', 'Carlsbad Caverns National Park', 'Kruger National Park', 'Virunga National Park', 'Cahuita National Park', 'Congaree National Park', 'Jasper National Park', 'Corcovado National Park', 'Waterton Lakes National Park', 'Cairngorms National Park', 'Kanha National Park', 'Quttinirpaaq National Park', 'Fundy National Park', 'Connemara National Park', 'Zion National Park', 'Yoho National Park', 'Hwange National Park', 'Bryce National Park', 'Banff National Park', 'Kakadu National Park', 'Taroko National Park', 'Isle Royale National Park', 'Kenting National Park', 'Black Canyon of the Gunnison', 'Gorongosa National Park', 'Biscayne National Park', 'Cotopaxi National Park', 'Tarangire National Park', 'Great Basin National Park', 'Fiordland National Park', 'Shenandoah National Park', 'Redwood National Park', 'Haleakala National Park', 'Chobe National Park', 'Abisko National Park', 'Thingvellir National Park', 'Cumberland Gap National Historical Park', 'Carara National Park', 'Hawaii Volcanoes National Park', 'Lake Clark National Park', 'Dartmoor National Park', 'Mammoth Cave National Park', 'Ranomafana National Park',
    'Isalo National Park', 'Kakum National Park', 'Snowdonia National Park', 'Tikal National Park', 'Big Bend National Park', 'Nahanni National Park', 'Channel Islands National Park', 'Mochima National Park', 'Grand Teton National Park', 'Pico Bonito National Park', 'National Park of American Samoa', 'Acadia National Park', 'Chankanaab National Park', 'Red Rock State Park', 'Pukaskwa National Park', 'Chirripo National Park', 'Bruce Peninsula National Park', 'Guadalupe National Park', 'Dry Tortugas National Park', 'Burren National Park', 'Lassen Volcanic National Park', 'Mesa Verde National Park', 'Bannerghatta National Park', 'Hot Springs National Park', 'Khao Yai National Park', 'Freycinet National Park', 'Badlands National Park', 'North Cascades National Park', 'Gunung Mulu National Park', 'Skaftafell National Park', 'Sequoia National Park', 'Kaziranga National Park', 'Pinnacles National Park', 'Uluru-Kata Tjuta National Park', 'Serengeti National Park', 'Kootenay National Park', 'Lucayan National Park', 'Tayrona National Park', 'Phong Nha-ke Bang National Park', 'Crater Lake National Park', 'Tongariro National Park', 'Amboseli National Park', 'Cinque Terre National Park', 'Muir Woods National Monument', 'Kaieteur National Park', 'Tortuguero National Park', 'Saguaro National Park', 'Kobuk Valley National Park', 'Chapada Diamantina National Park', 'Ranthambore National Park', 'Khao Sok National Park', 'Arches National Park', 'Harpers Ferry National Historical Park', 'Petrified Forest National Park', 'Kluane National Park', 'Kenai Fjords', 'Wind Cave National Park', 'Gates of the Arctic National Park', 'Yasuni National Park', 'Great Sand Dunes National Park and Preserve', 'Chitwan National Park', 'Virgin Islands National Park', 'Killarney National Park', 'Canyonlands National Park', 'Plitvice Lakes National Park', 'Katmai Provincial Park', 'Capitol Reef National Park', 'Wrangell-St. Elias National Park', 'Etosha National Park', 'Theodore Roosevelt National Park Facts'],

    ['Bromine', 'Zirconium', 'Iron', 'Germanium', 'Krypton', 'Molybdenum', 'Cobalt', 'Nickel', 'Technetium', 'Polonium', 'Caesium', 'Ruthenium', 'Zinc', 'Gallium', 'Copper', 'Yttrium', 'Xenon', 'Iridium', 'Arsenic', 'Palladium', 'Titanium', 'Potassium', 'Rubidium', 'Argon', 'Antimony', 'Iodine', 'Barium', 'Strontium', 'Manganese', 'Hafnium', 'Aluminium', 'Rhenium', 'Gold', 'Magnesium', 'Tin', 'Lead', 'Selenium', 'Fluorine', 'Tellurium', 'Mercury', 'Bismuth', 'Oxygen', 'Calcium', 'Silicon', 'Sulfur', 'Bohrium', 'Platinum', 'Meitnerium', 'Seaborgium', 'Nitrogen', 'Carbon', 'Tantalum', 'Niobium', 'Lutetium', 'Sodium', 'Rhodium', 'Silver', 'Cadmium', 'Scandium', 'Lawrencium', 'Helium', 'Chlorine', 'Indium', 'Thallium', 'Phosphorus', 'Radium', 'Beryllium', 'Osmium', 'Hassium', 'Tungsten', 'Darmstadtium', 'Lithium', 'Radon', 'Vanadium', 'Francium', 'Mendelevium', 'Neon', 'Astatine', 'Chromium', 'Cerium', 'Lanthanum', 'Praseodymium', 'Hydrogen', 'Dubnium', 'Rutherfordium', 'Nobelium', 'Boron', 'Neodymium Facts'],

    ['Connecticut', 'Idaho', 'Washington', 'Iowa', 'Maine', 'Delaware', 'Florida', 'Montana', 'Nebraska',
    'New Jersey', 'Wisconsin', 'Kansas', 'Alaska', 'Mississippi', 'Illinois', 'Indiana', 'Wyoming', 'Georgia', 'Louisiana', 'Maryland', 'Pennsylvania', 'Arizona', 'Colorado', 'Vermont', 'Nevada', 'North Carolina', 'Kentucky', 'Oklahoma', 'Arkansas', 'South Dakota', 'Utah', 'Hawaii', 'California', 'Alabama', 'Rhode Island', 'West Virginia', 'New York', 'North Dakota', 'Oregon', 'Massachusetts', 'Michigan', 'Missouri', 'Tennessee', 'New Hampshire', 'Texas', 'Virginia', 'New Mexico', 'Ohio', 'Minnesota', 'South Carolina', 'Puerto Rico Facts'],

    ['Christmas', 'Kwanzaa', "St. Patricks Day", 'Groundhog Day', 'Halloween', 'Easter', 'Hispanic Heritage Month', 'Columbus Day', "Bosss Day", 'Jackie Robinson Day', 'Constitution Day', "Mothers Day", 'Arbor Day', 'Cinco de Mayo', 'All Saints Day', "Valentines Day", 'Star Wars Day', 'Mardi Gras', 'Anzac Day', 'Chinese New Year', 'Ramadan', "Veterans Day", 'Ascension Day', 'Black History Month', 'Memorial Day', 'Victoria Day', 'Bastille Day', 'Thanksgiving', 'The 4th of July', 'Armed Forces Day', "April Fools Day", 'Remembrance Day', 'Super Bowl', 'Nurses Day', 'Red Nose Day', "Patriots Day", 'Summer Solstice', "Teachers Appreciation Day", 'Australia Day', 'Hanukkah', 'National Hotdog Day', 'National Sibling Day', 'Earth Day', "Presidents Day", 'Pancake Day', "Grandparents Day", 'Leif Erikson Day', 'Tax Day', 'Winter Solstice', 'Armistice Day', 'National Donut Day', 'Guy Fawkes', 'National Ice Cream Day', 'Administrative Professionals Day', 'Boxing Day', 'Flag Day', 'Labor Day', 'Take Your Child to Work Day', 'Holocaust Remembrance Day', 'World Health Day Facts'],

    ['Beagles', 'Australian Terrier', 'Dalmatian', 'Bullmastiff', 'Samoyed', 'Basenji dog', 'Doberman Pinscher', 'Cane Corso', 'Shetland Sheepdog', 'Affenpinscher', 'Basset Hound', 'Dogo Argentino', 'Dachshund', 'Weimaraner', 'Afghan Hound', 'Beagle', 'Entlebucher Mountain Dog', 'German Shorthaired Pointer', 'Ainu dog', 'Bernese Mountain Dog', 'German Pinscher', 'Havanese', 'Akbash dog', 'Bichon Frise', 'English Mastiff', 'Lhasa Apso', 'Akita dog', 'Bloodhound', 'Great Dane', 'Pug', 'Alaskan Malamute', 'Bluetick Coonhound', 'Greenland Dog', 'Rottweiler', 'American Bulldog', 'Bolognese dog', 'Jack Russell', 'Welsh Corgi', 'American Cocker Spaniel', 'Border Collie', 'Labradoodle', 'Cavalier King Charles Spaniel', 'American Coonhound', 'Boston Terrier', 'Poodle', 'English Springer Spaniel', 'American Eskimo dog', 'Boxer', 'Shih Tzu', 'Golden Retriever', 'American Foxhound', 'Bull Terrier', 'Siberian Husky', 'Labrador Retriever', 'American Pit Bull Terrier', 'Bulldog', 'St. Bernard', 'Miniature Schnauzer', 'Appenzeller Sennenhund', 'Chesapeake Bay Retriever', 'Yorkshire Terrier', 'Pomeranian', 'Australian Shepherd', 'Chihuahua', 'Airedale Terrier', 'Rhodesian Ridgeback Facts'],

    ['Apollo', 'Jupiter', 'Mars', 'Uranus', 'Sun', 'Pluto', 'Saturn', 'Mercury', 'Venus', 'Earth', 'Neptune', 'Solar System', 'Eris', 'Haumea', 'NASA', 'Atmosphere', 'Whirlpool Galaxy', 'Inner Planets', 'Astronomy', 'Meteors', 'Outer Space', 'Pinwheel Galaxy', 'Solar Eclipse', 'Cancer Constellation', 'Nebula', 'Space Shuttle', 'Sombrero Galaxy', 'Moon', 'Spiral Galaxy', 'Moon Phases', 'Spitzer Space Telescope', 'Milky Way', 'Universe', 'Lunar Eclipse', 'Stars', 'Galaxy', "Halleys Comet", 'Comet', 'Black Hole', 'Andromeda Galaxy', 'Telescope', 'Reflecting Telescope', 'Refracting Telescope', 'Hubble Space Telescope', 'The Antennae', 'Supernova', 'Kuiper Belt', 'Constellations', 'Moons', 'Triangulum Galaxy', 'Magellanic Clouds', 'Europa', 'Callisto', 'Triton', 'Messier 87', 'Oort Cloud', 'Dwarf Planets', 'Ceres', 'Titan', 'Makemake', 'Gas Giants', 'Phobos', 'Meteor Showers', 'Deimos', 'Ganymede Facts'],

    ['Tuskegee Airmen', 'Harvard University', 'Cherokee', 'Prohibition', 'September 11 2001', 'Iroquois', 'Biltmore Estate', 'Jefferson Davis', 'Tomochichi', 'Jamestown', 'Cheyenne Indian', 'Amish', 'Navajo', 'Roswell UFO Incident', 'Pocahontas', 'Jumano', 'Twin Towers', 'Crispus Attucks', 'John Dillinger', 'Shawnee Tribe', 'Madam C.J. Walker', 'Hopi Tribe', 'Dust Bowl', 'The Great Depression', 'Squanto',
    'Trail of Tears', 'Charlemagne', 'Hiroshima Bombing', 'Gandhi', 'Westward Expansion', 'Indian Removal Act', 'Sacagawea', 'Annie Oakley', 'Audrey Hepburn', 'First Transcontinental Railroad', 'Emancipation Proclamation', 'NASCAR', 'Rosie the Riveter', 'Sonia Sotomayor', 'Native American', 'Pearl Harbor', "I Have a Dream' Speech", 'Seneca Falls Convention', 'Lewis and Clark Expedition', 'Columbian Exchange', 'Guantanamo Bay', 'Mayflower', 'McCarthyism', 'Andersonville Prison', 'Declaration of Independence', 'Confederate Flag', 'Civil War Union Flag', 'American Flag', 'Star Spangled Banner', 'Canadian Pacific Railway', 'Louisiana Purchase', 'Segregation', 'Battle of Bunker Hill', 'Pilgrims', 'War on Terror Facts'], 

    ['Ecuador', 'Guatemala', 'Honduras', 'Spain', 'Switzerland', 'Venezuela', 'Germany', 'Japan', 'China', 'Brazil', 'Uruguay', 'France', 'Peru', 'Sweden', 'Paraguay', 'Thailand', 'Chile', 'Israel', 'Bahamas', 'Australia', 'Egypt', 'Mongolia', 'Djibouti', 'Botswana', 'Bolivia', 'Argentina', 'Italy', 'Haiti', 'Philippines', 'Liechtenstein', 'Ireland', 'Iceland', 'Luxembourg', 'Nicaragua', 'Ivory Coast', 'Estonia', 'Sierra Leone', 'Vatican City Facts'],

    ['Eiffel Tower', 'The Grand Canyon', 'Halong Bay', 'Victoria Falls', 'Mount Everest', 'The Aurora', 'Delta Works/ Zuiderzee Works', 'Sahara Desert', 'Komodo Island', 'Temple of Artemis at Ephesus', 'Amazon Rainforest', 'Christ the Redeemer', 'Panama Canal', 'Paricutin Volcano', 'The Great Barrier Reef', 'Leaning Tower of Pisa', 'Itaipu Dam', 'Empire State Building', 'Iguazu Falls', 'Porcelain Tower of Nanjing', 'Mausoleum at Halicarnassus', 'Petra', 'Hagia Sophia', 'Golden Gate Bridge', 'Table Mountain', 'Puerto Princesa Underground River', 'Cairo Citadel', 'Channel Tunnel', 'CN Tower', 'Cluny Abbey', 'Harbor of Rio de Janeiro', 'Colosseum', 'Ely Cathedral', 'Jeju Island', 'Great Wall of China', 'Stonehenge', 'Pyramids', 'Chichen Itza', 'Taj Mahal', 'Machu Picchu', 'Hanging Gardens of Babylon', 'Statue of Zeus at Olympia', 'Colossus of Rhodes', 'Lighthouse of Alexandria', 'Catacombs of Kom el Shoqafa', 'Great Pyramid of Giza', 'Boreal Forest Facts'],

    ['Dentist', 'Sucralose', 'Farts', 'Yoga', 'Pneumonia', 'Yellow Fever', 'Hemophilia', 'Gluten', 'Carbohydrates', 'Asthma', 'Shingles', 'Scoliosis', 'Anorexia', 'Breast Cancer', 'Nursing', 'Diabetes', 'Asperger Syndrome', 'Protein', 'Cannabis', 'Epilepsy', 'Bulimia', 'Caffeine', 'Liver Cancer', 'Dehydration', 'Ebola Virus', 'Botulism', 'Malaria', 'Influenza', 'Concussion', 'Hypertension', 'Dental Hygiene', 'Chiropractic', 'Vaccines', 'Hydration', 'Sunscreen', 'Leukemia', 'Insomnia', "Alzheimers Disease", 'Arthritis', 'Lipids', 'Meditation', 'Lice', 'E Coli', 'Progeria', 'Pediatricians', 'Flu', 'Lupus', 'Smallpox', 'Skin Cancer Facts'],
    
    ['Sampler', 'Ukulele', 'Xylophone', 'Guitar', 'Harp', 'Bassoon', 'Oboe', 'Tambourine', 'Glockenspiel', 'Accordion', 'Bagpipe', 'Conch', 'Pipe Organ', 'Turntable', 'Cajon', 'Tam-Tam', 'Laser Harp', 'Mandolin', 'Bugle', 'Electronic Organ', 'Drum Machine', 'Synthesizer', 'Castanets', 'Steel Pan', 'Keytar', 'Drum Kit', 'Clarinet', 'Taiko', 'French Horn', 'Hammond Organ', 'Lyre', 'Banjo', 'Celesta', 'Conga Drum', 'Piano', 'Recorder', 'Sitar', 'Timpani', 'Washtub Bass', 'Triangle', 'Bongo Drum', 'MIDI', 'Hang', 'Marimba', 'Fiddle', 'Talking Drum', 'Bass Drum', 'Snare Drum', 'Keyboard', 'Vibraphone Facts'],

    ['Taekwondo', 'Basketball', 'Skateboarding', 'Wrestling', 'Gymnastics', 'Golf', 'Hockey', 'Tennis', 'Bowling', 'Volleyball', 'Badminton', 'Baltimore Ravens', 'Archery', 'Rowing', 'Wimbledon', 'Winter Olympics', 'Michael Jordan', 'Carolina Panthers', 'Cincinnati Bengals', 'Softball', 'Detroit Lions', 'Houston Texans', 'NFL', 'Arizona Cardinals', 'Cristiano Ronaldo', 'Football', 'Ice Skating', 'New Orleans Saints', 'Soccer', 'Satchel Paige', 'Kobe Bryant', 'Scuba Diving', 'Skydiving', 'Atlanta Falcons', 'Buffalo Bills', 'Denver Broncos', 'Indianapolis Colts', 'Hunting', 'Green Bay Packers', 'Cleveland Browns', 'Dallas Cowboys', 'Baseball', 'Rugby', 'Jackie Chan', 'Chicago Bears', 'Bullfighting Facts'],
    
    ['Arabian Sea', 'Kara Sea', 'Central Baltic Sea', 'Baltic Sea', 'White Sea', 'Yellow Sea', 'Cape Cod Bay', 'Adriatic Sea', 'Mediterranean Sea', 'Argentine Sea', 'Red Sea', 'English Channel', 'Gulf of Mexico', 'Buzzards Bay', 'Hudson Bay', 'Baffin Bay', 'Laptev Sea', 'Persian Gulf', 'Sea of Japan', 'Coral Sea', 'Bay of Biscay', 'Irish Sea', 'Andaman Sea', 'James Bay', 'Archipelago Sea', 'Bering Sea', 'South China Sea', 'Timor Sea', 'Chukchi Sea', 'Bass Strait', 'Norwegian Sea', 'Black Sea', 'Chesapeake Bay', 'Bay of Bengal', 'Bay of Fundy', 'Caribbean Sea', 'Gulf of California', 'Gulf of St. Lawrence', 'Gulf of Thailand', 'The Northwest Passage', 'Celebes Sea', 'Aegean Sea', 'Drake Passage', 'Amundsen Sea', 'Celtic Sea', 'Banda Sea', 'Barents Sea', 'Alboran Sea', 'Arafura Sea', 'Beaufort Sea', 'Bohai Sea', 'Denmark Strait', 'Bali Sea', 'Bay of Campeche Facts'],

    ['Marie Antoinette', 'Hannibal', 'Helen Keller', 'Mussolini', 'Rwandan Genocide', 'Saddam Hussein', 'Hernando de Soto', 'Pope Francis', 'Alexander the Great', 'Boston Massacre', 'Dawes Act', 'Titanic', 'Bruce Lee', 'Japanese Internment Camps', 'Spider-man', 'Charles Lindbergh', 'Neanderthal', 'Berlin Wall', 'Photography', 'Cenozoic Era', 'Vikings', 'Korean War', 'Spanish American War', 'War of 1812', 'Boston Tea Party', 'Underground Railroad', 'American Revolution', 'Magna Carta', 'Pax Romana', 'Medieval Castles', 'Barbie', 'Kristallnacht', 'Spanish Armada', 'Oskar Schindler', 'Spinosaurus', 'Mummification', 'Mona Lisa Facts'],
    
    ['Holocaust', 'Ancient China', 'Hideki Tojo', 'Vasco da Gama', 'World War I', 'Vietnam War', 'World War II', 'Juan Manuel de Rosas', 'French Culture', 'Zhou Dynasty', 'Pompeii', 'Samurai', 'French and Indian War', 'Kremlin', 'Chernobyl', 'Normandy Invasion', 'Sui Dynasty', 'Terracotta Warriors', 'Crusades', 'Acropolis of Athens', 'Auschwitz', 'United Nations', 'Greek Culture', 'French Revolution', 'Warsaw Ghetto', 'Mansa Musa I', 'Viking', 'Tiananmen Square', 'Reign of Terror', 'Shang Dynasty', 'The Pantheon', 'Song Dynasty', 'Silk Road', 'Roanoke Colony', 'Black Plague', 'Harlem Renaissance', 'Vlad the Impaler Facts'],

    ['The Statue of Liberty', 'Great Smoky Mountains National Park', 'Yosemite National Park', 'Zion National Park', 'The White House', 'Yellowstone National Park', 'Liberty Bell', 'Olympic National Park', 'Niagara Falls', 'Pentagon', 'Rocky Mountain National Park', 'The Supreme Court Building', 'Acadia National Park', 'Mount Rushmore', 'The Alamo', 'Hoover Dam', 'Mount Rainier Volcano', 'Washington Monument', 'Broadway', 'Everglades National Park', 'Arlington National Cemetery', 'Denali (Mount McKinley)', 'Cuyahoga Valley National Park', 'Angel Island', 'The Great Lakes', 'Disneyland', 'Mount St. Helens', 'Ellis Island', 'Lake Tahoe', 'Lincoln Memorial', 'Vietnam Veterans Memorial Facts'], 

    ['Islands', 'Key West', 'South America', 'Guadeloupe', 'Plains', 'Caribbean', 'Dubai', 'San Andreas Fault', 'Geosphere', 'Lake Titicaca', 'Antarctica', 'Arctic Ocean', 'Ocean', 'Oceanography', 'Southern Ocean', 'Water', 'Pacific Ocean', 'Atlantic Ocean', 'Burj Khalifa', 'The Dead Sea', 'Mariana Trench', 'Himalayas', 'Waterfalls', 'Mountains', 'Valley', 'Sinkhole', 'Ocean Animals', 'Bermuda Triangle', 'Aral Sea', 'Indian Ocean', 'Glacier', 'Landform', 'Earth Layers', 'Angel Falls', 'Canyon', 'Shield Volcano Facts'], 
    
    ['Human T-Lymphotropic Virus', 'Hepatitis B Virus', 'Hepatitis E Virus', 'Monkeypox Virus', 'Human Parainfluenza Viruses', 'Herpes Simplex Virus', 'Yellow Fever', 'Human Papillomavirus', "Kaposis Sarcoma-Associated Herpes Virus", 'Norwalk Virus', 'Kunjin Virus', 'Chikungunya Virus', 'Hepatitis C Virus', 'Crimean-Congo Hemorrhagic Fever Virus', 'MERS Coronavirus', 'Lassa Virus', 'Dengue', 'Epstein-Barr Virus', 'Sars Coronavirus', 'Merkel Cell Polyomavirus', 'Ebola Virus', 'Hantavirus', 'Rotavirus', 'Varicella Zoster Virus', 'HIV', 'Human Coronavirus', 'Marburg Virus', 'Influenza', 'Rabies', 'Zika Virus Facts'], 
    
    ['Pancakes', 'Beef', 'Coffee', 'Bacon', 'M and Ms', 'McDonalds', 'Cadbury', 'Coca-Cola', 'Dr. Pepper', 'Sugar', 'Cheese', 'Lucozade', 'Chewing Gum', 'Burger King', 'Donuts', 'KFC', 'Pizza', 'Pasta', 'Agriculture', 'GMOs', 'Chocolate', 'Mushrooms', 'Gatorade', 'Popcorn', 'Factory Farming Facts'],

    ['Quinoa Nutrition', 'Broccoli Nutrition', 'Avocado Nutrition', 'Banana Nutrition', 'Kale Nutrition', 'Watermelon Nutrition', 'Blackberry', 'Sweet Potato Nutrition', 'Tofu Nutrition', 'Blackberry Nutrition', 'Popcorn Nutrition', 'Almonds Nutrition', 'Apple Nutrition', 'Egg Nutrition', 'Zucchini Nutrition', 'Milk Nutrition', 'Peanut Butter Nutrition', 'Potato Nutrition', 'Spinach Nutrition', 'Olives Nutrition', 'Strawberry Nutrition', 'Hummus Nutrition', 'Orange Juice', 'Calcium', 'Canola Oil Nutrition', 'Rice Nutrition', 'Vitamin D', 'Vitamin C', 'Folic Acid Facts'], 
    
    ['Zeus', 'Mesopotamia', 'Sparta', 'Mayans', 'Hercules', 'Hephaestus', 'Hieroglyphics', 'Medusa', 'Julius Caesar', 'Tenochtitlan', 'Parthenon', 'Xia Dynasty', 'Aztec', 'Isis Goddess', 'Athena', 'Cleopatra', 'Ancient Greece', 'King Tut', 'Aphrodite', 'Pharaohs', 'Mohenjo-daro', 'Poseidon', 'Ramses ii', 'Greek Gods', 'Queen Hatshepsut Facts'],

    ['Peridotite', 'Scoria', 'Iron Ore', 'Basalt', 'Pegmatite', 'Pumice', 'Rhyolite', 'Novaculite', 'Gabbro', 'Muscovite', 'Igneous Rocks', 'Tuff', 'Metamorphic Rocks', 'Amphibolite', 'Sedimentary Rocks', 'Sandstone', 'Limestone', 'Obsidian Rock', 'Andesite', 'Granite', 'Breccia', 'Hornfels', 'Coal', 'Phyllite', 'Soapstone', 'Marble', 'Chert', 'Siltstone', 'Conglomerate', 'Rocksalt', 'Flint Facts'],

    ['Southern Colonies', 'Pennsylvania Colony', 'New Hampshire Colony', 'Delaware Colony', 'New York Colony', 'Virginia Colony', 'South Carolina Colony', 'Connecticut Colony', 'Georgia Colony', 'Maryland Colony', 'North Carolina Colony', 'Massachusetts Colony', 'John Peter Zenger', 'New England Colonies',
    'Thomas Paine', 'New Jersey Colony', 'The Middle Passage', 'Middle Colonies', '13 Colonies', 'The Battles of Saratoga', 'Rhode Island Colony', 'The Townshend Acts', 'First Continental Congress', 'Second Continental Congress', 'The Tea Act Facts'], 
    
    ['Charlie Chaplin', 'Vincent Van Gogh', 'Elvis Presley', 'Salvador Dali', 'Paolo Uccello', 'Wassily Kandinsky', 'Pablo Picasso', 'Carlo Crivelli', 'Andy Warhol', 'Diego Rivera', 'Bob Marley', 'Andrea Mantegna', 'Masolino', 'Frida Kahlo', 'Titian', 'Andrea del Castagno', 'Phillis Wheatley', 'Raphael', 'Mozart', 'Fra Angelico', 'Luca Signorelli', 'Pisanello', 'Alessio Baldovinetti', 'Benozzo Gozzoli', 'Piero di Cosimo Facts'],

    ['Hurricanes', 'Tornadoes', 'Typhoon Haiyan', 'Tsunamis', 'Meteorology', 'Snowflake', 'Monsoon', 'Thermosphere', 'Cumulonimbus Clouds', 'Thunderstorm', 'Hurricane', 'Mesosphere', 'Stratosphere', 'Acid Rain', 'El Nino', 'Rainbow', 'Blizzard', 'Weather', 'Troposphere', 'Ozone Layer', 'Snow', 'Exosphere Facts'], 
    
    ['Loire River', 'Thames River', 'Danube River', 'Ganges River', 'Mekong River', 'Congo River', 'Nile River', 'Volga River', 'Rivers', 'Missouri River', 'Mississippi River', 'Amazon River', 'Orinoco River', 'Rhine River', 'Colorado River', 'Red River', 'Zambezi River', 'Yangtze River', 'Sepik River', 'Columbia River', 'Niger River', 'Rio Grande', 'Brisbane River Facts'], 

    ['Stegosaurus', 'Titanosaurus', 'Allosaurus', 'Torvosaurus', 'Ankylosaurus', 'Triceratops', 'Apatosaurus', 'Tyrannosaurus rex', 'Brachiosaurus', 'Velociraptor', 'Carnotaurus', 'Brontosaurus', 'Deinonychus', 'Diplodocus', 'Iguanodon', 'Parasaurolophus', 'Sauropods', 'Amphicoelias', 'Camarasaurus', 'Saurophaganax', 'Spinosaurus', 'Dilophosaurus', 'Pterodactyl Facts'],

    ['Bones', 'Teeth', 'Human Brain', 'Tongue', 'Albinism', 'Muscles', 'Hair', 'Skeletal System', 'Esophagus', 'Small Intestine', 'Digestive System', 'O Negative Blood', 'The Skin', 'The Skeleton', 'The Intestines', 'Bacteria', 'The Stomach', 'The Nose', 'Immune System', 'The Mouth', 'Kidneys', 'Liver', 'Heart', 'Lungs', 'The Pancreas', 'The Ears Facts'], 
    
    ['Pikachu', 'Slowbro', 'Scrabble', 'Lego', 'Monopoly', 'Bingo Game', 'Xbox 360', 'The Legend of Zelda', 'Nintendo Game Boy', 'Space Invaders', 'Call of Duty: Modern Warfare 2', "Microsofts Xbox One", 'Princess Peach', 'National Mario Day', "Nintendos Wii", 'Pac-Man', 'Pokemon Go', 'PlayStation 2', 'Jak and Daxter Games Facts'],

    ['Birman', 'British Shorthair', 'Himalayan cat', 'Abyssinian cat', 'Manx', 'African palm civet', 'Norwegian Forest cat', 'Burmese cat', 'Scottish Fold', 'Egyptian Mau', 'Siberian', 'Maine Coon', 'Turkish Van', 'Persian cat', 'Ragdoll', 'Russian Blue', 'Siamese', 'Sphynx', 'Tiffany', 'Turkish Angora', 'American Shorthair', 'Bengal cat Facts'],

    ['Emeralds', 'Diamond', 'Minerals', 'Quartz', 'Quartzite', 'Schist Rock', 'Lithosphere', 'Shale Rock', 'Slate', 'Calcite', 'Volcano', 'Crystals', 'Dolomite', 'Earthquake', 'Fluorite', 'Fossils', 'Geology', 'Gneiss', 'Gypsum', 'Halite', 'Inner Core Facts'],
    
    ['Biofuel', 'Radiation', 'Wind Power', 'Biodiesel', 'Biomass', 'Solar Energy', 'Sound Energy', 'Thermal Energy', 'Wind Energy', 'Fossil Fuel', 'Chemical Energy', 'Electrical Energy', 'Energy', 'Kinetic Energy', 'Light Energy', 'Mechanical Energy', 'Nuclear Energy', 'Potential Energy', 'Renewable Energy Facts'],

    ['Paracress', 'Radicchio', 'Amaranth', 'Rapini', 'Arugula', 'Rock samphire', 'Chaya', 'Sea kale', 'Common purslane', 'Vine spinach', 'Endive', 'Fat hen', 'Fiddlehead', 'Garden cress', 'Good King Henry', "Catsear Cats ear", "Lambs lettuce", "Lizards tail", 'Mizuna', 'Nalta jute Facts'],

    ['Battle of Nashville', 'Battle of the Wilderness', 'Battle of Spotsylvania Court House', 'Battle of Fredericksburg', 'Battle of Gettysburg', 'Battle of Fort Donelson', 'Battle of Chickamauga', 'The Second Battle of Bull Run', 'Battle of Wilsons Creek', 'Abner Doubleday', 'Albert Sidney Johnston', 'The Battle of Stones River', 'The Battle of Shiloh', 'The Battle of Chancellorsville', 'Alexander H. Stephens', 'Battle of Hampton Roads', 'Battles for Chattanooga', 'Battle of Fort Henry', 'Battle of Mobile Bay', 'Battle of Antietam Facts'],

    ['Tokyo', 'San Francisco', 'Amsterdam', 'Boston', 'Pittsburgh', 'Sacramento', 'London', 'Beijing', 'Madrid', 'Barcelona', 'New York City', 'Moscow', 'Shanghai', 'Kuala Lumpur', 'New Delhi Facts'], 
    
    ['Microscope', 'Microbiology', 'Batteries', 'Autism', 'Biotechnology', 'Hydroelectric Power', 'Psychology', 'Cosmetology', 'Density', 'Microwaves', 'Global Warming', 'Zoology', 'Salt Water', 'Radio Waves', 'Ecology', 'Cloning Facts'],

    ['Bitcoin', 'Snapchat', 'Android', 'Drones', 'Siri', 'Credit Cards', 'Driverless Cars', 'Virtual Reality', 'X-Ray', 'Robots', 'Apple Lisa', 'IPhone Facts'], 

    ['Deforestation', 'Recycling', 'Drought', 'Ocean Pollution', 'Food Chain', 'Avalanches', 'Oil Spill', 'Climate Change', 'Fracking', 'Bottled Water', 'Wildfires', 'Landfill', 'Polar Ice Caps', 'Exxon Valdez Oil Spill Facts'],

    ['Buddhism', 'Confucianism', 'Hinduism', 'Sikhism', 'Christianity', 'Taoism', 'Judaism', 'Islam', 'Jainism', 'Shintoism Facts'],

    ['Barite', 'Andalusite', 'Anhydrite', 'Apatite', 'Cassiterite', 'Azurite', 'Arsenopyrite', 'Augite', 'Benitoite', 'Bornite', 'Chalcocite', 'Chalcopyrite', 'Biotite', 'Bauxite Facts'],

    ['Pyranometer', 'Weather Stations', 'Hygrometer', 'Anemometer', 'Weather Satellites', 'Lightning Detectors', 'Thermometer', 'Ceilometer', 'Barometer', 'Rain Gauge', 'Weather Map', 'Wind Sock', 'Wind Vane', 'Weather Balloons', 'Snow Gauge Facts'], 
    
    ['Plastic', 'Atoms', 'Compounds', 'Arsenic', 'Dihydrogen Monoxide', 'Organic Chemistry', 'Mixtures', 'Mole', 'Inorganic Chemistry', 'Biochemistry', 'Physical Chemistry', 'Atomic Number Facts'], 
    
    ['Batman', 'Cinderella', 'Dragons', 'Witches', 'Hello Kitty', 'King Arthur', 'Unicorn', 'Superman', 'Vampires', 'Monsters', 'Odysseus', 'Mothman Facts'], 
    
    ['Las Vegas', 'Mauna Loa', 'Gateway Arch', 'Castillo de San Marcos', 'California Desert Region', 'Death Valley', 'Washington DC', 'Brooklyn Bridge', 'Okefenokee Swamp', 'Yellowstone Supervolcano', 'Alcatraz', 'Devils Tower Facts'],
    
    ['Twitter', 'BMW', 'Disneyworld', 'Stock Market', 'Chipotle', 'Walmart', 'Lamborghini', 'Starbucks', 'Bankruptcy', 'Nike Facts'],

    ['Helicopter', 'Bugatti', 'Train', 'Boat', 'Bicycle', 'Car', 'Airplane', 'Submarine', 'Bridges', 'Hot Air Balloon', 'Trains Facts'],

    ['Gaelic Culture', 'South African Culture', 'South Korean Culture', 'German Culture', 'Irish Culture', 'Mexican Culture', 'Japanese Culture', 'Aborigines', 'Russian Culture', 'Chinese Culture Facts'],

    ['Constitution', 'Executive Branch', 'Federalist', 'Bill of Rights', 'Marines', 'Watergate Scandal', 'Social Security', '19th Amendment', 'Judicial Branch Facts'],

    ['Beefalo', 'Cama', 'Coywolf', 'Dzo', 'Grolar bear', 'Liger', 'Savannah', 'Wholphin', 'Zonkey', 'Zorse Facts'],

    ['American lion', 'Aurochs', 'Carcharodon megalodon (C. megalodon)', 'Dodo', 'Moa', 'Passenger pigeon', 'Saber-toothed tiger', 'Stellers sea cow', 'Tasmanian tiger', 'Woolly mammoth Facts'],

    ['Glaciers', 'Vernal Equinox', 'Biosphere', 'Nitrogen Cycle', 'Oxygen Cycle', 'Phosphorus Cycle', 'Water Cycle', 'Asthenosphere', 'Autumnal Equinox Facts'], 
    
    ['Astrolabe', 'Antikythera Mechanism', 'Armillary Sphere', 'Planisphere', 'Quadrant', 'Triquetrum', 'Celestial Sphere', 'Zenith Telescope', 'Astronomical Clock Facts'],

    ['Paris', 'Notre Dame', 'British Museum', 'Big Ben', 'London Eye', 'La Sagrada Familia', 'Palace of Versailles', 'Arc de Triomphe Facts'], 

    ['E-waste in Guiyu, China', 'Minamata Disease', 'The Chernobyl Nuclear Explosion', 'The Seveso Disaster', 'Baia Mare Cyanide Spill', 'The Shrinking of the Aral Sea', 'The Love Canal', 'Gulf of Mexico Dead Zone', 'The Great Smog of 52', 'The Bhopal Disaster Facts'],

    ['Roman Forum', 'Trevi Fountain', 'Venice Italy', 'Baths of Caracalla', 'St Peters Basilica', 'Sistine Chapel', 'Roman Architecture', 'Mount Vesuvius', 'Piazza Navona Facts'],

    ['Fungi', 'Paramecium', 'Mold', 'Archaebacteria', 'Biodiversity', 'Carbon Cycle', 'Dinosaur', 'Fraternal Twins Facts'], 
    
    ['The Metropolitan Museum of Art', 'Rijksmuseum', 'Smithsonian Institution', 'State Hermitage', 'The Prado', 'Accademia Gallery', 'The Uffizi Gallery Facts'],

    ['Tuba', 'Violin', 'Saxophone', 'Trombone', 'Clarinet', 'The Beatles Facts'],

    ['Daintree Rainforest', 'Sinharaja Forest Reserve', 'Tongass National Forest', 'Pacific Temperate Rainforest', 'Valdivian Temperate Rainforest', 'Kinabalu National Park Facts'],

    ['Capitalism', 'Democracy', 'Misogyny', 'Minimum Wage', 'Communism', 'Socialism Facts'], 

    ['Lake Baikal', 'Kidd Mine', 'Krubera/Voronya Cave', 'Tagebau Hambach', 'Kola Superdeep Borehole', 'El Zacaton Facts'],

    ['Wizard of Oz', 'Pokemon', 'Hollywood', 'SpongeBob SquarePants', 'Jurassic Park Facts'],

    ['Algae', 'Zooplankton', 'Archaea', 'Eubacteria', 'Yeast Facts'],

    ['Hermes', 'Ares Greek God', 'Santa', 'Demeter Facts'], 
    
    ['Prehistoric', 'Paleolithic Age', 'Homo Habilis', 'Trilobite Facts'],

    ['Mexican Flag', 'Mexican Independence Day', 'La Reforma in Mexico Facts'], 
    
    ['Kilauea', 'Kilimanjaro', 'Stratovolcano'],

    ['Nunavut', 'British Columbia'], 
    
    ['Hunger Games', 'Romeo and Juliet Facts'],

    ['SeaWorld'], 
    
    ['Tide'],

    ['Lawyers'],

    ['Abrakadabra'] #'Date']
    ]


    for i in range(len(category_main)): #-1                    #зменяет большие буквы на маленькие
        category_main[i] = str(category_main[i].lower())
        category_main_for_found[i] = str(category_main_for_found[i].lower())
        for j in range(len(category_lev2[i])):
            category_lev2[i][j]=str(category_lev2[i][j].lower())

    url = ""

    if type(my_word) == list: #заменяет ключевое слово н маленькие буквы
        for i in my_word:
            i = i.lower()
    else: my_word = my_word.lower()
        

    my_word = 'princess'
    for i in range(len(category_main)): #ищет по категориям главным
        if url != "":
            break
        # print(my_word)
        #my_word = my_word.lower()
        #print(my_word, ' ====== ', category_main_for_found[i])
        if my_word == category_main_for_found[i] or my_word == category_main[i]:
            
            url = "https://fungenerators.com/random/facts"+'/'+category_main[i]
            break
            #print('Ok 1')

    for i in range(len(category_main)):    
        for j in range(len(category_lev2[i])): #ищет совпадения по подкатегориям
            #print(category_lev2[i][j])
            if my_word == category_lev2[i][j]:
                splitword = category_lev2[i][j].split(' ')
                together_word = ''
                for number_word in range(len(splitword)):
                    if number_word == 0 : 
                        together_word = splitword[0]
                    else:
                        together_word = together_word+'-'+splitword[number_word]
                url = "https://fungenerators.com/random/facts"+'/'+category_main[i]+'/'+together_word
                break
                #print('Ok 2')
            
    for i in range(len(category_main)):    
        for j in range(len(category_lev2[i])):      
            one_word = category_lev2[i][j].split(' ')  
           # if initailize == True:
            for k in one_word: # разбивает подкатегории на слова и ищет совпадения
                if my_word == k:
                    if url == '':
                        splitword = category_lev2[i][j].split(' ')
                        together_word = ''
                        for number_word in range(len(splitword)):
                            if number_word == 0 : 
                                together_word = splitword[0]
                            else:
                                together_word = together_word+'-'+splitword[number_word]
                        url = "https://fungenerators.com/random/facts"+'/'+category_main[i]+'/'+together_word #category_lev2[i][j]
                        break

        if url != '':
            break
                    #print('Ok 21')
    #print(url)
    from subprocess import Popen
    import requests
    from bs4 import BeautifulSoup

    def get_text(url):
        rs = requests.get(url)
        root = BeautifulSoup(rs.content, 'html.parser')
        text_out = str(root) 
        text = text_out[31000:34000]
        return text

    # print(url)
    if url == '':
        return 0
    #url = "https://fungenerators.com/random/facts" #+'/'+category_main[0]
    text = get_text(url)
    # text_out = str(text) 
    # text = text_out[31000:34000]

    number = 0
    spliting = text.split('>')
    for i in range(len(spliting)):
        if spliting[i] == '\n<h2 class="wow fadeInUp animated" data-wow-delay=".6s"':
            number = i+1
            break

    fact = spliting[number].split('<')
    fact = fact[0]
    #print('FFFFFAAACCCTTT ', fact)
    return fact

# i = 0
# with open("c:\\Users\\ALISA\\Desktop\\Вуз\\Проектная практика\\proba.txt") as f:
#     for line in f:
#         category_lev2.append([str(x) for x in line.split("\n")])

# for i in range(len(category_lev2)):
#     for j in range(len(category_lev2[i])):
#         if category_lev2[i][j] == '':
#             print('Пустое')
#             del category_lev2[i][j]

# print("1: ", category_lev2[0])
# print("2: ", category_lev2[1])
# print(category_lev2)

# a = "Animal Facts Plants Facts Scientists Facts Authors Facts Biography Facts National Parks Facts Periodic Table Facts US States Facts Holidays Facts Dogs Facts Space Facts US History Facts Countries Facts Wonders of the World Facts Health Facts Music Instruments Facts Sports Facts Seas Facts History Facts World History Facts US National Landmarks Facts Geography Facts Viruses Facts Food Facts Nutrition Facts Ancient Civilizations Facts Rocks Facts 13 Colonies Facts Artists Facts Weather Facts Rivers Facts Dinosaurs Facts Human Body Facts Games Facts Cats Facts Geology Facts Energy Facts Vegetables Facts Civil War Facts Cities Facts Science Facts Technology Facts Environmental Science Facts Religion Facts Minerals Facts Weather Instruments Facts Chemistry Facts Fiction Facts US Geography Facts Business Facts Transportation Facts Cultures Facts US Government Facts Hybrid Animals Facts Extinct Animals Facts Earth Systems Facts Astrological Instruments Facts Europe Facts Manmade Disasters Facts Rome Facts Biology Facts Museums Facts Music Facts Rain Forests Facts Social Studies Facts Deepest Places Facts Movies Facts Organisms Facts Mythology Facts Prehistoric Facts Mexico Facts Volcanoes Facts Canada Facts Literature Facts Marine Parks Facts Oceans Facts Careers Facts Numbers Facts"

#print(category_lev2[1][0])


# massiv = a.split(' Facts ')
# stroka = ''
# for word in massiv:
#     stroka = stroka+"'"+str(word)+"', "
# print(stroka)


# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
 
# words = ["game","gaming","gamed","games", "pony", "USA"] #делает слова проще
# ps = PorterStemmer()
 
# for word in words:
#     print(ps.stem(word))


# import nltk
# #nltk.download() #В SETUP И ЧТО ПОСТАВИТЬ
# from nltk.corpus import wordnet
# from nltk.corpus import words
# synonyms = []

# for syn in wordnet.synsets("puppy"):
#     for lm in syn.lemmas():
#              synonyms.append(lm.name())
# print (set(synonyms))




        