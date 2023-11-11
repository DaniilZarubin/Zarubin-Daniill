volume_disk_Mbit = 1.44
size_symbol_byte = 4

volume_disk_byte = volume_disk_Mbit * 1024 * 1024
size_book_byte = size_symbol_byte * 25 * 50 * 100

print("Количество книг, помещающихся на дискету:", int((volume_disk_byte/size_book_byte) // 1))
