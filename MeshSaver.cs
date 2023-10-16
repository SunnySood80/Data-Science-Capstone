using UnityEngine;
using UnityEngine.XR.ARFoundation;
using System.IO;
using System.Collections.Generic;

public class MeshSaver : MonoBehaviour
{
    public ARMeshManager meshManager;
    public string filename = "MyScan.ply";  // Ensure this is set to .ply in Unity's Inspector.
    public string savedMeshPath;  // This will store the path after the mesh is saved.

    public void SaveCurrentScan()
    {
        Debug.Log("Attempting to save mesh...");

        if (meshManager == null)
        {
            Debug.LogError("Mesh Manager not assigned!");
            return;
        }

        var allMeshes = meshManager.meshes;
        Debug.Log("Number of meshes detected: " + allMeshes.Count);

        if (allMeshes.Count == 0)
        {
            Debug.LogError("No meshes found to save.");
            return;
        }

        // Combine all meshes into one
        CombineInstance[] combine = new CombineInstance[allMeshes.Count];
        int i = 0;
        foreach (var mesh in allMeshes)
        {
            Mesh individualMesh = mesh.GetComponent<MeshFilter>().sharedMesh;
            combine[i].mesh = individualMesh;
            combine[i].transform = mesh.transform.localToWorldMatrix;
            i++;
        }

        Mesh mergedMesh = new Mesh();
        mergedMesh.CombineMeshes(combine);

        string fullPath = Path.Combine(Application.persistentDataPath, "DebugScan.ply");  // Hardcoding for debugging purposes.
        Debug.Log("Attempting to write to file: " + fullPath);

        try
        {
            PlyExporter.SaveToFile(fullPath, mergedMesh);
            Debug.Log("File successfully written to: " + fullPath);
            savedMeshPath = fullPath;  // Store the path in the variable.
        }
        catch (System.Exception e)
        {
            Debug.LogError("Error saving file: " + e.Message);
        }
    }
}
