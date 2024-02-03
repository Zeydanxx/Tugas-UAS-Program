#Menginput Nilai Tugas, UTS, dan UAS
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
 
#Menghitung Nilai Akhir sesuai dengan Bobot
nilai =  (0.20 * tugas) + (0.40 * uts) +  (0.55 * uas)
 
#Menentukan Grade Berdasarkan Nilai Akhir
if nilai > 85:
    grade = 'A'
elif nilai > 75:
    grade = 'B'
elif nilai > 65:
    grade = 'C'
elif nilai > 55:
    grade = 'D'
else:
    grade = 'E'
 
#Menentukan Status Kelulusan Berdasarkan Nilai Akhir
if nilai > 60:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'
 
#Menampilkan Nilai Akhir, Grade, dan Status Kelulusan
print('Nilai Akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))