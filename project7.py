x = input('Choose a number: ')   # ������� ��� �� ������ �� ������� ��� ������ ��� ��������

def  ThisNum(x): #� ��������� ���� �� ������ ��� ������ ��� ����� � �������
    if ((x**(1/2)) % 2 == 0) : #� ��������� ������� ��� �� �� ������� ��� 
        result = True                 # modulo ��� � ���� ��� ������� ����� �������� � ���     
    else:
        result = False

    return result

print(ThisNum(x)) # ����������� �� ���������� ��� ������  
