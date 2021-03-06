VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "����1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Function GetResponse(full_url) As String
    '''�������� url � ��������� ������'''

    
    '�������� ���������� ��� �������� ��������
    Dim xml_obj As MSXML2.XMLHTTP60
    Set xml_obj = New MSXML2.XMLHTTP60
    
    MsgBox (full_url)
    '�������� �������
    xml_obj.Open bstrMethod:="GET", bstrURL:=full_url
    
    '�������� �������
    xml_obj.send
    
    '����������� ����������� ������
    GetResponse = xml_obj.responseText
    
End Function

Function MakeRequest() As String
    '''��������, �������� ������� � ��������� ������'''
    

    '�������� IP �������
    Dim server_ip As String
    server_ip = "127.0.0.1"
    
    '�������� �����
    Dim port As String
    port = "5000"
    
    '�������� ���������� ��� ������ �������
    Dim response As String
    
    '�������� ���������� ��� �������������� �����
    Dim predicted_score As String
        
    '�������� ���������� ��� excel
    Dim sh As Worksheet
    Dim rw As Range
    Dim RowCount As Integer
    RowCount = 0

    Set sh = ActiveSheet
    
    '�������� ����� ��� ������������ �� �������
    For Each rw In sh.Rows
    
        '�������� ���������� �� ������������ �� �������
        If sh.Cells(rw.row, 1).Value = "" Then
            Exit For
        Else
            RowCount = RowCount + 1
          
            '������������ ���������
            If sh.Cells(rw.row, 5).Value = "" Then
                '��������� �������� ������ �� ����������
                team_A = Replace(sh.Cells(rw.row, 1).Value, " ", "_")
                team_B = Replace(sh.Cells(rw.row, 2).Value, " ", "_")
                
                '�������� url ��� �������� ������� �� ������
                url_for_predicting_score = "http://" + server_ip + ":" + port + "/api/v1.0/predict" + "?" + "team_A=" + team_A + "&" + "team_B=" + team_B
                
                '������������ ���������� �����
                predicted_score = GetResponse(url_for_predicting_score)
                
                '������ ���������� ����� � ��������������� ������
                sh.Cells(rw.row, 5).Value = predicted_score
                
                '�������� url ��� �������� ������� �� ������
                url_for_predicting_score = "http://" + server_ip + ":" + port + "/api/v1.0/calculate_advance" + "?" + "predicted_score=" + predicted_score
                
                '������������ ����
                predicted_advance = GetResponse(url_for_predicting_score)
                
                '������ ���� � ��������������� ������
                sh.Cells(rw.row, 6).Value = predicted_advance
                
            Else
                'do nothing
            End If
            
        End If
    
    Next rw
    
End Function

Private Sub RequestButton_Click()
    '''������� �� ������'''
    
    
    '����� �������, ������� ������ ������
    MakeRequest
    
End Sub
