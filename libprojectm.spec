%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define	oname	libprojectM
%define shortname projectm
%define	major	4
%define	libname	%mklibname projectm %{major}
%define	devname	%mklibname -d projectm

Summary:	Visualization library for OpenGL based on Milkdrop
Name:		libprojectm
Epoch:		1
Version:	4.1.7
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/projectM-visualizer/projectm
Source0:	https://github.com/projectM-visualizer/projectm/releases/download/v%{version}/projectM-%{version}.tar.gz
Patch0:		projectm-3.1.3-pthread.patch
Patch1:		projectm-3.1.3-dont-hardcode-libc++.patch
# Use C++20: current LLVM headers are not compatible with older C++ standards
Patch2:		projectm-3.1.3-cpp20.patch
Patch3:		projectm-4.1.7-clang.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(glm)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libglvnd)

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
# 4.x is CMake-only (no autotools configure); unpack + patches only in %%prep
%autosetup -p1 -n projectm-4.1.7

%build
%cmake \
	-DENABLE_SDL_UI=ON \
	-DENABLE_GLES=ON \
	-DENABLE_SYSTEM_GLM=ON \
	-DENABLE_SYSTEM_PROJECTM_EVAL=OFF \
	-DENABLE_INSTALL=ON
%cmake_build

%install
%cmake_install

#replace by symlink if fonts dir is present
if [ -d %{buildroot}%{_datadir}/projectM/fonts ]; then
	ln -sf ../../fonts/TTF/Vera.ttf %{buildroot}%{_datadir}/projectM/fonts/Vera.ttf 2>/dev/null || :
	ln -sf ../../fonts/TTF/VeraMono.ttf %{buildroot}%{_datadir}/projectM/fonts/VeraMono.ttf 2>/dev/null || :
fi

%files
# Optional SDL test UI (when ENABLE_SDL_UI=ON)
%{_bindir}/projectM-Test-UI

%files data
%{_datadir}/projectM/

%files -n %{libname}
%{_libdir}/libprojectM-%{major}.so.%{major}*
%{_libdir}/libprojectM-playlist.so.%{major}*

%files -n %{devname}
%{_includedir}/projectM-%{major}
%{_libdir}/libprojectM-%{major}.so
%{_libdir}/libprojectM-playlist.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/projectM4/
%{_libdir}/cmake/projectM4Playlist/
