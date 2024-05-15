# Study Kasus Singkat

## Pertanyaan
1. Jika diminta untuk melakukan mengirim dan menerima file ke suatu server, protokol apa yang digunakan? Jelaskan tahapan yang diperlukan untuk mengirim dan menerima file dengan protokol tersebut!
2. Jelaskan tahapan yang diperlukan untuk menulis hasil perintah ping ke sebuah file text!

## Jawaban
1. Berdasarkan pengalaman saya untuk kirim mengirim file ke server bisa menggunakan suatu protokol yakni FTP (File Transfer Protocol). FTP nantinya bisa berupa layanan yang akan diinstal atau diimplementasikan dalam server (FTP Server) dan nantinya bisa diakses melalui software (Filezilla dll) oleh client. FTP ini umumnya menggunakan port 21. Untuk FTP ini saya sudah pernah mempraktekkan ftp server pada debian server menggunakan proftpd namun belum menerapkan konsep “secure” (FTPS)  yang mana menurut saya dalam hal kirim mengirim file melalui server harus dijamin keamanannya agar tidak terjadi hal yang tidak diinginkan. Menurut saya ada 3 tahapan utama dalam kirim mengirim file dengan FTP yakni:
   - Pastikan server sudah mengimplementasikan FTP server
   - Pastikan Client sudah terkoneksi dengan server atau berada pada satu jaringan yang sama.
   - Pastikan Client sudah menginstall software seperti filezilla untuk kirim mengirim file ke server (opsional karena mungkin bisa juga menggunakan fitur bawaan dari sistem operasi seperti fitur File Explorer pada windows)

2.Berikut tahapan yang diperlukan untuk menulis hasil perintah ping ke sebuah file text:    
 - Pastikan kita sudah mengetahui alamat ip atau domain yang akan diuji konektivitasnya menggunakan ping. Contohnya google.com
 - Buka terminal dan masukan perintah:
  ```shell
  ping [ip/domain] > [namafile].txt
  ```
   Note : ip/domain diisi dengan alamat ip atau domain yang sudah dijelaskan pada langkah awal dan untuk nama file disesuaikan dengan nama file yang diinginkan.
![image](https://github.com/SetiaBudii/test-devops/assets/95162227/ddad01ac-2234-48bd-b1d8-1a5c5069605e)
![image](https://github.com/SetiaBudii/test-devops/assets/95162227/e6db9ae8-cf71-4a3b-94f1-d3c51c7ff3e2)

 - Kita bisa terus untuk mencatat hasil ping kedalam text menggunakan tag -t, dimana jika kita menggunakan tag tersebut maka hasil akan terus dicatat sampai kita menghentikan secara paksi perintah pingnya.
![image](https://github.com/SetiaBudii/test-devops/assets/95162227/fcaf29f1-c7fe-4bb5-a683-7c101f531c55)

-  Tambahan, kita juga bisa menambah output ke file tanpa menimpa file yang ada (Append) menggunakan >>
   ![image](https://github.com/SetiaBudii/test-devops/assets/95162227/e50742a3-fa75-4c0c-9498-edec9331d29d)

