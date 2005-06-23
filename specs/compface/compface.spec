# $Id$
# Authority: matthias

Summary: Programs for 48x48x1 image compression and decompression
Name: compface
Version: 1.4
Release: 1
License: MIT
Group: Applications/System
URL: http://freshmeat.net/projects/compface/
Source: http://www.ibiblio.org/pub/Linux/apps/graphics/convert/compface-%{version}.tar.gz
Patch0: compface-1.4-errno.patch
Patch1: compface-1.4-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The programs contained in this package convert 48x48x1 images to and from
compressed formats. The uncompressed images are expected to contain 48x48/4
(576) hex digits. The purpose is to allow the inclusion of face images within
mail headers using the field name `X-face: '.


%package devel
Summary: Static library and header file for compface
Group: Development/Libraries

%description devel
This package contains the static compface library which can be used to allow
the compface compression and decompression algorithms to be used in
applications such as mail dispatchers and mail notification daemons.


%prep
%setup
%patch0 -p1 -b .errno
%patch1 -p1 -b .makefile


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_bindir}/compface
%{_bindir}/uncompface
%{_mandir}/man1/compface.1*
%{_mandir}/man1/uncompface.1*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libcompface.a
%{_includedir}/compface.h
%{_mandir}/man3/compface.3*
%{_mandir}/man3/uncompface.3*


%changelog
* Tue May 11 2004 Matthias Saou <http://freshrpms.net/> 1.4-1
- Initial RPM release.

