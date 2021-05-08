import random


maps = ['Ruins 1', 'Arena 1', 'Stones 1', 'Bridge 1', 'Camp 1', 'Ruins 2', 'Canyon 1', 'Swamp 1', 'Ruins 3']
pc_level = int(input('PC level: '))
party_size = int(input('Party size: '))
toggle_weakness = input("Toggle Weakened Mob's: ").lower()
toggle_elite = input("Toggle Elite Mob's: ").lower()
toggle_Hazards = input("Toggle Hazard's?: ").lower()
environment = random.choice(maps)
width = ''
height = ''
terminate = ''
total_exp = int(input("Current party exp: "))
total_pc_gp = 0
total_party_gp = 0


monsters = {
    -1: ['Animated Broom', 'Bloodseeker', 'Compsognathus', 'Crawling Hand', 'Eagle', 'Flash Beetle', 'Giant Centipede', 'Giant Rat', 'Goblin Warrior', 'Guard Dog', 'Kobold Warrior', 'Mitflit', 'Raven', 'Skeleton Guard', 'Snapping Turtle', 'Sprite', 'Unseen Servant', 'Viper', 'Yellow Musk Thrall', 'Zombie Shambler'],
    0: ['Badger', 'Blue-Ringed Octopus', 'Buttlenose Dolphin', 'Dream Spider', 'Duergar Sharpshooter', 'Giant Maggot', 'Grindylow', 'Homunculus', 'Kobold Tunnelrunner', 'Leaf Leshy', 'Lemure', 'Melixie', 'Orc Brute', 'Pugwampi', 'Riding Pony', 'Ringhorn Ram', 'Sea Snake', 'Shoony Tiller', 'Spear Frog', 'Spider swarm', 'Stingray', 'Vampire Squid', 'Vine Lasher', 'Vine Leshy', 'Water Wisp'],
    1: ['Air Mephit', 'Akata', 'Amoeba Swarm', 'Animated Silverware Swarm', 'Arbiter', 'Augur', 'Ball Python', 'Biloko Warrior', 'Boggard Scout', 'Brownie', 'Cacodeamon', 'Caligni Dancer', 'Camel', 'Carbuncle', 'Cassisian', 'Catfolk pouncer', 'Cave Scorpion', 'Charau-ka Warrior', 'Coral Capuchin', 'Cunning Guide', 'Cythnigot', 'Deep Gnome Scout', 'Div, Doru', 'Drow Fighter', 'Duergar Bombardier', 'Dust Mephit', 'Earth Mephit', 'Electric Eel', 'Esipil', 'Festrog', 'Fetchling Scout', 'Fire Mephit', 'Flumph', 'Fuath', 'Gathlain Wanderer', 'Ghoul', 'Giant Amoeba', 'Giant Cockroach', 'Giant Fly', 'Giant Frog', 'Giant Gecko', 'Giant Skunk', 'Giant Solifugid', 'Giant Tick', 'Goblin Commando', 'Goblin Dog', 'Goblin Pyro', 'Goblin War Chanter', 'Gourd Leshy', 'Graveshell', 'Grig', 'Grioth Scout', 'Grippli Scout', 'Hellcrown', 'Hippocampus', 'Hobgoblin Soldier', 'House Drake', 'Hunting Spider', 'Hyena', 'Ice Mephit', 'Ifrit', 'Imp', 'Jinkin', 'Kami, Shikigami', 'Kobold Scout', 'Lantern Archon', 'Lizardfolk Defender', 'Lizardfolk Scout', 'Lyrakien', 'Manta Ray', 'Merfolk Warrior', 'Morlock Scavenger', 'Naiad', 'Nixie', 'Nosoi', 'Ooze Mephit', 'Orc Warrior', 'Oread', 'Ostovite', 'Petitioner', 'Plague Zombie', 'Quasit', 'Rakatavarna', 'Rat Swarm', 'Reef octopus', 'Reefclaw', 'Riding Dog', 'Riding Horse', 'Samsaran Anchorite', 'Sewer Ooze', 'Shaukeen', 'Silvanshee', 'Skulk', 'Squirrel Swarm', 'Steam Mephit', 'Stheno Harpist', 'Suli', 'Sunflower Leshy', 'Sylph', 'Undine', 'Vampire Bat Swarm', 'Vanara Disciple', 'Velociraptor', 'Vexgit', 'Void Zombie', 'Voidworm', 'War Pony', 'Water Mephit', 'Wayang Whisperblade', 'Wolf', 'Wyrwood Snake', 'Xulgath Warrior', 'Yzobu'],
    2: ['Anadi Hunter', 'Android Infiltrator', 'Angheuvore', 'Animated Armor', 'Azarketi Explore', 'Azer', 'Black Bear', 'Blindheim', 'Blink Dog', 'Bloodlash Bush', 'Boar', 'Bog Strider', 'Boggard Warrior', 'Bugbear Thug', 'Cactus Leshy', 'Caligni Creeper', 'Cave Fisher', 'Choker', 'Cobbleswarm', 'Cockroach Swarm', 'Corpselight', 'Crocodile', 'Deep Gnome Warrior', 'Deinonychus', 'Dero Stalker', 'Dhampir Wizard', 'Domovoi', 'Draugr', 'Dretch', 'Drow Rogue', 'Duende', 'Duergar Taskmaster', 'Ember Fox', 'Emperor Bird', 'Fading Fox', 'Faerie Dragon', 'Flaming Skull', 'Flickerwisp', 'Fungus Leshy', 'Ghast', 'Giant Ant', 'Giant Badger', 'Giant Bat', 'Giant Crab', 'Giant Flying Squirrel', 'Giant Leech', 'Giant Monitor Lizard', 'Giant Opossum', 'Giant Toad', 'Giant Viper', 'Gnoll Hunter', 'Grauladon', 'Herexen', 'Hippogriff', 'Icicle Snake', 'Incutilis', 'Ittan-Momen', 'Kappa', 'Kitsune Trickster', 'Kobold Dragon Mage', 'Ledalusca', 'Leopard', 'Leprechaun', 'Living Boulder', 'Lizardfolk Stargazer', 'Mechanical Carny', 'Merfolk Wavecaller', 'Monkey Swarm', 'Morlock', 'Mudwretch', 'Munavri Spellblade', 'Nagaji Soldier', 'Nuglub', 'Orc Warchief', 'Porcupine', 'Pteranodon', 'Rat Snake Swarm', 'Rokurokubi', 'Rosethorn', 'Sasquatch', 'Sea Devil Scout', 'Shadow Drake', 'Shocker Lizard', 'Shoony Militia Member', 'Sinspawn', 'Skeletal Champion', 'Skeletal Horse', 'Skum (Ulat-Kini)', 'Slime Mold', 'Slurk', 'Soulbound Doll', 'Spark Bat', 'Squirming Swill', 'Stinkweed Shambler', 'Stone Lion Cub', 'Strix Kinmate', 'Tatzlwyrm', 'Tengu', 'Terror Bird', 'Triton', 'War Horse', 'Warg', 'Werebat', 'Wereboar', 'Werecrocodile', 'Wererat', 'Wolverine', 'Xulgath Bilebearer', 'Xulgath Skulker', 'Yellow Musk Brute', 'Yellow Musk Creeper', 'Zombie Brute', 'Zrukbat', 'Zyss Serpentfolk'],
    3: ['Aapoph Serpentfolk', 'Akizendri', 'Animated Statue', 'Ankhrav', 'Assassin Vine', 'Binumir', 'Bogey', 'Boggard Swampseer', 'Brine Shark', 'Bugbear Tormentor', 'Bunyip', 'Buso', 'Caligni Slayer', 'Centaur', 'Centipede Swarm', 'Changeling Exile', 'Charau-ka Acolyte of Angazhan', 'Chimpanzee Visitant', 'Chupacabra', 'Cinder Rat', 'Cockatrice', 'Dero Strangler', 'Dire Wolf', 'Doppelganger', 'Draxie', 'Drow Priestress', 'Dryad', 'Dvorovoi', "D'ziriak", 'Esobok', 'Fen Mosquito Swarm', 'Ganzi', 'Gelatinous Cube', 'Ghoran Manipulator', 'Giant Chameleon', 'Giant Dragonfly Nymph', 'Giant Eagle', 'Giant Flea', 'Giant Mantis', 'Giant Scorpion', 'Giant Wasp', 'Giant Whiptail Centipede', 'Gnoll Cultist', 'Gorilla', 'Grioth Cultist', 'Grippli Archer', 'Grizzly Bear', 'Grothlut', 'Hell Hound', 'Hyaenodon', 'Kovintus Geomancer', 'Lion', 'Living Graffiti', 'Locathah Hunter', 'Megalictis', 'Moose', 'Morlock Engineer', 'Narwhal', 'Necrophidius', 'Ogre Warrior', 'Pachycephalosaurus', 'Pegasus', 'Piranah Swarm', 'Platecarpus', 'Quickling', 'Raven Swarm', 'River Drake', 'Rust Monster', 'Scalescribe', 'Scalliwing', 'Sea Hag', 'Seahorse', 'Seaweed Leshy', 'Shulsaga', 'Siege Shard', 'Skeletal Giant', 'Snapping Flytrap', 'Sod Hound', 'Spriggan Bully', 'Street Skelm', 'Tattoo Guardian', 'Tiefling', 'Tixitog', 'Tooth Fairy Swarm', 'Trailgaunt', 'Trilobite Swarm', 'Trollhound', 'Twigjack', 'Unicorn', 'Urdefhan Warrior', 'Vampiric Mist', 'Vermlek (Worm Demon)', 'Violet Fungus', 'Vishkanya Infiltrator', 'Vulture', 'Web Lurker', 'Werewolf', 'Wight', 'Wolliped', 'Xulgath Leader', 'Yeth Hound', 'Zebub (Accuser Devil)', 'Zephyr Hawk', 'Zuipnyrn (Moon Mole)'],
    4: ['Abrikandilu (Wrecker Demon)', 'Amphisbaena', 'Anadi Sage', 'Aphorite', 'Arboreal Warden', 'Attic Whisperer', 'Barghest', 'Biloko Veteran', 'Bison', 'Blood Ooze', 'Brood Leech Swarm', 'Cairn Wight', 'Calathgar', 'Caligni Stalker', 'Carrion Golem', 'Coil Spy', 'Corrupted Relic', 'Daeodon', 'Div, Aghash', 'Dreshkan', 'Drow Warden', 'Duskwalker', 'Earthen Destrier', 'Faceless Stalker (Ugothol)', 'Filth Fire', 'Flytrap Leshy', 'Frost Troll', 'Gancanagh (Passion Azata)', 'Gargoyle', 'Ghost Commoner', 'Giant Dragonfly', 'Giant Stag Beetle', 'Giant Wolverine', 'Gnoll Sergeant', 'Gray Ooze', 'Great White Shark', 'Green Hag', 'Griffon', 'Hadrosaurid', 'Hellbound Attorney', 'Hermit Crab Swarm', 'Hobgoblin Archer', 'Horned Archon', 'Hound Archon', 'Hulda', 'Janni', 'Kasa-Obake', 'Kelpie', 'Korred', 'Kushtaka', 'Living Thunderclap', 'Lovelorn', 'Luminous Ooze', 'Mandragora', 'Mimic', 'Minotaur', 'Mist Stalker', 'Morlock Cultist', 'Myceloid', 'Najra Lizard', 'Nightgaunt', 'Nucol', 'Ogre Glutton', 'Ogre Hurler', 'Otyugh', 'Ovinnik', 'Owlbear', 'Pangolin', 'Peryton', 'Phantom Knight', 'Pixie', 'Poracha', 'Ratfolk Grenadier', 'Rhinoceros', 'Satyr', 'Scalathrax', 'Scarecrow', 'Scorpion Swarm', 'Sea Devil Brute', 'Shabti Redeemer', 'Shadow', 'Shae', 'Shambler Troop', 'Shanrigol Heap', 'Shoony Hierarch', 'Stone lion', 'Tenome', 'Terror Shrike', 'Tiger', 'Vampire Spawn Rogue', 'Viper Swarm', 'Wasp Swarm', 'Werebear', 'Weretiger', ],
    5: ['Aasimar', 'Army Ant Swarm', 'Azuretzi', 'Barbazu (Bearded Devil)', 'Basidirond', 'Basilisk', 'Bog Mummy', 'Bone Croupier', 'Bore Worm Swarm', 'Brimorak (Arson Demon)', 'Caligni Vanguard', 'Catrina', 'Cecaelia Trapper', 'City Guard', 'Cloaker', 'Cyclops', 'Dandasuka', 'Deep Gnome Rockwarden', 'Dero Magister', 'Dig-Widget', 'Divine Warden Of Nethys', 'Djinni', 'Doorwarden', 'Emperor Cobra', 'Ether Spider', 'Eunemvro', 'Flame Drake', 'Flea Swarm', 'Forge-Spurned', 'Giant Crawling hand', 'Giant Frilled Lizard', 'Giant Hermit Crab', 'Giant Moray Eel', 'Gibbering Mouther', 'Gibtas Bounder', 'Globster', 'Grimstalker', 'Grippli Greenspeaker', 'Grodair', 'Harpy', 'Harpy Skeleton', 'Hieracosphinx', 'Hippopotamus', 'Ice Golem', 'Kami, Kodama', 'Leucrotta', 'Lion Visitant', 'Living Landslide', 'Living Waterfall', 'Living Whirlwind', 'Living Wildfire', 'Lurker In Light', 'Megatherium', 'Muse Phantom', 'Namorrodor', 'Ochre Jelly', 'Ogre Spider', 'Orca', 'Ostiarius', 'Penanggalan', 'Polar Bear', 'Poltergeist', 'Redcap', 'Sabosan', 'Shrine Skelm', 'Skaveling', 'Skinstitch', 'Spiny Eurypterid', 'Storm Hag', 'Troll', 'Urdefhan Tormentor', 'Winter Wolf', 'Wizard Sponge', 'Xulgath Spinesnapper', 'Yeti'],
    6: ['Abandoned Zealot', 'Ahuizotl', 'Anadi Elder', 'Ankylosaurus', 'Annis Hag', 'Asanbosam', 'Awakened Tree', 'Babau (Blood Demon)', 'Baobhan Sith', 'Bauble Beast', 'Belker', 'Blizzardborn', 'Blodeuwedd', 'Blood Boar', 'Bone Skipper Swarm', 'Bralani (Wind Azata)', 'Bugaboo', 'Caligni Caller', 'Cat Sith', 'Cave Bear', 'Cave Giant', 'Cavern Troll', 'Ceustodaemon (Guardian Daemon)', 'Charau-ka Butcher', 'Choral (Choir Angel)', 'Chouchin-Obake', 'Clockwork Soldier', 'Drider', 'Elananx', 'Ettin', 'Evangelist', 'Fire Jellyfish Swarm', 'Giant Mosquito', 'Giant Tarantula', 'Gibtas Spawn Swarm', 'Gurgist', 'Hobgoblin General', 'Hodag', 'Hydra', 'Iguanodon', 'Jungle Drake', 'Kurnugian Jackal', 'Kurobozu', 'Lamia', 'Lampad', 'Living Sap', 'Lunar Naga', 'Maftet Guardian', 'Manticore', 'Mi-Go', 'Mummy Guardian', 'Nightmare', 'Owb', 'Revenant', 'Rhu-Chalik', 'Sand Sentry', 'Scythe Tree', 'Sea Devil Baron', 'Sea Drake', 'Seugathi Servant', 'Shambler', 'Skrik Nettle', 'Skull Peeler', 'Smilodon', 'Striding Fire', 'Sulfur Zombie', 'Terra-Cotta Soldier', 'Umasi', 'Urdefhan Death Scout', 'Vampire Count', 'Vaultbreaker Ooze', 'Verdurous Ooze', 'Vrykolakas Spawn', 'Vulpinal (Fox Agathion)', 'Wihsaak', "Will-o'-Wisp", 'Witchwyrd', 'Wood Giant', 'Wood Golem', 'Wooly Rhinoceros', 'Wraith', 'Wyvern', 'Xill', 'Young White Dragon', 'Zombie Hulk'],
    7: ['Adhukait', 'Ahvothian', 'Alghollthu Master (Aboleth)', 'Arboreal Reaper', 'Black Pudding', 'Caulborn', 'Chuul', 'Crossroads Guardian', 'Cu Sith', 'Culdewen', 'Dark Naga', 'Div, Pairaka', 'Drainberry Bush', 'Drow Hunter', 'Dullahan', 'Dweomercat', 'Elasmosaurus', 'Elephant', 'Eloko', 'Empress Bore Worm', 'Excorion', 'Fortune Eater', 'Frost Drake', 'Fuming Sludge', 'Gahlepod (Juvenile Brughadatch)', 'Giant Animated Statue', 'Giant Bone Skipper', 'Giant Jellyfish', 'Greater Barghest', 'Greater Shadow', 'Hellcat', 'Hill Giant', 'Hound of Tindalos', 'Invidiak (Shadow Demon)', 'Invisible Stalker', 'Iridescent Animal', 'Kirin', 'Legion Archon', 'Levaloch (Warmonger Devil)', 'Lillend (Muse Azata)', 'Manticore Paaridar', 'Medusa', 'Megalania', 'Mothman', 'Mulventok', 'Naiad Queen', 'Naunet', 'Ogre Boss', 'Pukwudgie', 'Quatoid', 'Quetzalcoatlus', 'Remorhaz', 'Salamander', 'Sceaduinar', 'Shaitan', 'Shoggti', 'Skeletal Hulk', 'Slithering Pit', 'Soul Eater', 'Sportlebore Swarm', 'Spriggan Warlord', 'Stegosaurus', 'Stygira', 'Succubus (Lust Demon)', 'Tendriculos', 'Theletos', 'Tiddalik', 'Totenmaske', 'Tupilaq', 'Urdefhan Lasher', 'Vanth', 'Winter Hag', 'Xorn', 'Young Black Dragon', 'Young Brass Dragon', 'Young Crystal Dragon', 'Young Underworld Dragon', 'Zetogeki'],
    8: ['Anancus', 'Angazhani', 'Animate Dream', 'Arboreal Regent', 'Avarek', 'Axiomite', 'Balisse (Confessor Angel)', 'Behir', 'Bida', 'Blood Hag', 'Bodak', 'Bone Prophet', 'Brain Collector', 'Bulette', 'Cavalry Brigade', 'Chimera', 'Denizen of Leng', 'Desert Drake', 'Destrachan', "Dragon's Blood Puffball", 'Dreadsong Dancer', 'Drow Shootist', 'Erinyes (Fury Devil)', 'Flesh Golem', 'Giant Anaconda', 'Giant Hippocampus', 'Giant Octopus', 'Giant Slug', 'Gibtanius', 'Girtablilu Sentry', 'Glass Golem', 'Gorgon', 'Granite Glyptodont', 'Guecubu', 'Hadrinnex', 'Harrow Doll', 'Hellwasp Swarm', 'Hive Mother', 'Intellect Devourer', 'Kishi', 'Krooth', 'Lamia Matriarch', 'Lifeleecher', 'Magma Scorpion', 'Marsh Giant', 'Megaprimatus', 'Mix Couatl', 'Mohrg', 'Moonflower', 'Nabasu (Gluttony Demon)', 'Nosferatu Thrall', 'Onidoshi', 'Palace Skelm', 'Phantom Beast', 'Procyal (Raccoon Agathion)', 'Sandpoint Devil', 'Sarglagon (Drowning Devil)', 'Shantak', 'Sphinx', 'Stone Giant', 'Svartalfar', 'Triceratops', 'Two-Headed Troll', 'Tylosaurus', 'Urdefhan Blood Mage', 'Voidglutton', 'Xulgath Stoneliege', 'Young Brine Dragon', 'Young Copper Dragon', 'Young Green Dragon', 'Young Sea Dragon'],
    9: ['Alchemical Golem', 'Animated Furnace', 'Aurumvorax', 'Barnacle Ghoul', 'Baykok', 'Blood Painter', 'Bregdi', 'Bright Walker', 'Clockwork Mage', 'Deepwater Dhuthorex', 'Deinosuchus', 'Desert Giant', 'Dracolisk', 'Dragon Turtle', 'Drakauthix', 'Dread Wisp', 'Dread Wraith', 'Efreeti', 'Firewyrm', 'Frost Giant', 'Galvo', 'Garuda', 'Giant Snapping Turtle', 'Giant Squid', 'Gliminal', 'Hesperid', 'Irnakurse', 'Jyoti', 'Khravgodon', 'Leukodaemon (Pestilence Daemon)', 'Marid', 'Mastodon', 'Megalodon', 'Mokele-Mbembe', 'Mokele-Mbembes', 'Mummy Pharaoh', 'Nessian Warhound', 'Night Hag', 'Nuckelavee', 'Osyluth (Bone Devil)', 'Pakalchi', 'Reaper Skull Puffball', 'Roc', 'Roiling Incant', 'Seugathi Reality Warper', 'Shanrigol Behemoth', 'Spirit Naga', 'Stone Mauler', 'Storm Lord', 'Teraphant', 'Tick Swarm', 'Tidal Master', 'Tikbalang', 'Titan Centipede', 'Tyrannosaurus Skeleton', 'Vampire Mastermind', 'Vrock (Wrath Demon)', 'Witchfire', 'Yithian', 'Young Blue Dragon', 'Young Bronze Dragon', 'Young Magma Dragon', 'Young Sky Dragon', 'Zelekhut', 'Zombie Dragon'],
    10: ['Adlet', 'Adult White Dragon', 'Aluum Enforcer', 'Bebilith', 'Behemoth Hippopotamus', 'Bogeyman', 'Brontosaurus', 'Brughadatch (Midlife Brughadatch)', 'Chyzaedu', 'Clacking Skull Swarm', 'Clay Golem', 'Counteflora', 'Dezullon', 'Divine Warden Of Brigh', 'Eberark', 'Einherji', 'Etioling', 'Feathered Bear', 'Fire Giant', 'Ghonhatine', 'Ghost Mage', 'Giant Flytrap', 'Graveknight', 'Guardian Naga', 'Gug', 'Herecite of Zevgavizeb', 'Icewyrm', 'Imentesh', 'Kalavakus (Silver Demon)', 'Kami, Zuishin', 'Leng Ghoul', 'Mammoth', 'Melody On The Wind', 'Mobogo', 'Moon Hag', 'Movanic Deva (Guardian Angel)', 'Nereid', 'Nilith', 'Nosferatu Malefactor', 'Nyogoth', 'Ofalth', 'Peluda', 'Phistophilus (Contract Devil)', 'Piscodaemon (Venom Daemon)', 'Quetz Couatl', 'Quintessivore', 'Raja Rakshasa', 'Remnant of Barzillai', 'Roper', 'Sacristan', 'Shield Archon', 'Soul Skelm', 'Swordkeeper', 'Troll King', 'Tyrannosaurus', 'Urdefhan High Tormentor', 'Vrykolakas Master', 'Water Orm', 'Xulgath Gutrager', 'Yaganty', 'Young Cloud Dragon', 'Young Forest Dragon', 'Young Red Dragon', 'Young Silver Dragon'],
    11: ['Adult Black Dragon', 'Adult Brass Dragon', 'Adult Crystal Dragon', 'Adult Underworld Dragon', 'Brainchild', 'Carnivorous Crystal', 'Cloud Giant', 'Deadly Mantis', 'Devourer', 'Dread Dhuthorex', 'Elemental Avalanche', 'Elemental Hurricane', 'Elemental Inferno', 'Elemental Tsunami', 'Faceless Butcher', 'Goliath Spider', 'Gosreg', 'Greater Nightmare', 'Hamatula (Barbed Devil)', 'Harmona', 'Hezrou (Toad Demon)', 'Isqulug', 'Kongamato', 'Mari Lwyd', 'Meladaemon (Famine Daemon)', 'Munagola (Executioner Devil)', 'Quoppopak', 'Rancorous Priesthood', 'Seething Spirit', 'Skeleton Infantry', 'Spinosaurus', 'Spiral Centurion', 'Stone Golem', 'Tallow Ooze', 'Thunderbird', 'Young Gold Dragon', 'Young Sovereign Dragon', 'Young Umbral Dragon'],
    12: ['Adult Brine Dragon', 'Adult Copper Dragon', 'Adult Green Dragon', 'Adult Sea Dragon', 'Arboreal Archive', 'Athach', 'Betobeto-San', 'Bugul Noz', 'Calikang', 'Catoblepas', 'Cauthooj', 'Chernobue', 'Deculi', 'Derghodaemon (Ravager Daemon)', 'Feral Skull Swarm', 'Fossil Golem', 'Frost Worm', 'Gimmerling', 'Girtablilu Seer', 'Gogiteth', 'Great Cyclops', 'Interlocutor', 'Japalisura', 'Kokogiak', 'Kolyarut', 'Lich', 'Misery Siktempora', 'Monadic Deva (Soul Angel)', 'Omox (Slime Demon)', 'Rusalka', 'Sea Serpent', 'Shining Child', 'Shuln', 'Taiga Giant', 'Tidehawk', 'Tomb Giant', 'Urdefhan Hunter', 'Valkyrie', 'Xilvirek', 'Xiuh Couatl', 'Xulgath Deepmouth', 'Zealborn'],
    13: ['Adachros', 'Adult Blue Dragon', 'Adult Bronze Dragon', 'Adult Magma Dragon', 'Adult Sky Dragon', 'Amalgamite', 'Animated Trebuchet', 'Carnivorous Blob', 'Clockwork Assassin', 'Consonite Choir', 'Dalos', 'Doblagub (Elder Brughadatch)', 'Dragonscarred Dead', 'Dryad Queen (Hamadryad)', 'Froghemoth', 'Frost Yai', 'Gashadokuro', 'Gelugon (Ice Devil)', 'Ghaele (Crusader Azata)', 'Glabrezu (Treachery Demon)', 'Irlgaunt', 'Iron Golem', 'Jorogumo', 'Leng Spider', 'Living Rune', 'Millindemalion', 'Owb Prophet', 'Purple Worm', 'Shadow Giant', 'Storm Giant', 'Terra-Cotta Garrison', 'Thanadaemon (Death Daemon)', 'Viper Vine', 'Vrykolakas Ancient'],
    14: ['Adult Cloud Dragon', 'Adult Forest Dragon', 'Adult Red Dragon', 'Adult Silver Dragon', 'Ankou', 'Astral Deva (Emissary Angel)', 'Augnagar', 'Crag Linnorm', 'Div, Sepid', 'Doprillu', 'Dramofir', 'Fire Yai', 'Giant Aukashungi', 'Grikkitog', 'Gylou (Handmaiden Devil)', 'Kuchisake-Onna', 'Mezlan', 'Nalfeshnee (Boar Demon)', 'Nightmarchers', 'Nikaramsa', 'Obrousian', 'Peri', 'Plague Giant', 'Ravener Husk', 'Ravenile', 'Shatterling', 'Sorcerous Skull Swarm', 'Triumph Siktempora', 'Trumpet Archon', 'Urdefhan Dominator', 'Uthul', 'Veiled Master (Vidileth)', 'Worm That Walks'],
    15: ['Adult Gold Dragon', 'Adult Sovereign Dragon', 'Adult Umbral Dragon', 'Ancient White Dragon', 'Animated Colossus', 'Azure Worm', 'Black Scorpion', 'Crucidaemon (Torture Daemon)', 'Demilitch', 'Dybbuk', 'Hegessik', 'Hyakume', 'Immortal Ichor', 'Jotund Troll', 'Kami, Toshigami', 'Lampad Queen', 'Marrmora', 'Marut', 'Morrigna', 'Mukradi', 'Nemhaith', 'Nosferatu Overlord', 'Penqual', 'Phoenix', 'Popobawa', 'Quelaunt', 'Shoal Linnorm', 'Sordesdaemon (Pollution Daemon)', 'Soulbound Ruin', 'The Stabbing Beast', 'Tolokand', 'Umonlee', 'Viskithrel', 'Wemmuth', 'Xulgath Thoughtmaw'],
    16: ['Ancient Black Dragon', 'Ancient Brass Dragon', 'Ancient Crystal Dragon', 'Ancient Underworld Dragon', 'Astradaemon (Void Daemon)', 'Bythos', 'Clockwork Dragon', 'Cornugon (Horned Devil)', 'Elder Sphinx', 'Elemental Vessel, Water', 'Fjord Linnorm', 'Lesser Death', 'Love Siktempora', 'Mithral Golem', 'Planetar (Justice Angel)', 'Precentor', 'Rune Giant', 'Saurian Warmonger', 'Shemhazian (Mutilation Demon)', 'Spiritbound Aluum', 'Sumbreiva', 'Vilderavn', 'Warsworn', 'Zaramuun', 'Zomok'],
    17: ['Ancient Brine Dragon', 'Ancient Copper Dragon', 'Ancient Green Dragon', 'Ancient Sea Dragon', 'Banshee', 'Camarach', 'Deimavigga (Apostate Devil)', 'Ice Linnorm', 'Keketar', 'Leydroth', 'Lusca', 'Marilith (Pride Demon)', 'Qurashith', 'Radiant Warden', 'Thrasfyr', 'Vaspercham', 'Water Yai', 'Wendigo', 'Wyrmwraith', 'Ximtal', 'Xotanispawn'],
    18: ['Adamantine Golem', 'Aiudara Wraith', 'Ammut', 'Ancient Blue Dragon', 'Ancient Bronze Dragon', 'Ancient Magma Dragon', 'Ancient Sky Dragon', 'Aolaz', 'Ararda', 'Bone Ship', 'Cairn Linnorm', 'Crimson Worm', 'Deghuun (Children Of Mhar)', 'Duneshaker Solifugid', 'Hatred Siktempora', 'Kraken', 'Minchgorm', 'Myrucarx', 'Purrodaemon (War daemon)', 'Saurian Worldwatcher', 'Shoggoth', 'Simurgh', 'Skulltaker', 'Thulgant', 'Vavakia', 'Vitalia'],
    19: ['Agradaemon (Conflagration Daemon)', 'Ancient Cloud Dragon', 'Ancient Forest Dragon', 'Ancient Red Dragon', 'Ancient Silver Dragon', 'Grendel', 'Guthallath', 'Hesperid Queen', 'Nenchuuj', 'Sard', 'Star Archon', 'Sturzstromer', 'Taiga Linnorm', 'Terotricus', 'Tzitzimitl', 'Vrolikai (Death Demon)'],
    20: ['Ancient Gold Dragon', 'Ancient Sovereign Dragon', 'Ancient Umbral Dragon', 'Balor (Fire Demon)', 'Baomal', 'Bastion Archon', 'Clockwork Amalgam', 'Draconal (Dragon Agathion)', 'Eremite', 'Izfiitar', 'Kimenhul', 'Maharaja', 'Norn', 'Olethrodaemon (Apocalypse Daemon)', 'Pit Fiend (Tyrant Devil)', 'Pleroma', 'Tarn Linnorm', 'Vazgorlu', 'Veranallia (Rebirth Azata)', 'Xotani, The Firebleeder', 'Yamaraj'],
    21: ['Baatamidar', 'Elysian Titan', 'Grim Reaper', 'Iffdahsil', 'Krampus', 'Lerritan', 'Mu Spore', 'Ouroboros', 'Ravener', 'Tor Linnorm'],
    22: ['Dragonshard Guardian', 'Rhevanna', 'Thanatotic Titan'],
    23: ['Danava Titan', 'Elder Wyrmwraith', 'Jabberwock', 'Solar (Archangel)'],
    24: ['Green Man', 'Hekatonkheires Titan'],
    25: ['Tarrasque, The Armageddon Engine', 'Treerazer']
}

