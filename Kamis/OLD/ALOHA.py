import openpyxl
  
  wb = openpyxl.load_workbook('ALOHA.xlsx')	# �t�@�C�����J��
  ws = wb['Sheet']		# ���[�N�V�[�g���J��
  # ���肩��������
  for i in range(5):
      for j in range(6):
          ws.cell(row=i+1, column=j+1).value = 'ALOHA')
  
  # �t�@�C����ۑ�����
  wb.save('ALOHA.xlsx')