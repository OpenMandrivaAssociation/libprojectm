%define	oname	libprojectM
%define	major	2
%define	libname	%mklibname projectm %{major}
%define	devname	%mklibname -d projectm

Summary:	Visualization library for OpenGL based on Milkdrop 
Name:		libprojectm
Epoch:		1
Version:	2.1.0
Release:	14
License:	LGPLv2+
Group:		System/Libraries
Url:		http://projectm.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/projectm/2.1.0/projectM-complete-%{version}-Source.tar.gz
Patch0:		libprojectm-2.1.0-libsuffix.patch
Patch1:		libprojectm-2.1.0-path.patch
Patch2:		projectm-libsuffix-pkgconf.patch

BuildRequires:	cmake
BuildRequires:	gomp-devel
BuildRequires:	pkgconfig(ftgl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libpulse)

%track
prog %{name} = {
	url = http://sourceforge.net/projects/projectm/files/
	version = %{version}
	regex = "projectM-complete-(__VER__)-Source\.tar\.gz"
}

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
%setup -qn projectM-complete-%{version}-Source
%apply_patches

%build
cd src/libprojectM/
%cmake
%make

%install
cd src/libprojectM/
%makeinstall_std -C build

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

