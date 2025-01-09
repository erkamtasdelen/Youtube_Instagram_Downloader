import yt_dlp


def PullIt():
    f = open("./Genral_Infos/Downloaded_Videos.txt","r")
    text = (f.read()).split("\n")
    return text


Downloaded_Videos = PullIt()


def SaveIt(videoid):
    f = open("./Genral_Infos/Downloaded_Videos.txt","a")
    f.write(videoid+"\n")
    f.close()


def AskIt(videoid):

    if videoid in Downloaded_Videos:
        return False
    else:
        return True

    

class Youtube_Side:
    def __init__(self,url,katagori = "test",video_count=10):
        self.url = f"https://www.youtube.com/@{url}/shorts"
        
        #print(self.url)
        
        self.video_count = video_count
        self.katagori = katagori
        self.allvideos = []
    def get_channel_info(self):
        try:
            # yt-dlp seçeneklerini belirle
            ydl_opts = {
                'quiet': True,  # İlerleme durumu gösterme
                'extract_flat': True,  # Videoların sadece URL'lerini al
                'force_generic_extractor': True,  # Bazı kanallarda hata durumunu önler
            }

            # Kanalın videolarını çek
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(self.url, download=False)

                # Kanal video sayısını ve URL'lerini yazdır
                if 'entries' in result:
                    print(f"Kanalda {len(result['entries'])} video mevcut.")
                    #print("\nKanalın Videoları:")
                    for index, video in enumerate(result['entries'], start=1):
                        #print(f"{index}. {video['url']}")

                        if "shorts" in video['url']:
                            self.allvideos.append(video['url'])


            #print(self.allvideos[5])
            self.download_video()
        except Exception as e:
            print(f"Hata oluştu: {e}")
            
    def download_video(self):
        downloaded = 0
        for video in self.allvideos:
            videoId = video.split("/")[4]
            if AskIt(videoId):
                SaveIt(videoId)
                try:
                    # yt-dlp seçeneklerini belirle
                    ydl_opts = {
                        'format': 'best',  # En iyi video formatını seç
                        'outtmpl': f'Videos/{self.katagori}/'+'%(title)s.%(ext)s',  # Dosya adını video başlığına göre belirle
                        'quiet': False,  # İndirilen videonun ilerleme durumunu görmek için False yapın
                    }

                    # Video indir
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video])  # Verilen video URL'sinden indirme işlemini başlat

                    print("Video başarıyla indirildi.")
                    downloaded +=1

                except Exception as e:
                    print(f"Hata oluştu: {e}")
            if downloaded > self.video_count:
                print("\n#### İndirmenin Sonuna Gelindi ####\n")
                break
    # Test video URL'sini buraya girin




def ClassedAccounts():
    accounts = (open("./Genral_Infos/ACCOUNTLAR.txt" , "r").read()).split("\n")
    
    x = 0
    classed = []
    updated = []

    for account in accounts:
        updated.append(account)
        x+=1
        if x == 3:
            classed.append(updated)
            x = 0
            updated = []

    return classed




import instaloader
import os

