init 1 python:

    config.has_voice = True

    try:
        renpy.music.get_channel("rvp_voice")
    except Exception:
        renpy.music.register_channel(
            "rvp_voice",
            mixer="sfx",
            loop=False,
            file_prefix="",
            file_suffix=""
        )

    RVP_VOICE_EXTS = (".ogg", ".mp3", ".wav", ".opus")

    _rvp_voice_index = None
    rvp_voice_last_missing = None
    rvp_voice_debug_text = ""

    def _rvp_voice_norm(s):
        return s.replace("\\", "/").lstrip("/").lower()

    def _rvp_voice_build_index():
        """Строит {'a1/un/un_1.ogg': <реальный путь из renpy.list_files()>}."""
        global _rvp_voice_index
        idx = {}
        try:
            files = list(renpy.list_files())
        except Exception:
            files = []

        for f in files:
            low = _rvp_voice_norm(f)
            if not low.endswith(RVP_VOICE_EXTS):
                continue
            marker = "/voice/"
            if marker in low:
                key = low.rsplit(marker, 1)[1]
            elif low.startswith("voice/"):
                key = low[len("voice/"):]
            else:
                continue
            idx.setdefault(key, f)

        _rvp_voice_index = idx
        return idx

    def rvp_v(rel):
        """
        Проиграть озвучку для СЛЕДУЮЩЕЙ реплики.

            $ rvp_v("a1/un/un_1.ogg")
            un "Текст."
        """
        global _rvp_voice_index, rvp_voice_last_missing

        if _rvp_voice_index is None:
            _rvp_voice_build_index()

        key = _rvp_voice_norm(rel)
        last = key.split("/")[-1]
        if "." not in last:
            key += ".ogg"

        path = _rvp_voice_index.get(key)

        # Фолбэк: вдруг renpy.list_files() не отдал аудио.
        if not path:
            for root in ("sounds/voice",
                         "ray_v_panelke/sounds/voice",
                         "mods/ray_v_panelke/sounds/voice"):
                candidate = root + "/" + key
                try:
                    if renpy.music.playable(candidate, "rvp_voice"):
                        path = candidate
                        break
                except Exception:
                    pass

        # Гасим предыдущую реплику.
        try:
            renpy.sound.stop(channel="rvp_voice")
        except Exception:
            pass

        if not path:
            rvp_voice_last_missing = key
            return

        rvp_voice_last_missing = None

        # При перемотке не орём.
        if config.skipping:
            return

        try:
            renpy.sound.play(path, channel="rvp_voice")
        except Exception as e:
            rvp_voice_debug_text = "rvp_v ERROR: %r" % (e,)

    def rvp_voice_debug():
        """Вызвать в консоли: rvp_voice_debug()  — вернёт текст диагностики."""
        global rvp_voice_debug_text
        idx = _rvp_voice_build_index()

        lines = ["RVP VOICE DEBUG",
                 "indexed files: %d" % len(idx)]

        try:
            all_voice = [_rvp_voice_norm(f) for f in renpy.list_files()
                         if "/voice/" in _rvp_voice_norm(f)
                         or _rvp_voice_norm(f).startswith("voice/")]
        except Exception:
            all_voice = []

        lines.append("paths with /voice/: %d" % len(all_voice))
        for p in all_voice[:12]:
            lines.append("  " + p)

        for key in ("a1/un/un_1.ogg", "un_a1_1.ogg"):
            p = idx.get(key)
            lines.append("key %s -> %r" % (key, p))
            if p:
                try:
                    lines.append("   playable=%r" % renpy.music.playable(p, "rvp_voice"))
                except Exception as e:
                    lines.append("   playable ERROR %r" % (e,))

        lines.append("last missing: %r" % rvp_voice_last_missing)

        try:
            lines.append("volume sfx=%r voice=%r" % (
                _preferences.get_volume("sfx"),
                _preferences.get_volume("voice")))
        except Exception as e:
            lines.append("volume ERROR %r" % (e,))

        rvp_voice_debug_text = "\n".join(lines)
        try:
            renpy.notify(rvp_voice_debug_text[:180])
        except Exception:
            pass
        return rvp_voice_debug_text
