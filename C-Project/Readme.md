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
    
4. Jika langkah nomor 5 selesai buka halaman _minIO_ (http://localhost::9001/login ) lalu masukan _username_ **“minio_user”** dan _password_ **“minio_pwd”**
   
   _note: untuk username dan password bisa dilihat di file docker-compose.yml_
   
5. Pergi menu access key dan buat access key baru dengan menekan tombol “Create access key”
7. Isikan field yang tersedia seperti tanggal expire, name dan lain-lain dan jika sudah klik create
8. Pergi ke menu bucket dan buat bucket baru dengan menekan tombol Create bucket lalu isikan nama bucket yang ingin digunakan. Jika sudah klik Create.
9. Kembali ke terminal server, masukan perintah docker-compose down dan setting ulang docker-compose.yml dengan memasukan nama bucket, access key, dan secret key yang telah dibuat tadi di minIO.
10. Compose up lagi  semua service menggunakan perintah docker-compose up --build
11. Buka halaman mlflow ui lewat url “localhost:5000”
12. Untuk membuka database bisa melalui pgadmin dengan memasukan url berikut : “localhost:5050”
13. Masukan username “admin@admin.com” dan password “admin” saat login.
14. Create server baru dan masukan nama server, address port dan field lainnya seperti gambar dibawah:
15. Sampai disini mlflow ,minIO dan database sudah dapat diakses.
16. Untuk langkah selanjutnya merupakan test salah satu folder example. Contohnya disini akan mengetes sklearn_elasticnet_diabetes.
17. Untuk mengetes-nya disini saya menggunakan metode bash untuk mengakses secara langsung docker image mlflow_server. Pertama jalankan perintah sudo docker ps dan cari nama container dari mlflow_server.
18. Jika nama kontainer sudah didapat maka jalankan perintah “sudo docker exec -it <nama_kontainer>  /bin/bash” untuk membuka folder atau menjalankan bash pada container. Contoh “sudo docker exec -it mlflow_server  /bin/bash”
19. Selanjutnya buka direktori dari folder contoh yang ingin dijalankan berada menggunakan perintah “cd file/examples/sklearn_elasticnet_diabetes/linux”
20. Jalankan file train_diabetes.py menggunakan python dengan memasukan perintah “python train_diabetes.py”
21. Jika proses selesai maka bisa dilihat hasilnya seperti berikut:
22. Selanjutnya untuk melihat dari tracker atau mlflow ui  buka kembali “localhost:5000” maka secara otomatis contoh eksperimen yang dijalankan akan muncul.
    
