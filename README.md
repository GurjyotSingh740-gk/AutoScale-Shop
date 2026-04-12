# AutoScale Shop 🛒

**MCA 4th Semester Mini Project — CICD + Kubernetes for DevOps**

A full-stack event-driven order processing system demonstrating:

- CI/CD Pipeline with GitHub Actions + Jenkins
- Docker containerization
- Kubernetes deployment with HPA auto-scaling
- Prometheus + Grafana monitoring

## Services

| Service           | Port | Access               |
| ----------------- | ---- | -------------------- |
| Order API         | 5000 | NodePort:30001       |
| Inventory Service | 5001 | ClusterIP (internal) |

## Flow: Code Push → CI/CD → Docker Hub → Minikube → HPA → Grafana
