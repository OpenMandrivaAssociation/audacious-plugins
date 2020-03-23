#####################
# Hardcode PLF build
%define build_plf 0
#####################

%define _disable_lto 1

%{?_with_plf: %{expand: %%global build_plf 1}}

%if %{build_plf}
%define	extrarelsuffix	plf
%define	distsuffix	plf
%endif

%define build_smb 0

Summary:	Audacious Media Player core plugins
Name:		audacious-plugins
Version:	4.0
Release:	1%{?extrarelsuffix}
License:	GPLv2+
Group:		Sound
Url:		http://audacious-media-player.org/
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
Requires:	audacious
BuildRequires:  meson
BuildRequires:	pkgconfig(alsa)
# Disable it for now, because package is in unsupported repository (ex-contrib), re-enable it when pulled to main
#BuildRequires:  pkgconfig(adplug)
BuildRequires:	pkgconfig(audacious)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(jack)
BuildRequires:	lame-devel

BuildRequires:	pkgconfig(libavcodec) >= 53.40.0
BuildRequires:	pkgconfig(libbinio)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsidplayfp)

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
BuildRequires:	pkgconfig(soxr)

#QT Stack
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  qmake5

#gw currently does not build
#BuildRequires:	bluez-devel >= 2.22
%if %{build_plf}
BuildRequires:	libfaad2-static-devel
BuildRequires:  faad2-devel
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

%package  -n audacious-audiocd
Group:		Sound
Summary:	Audio CD input plugin for Audacious
Requires:	audacious

%description  -n audacious-audiocd
This is an Audio CD input plugin for Audacious

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
%autopatch -p1

%build
export LDFLAGS="-lm"
#gw else cdaudio does not build (2.2-beta2)
#define _disable_ld_no_undefined 1

%meson  \
        -Dfaad=false
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%dir %{_libdir}/audacious
%{_datadir}/audacious

%files -n audacious-audiocd

%files  -n audacious-wavpack

%files  -n audacious-jack
#%{_libdir}/audacious/Output/jack-ng.so

%files  -n audacious-pulse
#%{_libdir}/audacious/Output/pulse_audio.so

%files  -n audacious-sid
#%{_libdir}/audacious/Input/sid.so

%files  -n audacious-adplug
#{_libdir}/audacious/Input/adplug.so

%if 0
#%files  -n audacious-timidity
#%{_libdir}/audacious/Input/timidity.so
%endif

%files  -n audacious-fluidsynth
#%_libdir/audacious/Input/amidi-plug.so

%if %{build_smb}
#%files -n audacious-smb
#%{_libdir}/audacious/Transport/smb.so
%endif

