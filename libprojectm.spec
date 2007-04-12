%define name libprojectm
%define version 0.99
%define release %mkrel 2
%define oname libprojectM
%define major 0
%define libname %mklibname projectm %major

Summary: Visualization library for OpenGL based on Milkdrop 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://xmms-projectm.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libftgl-devel

%description
projectM is a reimplementation of Milkdrop under OpenGL.

%package data
Summary: Visualization library for OpenGL based on Milkdrop 
Group: Graphics

%description data
projectM is a reimplementation of Milkdrop under OpenGL. This contains data
files and presets.

%package -n %libname
Summary: Visualization library for OpenGL based on Milkdrop
Group: System/Libraries
Requires: %name-data >= %version

%description -n %libname
projectM is a reimplementation of Milkdrop under OpenGL.

%package -n %libname-devel
Summary: Visualization library for OpenGL based on Milkdrop
Group: Development/C
Requires: %libname = %version
Provides: libprojectm-devel = %version-%release

%description -n %libname-devel
projectM is a reimplementation of Milkdrop under OpenGL.


%prep
%setup -q -n %oname
aclocal -I m4
autoconf
automake

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

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

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/libprojectM.so
%_libdir/libprojectM.a
%_libdir/libprojectM.la
%_libdir/pkgconfig/*.pc
%_includedir/projectM/


