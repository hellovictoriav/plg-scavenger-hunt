# PLG Scavenger Hunt

An interactive mobile microsite for a Prospect Lefferts Gardens neighborhood scavenger hunt. Guests flip cards to reveal challenges, track progress on their phone, and snap photos along Flatbush Avenue.

## Live site

**https://withgraphite.github.io/vv-test-repo/**

Share that link or the QR code in [`qr.html`](qr.html) with your guests.

## How guests use it

1. Open the link on a phone (works in any mobile browser).
2. Tap a card to **flip** it and reveal the challenge.
3. Tap **Mark complete** when finished with a stop.
4. Tap **Add photo** to capture challenge snapshots (saved on their device only).
5. Complete all 8 stops to trigger the celebration screen.

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
| `images/` | Cover photos for card fronts |
| `qr.html` | Printable QR code for sharing |
