%define name audacious-plugins
%define version 3.2
%define prerel beta1
%define rel 1
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%if %mdvver >= 201100
%define extrarelsuffix plf
%else
%define distsuffix plf
%endif
%endif
%if %prerel
%define release		%mkrel -c %prerel %rel
%define fname %name-%version-%prerel
%else
%define fname %name-%version
%define release %mkrel %rel
%endif
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%endif
%define audacious %epoch:3.2

Summary:	Audacious Media Player core plugins
Name:		%name
Version:	%version
Release:	%release%{?extrarelsuffix}
Epoch:		5
Source0:	http://distfiles.audacious-media-player.org/%fname.tar.bz2
Patch1: audacious-plugins-3.2-beta1-linking.patch
#gw from Fedora, enable gnome keys by default
Patch2: audacious-plugins-3.0-alpha1-enable-gnomeshortcuts.patch
License:	GPLv2+
Group:		Sound
Url:		http://audacious-media-player.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	audacious >= %audacious
BuildRequires:	libaudacious-devel >= %audacious
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	oggvorbis-devel
BuildRequires:	libglade2.0-devel
#gw crossfade
BuildRequires:	libsamplerate-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmms-devel
BuildRequires:  liblirc-devel
%if %mdvver >= 201100
BuildRequires:	gtk+3-devel
%else
BuildRequires:	gtk2-devel >= 2.6.0
%endif
BuildRequires:  libmesaglut-devel
BuildRequires:  libxcomposite-devel
BuildRequires:  SDL-devel
BuildRequires:  libsndfile-devel
%if %mdvver >= 201100
BuildRequires:  jackit-devel >= 1.9.7
%endif
BuildRequires:  taglib-devel
BuildRequires:  libmad-devel
BuildRequires:  libmusicbrainz-devel
BuildRequires:  libnotify-devel
#gw currently does not build
#BuildRequires:  bluez-devel >= 2.22
BuildRequires:  libbinio-devel
#gw scrobbler and curl:
BuildRequires:  libcurl-devel >= 7.9.7
BuildRequires:  neon-devel >= 0.26
BuildRequires:  libfluidsynth-devel
BuildRequires:  libwavpack-devel
BuildRequires:  libmtp-devel >= 0.3.0
BuildRequires:  libflac-devel
BuildRequires:  libcddb-devel
BuildRequires:  libcdio-devel
BuildRequires:  imlib2-devel
BuildRequires:  libshout-devel
BuildRequires:  libbs2b-devel
%if %mdvver >= 201100
BuildRequires:  pkgconfig(libavcodec) >= 52.110.0
%endif
BuildRequires:  libcue-devel
BuildRequires:  libmpg123-devel
Provides:	beep-media-player-libvisual beep-media-player-lirc audacious-modplug
Obsoletes:	beep-media-player-libvisual beep-media-player-lirc audacious-modplug
%if %build_plf
BuildRequires: liblame-devel
BuildRequires: libfaad2-static-devel
Provides:beep-media-player-mp4 audacious-extra-plugins
Obsoletes:beep-media-player-mp4 audacious-extra-plugins
#gw ffmpeg plugin:
Obsoletes: audacious-musepack
Provides: audacious-musepack
%endif
#gw make sure the broken plugin is removed
Obsoletes: audacious-timidity
#gw 2.0.0 has its own crossfader and the old one does not build anymore
Provides: audacious-crossfade
Obsoletes: audacious-crossfade         

%description
Audacious is a media player based on the BMP music playing application.
Its primary goals are usability and usage of current desktop standards.

This contains the basic plugin distribution. Audacious is useless
without them.

%if %build_plf
This package is in PLF as it violates some patents.
%endif

%package  -n audacious-wavpack
Group: Sound
Summary:  Wavpack input plugin for Audacious
Requires:	audacious >= %audacious
Epoch: %epoch

%description  -n audacious-wavpack
This is a wavpack input plugin for Audacious based on libwavpack.

%if %mdvver >= 201100
%package  -n audacious-jack
Group: Sound
Summary:Audacious output plugin for the jack sound server
Epoch: %epoch
Requires:	audacious >= %audacious

