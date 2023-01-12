subjects={'열역학' : 'A+', '재료역학' : 'B+', '생산설계시스템' : 'A'}
student = '김태영'
subject = '생산설계시스템'
print('%s 학생의 %s 과목의 성적은 %s 입니다' % (student, subject, subjects[subject])) # old style
print("{0} 학생의 {1} 과목 성적은 {2} 입니다". format(student,subject,subjects[subject])) # mordern style
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]} 입니다') #f스트링 가장 최근
