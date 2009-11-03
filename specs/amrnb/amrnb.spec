# $Id$
# Authority: matthias

Summary: AMR NarrowBand speech codec
Name: amrnb
Version: 7.0.0.2
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.penguin.cz/~utx/amr

#Source: ftp://ftp.freebsd.org/pub/FreeBSD/ports/local-distfiles/kwm/amrnb-%{version}.tar.gz
#Source: http://distfiles.opendarwin.org/amrnb-%{version}.tar.gz
Source: http://ftp.penguin.cz/pub/users/utx/amr/amrnb-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
AMR-NB is a narrowband speech codec used in mobile phones.

%package devel
Summary: AMR NarrowBand speech codec development files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
AMR-NB is a narrowband speech codec used in mobile phones development files.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/amrnb-decoder
%{_bindir}/amrnb-decoder-etsi
%{_bindir}/amrnb-decoder-if2
%{_bindir}/amrnb-encoder
%{_bindir}/amrnb-encoder-etsi
%{_bindir}/amrnb-encoder-etsi-vad2
%{_bindir}/amrnb-encoder-if2
%{_bindir}/amrnb-encoder-if2-vad2
%{_bindir}/amrnb-encoder-vad2
%{_libdir}/libamrnb.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/amrnb/
%{_libdir}/libamrnb.so
%exclude %{_libdir}/libamrnb.la

%changelog
* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 7.0.0.2-1
- Updated to release 7.0.0.2.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.0.1-2
- Release bump to drop the disttag number in FC5 build.

* Fri Dec 16 2005 Matthias Saou <http://freshrpms.net/> 0.0.1-1
- Spec file inclusion in rpmforge.

* Wed Sep 07 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.0.1-0.lvn.1: initial package

