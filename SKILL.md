# Fashion Affiliate Video

Make affiliate fashion product videos for TikTok and Facebook Reels from
the user's product photo (+ a standard character photo when there is one).
Vertical 9:16, no subtitles, no on-screen text, no voiceover unless the
user asks for one specifically. This skill is modelled on the public repo
`charlotteh618/tao-video-thoi-trang-ai` (Aff Video Tool): the same
prompt templates, the same character-reference workflow, the same
ffmpeg concat/montage scripts — but written for this chat, where clips
are made with Muse's own media video tool instead of being pasted
manually into another chat.

Project folder (templates, scripts, working folders):
`./` — `prompts/`, `scripts/`, `input/`,
`character-reference/`, `output/`.

This skill is NOT the automuse gateway fashion tool
(`automuse/fashion.py`, `python cli.py fashion ...`). That tool logs in
with Muse cookies and generates through an account's gateway session.
This skill uses no cookie login and no internal API: clips are generated
in this chat, saved to `output/`, then joined with ffmpeg. Do not mix
the two paths in one job.

## Hard rules for every video

- Keep the product in the reference photo absolutely unchanged: same
  colour, same cut, same collar, same logo position and shape, same
  pattern and details. Never redesign, recolour, simplify or add details.
  Use stable camera angles and slow movement so details drift less.
- No subtitles, no text in the video, no voiceover or narration, unless
  the user asks for one specifically.
- Vertical 9:16.
- One single character throughout one video. Never change the character
  from scene to scene.
- Everyday, modest, family-appropriate presentation only: natural
  everyday clothing, natural poses, no suggestive posing, framing or
  description. The main genre of the reference repo is everyday
  children's outfit sets; if the user's product is for adults, replace
  the child-model wording in a template with the adult model description
  and keep everything else.
- Never invent a price, a use, an effect or a promotion the user did not
  give and that is not clearly visible in the photo.

## Collect product info first (only what is missing)

Ask only for what is still missing before generating:

- Product name.
- 2–3 highlights confirmed by the user.
- The call to action the user wants to use when posting.
- The product photo. If the photo shows several products or the main
  product is unclear, ask again which one is the main product.
- The character photo (see below).

## Standard character photo for a channel

- When the user sends a character photo, save a copy to
  `character-reference/` as the channel's
  standard character photo.
- Every later video for that channel uses that same standard photo
  together with that video's product photo.
- Generate with `media.generate_video` in this order: character photo
  first, product photo second, then the prompt text. Appearance comes
  from the character photo, clothing comes from the product photo —
  do not blend the two photos into each other.
- Keep the character consistent across videos: same face, hairstyle,
  hair colour, build and manner, only the outfit changes with the
  product and the setting changes with the request.
- If the user has no character photo yet, ask for one before starting a
  channel series, or use a consistent written character description
  temporarily and say clearly that it is temporary until a standard
  photo exists.
- Without a standard photo: generate the first scene, take a clear
  face frame from it as the standard character photo, then use that
  photo with the product photo for every later scene.

## Two main forms (ask which one if the user did not say)

- Studio: product on a clean background, studio light, camera orbits
  and changes angle to show front, side, material detail and stitching.
- Worn by a model: the model wears the product, turns and changes
  angle to show front, side, back and how the product sits while
  moving gently.

## Prompt templates (in `prompts/`)

Fill in the product name, collar, buttons, logo position/shape, fabric
and details from the user's photo — never copy a template's example
details onto a different product.

- `01-store.md` — model, full body, in a children's clothing boutique.
- `02-flatlay.md` — flat-lay product only, no model, top-down.
- `03-home-corner.md` — model in an everyday home corner.
- `04-hanger.md` — hands holding the outfit on a hanger in a shop.
- `05-natural-30s.md` — natural 30 seconds: 3 scenes x 10 seconds.
- `06-cool-montage-20s.md` — cool montage, about 20 seconds: 5 scenes
  cut to 4 seconds each.
