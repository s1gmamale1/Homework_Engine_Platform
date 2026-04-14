$base = "C:\Users\DaddysHere\Documents\Sigma_Edu_3000\standards\subject-family\grades"
$families = @("aniq-fanlar","til-fanlari","tabiat-fanlari","ijtimoiy-fanlari","tarbiya-sanat")
$langs = @("uz","ru")

for ($g = 5; $g -le 11; $g++) {
  foreach ($l in $langs) {
    foreach ($f in $families) {
      $dir = "$base\$g\$l\$f"
      New-Item -ItemType Directory -Force -Path $dir | Out-Null
      [System.IO.File]::WriteAllText("$dir\.gitkeep", "")
      Write-Host "Created $dir"
    }
  }
}
Write-Host "`nTotal .gitkeep files:"
(Get-ChildItem "$base" -Recurse -Filter ".gitkeep").Count
