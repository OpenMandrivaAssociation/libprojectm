%define name libprojectm
%define version 1.1
%define release %mkrel 1
%define oname libprojectM
%define major 2
%define libname %mklibname projectm %major
%define develname %mklibname -d projectm

Summary: Visualization library for OpenGL based on Milkdrop 
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: %{oname}-%{version}.tar.bz2
Patch: libprojectM-1.1-lib64.patch
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

%description -n %develname
projectM is a reimplementation of Milkdrop under OpenGL.


%prep
%setup -q -n %oname-%version
%patch -p1 -b .lib64

%build
%cmake
%make
cp config.inp ..

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

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

