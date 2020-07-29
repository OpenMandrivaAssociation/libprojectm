%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define	oname	libprojectM
%define shortname projectm
%define	major	3
%define	libname	%mklibname projectm %{major}
%define	devname	%mklibname -d projectm

Summary:	Visualization library for OpenGL based on Milkdrop 
Name:		libprojectm
Epoch:		1
Version:	3.1.7
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://projectm.sourceforge.net
Source0:        https://github.com/projectM-visualizer/projectm/releases/download/v%{version}/projectM-%{version}.tar.gz
Patch0:		projectm-3.1.3-pthread.patch
Patch1:		projectm-3.1.3-dont-hardcode-libc++.patch
# Use -std=gnu++20 instead of -std=c++11: Current LLVM headers aren't
# compatible with c++11 anymore
Patch2:		projectm-3.1.3-cpp20.patch

BuildRequires:  qmake5
BuildRequires:	cmake
BuildRequires:	gomp-devel
BuildRequires:	atomic-devel
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(jack)

# For Qt subpackage
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5QmlModels)
BuildRequires:  pkgconfig(Qt5QuickTest)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)

%description
projectM is a reimplementation of Milkdrop under OpenGL.

%package -n	%{libname}
Summary:	Visualization library for OpenGL based on Milkdrop
Group:		System/Libraries
Requires:	%{name}-data >= %{EVRD}

%description -n %{libname}
projectM is a reimplementation of Milkdrop under OpenGL.

%package	data
Summary:	Visualization library for OpenGL based on Milkdrop 
Group:		Graphics
Requires:	fonts-ttf-bitstream-vera

%description	data
projectM is a reimplementation of Milkdrop under OpenGL. This contains data
files and presets.

%package -n	%{devname}
Summary:	Visualization library for OpenGL based on Milkdrop
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	libprojectm-devel = %{EVRD}

%description -n	%{devname}
projectM is a reimplementation of Milkdrop under OpenGL.

%prep
%autosetup -p1 -n projectM-%{version}
# FIXME replace --disable-llvm with --enable-llvm once LLVM 10 is supported
%configure --disable-static --disable-rpath --enable-sdl --enable-threading \
    --enable-gles --enable-qt --enable-preset-subdirs --disable-llvm --enable-pulseaudio

%build
%make_build

%install
%make_install

#replace by symlink
ln -sf ../../fonts/TTF/{Vera.ttf,VeraMono.ttf} %{buildroot}%{_datadir}/projectM/fonts/

%files
%{_bindir}/projectM-jack
%{_bindir}/projectM-pulseaudio
%{_bindir}/projectM-unittest
%{_bindir}/projectMSDL
%{_datadir}/applications/projectM-jack.desktop
%{_datadir}/applications/projectM-pulseaudio.desktop
%{_datadir}/icons/hicolor/scalable/apps/projectM.svg
%{_mandir}/man1/projectM-jack.1*
%{_mandir}/man1/projectM-pulseaudio.1*

%files data
%{_datadir}/projectM/

%files -n %{libname}
%{_libdir}/libprojectM.so.%{major}*

%files -n %{devname}
%{_includedir}/libprojectM
%{_libdir}/libprojectM.so
%{_libdir}/pkgconfig/*.pc
