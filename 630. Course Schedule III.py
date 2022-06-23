def scheduleCourse(self, courses: List[List[int]]) -> int:
        course = []
        for i in sorted(courses, key = lambda x:x[1]):
            course.append(i[0])
            while sum(course) > i[1]:
                course.remove(max(course))
        return len(course)