- `07-real-and-cool-30s.md` — real yet cool, 30 seconds: 3 scenes x 10
  seconds, confident but not over-acted.

## Random setting and situation

When the user wants a random combination, pick a different setting +
situation combination each time, and do not repeat the combination
just made unless the user asks for it specifically.

- Settings: park, playground, shop stall, bookshop, outdoor café,
  walking street, beach, riverside, garden, market, supermarket,
  shopping mall, schoolyard, library, residential area, high-end
  studio, home corner.
- Situations: walking naturally, light happy running, standing and
  looking around, looking at goods on a shelf, holding an adult's hand
  while walking, playing on a slide or swing, resting on a bench,
  holding a toy and looking around, crossing a small bridge, walking
  along a row of trees.
- Every situation must look natural: eye-level camera, slight handheld
  movement, no stiff posing, no standing in one place too long.
- One setting + one situation makes one scene; every scene in a 30
  second video must be a different combination.

## A set of 3 videos from 1 product

When the user asks for 3 videos from 1 product, make 3 separate videos
that differ in ALL three points: setting, character and presentation.
List the three distinct combinations briefly first, so the user can see
the difference, then make the videos one by one.

- Example settings rotation: park, high-end studio, walking street or
  outdoor café, beach, playground.
- Example characters rotation: different models in hairstyle, height
  and manner, all wearing exactly the outfit in the photo.
- Example presentations rotation: follow-cam while moving, slow studio
  orbit with detail close-ups, confident street style walking toward
  camera.
- Media generation is capped at 6 videos per user message, so a set of
  3 long videos (3 scenes each = 9 clips) cannot be finished in one
  message: do one video per message/round and say which one is next.

## Generate, join, verify, deliver

1. Save the product photo to `input/` and the character photo (if any)
   to `character-reference/`; never commit real product photos to a
   public repo.
2. Pick a template, fill in the real product details, and generate the
   scenes in order (character photo first, product photo second, then
   text). At most 6 videos per user message.
3. Join with the scripts in `scripts/`:
   - 3 x 10s to 30s: `./scripts/concat.sh output/video-30s.mp4 clip1.mp4 clip2.mp4 clip3.mp4`
   - 5 scenes to about 20s montage: `./scripts/montage.sh output/video-20s.mp4 clip1.mp4 clip2.mp4 clip3.mp4 clip4.mp4 clip5.mp4`
   Both scripts normalise clips to 720x1280 at 30 fps before joining,
   so mixed-size clips still join cleanly.
4. Verify before delivering: `ffprobe` duration (about 30s or about
   20s for a montage) and 720x1280. A file that exists is not proof it
   is right — check the numbers.
5. Deliver the video as a sandbox link on its own line with a clear
   file name, plus one short caption suggestion, one call to action,
   and a note that the user adds their own affiliate/cart link in the
   TikTok or Facebook editor when posting (the delivered video itself
   has no subtitles).
6. If the user wants more versions, change one element at a time
   (angle, setting or one highlight) instead of rebuilding everything
   from scratch. At most 6 videos per request round; stop when the
   user has the number they asked for.

## Better results

- A sharp product photo on a white or real background shows the
  product more clearly than a blurry photo or a screenshot with text
  over it.
- If the user has a real video of the product, use the real video as
  the main material and use generated video only for an opening or a
  transition.

## Giao diện web quản lý (Web Studio)

Chạy trên máy của bạn, không đăng nhập, không gửi cookie hay key:

```
python3 web/server.py
python3 web/server.py --port 8080
```

Mở: http://127.0.0.1:8080

Các tab: Tổng quan, Tạo video (tải ảnh, chọn prompt, tạo job, copy
prompt), Nhân vật, Kết quả, Ghép clip (chọn các clip trong output/
theo đúng thứ tự, ghép bằng scripts/concat.sh hoặc montage.sh).
