#Manga recommender


print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.\n")

gen = input('What genre do you like? (action, romance, horror) --> ')
dura = input('How long should the manga be? (short, medium, long) --> ')
deca = input('Which decade? (1990s, 2000s, 2010s, 2020s, Ongoings) --> ')

if gen.lower() == "action":
    if deca == "1990s":
        if dura == "short":
            print("\n".join(["Yu Yu Hakusho", "Spriggan", "Golden Boy", "Bastard!!", "Flame of Recca"]))
        elif dura == "medium":
            print("\n".join(["Rurouni Kenshin", "Trigun", "Berserk", "GetBackers", "Great Teacher Onizuka"]))
        elif dura == "long":
            print("\n".join(["Hunter x Hunter", "One Piece", "Slam Dunk", "Dragon Ball Z", "Hajime no Ippo"]))
    elif deca == "2000s":
        if dura == "short":
            print("\n".join(["Fullmetal Alchemist", "Claymore", "Air Gear", "Samurai Champloo", "Tenjou Tenge"]))
        elif dura == "medium":
            print("\n".join(["Naruto", "Bleach", "D.Gray-man", "Soul Eater", "Gantz"]))
        elif dura == "long":
            print("\n".join(["Fairy Tail", "Katekyou Hitman Reborn!", "Eyeshield 21", "Black Cat", "Shaman King"]))
    elif deca == "2010s":
        if dura == "short":
            print("\n".join(["Akame ga Kill!", "Tokyo Ghoul", "Blue Exorcist", "Black Bullet", "Noragami"]))
        elif dura == "medium":
            print("\n".join(["Attack on Titan", "My Hero Academia", "One Punch Man", "Kill la Kill", "Magi"]))
        elif dura == "long":
            print("\n".join(["Hunter x Hunter (2011)", "JoJo’s Bizarre Adventure", "Fairy Tail (2014)", "Sword Art Online", "Nanatsu no Taizai"]))
    elif deca == "2020s":
        if dura == "short":
            print("\n".join(["Jujutsu Kaisen", "Chainsaw Man", "Akudama Drive", "Gleipnir", "Deca-Dence"]))
        elif dura == "medium":
            print("\n".join(["Demon Slayer", "Black Clover", "Dr. Stone", "The God of High School", "Tower of God"]))
        elif dura == "long":
            print("\n".join(["Boruto", "One Piece (continuing)", "My Hero Academia (continuing)", "Bleach: Thousand-Year Blood War", "Blue Lock"]))

elif gen.lower() == "romance":
    if deca == "1990s":
        if dura == "short":
            print("\n".join(["Marmalade Boy", "Kare Kano", "Video Girl Ai", "Boys Be...", "Kodocha"]))
        elif dura == "medium":
            print("\n".join(["Hana Yori Dango", "Fushigi Yuugi", "Kimagure Orange Road", "Glass Mask", "Tokimeki Tonight"]))
        elif dura == "long":
            print("\n".join(["Boys Over Flowers", "Maison Ikkoku", "Cardcaptor Sakura", "DNA²", "Wedding Peach"]))
    elif deca == "2000s":
        if dura == "short":
            print("\n".join(["Lovely★Complex", "Paradise Kiss", "Peach Girl", "Absolute Boyfriend", "Honey and Clover"]))
        elif dura == "medium":
            print("\n".join(["Fruits Basket", "Ouran High School Host Club", "Special A", "Itazura na Kiss", "Skip Beat!"]))
        elif dura == "long":
            print("\n".join(["Nana", "Kimi ni Todoke", "Clannad", "Vampire Knight", "Suzuka"]))
    elif deca == "2010s":
        if dura == "short":
            print("\n".join(["Say I Love You", "Golden Time", "Ao Haru Ride", "My Little Monster", "Wolf Girl and Black Prince"]))
        elif dura == "medium":
            print("\n".join(["Your Lie in April", "Toradora!", "ReLIFE", "Ore Monogatari!!", "Plastic Memories"]))
        elif dura == "long":
            print("\n".join(["Fruits Basket (2019)", "Kaguya-sama: Love is War", "Nisekoi", "Horimiya", "Domestic Girlfriend"]))
    elif deca == "2020s":
        if dura == "short":
            print("\n".join(["Tonikawa: Over the Moon for You", "Rent-a-Girlfriend", "My Dress-Up Darling", "Kubo Won’t Let Me Be Invisible", "The Angel Next Door Spoils Me Rotten"]))
        elif dura == "medium":
            print("\n".join(["Horimiya: Piece", "Kanojo mo Kanojo", "Oshi no Ko", "More Than a Married Couple, But Not Lovers", "Skip and Loafer"]))
        elif dura == "long":
            print("\n".join(["Kaguya-sama: Love is War (Final)", "Rent-a-Girlfriend (continuing)", "Fruits Basket: Prelude", "Blue Period", "Nagatoro-san"]))

elif gen.lower() == "horror":
    if deca == "1990s":
        if dura == "short":
            print("\n".join(["Uzumaki", "Gyo", "Hell Teacher Nube", "Petshop of Horrors", "Lament of the Lamb"]))
        elif dura == "medium":
            print("\n".join(["Tomie", "The Drifting Classroom", "Banana Fish", "MPD Psycho", "Leviathan"]))
        elif dura == "long":
            print("\n".join(["Bastard!!", "Guyver", "Hellsing (early)", "Berserk (1990s run)", "Vampire Princess Miyu"]))
    elif deca == "2000s":
        if dura == "short":
            print("\n".join(["Goth", "Parasyte (reprint)", "Alive: The Final Evolution", "Doubt", "Corpse Party"]))
        elif dura == "medium":
            print("\n".join(["Hellsing", "Elfen Lied", "Highschool of the Dead", "Another", "Shiki"]))
        elif dura == "long":
            print("\n".join(["I Am a Hero", "20th Century Boys", "Bloody Monday", "Kurosagi Corpse Delivery Service", "Fortune Arterial"]))
    elif deca == "2010s":
        if dura == "short":
            print("\n".join(["Another", "Tokyo Ghoul", "Corpse Party: Tortured Souls", "Ajin", "Paranoia Agent (re-air)"]))
        elif dura == "medium":
            print("\n".join(["The Future Diary", "Parasyte -the maxim-", "Devilman Crybaby", "Shinsekai Yori", "School-Live!"]))
        elif dura == "long":
            print("\n".join(["Attack on Titan", "Tokyo Ghoul:re", "Seraph of the End", "Deadman Wonderland", "Psycho-Pass"]))
    elif deca == "2020s":
        if dura == "short":
            print("\n".join(["Mieruko-chan", "High-Rise Invasion", "Junji Ito Maniac", "The Witch and the Beast", "Housing Complex C"]))
        elif dura == "medium":
            print("\n".join(["Hell's Paradise", "Chainsaw Man", "Call of the Night", "The Great Pretender", "Summer Time Rendering"]))
        elif dura == "long":
            print("\n".join(["Jujutsu Kaisen (dark arcs)", "Bleach: Thousand-Year Blood War", "Toilet-Bound Hanako-kun", "Akame ga Kill! (Re-air)", "Bastard!! 2022"]))

else:
    print("Sorry, I don't have a recommendation for that combination yet.")



#ginamitan ng kapangyarihan ni russel revillsa de luna
