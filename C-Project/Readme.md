# C-Project - Deployemt
Folder ini merupakan penjelasan dan praktik deployment mlflow, minIO dan Database menggunakan docker-compose.

## Langkah-langkah deploy
1. Clone repository : https://github.com/SetiaBudii/test-devops.git
2. Buka folder hasil clone melalui IDE (contoh Vscode) lalu masuk ke direktori
   
   ```shell
   cd C-Project
   ```
3. Jalankan perintah berikut :
   
      ```shell
      sudo docker-compose up  --build
      ```
   Atau jalankan perintah berikut untuk menjalankan semua service dalam background:

    ```shell
    sudo docker-compose up -d --build
    ```
    
4. Jika langkah nomor 3 selesai buka halaman _minIO_ (http://localhost::9001/login ) lalu masukan _username_ **“minio_user”** dan _password_ **“minio_pwd”**
   
   _note: untuk username dan password bisa dilihat di file docker-compose.yml_
   
5. Pergi menu _access key_ dan buat _access key_ baru dengan menekan tombol _“Create access key”_.
6. Isikan field yang tersedia seperti tanggal expire, name dan lain-lain dan jika sudah klik _create_.
7. Pergi ke menu _bucket_ dan buat _bucket_ baru dengan menekan tombol _Create bucket_ lalu isikan nama _bucket_ yang ingin digunakan. Jika sudah klik _Create_.
8. Kembali ke terminal server, masukan perintah _"sudo docker-compose down"_ dan setting ulang _docker-compose.yml_ dengan memasukan nama _bucket_, _access key_, dan _secret key_ yang telah dibuat tadi di _minIO_.
11. Compose up lagi  semua service menggunakan perintah:
    ```shell
    docker-compose up --build
    ```
12. Buka halaman _mlflow ui_ lewat url “localhost:5000”
13. Untuk membuka database bisa melalui pgadmin dengan memasukan url berikut : “localhost:5050”
14. Masukan _username_ “admin@admin.com” dan _password_ “admin” saat login.
15. Create server baru dan masukan nama server, address port dan field lainnya seperti gambar dibawah:
16. Sampai disini mlflow ,minIO dan database sudah dapat diakses.
17. Untuk langkah selanjutnya merupakan test salah satu folder example. Contohnya disini akan mengetes **sklearn_elasticnet_diabetes.**
18. Untuk mengetes-nya disini saya menggunakan metode bash untuk mengakses secara langsung docker image mlflow_server. Pertama jalankan perintah:
```shell
    sudo docker ps
```
Setelah itu dan cari nama container dari mlflow_server.
19. Jika nama kontainer sudah didapat maka jalankan perintah:
```shell
 sudo docker exec -it <nama_kontainer>  /bin/bash
```
untuk membuka folder atau menjalankan bash pada container. Contoh “sudo docker exec -it mlflow_server  /bin/bash”
20. Selanjutnya buka direktori dari folder contoh yang ingin dijalankan berada menggunakan perintah
```shell
cd file/examples/sklearn_elasticnet_diabetes/linux
```
21. Jalankan file _train_diabetes.py_ menggunakan python dengan memasukan perintah:
```shell
 python train_diabetes.py
```
22. Jika proses selesai maka bisa dilihat hasilnya seperti berikut:
23. Selanjutnya untuk melihat dari tracker atau mlflow ui  buka kembali “localhost:5000” maka secara otomatis contoh eksperimen yang dijalankan akan muncul.
    