class Instagram_Side:
    def __init__(self, username, category="test", post_count=10):
        self.username = username
        self.category = category
        self.video_count = post_count
        self.all_videos = []

        self.loader = instaloader.Instaloader(
            download_videos=True,  # Videoları indir
            download_video_thumbnails=False,  # Küçük resimleri indirme
            save_metadata=False  # Metadata dosyalarını kaydetme
        )

    def get_posts(self):
        try:
            # Kullanıcı bilgilerini al
            profile = instaloader.Profile.from_username(self.loader.context, self.username)

            # Gönderileri çek
            print(f"Kullanıcı: {self.username}")
            print(f"Toplam Gönderi Sayısı: {profile.mediacount}")
            
            for post in profile.get_posts():
                if post.is_video:  # Sadece videoları seç
                    if AskIt(str(post.mediaid)):
                        self.all_videos.append(post)

                if len(self.all_videos) >= self.video_count:
                    break

            print(f"{len(self.all_videos)} video alındı.")
            self.download_posts()
        except Exception as e:
            print(f"Hata oluştu: {e}")

    def download_posts(self):
        downloaded = 0
        save_path = f"Instagram"
        
        # Klasör oluştur

        for post in self.all_videos:
            videoid = str(post.mediaid)
            if AskIt(videoid):
                SaveIt(videoid)
                try:
                    # Video ID'sini al ve dosya adı olarak kullan

                    # Video indir
                    self.loader.download_post(post, target=save_path)
                    
                    
                    listofdir = os.listdir(save_path)

                    for file in listofdir:
                        if ".txt" in file:
                            os.remove(f"./{save_path}/{file}")


                    print(f"İndirilen Video: {videoid}")
                    downloaded += 1

                    if downloaded >= self.video_count:
                        print("İndirmenin Sonuna Gelindi.")
                        break
                except Exception as e:
                    print(f"Hata oluştu: {e}")

# Kullanım




HazirHesap = ClassedAccounts()



def CVPTESPT(cvp):
    if cvp == "ALL":
        return ["0"]
    elif len(HazirHesap)-int(cvp) <= 0:
        return ["2",ktgs[(len(HazirHesap)-int(cvp))*-1]]
    elif len(HazirHesap)-int(cvp) > 0:
        return ["1",[HazirHesap[int(cvp)]]]
    else:
        return False
    



def ALL():
    for hesap in HazirHesap:
        print(f"\n\n{hesap[0]} Hesabindan Videolar İndiriliyor\n\n")

        if hesap[1] == "Youtube":
            X = Youtube_Side(hesap[0],katagori=hesap[2],video_count=Download_Limit)
            X.get_channel_info()
        elif hesap[1] == "Instagram":
            instagram = Instagram_Side(username=hesap[0], category=hesap[2], post_count=Download_Limit)
            instagram.get_posts()

def Sellected(HESAPLAR):
    for hesap in HESAPLAR:
        print(f"\n\n{hesap[0]} Hesabindan Videolar İndiriliyor\n\n")

        if hesap[1] == "Youtube":
            X = Youtube_Side(hesap[0],katagori=hesap[2],video_count=Download_Limit)
            X.get_channel_info()
        elif hesap[1] == "Instagram":
            instagram = Instagram_Side(username=hesap[0], category=hesap[2], post_count=Download_Limit)
            instagram.get_posts()

def FoundKtgs(slcted):
    Updated = []
    for hesap in HazirHesap:
        if hesap[2] == slcted:
            Updated.append(hesap)
    return Updated




Download_Limit = 30 #Limitleri Değiştirmek İçin


while True:
    sayi = 0
    ktgs = []

    print(f"Şuanda tek seferde indirilicek video sayisi : {Download_Limit}\n")
    print("ALL - Tum Hesaplardan Indir")
    for hesap in HazirHesap:
        print(f"{sayi} - {hesap[0]} | {hesap[2]} | {hesap[1]}")
        sayi +=1
    print("- Yada Katagori Üstünden İndir -")

    for hesap in HazirHesap:
        if hesap[2] in ktgs:
            pass
        else:
            print(f"{sayi} - {hesap[2]}")
            sayi +=1
            ktgs.append(hesap[2])

    #print(ktgs)


    cvp = (CVPTESPT(input("CEVABINIZ : ")))

    print(cvp)
    if "0" in cvp:
        ALL()
    elif "1" in cvp:
        Sellected(cvp[1])
    elif "2" in cvp:
        Sellected(FoundKtgs(cvp[1]))

    




#X = Youtube_Side("the_blue_magazine")
#X.get_channel_info()


#instagram = Instagram_Side(username="heyppme", category="nature", post_count=15)
#instagram.get_posts()



#OKAY %100