%define name audacious-plugins
%define version 1.4.4
%define svn 0
%define pre 0
%define rel 2
%if %pre
%if %svn
%define release	%mkrel 0.%pre.%svn.%rel
%define fname %name-%svn
%else
%define release		%mkrel 0.%pre.%rel
%define fname %name-%version-%pre
%endif
%else
%define fname %name-%version
%define release %mkrel %rel
%endif
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif
%define audacious %epoch:1.4.1

%define build_arts 1

Summary:	Audacious Media Player core plugins
Name:		%name
Version:	%version
Release:	%release
Epoch:		5
Source0:	http://audacious-media-player.org/release/%fname.tbz2
License:	GPLv2+
Group:		Sound
Url:		http://audacious-media-player.org/
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
BuildRequires:	gtk2-devel >= 2.6.0
BuildRequires:  libmesaglut-devel
BuildRequires:  libxcomposite-devel
BuildRequires:  SDL-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libjack-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  taglib-devel
BuildRequires:  libmad-devel
BuildRequires:  libmusicbrainz-devel
BuildRequires:  libbinio-devel
BuildRequires:  libcurl-devel >= 7.9.7
BuildRequires:  libneon-devel >= 0.26
BuildRequires:  libfluidsynth-devel
BuildRequires:  libwavpack-devel
BuildRequires:  libprojectm-devel >= 1.0
BuildRequires:  libmtp-devel
BuildRequires:  libflac-devel
BuildRequires:  libcddb-devel
BuildRequires:  libcdio-devel
BuildRequires:  libimlib2-devel
Provides:	beep-media-player-libvisual beep-media-player-lirc audacious-modplug beep-media-player-scrobbler audacious-scrobbler
Obsoletes:	beep-media-player-libvisual beep-media-player-lirc audacious-modplug beep-media-player-scrobbler audacious-scrobbler
%if %build_plf
BuildRequires: liblame-devel
Provides:beep-media-player-mp4 audacious-extra-plugins
Obsoletes:beep-media-player-mp4 audacious-extra-plugins
%endif

%description
Audacious is a media player based on the BMP music playing application.
Its primary goals are usability and usage of current desktop standards.

This contains the basic plugin distribution. Audacious is useless
without them.

%if %build_plf
This package is in PLF as it violates some patents.
%endif

%package -n audacious-esd
Summary:	ESound output backend
Group:		Sound
BuildRequires:	esound-devel
Requires:	audacious
Requires:	esound >= 0.2.14
Provides: beep-media-player-esd
Obsoletes: beep-media-player-esd
Epoch: %epoch

%description  -n audacious-esd
Output plugin for Audacious media player for use with the esound package

%package  -n audacious-musepack
Group: Sound
Summary:  Musepack input plugin for Audacious
Requires: audacious
Epoch: %epoch

%description  -n audacious-musepack
This is a Musepack input plugin for Audacious based on libmpcdec.


%package  -n audacious-wavpack
Group: Sound
Summary:  Wavpack input plugin for Audacious
Requires: audacious
Epoch: %epoch

%description  -n audacious-wavpack
This is a wavpack input plugin for Audacious based on libwavpack.

%package  -n audacious-jack
Group: Sound
Summary:Audacious output plugin for the jack sound server
Epoch: %epoch
Requires: audacious

