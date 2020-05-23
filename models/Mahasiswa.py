
class Mahasiswa:

    @staticmethod
    def showAll(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM mahasiswa")
        result = cur.fetchall()
        cur.close()
        return result
        

    def insertData(msyql, nim, name, alamat):

        
        pass

    def deleteData(mysql, nim):
        pass
