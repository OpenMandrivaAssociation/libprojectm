%define name libprojectm
%define version 2.0.0
%define release %mkrel 4
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
Source0: %{oname}-%{version}-Source.tar.gz
Patch1: libprojectM-2.0.0-fix-linking.patch
License: LGPLv2+
Group: System/Libraries
Url: http://xmms-projectm.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libftgl-devel
BuildRequires: cmake
BuildRequires: libglew-devel
BuildRequires: libgomp-devel
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
%setup -q -n projectM-%{version}-Source
rm -fr build CMakeCache.txt
#patch0 -p1 -b .ftgl
%patch1 -p0 -b .link

%build
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



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.0-3mdv2011.0
+ Revision: 661516
- mass rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.0-2mdv2011.0
+ Revision: 609774
- rebuild

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 1:2.0.0-1mdv2010.1
+ Revision: 507413
- should be libgomp-devel
- BR gmp-devel for -fopenmp
- New version 2.0.0

* Thu Feb 18 2010 Götz Waschk <waschk@mandriva.org> 1:1.2.0-4mdv2010.1
+ Revision: 507404
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 1:1.2.0-3mdv2009.1
+ Revision: 341702
- symlink duplicated fonts

* Tue Dec 09 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.0-2mdv2009.1
+ Revision: 312132
- add ftgl.patch: adjust includes for new libftgl
- rebuild for new ftgl major

* Fri Jul 18 2008 Götz Waschk <waschk@mandriva.org> 1:1.2.0-1mdv2009.0
+ Revision: 238023
- new version
- drop patch
- fix build
- add conflict with old library package

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Götz Waschk <waschk@mandriva.org> 1:1.1-1mdv2009.0
+ Revision: 211182
- add epoch
- new version
- rediff patch 0
- drop patches 1,2,3
- new major

* Tue Feb 19 2008 Götz Waschk <waschk@mandriva.org> 1.01-5mdv2008.1
+ Revision: 173068
- add debian fixes for some crashes

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 1.01-4mdv2008.1
+ Revision: 165343
- rebuild for new libglew

* Sat Jan 05 2008 Götz Waschk <waschk@mandriva.org> 1.01-3mdv2008.1
+ Revision: 145761
- rebuild for new libglew

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Götz Waschk <waschk@mandriva.org> 1.01-2mdv2008.1
+ Revision: 100674
- fix deps

* Sat Oct 20 2007 Götz Waschk <waschk@mandriva.org> 1.01-1mdv2008.1
+ Revision: 100604
- new version
- build with cmake
- update file list
- NO major


* Fri Jan 26 2007 Götz Waschk <waschk@mandriva.org> 0.99-2mdv2007.0
+ Revision: 113965
- bump
- Import libprojectm

* Fri Jan 26 2007 Götz Waschk <waschk@mandriva.org> 0.99-1mdv2007.1
- initial package