hazards = {
    -1: ['Shrieker'],
    0: ['Hidden pit', 'Snowfall'],
    1: ['Hampering Web', 'Poisoned Lock', 'Slamming Door', 'Summoning Rune'],
    2: ['Brown Mold', 'Spear Launcher', 'Web Lurker Noose'],
    3: ['Electric Latch Rune', 'Treacherous Scree', 'Web Lurker Deadfall', 'Drowning pit'],
    4: ['Scythe Blades', 'Titanic Flytrap', 'Gravehall Trap', 'Spinning Blade Pillar'],
    5: ['Fireball Rune', 'Spectral Reflection'],
    6: ['Ghostly Choir', 'Hallucination Powder Trap', 'Wheel of Misery'],
    7: ["Pharaoh's Ward", 'Sportlebore', 'Eternal Flame'],
    8: ['Yellow Mold', 'Confounding Betrayal', 'Poisoned Dart Gallery'],
    9: ['Bottomless Pit', 'Greem Slime'],
    10: ['Bloodthirsty Urge', 'Lava Flume Tubes', 'Perilous Flash Flood'],
    11: ['Hammer of Forbiddance', 'Jealous Abjurer'],
    12: ['Polymorph Trap', 'Flensing Blades', 'Telekinetic Swarm Trap'],
    13: ['Planar Rift'],
    14: ['Darkside Mirror'],
    15: ['Plummeting Doom'],
    16: ['Dance of Death'],
    17: ['Frozen Moment', 'Grasp of the Damned'],
    18: ["Banshee's Symphony"],
    19: ['Vorpal Executioner'],
    20: [''],
    21: ['Second Chance'],
    22: [''],
    23: ['Armageddon Orb']
}

