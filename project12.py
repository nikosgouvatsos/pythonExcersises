print ��������� ���� ���� �������� ������� �� ���� ������ ��� ������ ��� �� �������� �� ��������� ��� �� ���������� �������
print ������� ���� ���� ��� �� ����� ������� �� ������ �� ����� �������� 180 ������

a = input('�������� ���� ������ ��� ������ ������ : ')   # ������� ��� �� ������ �� ������� ��� ������ ��� ��������
b = input('�������� ���� ������ ��� �������� ������ : ') 
c =input('�������� ���� ������ ��� ������ ������ : ') 



                  
 def  Triangle(a,b,c):                                                                                                                       
   if(a+b+c==180 & ((a|b|c)>=90): 
        result = 2                                # �� �������� ��������� ��� �� �������� �� ������������      
else if (a+b+c==180 & ((a|b|c)==90) ): # ��� ����� �� ��� �� �������� ��� ������ ����� ��� �� 180   
        result = 3                                           # ���� �� ����� ������� ��� ��� ��� ��� ��� ������ ��� 
 else   if (a+b+c==180):                             # ����� ������ � ����.
         result = 1                                          # ��� �� �������� ��� ������ ������� �� 
 else:                                                          # ������������� ���� �� ��� ����� ����� ������ 
       result = -1                                            # � ����� ���� ����� �������� �������
    
return result


print(Triangle(a,b,c))   # ����������� �� ���������� ��� ������  