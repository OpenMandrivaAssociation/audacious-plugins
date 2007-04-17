%define name audacious-plugins
%define svn 0
%define pre 0
%if %pre
%if %svn
%define release	%mkrel 0.%pre.%svn.1
%define fname %name-%svn
%else
%define release		%mkrel 0.%pre.1
%define fname %name-%version-%pre
%endif
%else
%define fname %name-%version
%define release %mkrel 1
%endif
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif
%define audacious %epoch:1.3.0-0.rc1

Summary:	Audacious Media Player core plugins
Name:		%name
Version:	1.3.3
Release:	%release
Epoch:		4
Source0:	http://audacious-media-player.org/release/%fname.tar.bz2
Patch3: audacious-862-timidity-config.patch
License:	GPL
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
BuildRequires:	gtk2-devel >= 2.6.0
BuildRequires: libmesaglut-devel
BuildRequires:  SDL-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libjack-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  taglib-devel
BuildRequires:  libmad-devel
BuildRequires:  libmusicbrainz-devel
BuildRequires:  libcurl-devel
BuildRequires:  libbinio-devel
BuildRequires:  libfluidsynth-devel
BuildRequires:  libwavpack-devel
BuildRequires:  libprojectm-devel
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
cd src
%patch3 -p3 -b .timidity
cd ..
%if %svn
sh ./autogen.sh
%endif

%build
%configure2_5x --enable-amidiplug --enable-timidity
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f %buildroot%_includedir/mp4.h
%if !%build_plf
rm -fv %buildroot%_libdir/audacious/Input/libaac.so
rm -fv %buildroot%_libdir/audacious/Input/libwma.so
%endif

%find_lang %name
%clean
rm -rf $RPM_BUILD_ROOT


%files -f %name.lang
%defattr(0644,root,root,0755)
%doc AUTHORS NEWS 
%dir %_libdir/amidi-plug/
%dir %_libdir/amidi-plug/audacious/
%_libdir/amidi-plug/audacious/ap-alsa.so
%_libdir/amidi-plug/audacious/ap-dummy.so
%dir %{_libdir}/audacious
%dir %{_libdir}/audacious/Container
%{_libdir}/audacious/Container/libm3u.so
%{_libdir}/audacious/Container/libmms.so
%{_libdir}/audacious/Container/libpls.so
%{_libdir}/audacious/Container/libstdio.so
%{_libdir}/audacious/Container/libxspf.so
%dir %{_libdir}/audacious/General
%{_libdir}/audacious/General/libalarm.so
%{_libdir}/audacious/General/libaosd.so
%{_libdir}/audacious/General/libcurl.so
%{_libdir}/audacious/General/libevdev-plug.so
%{_libdir}/audacious/General/liblirc.so
%{_libdir}/audacious/General/libscrobbler.so
%{_libdir}/audacious/General/libstatusicon.so
%{_libdir}/audacious/General/libsong_change.so
%dir %{_libdir}/audacious/Input
%{_libdir}/audacious/Input/libalac.so
%{_libdir}/audacious/Input/libamidi-plug.so
%{_libdir}/audacious/Input/libcdaudio.so
%{_libdir}/audacious/Input/libconsole.so
%{_libdir}/audacious/Input/libcuesheet.so
%{_libdir}/audacious/Input/libflac.so
%{_libdir}/audacious/Input/libmadplug.so
%{_libdir}/audacious/Input/libmetronom.so
%{_libdir}/audacious/Input/libmodplug.so
%{_libdir}/audacious/Input/libtonegen.so
%{_libdir}/audacious/Input/libtta.so
%{_libdir}/audacious/Input/libvorbis.so
%{_libdir}/audacious/Input/libvtx.so
%{_libdir}/audacious/Input/libwav.so
#
%{_libdir}/audacious/Input/libsexypsf.so
#
%if %build_plf
%_libdir/audacious/Input/libaac.so
%_libdir/audacious/Input/libwma.so
%endif
%dir %{_libdir}/audacious/Effect/
%{_libdir}/audacious/Effect/libaudiocompress.so
%{_libdir}/audacious/Effect/libecho.so
%{_libdir}/audacious/Effect/libladspa.so
%{_libdir}/audacious/Effect/libsndstretch.so
%{_libdir}/audacious/Effect/libstereo.so
%{_libdir}/audacious/Effect/libvoice_removal.so
%dir %{_libdir}/audacious/Output
%{_libdir}/audacious/Output/libOSS.so
%{_libdir}/audacious/Output/libALSA.so
%{_libdir}/audacious/Output/libdisk_writer.so
%if %build_plf
%{_libdir}/audacious/Output/liblame.so
%endif
%{_libdir}/audacious/Output/libnull.so
%dir %{_libdir}/audacious/Visualization
%{_libdir}/audacious/Visualization/libbscope.so
%{_libdir}/audacious/Visualization/libparanormal.so
%{_libdir}/audacious/Visualization/librocklight.so
%{_libdir}/audacious/Visualization/librovascope.so
%{_libdir}/audacious/Visualization/libspectrum.so
%_datadir/audacious
%dir %_datadir/%name
%_datadir/%name/paranormal

%files  -n audacious-esd
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/libESD.so

%files  -n audacious-musepack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Input/libmpc.so

%files  -n audacious-wavpack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Input/libwavpack.so

%files  -n audacious-jack
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/libjackout.so

%files  -n audacious-pulse
%defattr(0644,root,root,0755)
%{_libdir}/audacious/Output/libpulse_audio.so

%files  -n audacious-sid
%defattr(-,root,root)
%{_libdir}/audacious/Input/libsid.so

%files  -n audacious-adplug
%defattr(-,root,root)
%{_libdir}/audacious/Input/libadplug.so

%files  -n audacious-timidity
%defattr(-,root,root)
%{_libdir}/audacious/Input/libtimidity.so

%files  -n audacious-arts
%defattr(-,root,root)
%{_libdir}/audacious/Output/libarts.so
%_bindir/audacious-arts-helper

%files  -n audacious-fluidsynth
%defattr(0644,root,root,0755)
%_libdir/amidi-plug/audacious/ap-fluidsynth.so

%files  -n audacious-projectm
%defattr(-,root,root)
%{_libdir}/audacious/Visualization/libprojectm.so
