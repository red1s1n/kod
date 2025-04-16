
define e = Character("Lara ", color="#ce6d35")
define b = Character("Mom", color = "#ec12cf")
define k = Character("Mickael", color = "#00c8fa")
define n = Character("Axel", color = "#ff0000")
 
define audio.musKach = "audio/Kach.mp3"
define audio.musnarik = "audio/baba.mp3"
define audio.musnormal = "audio/narik.mp3"
define audio.mussmert = "audio/xuy.mp3"



label start: 
    stop music 
    
    scene bg room baba
    
    play audio musnormal

    show baba
  
    e "Я помню только удовольствие..."

    e "страх с болью, а потом чайка..."

    hide baba

    "..." "Девушка Лара жила в небольшом городке Глекрон."

    "..." "Что могло случиться с этой девочкой?..."

    scene bg room baba

    with fade

    show tel baba

    "Phone" "~Вибрация~"
    
    hide tel baba

    show baba spid

    e "Ммм...уже утро"

    show baba zlo at right
    with dissolve

    e "Мама снова звонит"

    show mummy at left
    with dissolve

    b "Доброе утро, мой малыш"

    e "Ага. Что случилось?"

    b "Я просто звоню, чтобы разбудить тебя. И не забудь позавтракать..."

    e "Ага. Я подумаю... Пока."

    hide mummy
    show tele baba
    e "Как я устала..."
    hide tele baba
    show baba spid
    hide baba spid
    stop audio 
    scene bg room baba

    with fade
    
    "..." "Лара продолжала лежать на кровати и листала рекомендации"
    "..." "Прошло около часа и у неё заурчало в животе"
    
    

    show baba 
    

    menu :
        
        "Что сделать?"

        "Поесть":
            jump poela_jiva
           
        "Не есть":
            jump ymerla
    return

    

    
label poela_jiva:
   
    play audio musKach

    "..." "Лара решила всё таки поесть..."  
    "..." "Теперь, она довольна и решила пригласить к себе друга"
    "..." "Но он не брал трубку, поэтому Лара сама решила пойти к нему"

    scene bg ul


    "..." "Лара шла по улице задумавшись о своём"

    show baba
    e "Странно, что Мика не брал трубку..."
    e "Думаю он спит, прийду и разбужу его"

    hide baba
    show babat

    "..." "Девочка почти дошла до дома друга как вдруг..."

    hide babat

    "..." "!В неё влетел какой-то парень!"

    show baba zlo
    e "Ауч! Смотри куда бежишь!"

    show narik at left

    n "Сама смотри куда идёшь!"

    "..." "Он оттолкнул Лару и побежал дальше"

    hide narik





    return

label ymerla: 
    play audio mussmert
    scene bg vanna baba  
    
    "..."  "Лара решила ни есть" 
   
    

    scene bg vanna sm
    "..."   "Через какое-то время она пошла в ванную, и из-за того, что она не ела, упала в обморок и захлебнулась... "



    scene bg sm
    "..."  "Лара умерла..."

   
    stop audio
    return
 
 
        




