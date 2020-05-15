%define	oname	libprojectM
%define shortname projectm
%define	major	2
%define	libname	%mklibname projectm %{major}
%define	devname	%mklibname -d projectm

Summary:	Visualization library for OpenGL based on Milkdrop 
Name:		libprojectm
Epoch:		1
Version:	3.1.3
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://projectm.sourceforge.net
Source0:        https://github.com/projectM-visualizer/projectm/releases/download/v%{version}/projectM-%{version}.tar.gz
Patch0:     projectm-3.1.3-pthread.patch

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
%setup -qn projectM-%{version}
%autopatch -p1

%build
%global optflags %{optflags} -Wno-narrowing -Wno-c++11-narrowing
#./autogen.sh
%configure --disable-static --disable-rpath --enable-sdl --enable-threading \
    --enable-gles --enable-qt --enable-preset-subdirs --enable-llvm --enable-pulseaudio
%make_build

%install
cd src/libprojectM/
%make_install -C build

#replace by symlink
ln -sf %{_datadir}/fonts/TTF/{Vera.ttf,VeraMono.ttf} %{buildroot}%{_datadir}/projectM/fonts/

%files data
%{_datadir}/projectM/

%files -n %{libname}
%{_libdir}/libprojectM.so.%{major}*

%files -n %{devname}
%{_includedir}/libprojectM
%{_libdir}/libprojectM.so
%{_libdir}/pkgconfig/*.pc

