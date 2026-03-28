class Solution(object):
    def countStudents(self, students, sandwiches):
        st_count0 = students.count(0)
        st_count1 = students.count(1)
        for s in sandwiches:
            if s==1:
                if st_count1 > 0 :
                    st_count1 -=1
                else:
                    break
            else:
                if st_count0 >0:
                    st_count0-=1
                else:
                    break
        return st_count0 + st_count1


