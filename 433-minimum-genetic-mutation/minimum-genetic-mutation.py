from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = {startGene}
        genes = "ACGT"

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            gene = list(gene)

            for i in range(8):
                original = gene[i]

                for ch in genes:
                    if ch == original:
                        continue

                    gene[i] = ch
                    new_gene = "".join(gene)

                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        q.append((new_gene, steps + 1))

                gene[i] = original

        return -1