income = {
    1: 175,
    2: 300,
    3: 500,
    4: 850,
    5: 1350,
    6: 2000,
    7: 2900,
    8: 4000,
    9: 5700,
    10: 8000,
    11: 11500,
    12: 16500,
    13: 25000,
    14: 36500,
    15: 54500,
    16: 82500,
    17: 128000,
    18: 208000,
    19: 355000,
    20: 490000
}


if environment == 'Ruins 1':
    height = 34
    width = 24
elif environment == 'Arena 1':
    height = 15
    width = 15
elif environment == 'Stones 1':
    height = 34
    width = 34
elif environment == 'Bridge 1':
    height = 34
    width = 34
elif environment == 'Camp 1':
    height = 44
    width = 30
elif environment == 'Ruins 2':
    height = 38
    width = 24
elif environment == 'Canyon 1':
    height = 34
    width = 34
elif environment == 'Swamp 1':
    height = 69
    width = 23
elif environment == 'Ruins 3':
    height = 49
    width = 31


def get_exp(npc_levels, pc_levels):
    if npc_levels == pc_levels:
        return 40
    elif npc_levels == pc_levels + 1:
        return 60
    elif npc_levels == pc_levels + 2:
        return 80
    elif npc_levels == pc_levels + 3:
        return 120
    elif npc_levels == pc_levels + 4:
        return 160
    elif npc_levels == pc_levels - 1:
        return 30
    elif npc_levels == pc_levels - 2:
        return 20
    elif npc_levels == pc_levels - 3:
        return 15
    elif npc_levels == pc_levels - 4:
        return 10
    else:
        print('error')


