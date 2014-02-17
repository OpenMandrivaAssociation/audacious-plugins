#####################
# Hardcode PLF build
%define build_plf 0
#####################

%{?_with_plf: %{expand: %%global build_plf 1}}

%if %{build_plf}
%define	extrarelsuffix	plf
%define	distsuffix	plf
%endif

%define build_smb 0

Summary:	Audacious Media Player core plugins
Name:		audacious-plugins
Version:	3.3.4
Release:	1%{?extrarelsuffix}
Epoch:		5
License:	GPLv2+
Group:		Sound
Url:		http://audacious-media-player.org/
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
#gw from Fedora, enable gnome keys by default
Patch2:		audacious-plugins-3.3-enable-gnomeshortcuts.patch
Requires:	audacious
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audacious)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(jack)

BuildRequires:	pkgconfig(libavcodec) >= 53.40.0
BuildRequires:	pkgconfig(libbinio)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsidplay2)
#BuildRequires:	sidplay-devel

BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(xcomposite)

#gw currently does not build
#BuildRequires:	bluez-devel >= 2.22
%if %{build_plf}
BuildRequires:	liblame-devel
BuildRequires:	libfaad2-static-devel
#gw ffmpeg plugin:
Provides:	audacious-musepack
%endif

%description
Audacious is a media player based on the BMP music playing application.
Its primary goals are usability and usage of current desktop standards.

This contains the basic plugin distribution. Audacious is useless
without them.

%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%package  -n audacious-wavpack
Group:		Sound
Summary:	Wavpack input plugin for Audacious
Requires:	audacious

%description  -n audacious-wavpack
This is a wavpack input plugin for Audacious based on libwavpack.

%package  -n audacious-jack
Group:		Sound
Summary:	Audacious output plugin for the jack sound server
Requires:	audacious

%description  -n audacious-jack
Audacious audio output plugin for the jack audio server.

%package  -n audacious-pulse
Group:		Sound
Summary:	Audacious output plugin for the Pulseaudio sound server
Requires:	audacious

%description  -n audacious-pulse
Audacious audio output plugin for the pulseaudio
server.

%package  -n audacious-adplug
Summary:	AdLib player plugin for audacious
Group:		Sound
Requires:	audacious

%description  -n audacious-adplug
AdPlug is an Audacious input plugin It uses the AdPlug AdLib sound
player library to play back a wide range of AdLib (OPL2) music file
formats on top of an OPL2 emulator.  No OPL2 chip is required for
playback.

%package  -n audacious-fluidsynth
Summary:	Fluidsynth MIDI plugin for audacious
Group:		Sound
Requires:	audacious

%description  -n audacious-fluidsynth
FluidSynth is a real-time software synthesizer based on the SoundFont 2
specifications. It is a "software synthesizer". FluidSynth can read MIDI
events from the MIDI input device and render them to the audio device.

This is a fluidsynth backend for the Audacious Media Player to support the
playback of MIDI files with the fluidsynth engine.

%package  -n audacious-sid
Group:		Sound
Summary:	Audacious input plugin for C64 SID files
Requires:	audacious

%description  -n audacious-sid
Audacious-SID is a plugin for the Audacious Media Player which provides
support for playing the so-called "SID tunes", which are music
from old Commodore computer programs like games, demos, etc.

For the actual playing, it uses the excellent libsidplay (1|2)
emulator engine that emulates 6510 CPU and 6581/8580 Sound Interface
Device (SID) chip.

%if %{build_smb}
%package -n audacious-smb
Group:		Sound
Summary:	SMB/CIFS file system plugin for the Audacious media player
Requires:	audacious
BuildRequires:	pkgconfig(smbclient)

%description -n audacious-smb
This plugin allows Audacious to play content from a Samba or Windows network
file system.
%endif

%prep
%setup -q
%apply_patches

%build
export LDFLAGS="-lm"
#gw else cdaudio does not build (2.2-beta2)
#define _disable_ld_no_undefined 1
%configure2_5x --enable-amidiplug \
%if %{build_smb}
--enable-smb \
%endif
--enable-scrobbler
%ifarch %ix86 x86_64
#--enable-usf
%endif

%make

%install
%makeinstall_std

