# meetup-kafka

Obtaining event names from a kafka stream from meetup.com

## 1. Installation

Run the following commands in your terminal:

    pipenv install -d
    docker-compose up
    
## 2. Run

In a new terminal window, run the producer with python:

    pipenv shell
    python src/producer.py localhost:9092 http://stream.meetup.com/2/rsvps
    
In another terminal window run:
    
    pipenv shell
    python src/consumer.py
    
Example output:

    Indy Witches and Pagans Meetup
    Perry's Wednesday 1/2 NL Texas Hold'em with Pineapple & PLO
    $28 Tickets!!! ROBERT LEPAGE'S 887 + pre-show chat (65% off Canadian Stage)
    AWS Cloud Development Kit - Infrastructure as Code (not YAML!)
    TechExeter / Digital Exeter Summer Social
    Swift NIO Intro Workshop
    CO-ED 3s & 4s Grass V-ball @ Observatory Park
    Meetup At The Mill
    Meet and Greet Mixer
    How to Climb a 14er - REI Workshop - WED JUNE 12 @ 600pm
    Downtown Rooftop BYOB Get-Together!
    Mindfulness-Based Recovery Support
    Bike Night
    Free Crash Course | Build a Web App with JavaScript & jQuery
    اللقاء الثاني : كتاب إبريل  "ماجدولين" 📖🌿
    Big Data & Deep Learning in Genomics
    DC Micro Tech Talks: Small Groups Discuss Big Ideas in Tech!
    Raise Your Vibe: Spring Into Action!
    How to Grow a 'Resilience Tree' for a Happier, Healthier Life
    Free English classes ( failte isteach)
    Friday tennis
    Sunday Jazz Brunch 
    Deer Creek Canyon - level 6
    Rare Plant Sale and Buffet. 
    WTM Meetup #5
    Pick-Up Soccer at the ** National Mall **
    Tandem Language exchange with PAELLA PARTY - SANGRIA Y AMIGOS
    WESO Program: Never Wrestle with a Pig
    The All American Steakhouse Wednesdays 630 and 830 pm!
    Friday Night Games at Bud's Place in Leeds
    Intro to TensorFlow.js
    French and Americans Friendship @ Tavern Breizh
    Intelligent Projects with AI & JavaScript 
    Standard paced potter to Waterside Cafe @ Hawkhurst Fish Farm
    Tech Talk:  Modernizing Your Printer with Keith Kovala
    (1st) Event in Hinesville, GA
    Deep Learning
    ¿Cómo llevar tu empresa al Marketing Digital?
    Google I/O 2019 Extended + Writing Accessible Go with Julia Ferraioli
    MemDevOps May 2019 Meeting
    Sony Be Alpha Day at Henry's Vancouver
    Qigong at Oak Knoll Lutheran in Minnetonka
     Experiment with Steel Wool Photography (Every April Event)
    IGDA NH Presents: Sam Sarette - Interactive Storytelling with Ink
    Avengers: Endgame 'satisfying' and 'glorious', 96% score on reviews
    ⛰️EMT⛰️ 🥊🆙Drilling Class🆙🥊 HADRON
    Golang SP – Luizalabs  | Image Processing & Go on Azure
    Real Networking
    Camí dels presos-Puig de So Na Moixa-Cala Varques
    Barnyard Birthday Bash & Volunteer Party
    Google I/O Extended 2019
    How to do better launches with gradual rollouts, sponsored by Optimizely
    Cinco de Drinko - Part Dos
    LLVM Austin Area Meetup
    UX Jobs Panel
    Awesome Automated APIs with Automagic REST
    Ravioli Pasta Making Party!
    My Brilliant Friend - Come Discuss, Laugh and Drink Wine!
    Beers with Bandits // Spring Edition
    Intercambio alemán-español / Deutsch-Spanisch Austausch🇩🇪
    Koffie & kletsen in Amsterdam West
    Las Trampas Regional Wilderness
    Beltane Fire Festival @ Calton Hill 🔥
    Saturday Socialising @ The Conductor (Exclusive hire of this New Venue) 
     Let's Hike Richfield Heritage Preserve- Intermediate/fast 
    ValpoHacks Meetup
    Rockefeller main lot Thursday hike with Bob
    Disturbed Gig
    Shopify Meetup: Grow Your Own E-Commerce
    Alpharetta Beach - NEW: B/BB Coed 3s/4s
    Intimate Kirtan with Girish
    Ultimate Frisbee
    SQL Server on Azure
    Coffee, Chat & Night
    Go Meetup at Bonnier Broadcasting
    Thursday Night Tex Mex and Margaritas 
    Clearing the Clutter Inside & Out
    Meetup 388
    Meetup #23 - Rédaction web
    The Hard Truth - Tuesdays
    Belly Dance/Baladi class Monday 7:00 - 8:00 at Studios Accento
    Conversation group in English- Let's make new friends using our English!
    Innovation Jam: Design Accessibility Training (Part 1)
    Verde Canyon Railroad
    SAN FRANCISCO: SF Cuddles Daytime Cuddle Party - May 25th 2019
    Patterns & Systems Thinking + Design Critique for Efficiency & Success
    DCJS[69] - A Series of Short Talks by Awesome Folks
    Mini Makers and Experimenters Lab
    Soho Forum Debate Nina Teicholz VS David Katz buy ticket
    Free Tickets to Revelation the Musical
    Spreken als een pro
    9:00  AM Sunday Doubles @ Lions Park
    Boba & Books! (Must read: Kafka on the Shore)
    Life and Success Coaching Certification 
    MS Build 2019 Streaming Event
    MotionLayout: Complex animations without the hassle
    WWDB #01
    Let’s meet for the Old Ellicott City 2019 Springfest!
    Wednesday Evening Pick-up Soccer in San Lorenzo
    U-speak! Toastmasters meeting    
