# $Id$
# Authority: matthias

Summary: Programs for 48x48x1 image compression and decompression
Name: compface
Version: 1.5.2
Release: 1%{?dist}
License: MIT
Group: Applications/System
URL: 		http://www.ibiblio.org/pub/Linux/apps/graphics/convert/
Source0:        http://ftp.xemacs.org/pub/xemacs/aux/%{name}-%{version}.tar.gz
Source1:        compface-test.xbm
Source2:        compface-README.copyright
Patch0:         http://ftp.debian.org/debian/pool/main/libc/libcompface/libcompface_1.5.2-3.diff.gz
Patch1:         compface-1.5.2-stack-smashing.patch
Patch2:         %{name}-1.5.2-build.patch
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
%setup -q
%patch0 -p1
%patch1 -p1 -b .stack-smashing
%patch2 -p0


%build
export CFLAGS="%{optflags} -fPIC"
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README xbm2xface.pl
#%doc _extdoc/README.copyright
%{_bindir}/compface
%{_bindir}/uncompface
%{_libdir}/libcompface.so.*
%{_mandir}/man1/compface.1*
%{_mandir}/man1/uncompface.1*

%files devel
%defattr(-,root,root,-)
%{_includedir}/compface.h
%{_libdir}/libcompface.so
%{_mandir}/man3/compface.3*
%{_mandir}/man3/uncompface.3*


%changelog
* Sun Aug 12 2007 Heiko Adams <info@fedora-blog.de> 1.5.2
- Update to 1.5.2

* Tue May 11 2004 Matthias Saou <http://freshrpms.net/> 1.4-1
- Initial RPM release.

