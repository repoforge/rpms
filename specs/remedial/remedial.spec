# $Id$

# Authority: dag

%define _libdir %{_prefix}/lib/remedial/

Summary: Remedial AVI player
Name: remedial
Version: 0.2.22
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://leapster.org/remedial/

Source: http://apt.leapster.org/src/remedial/remedial-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: avifile-devel >= 0.7.7, expat-devel
BuildRequires: qt-devel >= 2.1.0, libvorbis-devel, libao-devel, libmad-devel

%description
Remedial is a front-end for the avifile libraries.

%prep
%setup

%build
source "%{_sysconfdir}/profile.d/qt.sh"
CFLAGS="%{optflags}" ./am_edit --no-final
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/remedial/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING LICENCE NEWS README
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/remedial.xml
%{_bindir}/*
%{_libdir}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.22-0.2
- Rebuild for Fedora Core 5.

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.2.22-0
- Initial package. (using DAR)
