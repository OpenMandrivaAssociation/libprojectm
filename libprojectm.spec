%define name libprojectm
%define version 1.2.0
%define release %mkrel 3
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
Source0: %{oname}-%{version}.tar.bz2
# Adjust for libftgl 2.1.3+ - AdamW 2008/12
Patch0: libprojectM-1.2.0-ftgl.patch
License: LGPLv2+
Group: System/Libraries
Url: http://xmms-projectm.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libftgl-devel
BuildRequires: cmake
BuildRequires: libglew-devel
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
%setup -q -n %oname-%version
%patch0 -p1 -b .ftgl

%build
export LDFLAGS=-lpthread
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

#replace by symlink
ln -sf %_datadir/fonts/TTF/{Vera.ttf,VeraMono.ttf} %buildroot%_datadir/projectM/fonts/


%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files data
%defattr(-,root,root)
%doc ChangeLog
%_datadir/projectM/

%files -n %libname
%defattr(-,root,root)
%_libdir/libprojectM.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/pkgconfig/*.pc
%_includedir/libprojectM/
%_libdir/libprojectM.so

