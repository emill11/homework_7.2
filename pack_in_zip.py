from zipfile import ZipFile

with ZipFile("resources/zip.zip", 'w') as zip_file:
    zip_file.write("resources/xlsx.xlsx")
    zip_file.write("resources/pdf.pdf")
    zip_file.write("resources/users.csv")

    print(zip_file.namelist())
