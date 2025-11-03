# Prueba DevSecOps 🛠️

Pipeline básico CI/CD + GitOps con:
- **GitHub Actions**
- **Docker**
- **Helm**
- **Kubernetes / OpenShift**
- **ArgoCD**

## Flujo general

1. Se ejecuta automáticamente con cada `git push` en `main`.
2. Construye y sube la imagen Docker a Docker Hub.
3. Actualiza el archivo `values.yaml` con el nuevo tag (`commit SHA`).
4. ArgoCD sincroniza los cambios y despliega la nueva versión en el clúster.

## Estructura

```
app.py                # App Flask
Dockerfile            # Imagen Docker
helm/                 # Chart Helm
.github/workflows/    # Pipeline CI/CD
```