%if ! %{build_plf}
rm -fv %{buildroot}%{_libdir}/audacious/Input/aac.so
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS
%dir %{_libdir}/audacious/Input/amidi-plug/
%{_libdir}/audacious/Input/amidi-plug/ap-alsa.so
%dir %{_libdir}/audacious
%dir %{_libdir}/audacious/Container
%{_libdir}/audacious/Container/asx.so
%{_libdir}/audacious/Container/audpl.so
%{_libdir}/audacious/Container/cue.so
%{_libdir}/audacious/Container/m3u.so
%{_libdir}/audacious/Container/pls.so
%{_libdir}/audacious/Container/xspf.so
%dir %{_libdir}/audacious/General
%{_libdir}/audacious/General/alarm.so
%{_libdir}/audacious/General/albumart.so
%{_libdir}/audacious/General/aosd.so
#%{_libdir}/audacious/General/bluetooth.so
%{_libdir}/audacious/General/cd-menu-items.so
%{_libdir}/audacious/General/gnomeshortcuts.so
%{_libdir}/audacious/General/gtkui.so
%{_libdir}/audacious/General/hotkey.so
%{_libdir}/audacious/General/lirc.so
%{_libdir}/audacious/General/lyricwiki.so
%{_libdir}/audacious/General/mpris2.so
%{_libdir}/audacious/General/notify.so
%{_libdir}/audacious/General/scrobbler.so
%{_libdir}/audacious/General/search-tool.so
%{_libdir}/audacious/General/skins.so
%{_libdir}/audacious/General/statusicon.so
%{_libdir}/audacious/General/song_change.so
%dir %{_libdir}/audacious/Input
%{_libdir}/audacious/Input/ffaudio.so
%{_libdir}/audacious/Input/amidi-plug.so
%{_libdir}/audacious/Input/cdaudio-ng.so
%{_libdir}/audacious/Input/console.so
%{_libdir}/audacious/Input/flacng.so
%{_libdir}/audacious/Input/madplug.so
%{_libdir}/audacious/Input/metronom.so
%{_libdir}/audacious/Input/modplug.so
%{_libdir}/audacious/Input/psf2.so
%{_libdir}/audacious/Input/sndfile.so
%{_libdir}/audacious/Input/tonegen.so
%ifarch %{ix86} x86_64
#%{_libdir}/audacious/Input/usf.so
%endif
%{_libdir}/audacious/Input/vorbis.so
%{_libdir}/audacious/Input/vtx.so
%{_libdir}/audacious/Input/xsf.so
%if %{build_plf}
%{_libdir}/audacious/Input/aac.so
%endif
%dir %{_libdir}/audacious/Effect/
%{_libdir}/audacious/Effect/bs2b.so
%{_libdir}/audacious/Effect/compressor.so
%{_libdir}/audacious/Effect/crossfade.so
%{_libdir}/audacious/Effect/crystalizer.so
%{_libdir}/audacious/Effect/echo.so
%{_libdir}/audacious/Effect/ladspa.so
%{_libdir}/audacious/Effect/mixer.so
%{_libdir}/audacious/Effect/resample.so
%{_libdir}/audacious/Effect/speed-pitch.so
%{_libdir}/audacious/Effect/stereo.so
%{_libdir}/audacious/Effect/voice_removal.so
%dir %{_libdir}/audacious/Output
%{_libdir}/audacious/Output/alsa.so
%{_libdir}/audacious/Output/filewriter.so
%{_libdir}/audacious/Output/sdlout.so
%dir %{_libdir}/audacious/Transport/
%{_libdir}/audacious/Transport/gio.so
%{_libdir}/audacious/Transport/mms.so
%{_libdir}/audacious/Transport/neon.so
%{_libdir}/audacious/Transport/unix-io.so
%dir %{_libdir}/audacious/Visualization
%{_libdir}/audacious/Visualization/blur_scope.so
%{_libdir}/audacious/Visualization/cairo-spectrum.so
%{_datadir}/audacious

%files  -n audacious-wavpack
%{_libdir}/audacious/Input/wavpack.so

%files  -n audacious-jack
%{_libdir}/audacious/Output/jackout.so

%files  -n audacious-pulse
%{_libdir}/audacious/Output/pulse_audio.so

%files  -n audacious-sid
%{_libdir}/audacious/Input/sid.so

%files  -n audacious-adplug
%{_libdir}/audacious/Input/adplug.so

%if 0
%files  -n audacious-timidity
%{_libdir}/audacious/Input/timidity.so
%endif

%files  -n audacious-fluidsynth
%_libdir/audacious/Input/amidi-plug/ap-fluidsynth.so

%if %{build_smb}
%files -n audacious-smb
%{_libdir}/audacious/Transport/smb.so
%endif