%description  -n audacious-jack
Audacious audio output plugin for the jack audio
server(http://jackit.sourceforge.net).
%endif

%package  -n audacious-pulse
Group: Sound
Summary:Audacious output plugin for the Pulseaudio sound server
Epoch: %epoch
Requires: audacious >= %audacious
Provides: audacious-esd
Obsoletes: audacious-esd
BuildRequires: libpulseaudio-devel

%description  -n audacious-pulse
Audacious audio output plugin for the pulseaudio
server.

%package  -n audacious-adplug
Summary: AdLib player plugin for audacious
Group: Sound
Requires: audacious >= %audacious
Epoch: %epoch

%description  -n audacious-adplug
AdPlug is an Audacious input plugin It uses the AdPlug AdLib sound
player library to play back a wide range of AdLib (OPL2) music file
formats on top of an OPL2 emulator.  No OPL2 chip is required for
playback.


%package  -n audacious-fluidsynth
Summary: Fluidsynth MIDI plugin for audacious
Group: Sound
Requires: audacious >= %audacious
Epoch: %epoch

%description  -n audacious-fluidsynth
FluidSynth is a real-time software synthesizer based on the SoundFont 2
specifications. It is a "software synthesizer". FluidSynth can read MIDI
events from the MIDI input device and render them to the audio device.

This is a fluidsynth backend for the Audacious Media Player to support the
playback of MIDI files with the fluidsynth engine.

%package  -n audacious-sid
Group: Sound
Summary: Audacious input plugin for C64 SID files
BuildRequires: sidplay-devel
BuildRequires: sidplay2-devel
Provides: beep-media-player-sid
Obsoletes: beep-media-player-sid
Epoch: %epoch
Requires: audacious >= %audacious

%description  -n audacious-sid
Audacious-SID is a plugin for the Audacious Media Player which provides
support for playing the so-called "SID tunes", which are music
from old Commodore computer programs like games, demos, etc.

For the actual playing, it uses the excellent libsidplay (1|2)
emulator engine that emulates 6510 CPU and 6581/8580 Sound Interface
Device (SID) chip.

%package -n audacious-smb
Group: Sound
Summary: SMB/CIFS file system plugin for the Audacious media player
Epoch: %epoch
Requires: audacious >= %audacious
BuildRequires: libsmbclient-devel

%description -n audacious-smb
This plugin allows Audacious to play content from a Samba or Windows network
file system.

%prep
%setup -q -n %fname
%apply_patches

%build
#gw else cdaudio does not build (2.2-beta2)
#define _disable_ld_no_undefined 1
%configure2_5x --enable-amidiplug --enable-smb \
--enable-scrobbler
%ifarch %ix86 x86_64
#--enable-usf
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if !%build_plf
rm -fv %buildroot%_libdir/audacious/Input/aac.so
%endif

%find_lang %name
%clean
rm -rf %{buildroot}


%files -f %name.lang
%defattr(0644,root,root,0755)
%doc AUTHORS
%dir %_libdir/audacious/Input/amidi-plug/
%_libdir/audacious/Input/amidi-plug/ap-alsa.so
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
%{_libdir}/audacious/General/lyricwiki.so
%{_libdir}/audacious/General/mtp_up.so
%{_libdir}/audacious/General/notify.so
%{_libdir}/audacious/General/scrobbler.so
%{_libdir}/audacious/General/search-tool.so
%{_libdir}/audacious/General/skins.so
%{_libdir}/audacious/General/statusicon.so
%{_libdir}/audacious/General/song_change.so
%dir %{_libdir}/audacious/Input
%if %mdvver >= 201100
%{_libdir}/audacious/Input/ffaudio.so
%endif
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
%ifarch %ix86 x86_64
#%{_libdir}/audacious/Input/usf.so
%endif
%{_libdir}/audacious/Input/vorbis.so
%{_libdir}/audacious/Input/vtx.so
%{_libdir}/audacious/Input/xsf.so
%if %build_plf
%_libdir/audacious/Input/aac.so
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
%{_libdir}/audacious/Effect/sndstretch.so
%{_libdir}/audacious/Effect/stereo.so
%{_libdir}/audacious/Effect/voice_removal.so
%dir %{_libdir}/audacious/Output
#%{_libdir}/audacious/Output/OSS.so
%{_libdir}/audacious/Output/alsa.so
%{_libdir}/audacious/Output/filewriter.so
%{_libdir}/audacious/Output/null.so
%{_libdir}/audacious/Output/sdlout.so
%dir %{_libdir}/audacious/Transport/
#%{_libdir}/audacious/Transport/gio.so
%{_libdir}/audacious/Transport/mms.so
%{_libdir}/audacious/Transport/neon.so
%{_libdir}/audacious/Transport/unix-io.so
%dir %{_libdir}/audacious/Visualization
%{_libdir}/audacious/Visualization/blur_scope.so
%{_libdir}/audacious/Visualization/cairo-spectrum.so
%_datadir/audacious

%files  -n audacious-wavpack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Input/wavpack.so

%if %mdvver >= 201100
%files  -n audacious-jack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/jackout.so
%endif

%files  -n audacious-pulse
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/pulse_audio.so

%files  -n audacious-sid
%defattr(-,root,root)
%{_libdir}/audacious/Input/sid.so

%files  -n audacious-adplug
%defattr(-,root,root)
%{_libdir}/audacious/Input/adplug.so

%if 0
%files  -n audacious-timidity
%defattr(-,root,root)
%{_libdir}/audacious/Input/timidity.so
%endif

%files  -n audacious-fluidsynth
%defattr(0644,root,root,0755)
%_libdir/audacious/Input/amidi-plug/ap-fluidsynth.so

%files -n audacious-smb
%defattr(-,root,root)
%_libdir/audacious/Transport/smb.so
