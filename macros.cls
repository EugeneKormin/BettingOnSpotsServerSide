VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Лист1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Function GetResponse(full_url) As String
    '''Отправка url и получение ответа'''

    
    'Создание переменных для создания запросов
    Dim xml_obj As MSXML2.XMLHTTP60
    Set xml_obj = New MSXML2.XMLHTTP60
    
    MsgBox (full_url)
    'Создание запроса
    xml_obj.Open bstrMethod:="GET", bstrURL:=full_url
    
    'Отправка запроса
    xml_obj.send
    
    'Возвращение полученного ответа
    GetResponse = xml_obj.responseText
    
End Function

Function MakeRequest() As String
    '''Создание, отправка запроса и получения ответа'''
    

    'Указание IP сервера
    Dim server_ip As String
    server_ip = "127.0.0.1"
    
    'Указание порта
    Dim port As String
    port = "5000"
    
    'Создание переменной для ответа сервера
    Dim response As String
    
    'Создание переменной для предсказанного счета
    Dim predicted_score As String
        
    'Создание переменных для excel
    Dim sh As Worksheet
    Dim rw As Range
    Dim RowCount As Integer
    RowCount = 0

    Set sh = ActiveSheet
    
    'Создание цикла для итерирования по строкам
    For Each rw In sh.Rows
    
        'Проверка необходимо ли предсказание по строкам
        If sh.Cells(rw.row, 1).Value = "" Then
            Exit For
        Else
            RowCount = RowCount + 1
          
            'Предсказание построчно
            If sh.Cells(rw.row, 5).Value = "" Then
                'Получение названий команд из аргументов
                team_A = Replace(sh.Cells(rw.row, 1).Value, " ", "_")
                team_B = Replace(sh.Cells(rw.row, 2).Value, " ", "_")
                
                'Создание url для отправки запроса на сервер
                url_for_predicting_score = "http://" + server_ip + ":" + port + "/api/v1.0/predict" + "?" + "team_A=" + team_A + "&" + "team_B=" + team_B
                
                'Предсказание ожидаемого счёта
                predicted_score = GetResponse(url_for_predicting_score)
                
                'Запись ожидаемого счёта в соответствующую ячейку
                sh.Cells(rw.row, 5).Value = predicted_score
                
                'Создание url для отправки запроса на сервер
                url_for_predicting_score = "http://" + server_ip + ":" + port + "/api/v1.0/calculate_advance" + "?" + "predicted_score=" + predicted_score
                
                'Предсказание форы
                predicted_advance = GetResponse(url_for_predicting_score)
                
                'Запись форы в соответствующую ячейку
                sh.Cells(rw.row, 6).Value = predicted_advance
                
            Else
                'do nothing
            End If
            
        End If
    
    Next rw
    
End Function

Private Sub RequestButton_Click()
    '''Нажатие на кнопку'''
    
    
    'Вызов функции, которая создаёт запрос
    MakeRequest
    
End Sub
