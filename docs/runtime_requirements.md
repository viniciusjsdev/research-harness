# Runtime Requirements

This project can be developed without Hermes Agent, but Hermes is the intended
runtime/orchestrator for the full research workflow.

## Local Harness Requirements

Minimum requirements for the helper scripts:

- Python 3.10 or newer
- Internet access for academic search APIs
- `pip install -r requirements.txt`

Optional environment variables for academic providers can be copied from
`.env.example` into a local `.env` file. Do not commit real tokens or API keys.

## Hermes Agent On Drive D

Keep Hermes runtime files outside this repository. On Windows, use `D:\Hermes`
so code, config, sessions, logs, downloaded tools, and auth state do not land on
the default user profile path on drive C.

The important variables are:

- `HERMES_HOME`: Hermes data directory, including config, sessions, logs, and
  local runtime state.
- `HERMES_INSTALL_DIR`: Hermes code checkout/install directory.

Recommended layout:

```text
D:\Hermes\
  .hermes\
  hermes-agent\
  install.ps1
```

### Native Windows PowerShell

Native Windows support is currently marked as early beta by Hermes. Run this in
PowerShell:

```powershell
$HermesRoot = "D:\Hermes"
$HermesHome = "$HermesRoot\.hermes"
$HermesInstall = "$HermesRoot\hermes-agent"

New-Item -ItemType Directory -Force -Path $HermesRoot, $HermesHome | Out-Null

[Environment]::SetEnvironmentVariable("HERMES_HOME", $HermesHome, "User")
[Environment]::SetEnvironmentVariable("HERMES_INSTALL_DIR", $HermesInstall, "User")

$env:HERMES_HOME = $HermesHome
$env:HERMES_INSTALL_DIR = $HermesInstall

Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1" `
  -OutFile "$HermesRoot\install.ps1"

powershell -ExecutionPolicy Bypass -File "$HermesRoot\install.ps1" `
  -HermesHome $HermesHome `
  -InstallDir $HermesInstall
```

Close and reopen PowerShell, then verify:

```powershell
hermes setup
hermes doctor
```

### WSL2 Install Using Drive D

WSL2 is the more battle-tested Windows path according to the Hermes
installation docs. Run this inside the WSL2 shell:

```bash
mkdir -p /mnt/d/Hermes/.hermes /mnt/d/Hermes/hermes-agent

export HERMES_HOME=/mnt/d/Hermes/.hermes
export HERMES_INSTALL_DIR=/mnt/d/Hermes/hermes-agent

echo 'export HERMES_HOME=/mnt/d/Hermes/.hermes' >> ~/.bashrc
echo 'export HERMES_INSTALL_DIR=/mnt/d/Hermes/hermes-agent' >> ~/.bashrc

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh \
  | bash -s -- --hermes-home "$HERMES_HOME" --dir "$HERMES_INSTALL_DIR"

source ~/.bashrc
hermes setup
hermes doctor
```

## Running Hermes With This Harness

After Hermes is installed and authenticated, run it from the repository root:

```powershell
cd D:\Projetos\Github_ViniciusJ\research-harness
hermes
```

Hermes should read `AGENTS.md`, use the prompts and schemas in this repository,
and keep runtime state in `HERMES_HOME`, not in the repository.

## References

- Hermes install docs:
  `https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/installation.md`
- Windows installer:
  `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1`
- Linux/WSL installer:
  `https://github.com/NousResearch/hermes-agent/blob/main/scripts/install.sh`