while terminate != 'yes' and total_exp <= 1000:
    total_mob = []
    encounter_exp = 0
    exp_budget = 0
    exp_reward = 0
    npc_level = 0
    happiness = ''
    threat_level = ''
    random_choice = ['trivial', 'low', 'moderate', 'severe', 'extreme']
    while exp_budget == 0:
        threat_level = input('Threat: ').lower()
        if threat_level == 'trivial':
            exp_budget = 10 * party_size
            exp_reward = 40
        elif threat_level == 'low':
            exp_budget = 15 * party_size
            exp_reward = 60
        elif threat_level == 'moderate':
            exp_budget = 20 * party_size
            exp_reward = 80
        elif threat_level == 'severe':
            exp_budget = 30 * party_size
            exp_reward = 120
        elif threat_level == 'extreme':
            exp_budget = 40 * party_size
            exp_reward = 160
        elif threat_level == 'random':
            threat_level = random.choice(random_choice)
            if threat_level == 'trivial':
                exp_budget = 10 * party_size
                exp_reward = 40
            elif threat_level == 'low':
                exp_budget = 15 * party_size
                exp_reward = 60
            elif threat_level == 'moderate':
                exp_budget = 20 * party_size
                exp_reward = 80
            elif threat_level == 'severe':
                exp_budget = 30 * party_size
                exp_reward = 120
            elif threat_level == 'extreme':
                exp_budget = 40 * party_size
                exp_reward = 160
        else:
            print('''Choose between:
Trivial
Low
Moderate
Severe
Extreme
or Random''')
    while encounter_exp != exp_budget:
        npc_level = random.randint(pc_level - 4, pc_level + 4)
        temp = get_exp(npc_level, pc_level)
        if temp + encounter_exp <= exp_budget:
            total_mob.append(npc_level)
            encounter_exp += temp
        if encounter_exp == exp_budget - 5:
            encounter_exp = 0
            total_mob = []
    print(f'Environment: {environment}')
    while happiness != 'yes':
        monster_group = []
        for mob in total_mob:
            mod = random.randint(1, 100)
            if 24 <= mob <= -2 or mod <= 5 and toggle_weakness == 'yes':
                if mob <= 3:
                    temp_monster = monsters.get(mob + 2)
                else:
                    temp_monster = monsters.get(mob + 1)
                temp_monster = 'Weakened ' + random.choice(temp_monster)
            elif mod >= 95 and mob >= 1 and toggle_elite == 'yes':
                if mob <= 3:
                    temp_monster = monsters.get(mob - 2)
                else:
                    temp_monster = monsters.get(mob - 1)
                temp_monster = 'Elite ' + random.choice(temp_monster)
            else:
                if toggle_Hazards == 'yes' and 90 <= mod <= 95 and mob != 20 and mob != 22 and mob <= 23:
                    temp_monster = hazards.get(mob)
                    temp_monster = random.choice(temp_monster)
                else:
                    temp_monster = monsters.get(mob)
                    temp_monster = random.choice(temp_monster)
            monster_group.append(temp_monster)
        for enemies in monster_group:
            print(f'{enemies} | Spawning: W:{random.randint(1, width)} H:{random.randint(1, height)}')
        happiness = input("Happy with these Mob's?: ").lower()
    value = (income[pc_level] / 4) / 1000
    pc_gp_reward = value * exp_reward
    party_gp_reward = pc_gp_reward * party_size
    print(f'Difficulty: {threat_level}, exp reward: {exp_reward}')
    print(f'Player Gp reward: {pc_gp_reward}')
    print(f'Party GP reward: {party_gp_reward}')
    total_party_gp += party_gp_reward
    total_pc_gp += pc_gp_reward
    total_exp += exp_reward
    terminate = input("Done?: ")
print(f'Total exp so far: {total_exp}')
print(f'Total Gp PC: {total_pc_gp}')
print(f'Total Gp Party: {total_party_gp}')
