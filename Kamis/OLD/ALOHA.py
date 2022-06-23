import openpyxl
  
  wb = openpyxl.load_workbook('ALOHA.xlsx')	# ファイルを開く
  ws = wb['Sheet']		# ワークシートを開く
  # くりかえし処理
  for i in range(5):
      for j in range(6):
          ws.cell(row=i+1, column=j+1).value = 'ALOHA')
  
  # ファイルを保存する
  wb.save('ALOHA.xlsx')