sentence = raw_input('Enter your input:') #������� ��� ��� ������ �� ������� �� �������   
#��� ������������ ��� NSFW ������� �� ��� ���������� ��� ����� �� �����

t = input('Insert the time you want to be completed: ')  # ������ ��� ��� ������ �� ��� ����� ���     #����� ���� ����� ����� �� ������������ �� ��������

def  ChessBoard(t,sentence): 
   d = sentence.count('N,S,F,W') # �� �� ������� ��� ���������� count ������� ��� ������                      #��� N S F W ��� �������� ��� ������� �������.
 if : 
          d == t    # ������� �������� ��� ��� �� �������� ������� �� ������������ ��� ������� 
  result  = True    #����� � ��������� ���������� True ����������� ���������� false      
    else:
        result = False

    return result

print(ChessBoard(t,sentence)) # ����������� �� ���������� ��� ������  