[DE](https://github.com/necirvanalpar/nina-beep/blob/main/README.md)
We haven't made the English version as it's currently in the testing phase.

# Nina Uyarıları Alarmı

Bu Python betiği, Almanya'daki Nina uyarılarından anında haberdar olmak için oluşturulmuştur. Belirli bir ARS numarasına sahip bir bölge için tehlike seviyesi "Immediate" olan uyarılar algılanırsa, bilgisayarınızda bir alarm bip sesi çalar.

## Başlarken

Bu betiği kullanmak için, [Python](https://www.python.org/) ve [requests](https://pypi.org/project/requests/) ve [json](https://docs.python.org/3/library/json.html) kütüphanelerinin yüklü olması gerekiyor. Ayrıca, `winsound` modülü yalnızca Windows işletim sistemlerinde çalışır.

```bash
pip install requests
```

## Kullanım

1. `ninaBaseUrl` değişkeninde Nina sunucusunun URL'sini belirtin.
2. `arsNo` değişkenindeki [ARS](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) numarasını kendi bölgenize göre güncelleyin.
3. `tehlike_seviyesi` değişkenindeki tehlike seviyesini ayarlayın.
4. `filename` değişkeninde JSON dosyasının adını belirleyin.
5. Betiği çalıştırın: `python nina_uyarilari.py`

## Katkıda Bulunma

Herhangi bir sorun veya öneri için lütfen bir GitHub Issue açın veya bir Pull Request gönderin.
