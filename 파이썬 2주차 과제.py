def Score():

   num = int(input("과제개수: ")) 
   s = 0

   for i in range(1, num+1):
       a = float(input("%d 번째 과제점수: "%i))
       s += a

   exam_m = int(input("중간고사 점수: "))
   exam_f = int(input("기말고사 점수: "))
   
   s /= num
   
   n = s * 0.4
   m = exam_m * 0.3
   f = exam_f * 0.3

   total = n + m + f
   if  100 >= total >= 90:
       grade = "A"
   elif 90 >= total >= 80:
        grade = "B"
   elif 80 >= total >= 70:
        grade = "C"
   elif 70 >= total >= 60:
        grade = "D"
   elif total < 60:
        grade = "F"

   print("\n과제점수 = %.2f ( 반영비율 0.4 )"%n)
   print("중간점수 = %.2f ( 반영비율 0.3 )"%m)
   print("기말점수 = %.2f ( 반영비율 0.3 )"%f)
   print("합계 = %.2f"%(n+m+f))
   print("등급 = %s"%grade)

Score()