%description  -n audacious-jack
Audacious audio output plugin for the jack audio
server(http://jackit.sourceforge.net).


%package  -n audacious-pulse
Group: Sound
Summary:Audacious output plugin for the Pulseaudio sound server
Epoch: %epoch
Requires: audacious
BuildRequires: libpulseaudio-devel

%description  -n audacious-pulse
Audacious audio output plugin for the pulseaudio
server.

%package  -n audacious-adplug
Summary: AdLib player plugin for audacious
Group: Sound
Requires: audacious
Epoch: %epoch

%description  -n audacious-adplug
AdPlug is an Audacious input plugin It uses the AdPlug AdLib sound
player library to play back a wide range of AdLib (OPL2) music file
formats on top of an OPL2 emulator.  No OPL2 chip is required for
playback.


%package  -n audacious-fluidsynth
Summary: Fluidsynth MIDI plugin for audacious
Group: Sound
Requires: audacious
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
Requires: audacious

%description  -n audacious-sid
Audacious-SID is a plugin for the Audacious Media Player which provides
support for playing the so-called "SID tunes", which are music
from old Commodore computer programs like games, demos, etc.

For the actual playing, it uses the excellent libsidplay (1|2)
emulator engine that emulates 6510 CPU and 6581/8580 Sound Interface
Device (SID) chip.

%package  -n audacious-timidity
Group: Sound
Summary: MIDI support for Audacious
Requires: audacious
Epoch: %epoch
#gw for the instruments
Requires: TiMidity++

%description  -n audacious-timidity
This adds MIDI support to Audacious.

%if %build_arts
%package  -n audacious-arts
Group: Sound
Summary: Arts output plugin for Audacious Media Player
Requires: audacious
BuildRequires: libarts-devel
Provides: beep-media-player-arts
Obsoletes: beep-media-player-arts
Epoch: %epoch

%description  -n audacious-arts
This is a Arts output plugin for Audacious Media Player.
%endif

%package  -n audacious-projectm
Group: Sound
Summary: Visualization for Audacious, based on projectM
Requires: audacious
Epoch: %epoch

%description  -n audacious-projectm
This adds Visualization support to Audacious, based on projectM.

%prep
%if %svn
%setup -q -n %name
%else
%setup -q -n %fname
%endif
%if %svn
sh ./autogen.sh
%endif

%build
%configure2_5x --enable-amidiplug --enable-timidity \
%ifarch %ix86
--disable-sse2 \
%endif
%if ! %build_arts
--disable-arts
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%_includedir/mp4.h
%if !%build_plf
rm -fv %buildroot%_libdir/audacious/Input/aac.so
rm -fv %buildroot%_libdir/audacious/Input/wma.so
%endif

%find_lang %name
%clean
rm -rf %{buildroot}


%files -f %name.lang
%defattr(0644,root,root,0755)
%doc AUTHORS NEWS 
%dir %_libdir/audacious/Input/amidi-plug/
%_libdir/audacious/Input/amidi-plug/ap-alsa.so
%_libdir/audacious/Input/amidi-plug/ap-dummy.so
%dir %{_libdir}/audacious
%dir %{_libdir}/audacious/Container
%{_libdir}/audacious/Container/m3u.so
%{_libdir}/audacious/Container/pls.so
%{_libdir}/audacious/Container/xspf.so
%dir %{_libdir}/audacious/General
%{_libdir}/audacious/General/alarm.so
%{_libdir}/audacious/General/aosd.so
%{_libdir}/audacious/General/evdev-plug.so
%{_libdir}/audacious/General/gnomeshortcuts.so
%{_libdir}/audacious/General/hotkey.so
%{_libdir}/audacious/General/lirc.so
%{_libdir}/audacious/General/mtp_up.so
%{_libdir}/audacious/General/scrobbler.so
%{_libdir}/audacious/General/statusicon.so
%{_libdir}/audacious/General/song_change.so
%dir %{_libdir}/audacious/Input
%{_libdir}/audacious/Input/alac.so
%{_libdir}/audacious/Input/amidi-plug.so
%{_libdir}/audacious/Input/cdaudio-ng.so
%{_libdir}/audacious/Input/console.so
%{_libdir}/audacious/Input/cuesheet.so
%{_libdir}/audacious/Input/flacng.so
%{_libdir}/audacious/Input/madplug.so
%{_libdir}/audacious/Input/metronom.so
%{_libdir}/audacious/Input/modplug.so
%{_libdir}/audacious/Input/tonegen.so
%{_libdir}/audacious/Input/tta.so
%{_libdir}/audacious/Input/vorbis.so
%{_libdir}/audacious/Input/vtx.so
%{_libdir}/audacious/Input/wav.so
#
%{_libdir}/audacious/Input/sexypsf.so
#
%if %build_plf
%_libdir/audacious/Input/aac.so
%_libdir/audacious/Input/wma.so
%endif
%dir %{_libdir}/audacious/Effect/
%{_libdir}/audacious/Effect/audiocompress.so
%{_libdir}/audacious/Effect/echo.so
%{_libdir}/audacious/Effect/ladspa.so
%{_libdir}/audacious/Effect/sndstretch.so
%{_libdir}/audacious/Effect/stereo.so
%{_libdir}/audacious/Effect/voice_removal.so
%dir %{_libdir}/audacious/Output
%{_libdir}/audacious/Output/OSS.so
%{_libdir}/audacious/Output/ALSA.so
%{_libdir}/audacious/Output/filewriter.so
%{_libdir}/audacious/Output/null.so
%dir %{_libdir}/audacious/Transport/
%{_libdir}/audacious/Transport/lastfm.so
%{_libdir}/audacious/Transport/mms.so
%{_libdir}/audacious/Transport/neon.so
%{_libdir}/audacious/Transport/stdio.so
%dir %{_libdir}/audacious/Visualization
%{_libdir}/audacious/Visualization/blur_scope.so
%{_libdir}/audacious/Visualization/paranormal.so
%{_libdir}/audacious/Visualization/rocklight.so
%{_libdir}/audacious/Visualization/rootvis.so
%{_libdir}/audacious/Visualization/spectrum.so
%_datadir/audacious

%files  -n audacious-esd
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/ESD.so

%files  -n audacious-musepack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Input/musepack.so

%files  -n audacious-wavpack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Input/wavpack.so

%files  -n audacious-jack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/jackout.so

%files  -n audacious-pulse
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/pulse_audio.so

%files  -n audacious-sid
%defattr(-,root,root)
%{_libdir}/audacious/Input/sid.so

%files  -n audacious-adplug
%defattr(-,root,root)
%{_libdir}/audacious/Input/adplug.so

%files  -n audacious-timidity
%defattr(-,root,root)
%{_libdir}/audacious/Input/timidity.so

%if %build_arts
%files  -n audacious-arts
%defattr(-,root,root)
%{_libdir}/audacious/Output/arts.so
%_bindir/audacious-arts-helper
%endif

%files  -n audacious-fluidsynth
%defattr(0644,root,root,0755)
%_libdir/audacious/Input/amidi-plug/ap-fluidsynth.so

%files  -n audacious-projectm
%defattr(-,root,root)
%{_libdir}/audacious/Visualization/projectm-1.0.so
