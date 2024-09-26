import pandas as pd

# Excel dosyalarını oku
df_smiley = pd.read_excel('DB_smiley.xlsx')
df_liking = pd.read_excel('DB_liking.xlsx')
df_sad = pd.read_excel('DB_sad.xlsx')
df_shocked = pd.read_excel('DB_shocked.xlsx')

# Verileri birleştir
raw_data = pd.concat([df_smiley, df_liking, df_sad, df_shocked], ignore_index=True)

# Yeni Excel dosyasına yaz
raw_data.to_excel('0000_raw_data.xlsx', index=False)

print("Veriler başarıyla birleştirildi ve '0000_raw_data.xlsx' dosyasına kaydedildi.")

