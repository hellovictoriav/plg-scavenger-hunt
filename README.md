# PLG Scavenger Hunt

An interactive mobile microsite for a Prospect Lefferts Gardens neighborhood scavenger hunt, styled like a vintage Brooklyn photo archive. Guests move through a welcome "subway map" hub into one full page per challenge, tracking progress on their phone and snapping photos along Flatbush Avenue.

## Live site

**https://hellovictoriav.github.io/plg-scavenger-hunt/**

Share that link or the QR code in [`qr.html`](qr.html) with your guests.

## How guests use it

1. Open the link on a phone (works in any mobile browser).
2. On the welcome page, tap **Begin the Hunt** or pick any stop from **The Line**.
3. Each challenge is its own full page — read it, then use **Prev / Next** to move along.
4. Tap **Mark complete** when finished with a stop.
5. Tap **Add photo** to capture challenge snapshots (saved on their device only).
6. Complete all 8 stops to reach the celebration screen.

## Edit stops or your home address

Open [`index.html`](index.html) and edit the `CONFIG` and `STOPS` arrays near the top of the `<script>` block:

```javascript
const CONFIG = {
  finishAddress: "Your home address, PLG Brooklyn",
  finishMapsQuery: "Prospect Lefferts Gardens Brooklyn NY"
};
```

## Swap cover photos

Add or replace images in [`images/`](images/). See [`images/ATTRIBUTIONS.md`](images/ATTRIBUTIONS.md) for filenames and photo credits.

No code changes needed — the site auto-detects `.jpg`, `.png`, or `.svg` per stop.

## Redeploy after edits

```bash
git add index.html images/
git commit -m "Update scavenger hunt"
git push
```

GitHub Pages updates within ~1 minute.

## Reset (for testing)

Tap **Reset my hunt** at the bottom of the site to clear progress and photos on that device.

## Project files

| File | Purpose |
|------|---------|
| `index.html` | Entire microsite (HTML, CSS, JS) |
| `images/` | Historic cover photos, one per stop |
| `qr.html` | Printable QR code for sharing |
