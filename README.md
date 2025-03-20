# 🌟 GitHub Projem

Bu proje, Git/GitHub komutlarını öğrenmek ve temel bir yazılım geliştirme sürecini deneyimlemek için hazırlanmıştır.

## 📌 Proje Yapısı:
- **img/** → README içine eklenecek resimler burada tutulur.
- **tests/** → Test dosyalarının bulunduğu klasör (ilk başta boş).
- **coordinates.csv** → Nokta verilerini içeren CSV dosyası.
- **point.py** → CSV dosyasını okuyan ve işlem yapan Python kodu.

## 📌 Kullanılan Git Komutları:
- `git init` → Yeni bir Git deposu başlatır.
- `git add .` → Tüm değişiklikleri sahneye alır.
- `git commit -m "İlk commit"` → Yapılan değişiklikleri kaydeder.
- `git push origin main` → Değişiklikleri GitHub'a gönderir.

## 📌 Git İş Akışı:
### **Yerel Git İş Akışı (Local Workflow)**
1. Proje klasörünü oluştur ve içine dosyaları ekle.
2. `git add .` komutu ile tüm değişiklikleri takip et.
3. `git commit -m "Değişiklik mesajı"` ile kaydet.
4. `git push origin main` ile GitHub’a yükle.

### **GitHub İş Akışı (Remote Workflow)**
1. GitHub’da yeni bir depo oluştur.
2. Yerel Git deposunu GitHub’a bağla (`git remote add origin <repo-link>`).
3. `git pull origin main` ile güncellemeleri çek.
4. `git push` ile değişiklikleri yükle.

## 📌 Karşılaşılan Zorluklar:
> - İlk kez Git kullanırken `commit` yapmayı unuttum.  
> - GitHub'a dosya yüklerken `push` işlemini doğru yapmam gerektiğini öğrendim.  
> - Terminal komutlarını öğrenmek başlangıçta zor oldu, ancak tekrar ettikçe kolaylaştı.  

## 📌 Yapay Zeka Kullanımı:
Bu süreçte ChatGPT'ye şu soruları sordum:
- **"GitHub'da yeni bir depo nasıl oluşturulur?"**
- **"Git commit yaparken nelere dikkat edilmelidir?"**

Bu sayede, Git iş akışını daha iyi kavradım.