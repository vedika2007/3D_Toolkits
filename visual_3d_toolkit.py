import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ---------- 3D Line Plot ----------
def plot_3d_line(x, y, z, title="3D Line Plot", xlabel="X", ylabel="Y", zlabel="Z"):
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color="blue", lw=2)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()

# ---------- 3D Scatter Plot ----------
def plot_3d_scatter(x, y, z, title="3D Scatter Plot", xlabel="X", ylabel="Y", zlabel="Z", color="red"):
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=color, s=50, depthshade=True)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()

# ---------- 3D Surface Plot ----------
def plot_3d_surface(X, Y, Z, title="3D Surface Plot", xlabel="X", ylabel="Y", zlabel="Z", cmap="viridis"):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='k', alpha=0.8)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()

# ---------- 3D Wireframe Plot ----------
def plot_3d_wireframe(X, Y, Z, title="3D Wireframe Plot", xlabel="X", ylabel="Y", zlabel="Z", color="green"):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(X, Y, Z, color=color, linewidth=1)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()

# ---------- Example Usage ----------
if __name__ == "__main__":
    # Sample data
    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t

    plot_3d_line(x, y, z)
    plot_3d_scatter(x, y, z)

    X = np.linspace(-5, 5, 50)
    Y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    plot_3d_surface(X, Y, Z)
    plot_3d_wireframe(X, Y, Z)
