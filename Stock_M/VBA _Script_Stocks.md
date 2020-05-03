Sub stock_summary():

    '-------------------------------------
    'Looping through all sheets in file
    '--------------------------------------
    'Creating a variable to hold file name
    For Each ws In Worksheets
        ws.Range("J1") = "Ticker"
        ws.Range("K1") = "Yearly Change"
        ws.Range("L1") = "Percent Change"
        ws.Range("M1") = "Total Stock Volume"
        
        'Create a variable to hold summary table row
        Dim Ticker As String
        Dim Summary_Table_Row As Integer
        Dim OpenNum As Long
        Dim CloseNum As Double
        Dim YearlyChange As Double
        Dim PercentChange As Double
        Dim TotalStock As Double
        
        
        Start = 2
        Summary_Table_Row = 2
        'Creating a variable to hold last row and last column
        LastRow = Cells(Rows.Count, 1).End(xlUp).Row
        
        
         For i = Start To LastRow
    
             Ticker = ws.Cells(i, 1)
             OpenNum = ws.Cells(Start, 3)
             CloseNum = ws.Cells(i, 6)
             StockVolume = ws.Cells(i, 7)
             
            If ws.Cells(i + 1, 1) = ws.Cells(i, 1) Then
                TotalStock = TotalStock + StockVolume
                   
            Else
                'if the ticker changes
                TotalStock = TotalStock + StockVolume
            
                'To calculate the Yearly Change
                YearlyChange = CloseNum - OpenNum
        
                    'Set Percent Change
                    If OpenNum <> 0 Then
                    'Source: https://www.youtube.com/watch?v=XCJkd3NFpQw
                     
                    PercentChange = Round((CLng(YearlyChange) / OpenNum * 100), 2)
                    'Source: https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/overflow-error-6
                    End If
             
             'This starts the next ticker
             Start = i + 1
             
             'Print results to Summary Table
             ws.Range("J" & Summary_Table_Row) = Ticker
             ws.Range("K" & Summary_Table_Row) = Round(YearlyChange, 2)
             ws.Range("L" & Summary_Table_Row) = "%" & PercentChange
             ws.Range("M" & Summary_Table_Row) = TotalStock
             
             'Reset Total Stock and Total Open
             TotalStock = 0
             YearlyChange = 0
             'Add one to the Summary Table Row
             Summary_Table_Row = Summary_Table_Row + 1
             
        End If
         
    Next i
        
Next ws
    

End Sub

Sub ColorFormat()
    Dim ws As Worksheet
    'Creating a variable to hold file name
    For Each ws In Worksheets
    ws.Activate
    'Color code Yearly Change Column'
    '----------------------------------------------------
    Summary_Table_LastRow = Cells(Rows.Count, 10).End(xlUp).Row
    For i = 2 To Summary_Table_LastRow
           
            If Cells(i, 11) < 0 Then
                Cells(i, 11).Interior.ColorIndex = 3 'Red
                
            ElseIf Cells(i, 11) >= 0 Then
                Cells(i, 11).Interior.ColorIndex = 4 'Green
            End If
        
        Next i
    
    Next ws
    

End Sub

