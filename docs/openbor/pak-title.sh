#!/bin/sh
# Pull the title screen out of an OpenBOR .pak that sits on an Android device, without copying the pak.
# Usage: pak-title.sh "/storage/emulated/0/Games/openbor/Game.pak" outdir
# Output: outdir/title.gif and outdir/titleb.gif (titleb is the "press start" variant); .png copies when
#         sips (macOS) or ImageMagick convert is installed.
# Needs: adb, python3. Pak layout: the last 4 bytes hold the offset of the file table; each table entry is
#        u32 entry_size, u32 offset, u32 size, then the backslash path, NUL padded to entry_size.
p="$1"; out="$2"; mkdir -p "$out"
sz=$(adb shell "stat -c %s '$p'" </dev/null | tr -d '\r')
tbl=$(adb shell "dd if='$p' bs=1 skip=$((sz-4)) count=4 2>/dev/null | od -An -tu4 | tr -d ' '" </dev/null | tr -d '\r')
adb shell "dd if='$p' bs=1 skip=$tbl count=$((sz-4-tbl)) 2>/dev/null" </dev/null > "$out/table.bin"
python3 - "$out/table.bin" <<'PY' > "$out/pick.txt"
import struct, sys
d = open(sys.argv[1], 'rb').read(); i = 0; ents = {}
while i + 12 <= len(d):
    esz, off, size = struct.unpack_from('<III', d, i)
    if esz < 13 or esz > 512: break
    name = d[i+12:i+esz].split(b'\0')[0].decode('latin1')
    ents[name.lower().replace('\\', '/')] = (off, size); i += esz
for k in ('data/bgs/title.gif', 'data/bgs/titleb.gif'):
    if k in ents: print(k.split('/')[-1][:-4], *ents[k])
PY
while read kind off size; do
  adb shell "dd if='$p' bs=1 skip=$off count=$size 2>/dev/null" </dev/null > "$out/$kind.gif"
  if command -v sips >/dev/null; then sips -s format png "$out/$kind.gif" --out "$out/$kind.png" >/dev/null 2>&1
  elif command -v convert >/dev/null; then convert "$out/$kind.gif[0]" "$out/$kind.png"; fi
  echo "$out/$kind.gif"
done < "$out/pick.txt"
rm -f "$out/table.bin" "$out/pick.txt"
