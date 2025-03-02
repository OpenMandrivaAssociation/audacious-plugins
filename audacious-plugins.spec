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
Version:	4.4.2
Release:	2
License:	GPLv2+
Group:		Sound
Url:		https://audacious-media-player.org/
Source0:	https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2

#Patch1:		audacious-plugins-no-underlinking.patch
Requires:	audacious
BuildRequires:	gettext
BuildRequires:  meson
BuildRequires:	pkgconfig(alsa)
# Disable it for now, because package is in unsupported repository (ex-contrib), re-enable it when pulled to main
#BuildRequires:  pkgconfig(adplug)
BuildRequires:	pkgconfig(audacious)
# This is ducking wrong like whole splits, ducking wrong
# WHY ducking hooked noses don't think about the consequences. Enough fucking splits, revert that ducking mess
BuildRequires:  %{_lib}audgui6
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(jack)
BuildRequires:	lame-devel
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libavcodec) >= 53.40.0
BuildRequires:	pkgconfig(libbinio)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(dbus-glib-1)
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
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  qmake-qt6

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


%prep
%autosetup -p1
%meson \
        -Dgtk=true

%build
#export LDFLAGS="-lm"
#gw else cdaudio does not build (2.2-beta2)
#define _disable_ld_no_undefined 1
%meson_build

%install
%meson_install

%find_lang %{name}

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
