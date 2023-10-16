using UnityEngine;
using System.IO;
using System.Text;

public static class PlyExporter
{
    public static string MeshToPlyString(Mesh mesh)
    {
        StringBuilder sb = new StringBuilder();

        Color[] colors = mesh.colors;

        sb.AppendLine("ply");
        sb.AppendLine("format ascii 1.0");
        sb.AppendLine($"element vertex {mesh.vertexCount}");
        sb.AppendLine("property float x");
        sb.AppendLine("property float y");
        sb.AppendLine("property float z");
        sb.AppendLine("property uchar red");
        sb.AppendLine("property uchar green");
        sb.AppendLine("property uchar blue");
        sb.AppendLine($"element face {mesh.triangles.Length / 3}");
        sb.AppendLine("property list uchar int vertex_index");
        sb.AppendLine("end_header");

        for (int i = 0; i < mesh.vertexCount; i++)
        {
            Vector3 vertex = mesh.vertices[i];
            Color color = colors.Length > i ? colors[i] : Color.white; // Use white if no color is provided
            sb.AppendLine($"{vertex.x} {vertex.y} {vertex.z} {(int)(color.r * 255)} {(int)(color.g * 255)} {(int)(color.b * 255)}");
        }

        int[] triangles = mesh.triangles;
        for (int i = 0; i < triangles.Length; i += 3)
        {
            sb.AppendLine($"3 {triangles[i]} {triangles[i + 1]} {triangles[i + 2]}");
        }

        return sb.ToString();
    }

    public static void SaveToFile(string filename, Mesh mesh)
    {
        using (StreamWriter sw = new StreamWriter(filename))
        {
            sw.Write(MeshToPlyString(mesh));
        }
    }
}
