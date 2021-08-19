Getting Started with Gauge
==========================

This is an executable specification file. This file follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.
To execute this specification, use `mvn test`

1) Kullanıcı girişi yapılarak sepete ürün eklenmesi
-------------------------------------------------
*Giriş yap butonuna tıklanır
*Kullanıcı bilgileri girilir
*"5" saniye kadar bekle!
*Kullanıcı, ürün için arama yapar
*"2" saniye kadar bekle!
*Kullanıcı, ürün listesinden ürünü seçer
*"2" saniye kadar bekle!
*Seçilen ürün iki tane farklı satıcıdan ürün seçilip sepete eklenir
*"7" saniye kadar bekle!


2) Kullanıcı girişi yapmadan belirtilen ürünü sepete ekleme
-----------------------------------------------------------
*Kullanıcı Kitap, Müzik, Film, Hobi kategorisini seçer
*Kullanıcı uzaktan kumandalı araçlar sekmesini açar
*Drone yedek parçaları seçilir
*Kullanıcı random ürünü seçer
*Kullanıcı ürünü sepete ekler


3) Analiz: Aynı satıcıdan alınan ve teslimat seçenekleri aynı olan ürünlerin paket gruplamasını gözleme
-------------------------------------------------------------------------------------------------------
*Giriş yap butonuna tıklanır
*Kullanıcı bilgileri girilir
 *"3" saniye kadar bekle!
*Kullanıcı, ürün için arama yapar
 *"3" saniye kadar bekle!
*Kullanıcı, ürün listesinden ürünü seçer
*Ürün sepete eklenir
*Satıcının sayfasına gidilir
*Satıcının sayfasından başka bir ürün seçilir
*Ürün sepete eklenir
*Sepete gidilir
*Alışverişi tamamla'ya tıklanır
*"10" saniye kadar bekle!

