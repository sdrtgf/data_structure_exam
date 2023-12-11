
class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)
    
    
#example of usage of the StudentQueue class:


def main():
    
    student_queue = StudentQueue()

    # Addition of some students to the queue
    student_queue.enqueue("Nicole")
    student_queue.enqueue("Bob")
    student_queue.enqueue("Charlie")
    student_queue.enqueue("Gerald")
    


    # Print the current size of the queue
    print("Queue size:", student_queue.get_size())

    # Simulate serving students from the queue
    served_student = student_queue.dequeue()
    print("Served student:", served_student)

    
    print("Queue size:", student_queue.get_size())

    
    if student_queue.is_empty():
        print("Queue is empty.")
    else:
        print("Queue is not empty.")

if __name__ == "__main__":
    main()























    9





    9