# ody-shbayeh 1201462
# abd elrahman abed 1193191


from genes import *
import random
import numpy as np

def readfile():
    filedata = {}
    try:
        with open("jobs.txt") as file:
            for line in file:
                parts = line.strip().split(",")
                job_number, machine_number, machine_time = map(int, parts)
                if job_number not in filedata:
                    filedata[job_number] = []
                filedata[job_number].append(genes(job_number, machine_number, machine_time))
    except FileNotFoundError:
        print("The input file doesn't exist :(")
    
    return filedata

def generate_random_chromosome(jobs_data):
    chromosome = []
    job_task_indices = {job_number: 0 for job_number in jobs_data}
    job_numbers = list(jobs_data.keys())

    while any(job_task_indices[job_number] < len(jobs_data[job_number]) for job_number in job_numbers):
        random.shuffle(job_numbers)
        for job_number in job_numbers:
            job_tasks = jobs_data[job_number]
            task_index = job_task_indices[job_number]
            if task_index < len(job_tasks):
                task = job_tasks[task_index]
                chromosome.append(task)
                job_task_indices[job_number] += 1

    return chromosome

def generate_chromosomes(jobs_data, num_chromosomes):
    chromosomes = []
    for _ in range(num_chromosomes):
        chromosome = generate_random_chromosome(jobs_data)
        chromosomes.append(chromosome)
        print(f"Chromosome : {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in chromosome]}")
    return chromosomes

def execute_chromosomes(chromosomes, flag=True):
    chromosomes_waiting_time = []

    if flag:
        print(f"\n=================================================== Waiting time for the chromosomes ==================================================\n")

    for i, chromosome in enumerate(chromosomes):
        waiting_time = 0
        current_machine = {}
        
        for gene in chromosome:
            job, machine, time = gene.job_number, gene.machine_number, gene.machine_time
            if machine not in current_machine:
                current_machine[machine] = 0
            waiting_time += max(current_machine[machine] - time, 0)
            current_machine[machine] = max(current_machine[machine], time) + time
        if flag:
            print(f"Chromosome {i+1}: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in chromosome]} - Waiting Time: {waiting_time}")
        chromosomes_waiting_time.append((chromosome, waiting_time))

    chromosomes_waiting_time.sort(key=lambda x: x[1])

    weights = [1 / wt for _, wt in chromosomes_waiting_time]
    total_weight = sum(weights)
    probabilities = [w / total_weight for w in weights]

    num_to_select = min(2, len(chromosomes_waiting_time))
    selected_indices = np.random.choice(len(chromosomes_waiting_time), size=num_to_select, replace=False, p=probabilities)
    parents = [chromosomes_waiting_time[i][0] for i in selected_indices]
    
    if flag:
        print(f"\n=================================================== Sorted chromosomes by waiting time ==================================================\n")
        for chromosome, waiting_time in chromosomes_waiting_time:
            print(f"Chromosome: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in chromosome]} - Waiting Time: {waiting_time}")
        print(f"\n======================================================== The selected parents ========================================================\n")
        for i, parent in enumerate(parents):
            parent_waiting_time = chromosomes_waiting_time[selected_indices[i]][1]
            print(f"Parent {i+1}: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in parent]} - Waiting Time: {parent_waiting_time}")
    if not flag:
        print(f"the performance of the passed chromosome is: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in chromosomes[0]]} - Waiting Time: {chromosomes_waiting_time[0][1]}") 
    return parents, [chromosomes_waiting_time[i][1] for i in selected_indices]

def mutation(childs):
    child_index = random.randint(0, len(childs) - 1)
    child = childs[child_index]
    
    print("========================================== Selected child for mutation ==========================================")
    print(f"Selected child: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in child]}\n")

    gene1, gene2 = random.sample(range(len(child)), 2)
    print(f"The selected genes to swap are: gene1: {gene1} and gene2: {gene2}")

    child[gene1], child[gene2] = child[gene2], child[gene1]
    print("================================================= Mutated child =================================================")
    print(f"Mutated child: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in child]}\n")
    
    return child

def cross_over(parents):
    childs = []
    parent1 = parents[0]
    parent2 = parents[1]

    cross_point = random.randint(1, len(parent1) - 1)
    print("===============================================================================================================")
    print(f"\nThe cross_point is: {cross_point}\n")
    print("===============================================================================================================")

    child1 = parent1[:cross_point] + parent2[cross_point:]
    child2 = parent2[:cross_point] + parent1[cross_point:]

    childs.append(child1)
    childs.append(child2)

    print(f"Child 1: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in child1]}")
    print(f"Child 2: {[(gene.job_number, gene.machine_number, gene.machine_time) for gene in child2]}")
    
    return childs

def new_generations(chromosomes, parents, num_chromosomes, mutation_rate=0.1):
    new_generation = list(chromosomes)
    
    removed_indices = random.sample(range(len(new_generation)), 2)
    removed_chromosomes = [new_generation.pop(index) for index in sorted(removed_indices, reverse=True)]
    
    while len(new_generation) < int(num_chromosomes):
        parent1, parent2 = random.sample(parents, 2)
        children = cross_over([parent1, parent2])
        for child in children:
            if random.random() < mutation_rate:
                child = mutation([child])
            if len(new_generation) >= int(num_chromosomes):
                break
            new_generation.append(child)
    print(f"\n\nchilds have been added seccsfully")        
    return new_generation


def main():

    num_chromosomes = input("Please enter the number of chromosomes for the initial generation: ")
    num_generations = input("Please enter the number of generations to generate: ")

    filedata = readfile()
    chromosomes = generate_chromosomes(filedata, int(num_chromosomes))

    for generation in range(int(num_generations)):
        print(f"\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Generation : {generation + 1}\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n\n")
        parents, _ = execute_chromosomes(chromosomes, True)
        chromosomes = new_generations(chromosomes,parents, int(num_chromosomes), 0.1)

if __name__ == "__main__":
    main()