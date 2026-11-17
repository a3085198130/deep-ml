def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = initial_centroids.copy()
    dim = len(points[0])

    for p in range(max_iterations):
        # 初始化k个簇
        clusters=[[] for _ in range(k)]
        for p in points:
            dists=[]
            for c in centroids:
                s=0.0
                for pi,ci in zip(p,c):
                    s+=(pi-ci)**2
                dists.append(s)
            nearest_idx=dists.index(min(dists))
            clusters[nearest_idx].append(p)
        # 更新质心
        new_centroids=[]
        for cluster in clusters:
            avg=[0.0]*dim
            cnt=len(cluster)
            for p in cluster:
                for d_idx in range(dim):
                    avg[d_idx]+=p[d_idx]
            avg=[x/cnt for x in avg]
            avg_rounded=[round(x,4) for x in avg]
            new_centroids.append(tuple(avg_rounded))
        centroids=new_centroids
    return centroids