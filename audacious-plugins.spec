#####################
# Hardcode PLF build
%define build_plf 0
#####################
%{?_with_plf: %{expand: %%global build_plf 1}}

%if %{build_plf}
%define	extrarelsuffix	plf
%define	distsuffix	plf
%endif

%global _disable_lto 1
%define build_smb 0

Summary:	Audacious Media Player core plugins
Name:	audacious-plugins
Version:	4.5
Release:	2
License:	GPLv2+
Group:	Sound
Url:		https://audacious-media-player.org/
Source0:	https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	meson >= 0.53
BuildRequires:	ninja
BuildRequires:	qmake-qt6
# This is ducking wrong like whole splits, ducking wrong
# WHY ducking hooked noses don't think about the consequences. Enough fucking splits, revert that ducking mess
BuildRequires:	%{_lib}audgui6
BuildRequires:	pkgconfig(alsa)
# Disable it for now, because package is in Extra, re-enable it when pulled to main
#BuildRequires:	pkgconfig(adplug)
BuildRequires:	pkgconfig(audacious) >= 4.5
BuildRequires: pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(glib-2.0) >= 2.32
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lame)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libavcodec) >= 53.40.0
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libbinio)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgme)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsidplayfp)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(opusfile)
#QT Stack
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl3)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(sndio)
BuildRequires:	pkgconfig(soxr)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisenc)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xrender)

%if %{build_plf}
BuildRequires:	libfaad2-static-devel
BuildRequires:	faad2-devel
#gw ffmpeg plugin:
Provides:	audacious-musepack
%endif
Requires:	audacious = %{version}-%{release}

%description
Audacious is a media player based on the BMP music playing application.
Its primary goals are usability and usage of current desktop standards.
This contains the basic plugin distribution. Audacious is useless without
them.
%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%files -f %{name}.lang
%dir %{_libdir}/audacious
%{_datadir}/audacious
%{_libdir}/audacious/Container/*
%{_libdir}/audacious/Effect/*
%{_libdir}/audacious/General/*
%{_libdir}/audacious/Input/*
%{_libdir}/audacious/Output/*
%{_libdir}/audacious/Transport/*
%{_libdir}/audacious/Visualization/

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%meson -Dgtk=true -Dqt=true
%meson_build


%install
%meson_install

%find_lang %{name}
