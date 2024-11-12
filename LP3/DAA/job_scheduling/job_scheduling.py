class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadlines(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    result = [-1] * max_deadline
    slot_occupied = [False] * max_deadline
    total_profit = 0
    for job in jobs:
        for slot in range(min(job.deadline - 1, max_deadline - 1), -1, -1):
            if not slot_occupied[slot]:
                result[slot] = job.id
                slot_occupied[slot] = True
                total_profit += job.profit
                break

    scheduled_jobs = [job_id for job_id in result if job_id != -1]
    return scheduled_jobs, total_profit


jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15),
]

scheduled_jobs, total_profit = job_sequencing_with_deadlines(jobs)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)
