%define name libprojectm
%define version 2.1.0
%define release 1
%define oname libprojectM
%define major 2
%define libname %mklibname projectm %major
%define develname %mklibname -d projectm
%define oldlibname %mklibname projectm

Summary: Visualization library for OpenGL based on Milkdrop 
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: http://downloads.sourceforge.net/project/projectm/2.1.0/projectM-complete-%{version}-Source.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://projectm.sourceforge.net
BuildRequires: libftgl-devel
BuildRequires: cmake
BuildRequires: libglew-devel
BuildRequires: libgomp-devel
BuildRequires: pulseaudio-devel
Patch0:	libprojectm-2.1.0-libsuffix.patch
Patch1:	libprojectm-2.1.0-path.patch

Requires: %name-data >= %epoch:%version

%description
projectM is a reimplementation of Milkdrop under OpenGL.

%package -n %libname
Summary: Visualization library for OpenGL based on Milkdrop
Group: System/Libraries
Requires: %name-data >= %epoch:%version

%description -n %libname
projectM is a reimplementation of Milkdrop under OpenGL.


%package data
Summary: Visualization library for OpenGL based on Milkdrop 
Group: Graphics
Requires:	fonts-ttf-bitstream-vera

%description data
projectM is a reimplementation of Milkdrop under OpenGL. This contains data
files and presets.

%package -n %develname
Summary: Visualization library for OpenGL based on Milkdrop
Group: Development/C
Requires: %libname = %epoch:%version
Provides: libprojectm-devel = %epoch:%version-%release
Obsoletes: %mklibname -d projectm 0
Requires: libglew-devel
Conflicts: %oldlibname

%description -n %develname
projectM is a reimplementation of Milkdrop under OpenGL.


%prep
%setup -q -n projectM-complete-%{version}-Source
%patch0 -p1
%patch1 -p1

%build
cd src/libprojectM/
%cmake
%make

%install
cd src/libprojectM/
%makeinstall_std -C build
%ifarch x86_64
	mv %{buildroot}/usr/lib/pkgconfig/ %{buildroot}/%{_libdir}
%endif

#replace by symlink
ln -sf %_datadir/fonts/TTF/{Vera.ttf,VeraMono.ttf} %buildroot%_datadir/projectM/fonts/


%files data
#% doc ChangeLog
%_datadir/projectM/

%files -n %libname
%_libdir/libprojectM.so.%{major}*

%files -n %develname
%_libdir/pkgconfig/*.pc
%_includedir/libprojectM/
%_libdir/libprojectM.so

