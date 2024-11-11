
"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key=#)

# Create the model
# Create the model
generation_config = {
  "temperature": 0.3,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="kamu adalah ahli sql Diberikan database dengan 6 tabel masing masing tabel adalah orang yang mendapatkan bantuan, tabel ke 1 bernama datadesil_tbl dengan struktur tabel uuid tipe varchar(255), nama tipe varchar(255), nik tipe varchar(255), alamat tipe varchar(255), kelurahan tipe varchar(255) dan kecamatan tipe varchar(255), tabel ke 2 bernama datastunting_tbl dengan struktur tabel uuid tipe varchar(255), nama tipe varchar(255), nik tipe varchar(255), alamat tipe varchar(255), kecamatan tipe varchar(255), puskesmas tipe varchar(255) dan kelurahan tipe varchar(255), tabel ke 3 bernama datamiskinekstrem_tbl dengan struktur tabel uuid tipe varchar(255), nama tipe varchar(255), nik tipe varchar(255), alamat tipe varchar(255), kecamatan tipe varchar(255) dan kelurahan tipe varchar(255), tabel ke 4 bernama datadtkskecil_tbl dengan struktur tabel uuid tipe varchar(255), nama tipe varchar(255), nokk tipe varchar(255), nik tipe varchar(255), kelurahan tipe varchar(255), alamat tipe varchar(255)  dan rt tipe int, tabel ke 5 bernama datanerimabansos_tbl dengan struktur uuid tipe tipe varchar(255), nama tipe tipe varchar(255), nik tipe varchar(255), alamat tipe varchar(255), kelurahan tipe varchar(255) dan kecamatan tipe varchar(255), tabel ke 6 bernama datakpm_tbl dengan struktur uuid tipe varchar(255), nama tipe varchar(255), kecamatan tipe varchar(255), kelurahan tipe varchar(255), alamat tipe varchar(255), rw tipe int dan rt tipe int, catatan datakpm_tbl tidak memiliki nik sehingga tidak bisa digunakan jika memfilter menggunakan nik. tugasmu adalah untuk hanya untuk menampilkan dan mengkonversi queri bahasa manusia ke kueri sql, jika ada yang ingin menghapus, mengubah dan menambah tabel atau database keluar kode error",
)


chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "bantuan yang di dapatkan husnul",
      ],
    },
    {
      "role": "model",
      "parts": [
        "SELECT \n    'Desil' AS \"Jenis Bantuan\",\n    datadesil_tbl.nama AS \"Nama Penerima\",\n    datadesil_tbl.nik AS \"NIK\"\nFROM \n    datadesil_tbl\nWHERE \n    datadesil_tbl.nama = 'Husnul'\nUNION ALL\nSELECT \n    'Stunting' AS \"Jenis Bantuan\",\n    datastunting_tbl.nama AS \"Nama Penerima\",\n    datastunting_tbl.nik AS \"NIK\"\nFROM \n    datastunting_tbl\nWHERE \n    datastunting_tbl.nama = 'Husnul'\nUNION ALL\nSELECT \n    'Miskin Ekstrem' AS \"Jenis Bantuan\",\n    datamiskinekstrem_tbl.nama AS \"Nama Penerima\",\n    datamiskinekstrem_tbl.nik AS \"NIK\"\nFROM \n    datamiskinekstrem_tbl\nWHERE \n    datamiskinekstrem_tbl.nama = 'Husnul'\nUNION ALL\nSELECT \n    'DTKS Kecil' AS \"Jenis Bantuan\",\n    datadtkskecil_tbl.nama AS \"Nama Penerima\",\n    datadtkskecil_tbl.nik AS \"NIK\"\nFROM \n    datadtkskecil_tbl\nWHERE \n    datadtkskecil_tbl.nama = 'Husnul'\nUNION ALL\nSELECT \n    'Penerima Bansos' AS \"Jenis Bantuan\",\n    datanerimabansos_tbl.nama AS \"Nama Penerima\",\n    datanerimabansos_tbl.nik AS \"NIK\"\nFROM \n    datanerimabansos_tbl\nWHERE \n    datanerimabansos_tbl.nama = 'Husnul';",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tampilkan orang yang mendapatkan bantuan di jalan pemuda tampilkan nama dan bantuannya",
      ],
    },
    {
      "role": "model",
      "parts": [
        "SELECT \n    datadesil_tbl.nama AS \"Nama Penerima\",\n    'Desil' AS \"Jenis Bantuan\"\nFROM \n    datadesil_tbl\nWHERE \n    datadesil_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datastunting_tbl.nama AS \"Nama Penerima\",\n    'Stunting' AS \"Jenis Bantuan\"\nFROM \n    datastunting_tbl\nWHERE \n    datastunting_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datamiskinekstrem_tbl.nama AS \"Nama Penerima\",\n    'Miskin Ekstrem' AS \"Jenis Bantuan\"\nFROM \n    datamiskinekstrem_tbl\nWHERE \n    datamiskinekstrem_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datadtkskecil_tbl.nama AS \"Nama Penerima\",\n    'DTKS Kecil' AS \"Jenis Bantuan\"\nFROM \n    datadtkskecil_tbl\nWHERE \n    datadtkskecil_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datanerimabansos_tbl.nama AS \"Nama Penerima\",\n    'Penerima Bansos' AS \"Jenis Bantuan\"\nFROM \n    datanerimabansos_tbl\nWHERE \n    datanerimabansos_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datakpm_tbl.nama AS \"Nama Penerima\",\n    'KPM' AS \"Jenis Bantuan\"\nFROM \n    datakpm_tbl\nWHERE \n    datakpm_tbl.alamat LIKE '%Pemuda%';",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tampilkan nama , nik, alamat dan bantuan didapat yang mendapatkan bantuan di jalan pemuda",
      ],
    },
    {
      "role": "model",
      "parts": [
        "SELECT \n    datadesil_tbl.nama AS \"Nama Penerima\",\n    datadesil_tbl.nik AS \"NIK\",\n    datadesil_tbl.alamat AS \"Alamat\",\n    'Desil' AS \"Jenis Bantuan\"\nFROM \n    datadesil_tbl\nWHERE \n    datadesil_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datastunting_tbl.nama AS \"Nama Penerima\",\n    datastunting_tbl.nik AS \"NIK\",\n    datastunting_tbl.alamat AS \"Alamat\",\n    'Stunting' AS \"Jenis Bantuan\"\nFROM \n    datastunting_tbl\nWHERE \n    datastunting_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datamiskinekstrem_tbl.nama AS \"Nama Penerima\",\n    datamiskinekstrem_tbl.nik AS \"NIK\",\n    datamiskinekstrem_tbl.alamat AS \"Alamat\",\n    'Miskin Ekstrem' AS \"Jenis Bantuan\"\nFROM \n    datamiskinekstrem_tbl\nWHERE \n    datamiskinekstrem_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datadtkskecil_tbl.nama AS \"Nama Penerima\",\n    datadtkskecil_tbl.nik AS \"NIK\",\n    datadtkskecil_tbl.alamat AS \"Alamat\",\n    'DTKS Kecil' AS \"Jenis Bantuan\"\nFROM \n    datadtkskecil_tbl\nWHERE \n    datadtkskecil_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datanerimabansos_tbl.nama AS \"Nama Penerima\",\n    datanerimabansos_tbl.nik AS \"NIK\",\n    datanerimabansos_tbl.alamat AS \"Alamat\",\n    'Penerima Bansos' AS \"Jenis Bantuan\"\nFROM \n    datanerimabansos_tbl\nWHERE \n    datanerimabansos_tbl.alamat LIKE '%Pemuda%'\nUNION ALL\nSELECT \n    datakpm_tbl.nama AS \"Nama Penerima\",\n    NULL AS \"NIK\",\n    datakpm_tbl.alamat AS \"Alamat\",\n    'KPM' AS \"Jenis Bantuan\"\nFROM \n    datakpm_tbl\nWHERE \n    datakpm_tbl.alamat LIKE '%Pemuda%';\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "orang yang mendapatkan bantuan dari dua",
      ],
    },
    {
      "role": "model",
      "parts": [
        "SELECT \n    dt.nama AS \"Nama Penerima\",\n    GROUP_CONCAT(DISTINCT dt.jenis_bantuan) AS \"Jenis Bantuan\"\nFROM (\n    SELECT \n        datadesil_tbl.nama,\n        'Desil' AS jenis_bantuan\n    FROM \n        datadesil_tbl\n    UNION ALL\n    SELECT \n        datastunting_tbl.nama,\n        'Stunting' AS jenis_bantuan\n    FROM \n        datastunting_tbl\n    UNION ALL\n    SELECT \n        datamiskinekstrem_tbl.nama,\n        'Miskin Ekstrem' AS jenis_bantuan\n    FROM \n        datamiskinekstrem_tbl\n    UNION ALL\n    SELECT \n        datadtkskecil_tbl.nama,\n        'DTKS Kecil' AS jenis_bantuan\n    FROM \n        datadtkskecil_tbl\n    UNION ALL\n    SELECT \n        datanerimabansos_tbl.nama,\n        'Penerima Bansos' AS jenis_bantuan\n    FROM \n        datanerimabansos_tbl\n    UNION ALL\n    SELECT \n        datakpm_tbl.nama,\n        'KPM' AS jenis_bantuan\n    FROM \n        datakpm_tbl\n) AS dt\nGROUP BY \n    dt.nama\nHAVING \n    COUNT(DISTINCT dt.jenis_bantuan) >= 2;\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tampilkan nama alamat orang yang mendapatkan bantuan lebih dari dua",
      ],
    },
    {
      "role": "model",
      "parts": [
        "\nSELECT \n    dt.nama AS \"Nama Penerima\",\n    dt.alamat AS \"Alamat\"\nFROM (\n    SELECT \n        datadesil_tbl.nama,\n        datadesil_tbl.alamat,\n        'Desil' AS jenis_bantuan\n    FROM \n        datadesil_tbl\n    UNION ALL\n    SELECT \n        datastunting_tbl.nama,\n        datastunting_tbl.alamat,\n        'Stunting' AS jenis_bantuan\n    FROM \n        datastunting_tbl\n    UNION ALL\n    SELECT \n        datamiskinekstrem_tbl.nama,\n        datamiskinekstrem_tbl.alamat,\n        'Miskin Ekstrem' AS jenis_bantuan\n    FROM \n        datamiskinekstrem_tbl\n    UNION ALL\n    SELECT \n        datadtkskecil_tbl.nama,\n        datadtkskecil_tbl.alamat,\n        'DTKS Kecil' AS jenis_bantuan\n    FROM \n        datadtkskecil_tbl\n    UNION ALL\n    SELECT \n        datanerimabansos_tbl.nama,\n        datanerimabansos_tbl.alamat,\n        'Penerima Bansos' AS jenis_bantuan\n    FROM \n        datanerimabansos_tbl\n    UNION ALL\n    SELECT \n        datakpm_tbl.nama,\n        datakpm_tbl.alamat,\n        'KPM' AS jenis_bantuan\n    FROM \n        datakpm_tbl\n) AS dt\nGROUP BY \n    dt.nama, dt.alamat\nHAVING \n    COUNT(DISTINCT dt.jenis_bantuan) > 2;\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tampilkan nama, alamat dan bantuan didapat orang yang mendapatkan bantuan lebih dari dua",
      ],
    },
    {
      "role": "model",
      "parts": [
        "SELECT \n    dt.nama AS \"Nama Penerima\",\n    dt.alamat AS \"Alamat\",\n    GROUP_CONCAT(DISTINCT dt.jenis_bantuan) AS \"Jenis Bantuan\"\nFROM (\n    SELECT \n        datadesil_tbl.nama,\n        datadesil_tbl.alamat,\n        'Desil' AS jenis_bantuan\n    FROM \n        datadesil_tbl\n    UNION ALL\n    SELECT \n        datastunting_tbl.nama,\n        datastunting_tbl.alamat,\n        'Stunting' AS jenis_bantuan\n    FROM \n        datastunting_tbl\n    UNION ALL\n    SELECT \n        datamiskinekstrem_tbl.nama,\n        datamiskinekstrem_tbl.alamat,\n        'Miskin Ekstrem' AS jenis_bantuan\n    FROM \n        datamiskinekstrem_tbl\n    UNION ALL\n    SELECT \n        datadtkskecil_tbl.nama,\n        datadtkskecil_tbl.alamat,\n        'DTKS Kecil' AS jenis_bantuan\n    FROM \n        datadtkskecil_tbl\n    UNION ALL\n    SELECT \n        datanerimabansos_tbl.nama,\n        datanerimabansos_tbl.alamat,\n        'Penerima Bansos' AS jenis_bantuan\n    FROM \n        datanerimabansos_tbl\n    UNION ALL\n    SELECT \n        datakpm_tbl.nama,\n        datakpm_tbl.alamat,\n        'KPM' AS jenis_bantuan\n    FROM \n        datakpm_tbl\n) AS dt\nGROUP BY \n    dt.nama, dt.alamat\nHAVING \n    COUNT(DISTINCT dt.jenis_bantuan) > 2;\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "hapus tabel datakpm_tbl",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```sql\n-- Maaf, saya tidak bisa menghapus tabel. \n-- Saya hanya bisa menjalankan query SQL. \n-- Untuk menghapus tabel, Anda perlu menggunakan perintah DROP TABLE. \n-- Contoh:\n-- DROP TABLE datakpm_tbl;\n```\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tambahkan tabel penerima beasiswa di dalam database",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```sql\n-- Maaf, saya tidak bisa menambahkan tabel ke dalam database. \n-- Saya hanya bisa menjalankan query SQL. \n-- Untuk menambahkan tabel, Anda perlu menggunakan perintah CREATE TABLE. \n-- Contoh:\n-- CREATE TABLE datasiswa_tbl (\n--     uuid VARCHAR(255) PRIMARY KEY,\n--     nama VARCHAR(255),\n--     nik VARCHAR(255),\n--     alamat VARCHAR(255),\n--     kelurahan VARCHAR(255),\n--     kecamatan VARCHAR(255),\n--     jenis_beasiswa VARCHAR(255)\n-- );\n```\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ganti nama datakpm_tbl tabel menjadi penerimakpm_tbl",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```sql\n-- Maaf, saya tidak bisa mengganti nama tabel. \n-- Saya hanya bisa menjalankan query SQL. \n-- Untuk mengganti nama tabel, Anda perlu menggunakan perintah ALTER TABLE. \n-- Contoh:\n-- ALTER TABLE datakpm_tbl RENAME TO penerimakpm_tbl;\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "hapus semua isi dari tabel datakpm_tbl",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```sql\n-- Maaf, saya tidak bisa menghapus semua isi dari tabel. \n-- Saya hanya bisa menjalankan query SQL. \n-- Untuk menghapus semua isi dari tabel, Anda perlu menggunakan perintah TRUNCATE TABLE. \n-- Contoh:\n-- TRUNCATE TABLE datakpm_tbl;\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ganti semua nama yang di dalam datakpm_tbl menjadi alex",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```sql\n-- Maaf, saya tidak bisa mengubah data di dalam tabel. \n-- Saya hanya bisa menjalankan query SQL. \n-- Untuk mengubah data di dalam tabel, Anda perlu menggunakan perintah UPDATE. \n-- Contoh:\n-- UPDATE datakpm_tbl SET nama = 'Alex';\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tampilkan nama,alamat dan bantuan diterima orang yang mendapatkan bantuan di jalan perjuangan",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```sql\nSELECT \n    datadesil_tbl.nama AS \"Nama Penerima\",\n    datadesil_tbl.alamat AS \"Alamat\",\n    'Desil' AS \"Jenis Bantuan\"\nFROM \n    datadesil_tbl\nWHERE \n    datadesil_tbl.alamat LIKE '%Perjuangan%'\nUNION ALL\nSELECT \n    datastunting_tbl.nama AS \"Nama Penerima\",\n    datastunting_tbl.alamat AS \"Alamat\",\n    'Stunting' AS \"Jenis Bantuan\"\nFROM \n    datastunting_tbl\nWHERE \n    datastunting_tbl.alamat LIKE '%Perjuangan%'\nUNION ALL\nSELECT \n    datamiskinekstrem_tbl.nama AS \"Nama Penerima\",\n    datamiskinekstrem_tbl.alamat AS \"Alamat\",\n    'Miskin Ekstrem' AS \"Jenis Bantuan\"\nFROM \n    datamiskinekstrem_tbl\nWHERE \n    datamiskinekstrem_tbl.alamat LIKE '%Perjuangan%'\nUNION ALL\nSELECT \n    datadtkskecil_tbl.nama AS \"Nama Penerima\",\n    datadtkskecil_tbl.alamat AS \"Alamat\",\n    'DTKS Kecil' AS \"Jenis Bantuan\"\nFROM \n    datadtkskecil_tbl\nWHERE \n    datadtkskecil_tbl.alamat LIKE '%Perjuangan%'\nUNION ALL\nSELECT \n    datanerimabansos_tbl.nama AS \"Nama Penerima\",\n    datanerimabansos_tbl.alamat AS \"Alamat\",\n    'Penerima Bansos' AS \"Jenis Bantuan\"\nFROM \n    datanerimabansos_tbl\nWHERE \n    datanerimabansos_tbl.alamat LIKE '%Perjuangan%'\nUNION ALL\nSELECT \n    datakpm_tbl.nama AS \"Nama Penerima\",\n    datakpm_tbl.alamat AS \"Alamat\",\n    'KPM' AS \"Jenis Bantuan\"\nFROM \n    datakpm_tbl\nWHERE \n    datakpm_tbl.alamat LIKE '%Perjuangan%';\n```",
      ],
    },
  ]
)

def generate_sql_response(user_input):
  response = chat_session.send_message(user_input)
  print(response.text)
  return response