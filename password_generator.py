from argparse import ArgumentParser
import secrets
import random
import string

# Menyiapkan Parser Argumen
parser = ArgumentParser(
    prog="Password Generator",
    description="Menghasilkan Beberapa Password Kuat Dengan Alat Ini"
)

# Menambahkan Argumen ke Parser
parser.add_argument("-n", "--numbers", default=0, help="Jumlah Angka dalam Password", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Jumlah Huruf Kecil dalam Password", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Jumlah Huruf Besar dalam Password", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Jumlah Karakter Khusus dalam Password", type=int)

# Menambahkan Argumen Panjang Total PW
parser.add_argument("-t", "--total-length", type=int, help="Panjang Total Password. Jika disediakan, akan diabaikan -n, -l, -u, dan menghasilkan password sepenuhnya acak dengan panjang yang ditentukan")

# Jumlah merupakan angka sehingga kita memeriksa tipe data int.
parser.add_argument("-a ", "--amount", default=1, type=int)
parser.add_argument("-o", "--output-file")

# Melakukan parsing argumen baris perintah.
args = parser.parse_args()

# list password
passwords = []

# Melalui jumlah password
for _ in range(args.amount):
    if args.total_length:
        # Menghasilkan password acak dengan panjang
        # total_length berdasarkan semua karakter yang tersedia
        passwords.append("".join(
            [secrets.choice(string.digits+string.ascii_letters+string.punctuation)
             for _ in range(args.total_length)]
        ))
    else:
        password = []
        # Jumlah angka yang harus ada dalam password
        for _ in range(args.numbers):
            password.append(secrets.choice(string.digits))
        # Jumlah Karakter Besar yang harus ada dalam password
        for _ in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))
        # Jumlah karakter kecil yang harus ada dalam password
        for _ in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))
        # Jumlah karakter khusus yang harus ada dalam password
        for _ in range(args.special_chars):
            password.append(secrets.choice(string.punctuation))

        # Mengacak daftar dengan semua huruf, angka, dan simbol yang mungkin
        random.shuffle(password)

        # Dapatkan huruf dari string hingga argumen panjang, lalu gabungkan
        password="".join(password)
        # Menambahkan password ini ke daftar password keseluruhan
        passwords.append(password)

# Menyimpan password ke file .txt
if args.output_file:
    with open(args.output_file, "w") as f:
        f.write("\n".join(passwords))
print("\n".join(passwords))