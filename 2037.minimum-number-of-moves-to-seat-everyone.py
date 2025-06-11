class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        time = 0
        for i in range(len(students)):
            min_student = min(students)
            min_seat = min(seats)
            time += abs(min_student-min_seat)
            students.remove(min_student)
            seats.remove(min_seat)
        return time
