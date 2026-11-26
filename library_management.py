import mysql.connector

class library_management:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user='root',password='hidar',host='localhost',database='library_management')
        except Exception:
            print('connection failed')
            self.con=None
    def add_book(self,title,author,category,total_copies,availiable_copies):
        if self.con is None:
            return
        try:
            c=self.con.cursor()
            query='insert into books(title,author,category,total_copies,availiable_copies) values(%s,%s,%s,%s,%s)'
            data=(title,author,category,total_copies,availiable_copies)
            c.execute(query,data)
            self.con.commit()
            if c.rowcount>0:
                print('inserted successfully')
            else:
                print('insertion failed')
        except Exception:
            print('operation failed')
        finally:
            c.close()

    def view_available(self):

        if self.con is None:
            return
        try:
            c = self.con.cursor()
            query = 'select * from books where availiable_copies >= 1 order by title asc limit 20'
            c.execute(query)
            records = c.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print('No available books found')

        except Exception:
            print('Operation failed:')

        finally:
            c.close()

    def search_book(self):
        if self.con is None:
            return
        try:
            c=self.con.cursor()
            query='select * from books where book_id=%s or title like %s or author like %s '

    def update_available(self, availiable_copies, book_id):
        if self.con is None:
            return
        try:
            c = self.con.cursor()
            query = 'update books set availiable_copies=%s where book_id=%s'
            data = (availiable_copies, book_id)
            if availiable_copies<=total_copies:
                c.execute(query, data)
                self.con.commit()
            else:
                print('error')
            if c.rowcount > 0:
                print('Updated successfully')
            else:
                print('Update failed or no changes made')

        except Exception as e:
            print('Operation failed:', e)
        finally:
            c.close()

    def delete(self, book_id):
        if self.con is None:
            return
        try:
            c = self.con.cursor()


            query = 'delete from books where book_id=%s'
            data = (book_id,)
            c.execute(query, data)
            self.con.commit()

            if c.rowcount > 0:
                print('Book deleted successfully')
            else:
                print('Book not found')

            query = 'select count(*), sum(available_copies), avg(total_copies) from books'
            c.execute(query)
            record = c.fetchone()
            if record:
                print(record)


        except Exception:
            print('Operation failed:')
        finally:
            c.close()

    def library_summary(self):
        pass

l=library_management()
while True:
    print('welcome to library database')
    print('1.Add Book')
    print('2.View Available Books')
    print('3.Search Book')
    print('4.Update Available Copies')
    print('5.Delete Book')
    print('6.Library Summary')
    print('7.Exit')
    ch=int(input('Enter your Choice : '))

    if ch==1:
        title=input('Enter the title: ')
        author=input('Enter author name: ')
        category=input('Enter the category: ')
        total_copies=int(input('Enter total number of copies: '))
        availiable_copies=int(input('Enter available number copies: '))
        if availiable_copies>=0 and total_copies>=0 and availiable_copies<=total_copies:
            l.add_book(title,author,category,total_copies,availiable_copies)
        else:
            print('invalid data')

    elif ch==2:
        l.view_available()

    elif ch==3:

    elif ch == 5:
    book_id = int(input('Enter book ID: '))
    l.delete(book_id)
    
    elif ch==7:
        exit()

    else:
        print('invalid choice')