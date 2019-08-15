import pyodbc

x = 0
while True:
    client_number = input(
            'Введите клиентский номер заказа\nили нажмите q для выхода --> '
            )
    if client_number == 'q':
        break

    conn = pyodbc.connect(
            '''DRIVER={SQL Server};SERVER=VILKOV-TEST\\SQL2008T;
                DATABASE=MAIN;Trusted_Connection=Yes;'''
            )

    cursor = conn.cursor()
    sql_get = '''SELECT oo.OrderNumber, oo.WaybillNumber
            FROM Ord_Orders oo (NOLOCK)
            where oo.ClientOrderNumber = '{}'
            ORDER BY oo.OrderNumber'''.format(client_number)
    cursor.execute(sql_get)
    gerrits = cursor.fetchall()
    
    for i in gerrits:
        x += 1
        for b in i:
            print(b)
        print('*' * 12)
    if x == 0:
        print('\nЗаказы не найдены' + '\n' )
    elif x == 1:
        print('\nНайден ' + str(x) + ' заказ.' + '\n' )
    elif x % 10 >= 2 and x % 10 <= 4:
        print('\nНайдено ' + str(x) + ' заказа' + '\n' )
    elif x%10==1:
        print('\nНайден ' + str(x) + ' заказ.' + '\n' )
    elif x % 100 >= 10 and x % 100 <= 20:
        print('\nНайдено ' + str(x) + ' заказов' + '\n' )
    else:
        print('\nНайдено ' + str(x) + ' заказов' + '\n' )
    x = 0
    conn.close()

    
