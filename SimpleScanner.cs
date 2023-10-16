using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.UI;

public class SimpleScanner : MonoBehaviour
{
    public ARMeshManager meshManager;
    public Button toggleButton;  // Reference to the button in Unity
    public Sprite defaultButtonSprite;  // Reference to the default button sprite (white circular)
    public Sprite recordingButtonSprite;  // Reference to the recording button sprite (green outline)

    private bool isScanning = false;

    // This ensures the ARMeshManager is disabled when the scene starts
    private void Start()
    {
        if (meshManager != null)
        {
            meshManager.enabled = false;
        }
        else
        {
            Debug.LogError("ARMeshManager is not assigned in the SimpleScanner script!");
        }
    }

    // This method toggles scanning and changes the button's appearance
    public void ToggleScanning()
    {
        if (meshManager == null)
        {
            Debug.LogError("ARMeshManager is not assigned in the SimpleScanner script!");
            return;
        }

        if (isScanning)
        {
            meshManager.enabled = false;
            toggleButton.image.sprite = defaultButtonSprite;
            isScanning = false;
        }
        else
        {
            meshManager.enabled = true;
            toggleButton.image.sprite = recordingButtonSprite;
            isScanning = true;
        }
    }
}
