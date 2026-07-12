# Sattela

A PVP Focused Minecraft Macro Client, The Name Comes From The Witch Of Envy From Rezero

## Safety

The project is open source, if you suspect any kind of malware you can read the source code. Or if you don't trust the .exe in releases; build it from source.

## Implemented Macros

### Mace

- Perl Catch
- Stun Slam

### Etc

- Mending
- Lunge Swap

## Building From Source

```bash
git clone https://github.com/MitoReads/Sattela.git
```

```bash
cd Sattela/
```

```bash
python -m venv venv
```

```bash
./venv/Scripts/activate
```

```bash
pip install -r requirements.txt
```

```bash
pip install pyinstaller
```

```bash
pyinstaller --onefile --console --name Sattela src/main.py
```

Done your .exe is in dist/Sattela.exe

## License

MIT
