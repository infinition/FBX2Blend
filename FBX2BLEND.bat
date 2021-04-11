cd "C:\Users\Bjornulf\Desktop\fbxspace\FBX2BLEND\"
for %%f in (*fbx) do ("C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" "C:\Users\Bjornulf\Desktop\fbxspace\FBX2BLEND\%%~nf.blend" -P FBX2BLEND.py)
