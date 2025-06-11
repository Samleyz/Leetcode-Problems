class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        people = []
        i = 0
        c = 1
        while True:
            if i == num_people:
                i = 0
            if candies - c <=0:
                if len(people) != num_people:
                    people.append(candies)
                    break
                people[i] +=candies
                break
            if len(people) == num_people:
                people[i] +=c

            else:
                people.append(c)
            candies -= c
            c+=1
            i+=1
       
        if len(people) < num_people:
            for i in range( num_people - len(people)):
                people.append(0)


        return people
