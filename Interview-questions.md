# Docker Interview based questions🚀

These questions cover advanced concepts, real-world scenarios, troubleshooting, and optimization techniques you are likely to encounter in an SRE role.

If this useful, please star this repo :)

---

### **Core Docker Concepts**  
1. **What is Docker, and how does it differ from Virtual Machines?**  
   *Explain containerization vs virtualization.*

2. **Can you explain the Docker architecture? What are the key components?**  
   *Docker Engine, Docker CLI, Docker Daemon, Docker Images, Containers, and Registries.*

3. **What happens when you run `docker run hello-world`? Explain step-by-step.**

4. **What is the difference between `docker run`, `docker start`, and `docker exec`?**

5. **What is the difference between `COPY` and `ADD` in a Dockerfile? When would you use each?**

6. **What are multi-stage builds in Docker? Why are they useful for production deployments?**

---

### **Docker Images and Containers**  
7. **How do you optimize Docker image size? Give practical steps.**  
   *E.g., using lightweight base images like Alpine, multistage builds, removing unnecessary files, minimizing layers, etc.*

8. **How can you debug a container that exits immediately after starting?**

9. **What is the difference between `ENTRYPOINT` and `CMD` in a Dockerfile? Can you override them?**

10. **How do you inspect the environment variables and configuration of a running container?**

11. **What is the role of `docker-compose`? What is the difference between `docker-compose up` and `docker-compose down`?**

12. **What happens if you do not specify a `WORKDIR` in a Dockerfile?**

13. **How do you handle logs for Docker containers? What tools would you use for log aggregation?**

14. **Explain how you would copy a file from a running container to the host machine.**

15. **How can you reduce container startup time for a large application?**

---

### **Networking**  
16. **What are Docker networks, and what are the different types of Docker networks?**  
   *Bridge, host, overlay, and macvlan networks.*

17. **How would you connect two containers running on different hosts?**

18. **Explain the difference between port binding (`-p`) and exposing a port (`EXPOSE`) in Docker.**

19. **How does Docker handle DNS resolution for containers?**

20. **What happens if you use `--network=host` mode? What are the advantages and disadvantages?**

---

### **Storage and Volumes**  
21. **What are Docker volumes? How do they differ from bind mounts?**

22. **How would you persist data from a container?**

23. **What is the difference between named volumes and anonymous volumes?**

24. **How can you back up and restore Docker volumes?**

---

### **Docker Security**  
25. **What are some security best practices you follow while working with Docker?**  
   *E.g., using non-root users, scanning images for vulnerabilities, minimizing image size, etc.*

26. **How can you restrict resource usage for a container (e.g., CPU and memory limits)?**  
   *Use `--cpus`, `--memory`, or cgroups.*

27. **How do you scan a Docker image for security vulnerabilities? What tools do you use?**

28. **What is Docker Content Trust, and how does it help improve image security?**

29. **Explain the concept of a Docker “rootless mode.” Why is it significant?**

30. **What is the purpose of `seccomp`, `AppArmor`, or `SELinux` in Docker security?**

---

### **Troubleshooting and Debugging**  
31. **How do you troubleshoot a container that keeps restarting?**

32. **What steps do you take when you encounter the error `OCI runtime create failed`?**

33. **How do you clean up unused Docker containers, volumes, and networks?**

34. **Explain how to handle zombie processes inside a container.**

35. **How can you check why a container is consuming too much memory or CPU?**

36. **How do you monitor Docker containers in production? What tools or methods do you use?**  
   *Prometheus, Grafana, cAdvisor, ELK stack, etc.*

37. **Explain how you would recover from a corrupted Docker image or container.**

38. **How do you resolve a `Docker daemon not responding` issue?**

---

### **Docker in CI/CD and Kubernetes**  
39. **How do you integrate Docker into CI/CD pipelines? Which tools do you use?**  
   *Jenkins, GitLab CI, GitHub Actions, etc.*

40. **What is a Docker registry? What are the differences between Docker Hub, ECR, and private registries?**

41. **How do you push and pull Docker images from a private registry?**

42. **How do you ensure Docker containers restart automatically on failure?**

43. **What role does Docker play in Kubernetes?**

44. **How do you manage secrets in a Docker container securely?**

---

### **Real-World Scenarios**  
45. **Imagine a containerized app works locally but fails in production. How would you debug it?**

46. **How would you troubleshoot a network connectivity issue between two containers?**

47. **What would you do if Docker images take too long to build during deployment?**

48. **How would you migrate containers running on a Docker Engine to Kubernetes?**

49. **How do you ensure zero downtime when deploying updates to a containerized application?**

50. **You have a container running out of memory and crashing. What tools and steps would you use to analyze and resolve it?**

---

### **Bonus Situational Questions**  
51. **If your Docker image builds are too large, what actions would you take to improve efficiency?**

52. **You notice a resource-intensive container affecting host performance. How would you limit its resource usage immediately?**

53. **A containerized application throws intermittent errors but works fine most of the time. What steps would you take to investigate this?**

54. **What would you do if you accidentally deleted a Docker volume containing important data?**

55. **A team member created a Dockerfile, but the container keeps crashing. How would you perform a code review to find the issue?**

---

### **Tools and Utilities**  
- **What tools do you use for container monitoring and health checks?**  
- **How do you automate container cleanup in production?**  
- **Which tools do you prefer for Docker image vulnerability scanning?**

---

### **Final Notes for Preparation**  
To ace these questions as an **SRE**, make sure you can:  
1. Explain concepts clearly.  
2. Use real-world examples or scenarios you've handled.  
3. Understand how Docker integrates with tools like Kubernetes, CI/CD, and monitoring systems.  
4. Troubleshoot and optimize effectively.  


#devops 
