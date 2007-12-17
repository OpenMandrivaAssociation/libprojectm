%define name libprojectm
%define version 1.01
%define release %mkrel 2
%define oname libprojectM
%define libname %mklibname projectm 
%define develname %mklibname -d projectm

Summary: Visualization library for OpenGL based on Milkdrop 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
Patch: libprojectM-1.01-lib64.patch
License: LGPL
Group: System/Libraries
Url: http://xmms-projectm.sourceforge.net/
BuildRequires: libftgl-devel
BuildRequires: cmake
BuildRequires: libglew-devel
Requires: %name-data >= %version

%description
projectM is a reimplementation of Milkdrop under OpenGL.

%if %_lib != lib
%package -n %libname
Summary: Visualization library for OpenGL based on Milkdrop
Group: System/Libraries
Requires: %name-data >= %version

%description -n %libname
projectM is a reimplementation of Milkdrop under OpenGL.
%endif

%package data
Summary: Visualization library for OpenGL based on Milkdrop 
Group: Graphics

%description data
projectM is a reimplementation of Milkdrop under OpenGL. This contains data
files and presets.

%package -n %develname
Summary: Visualization library for OpenGL based on Milkdrop
Group: Development/C
Requires: %libname = %version
Provides: libprojectm-devel = %version-%release
Obsoletes: %mklibname -d projectm 0
Requires: libglew-devel

%description -n %develname
projectM is a reimplementation of Milkdrop under OpenGL.


%prep
%setup -q -n %oname-%version
%patch -p1

%build
cmake . -DCMAKE_INSTALL_PREFIX=%_prefix \
%if "%_lib" != "lib" 
    -DLIB_SUFFIX=64
%endif

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
%_libdir/libprojectM.so

%files -n %develname
%defattr(-,root,root)
%_libdir/pkgconfig/*.pc
%_includedir/libprojectM/


