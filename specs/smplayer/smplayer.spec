# $Id$
# Authority: dries
# Upstream: <rvm$escomposlinux,org>

Summary: Frontend for mplayer
Name: smplayer
Version: 0.6.5.1
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://smplayer.berlios.de/

Source: http://dl.sf.net/smplayer/smplayer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch: smplayer-0.6.5.1-centos5-zyv.patch

BuildRequires: qt4-devel, gcc-c++
Requires: mplayer

%description
SMPlayer intends to be a complete front-end for Mplayer, from basic features 
like playing videos, DVDs, and VCDs to more advanced features like support 
for Mplayer filters and more. One of the main features is the ability to 
remember the state of a played file, so when you play it later it will resume 
at the same point and with the same settings.

%prep
%setup
%patch -p1

%build
export PATH=/usr/lib/qt4/bin/:${PATH}
%{__make} %{?_smp_mflags} PREFIX=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX=%{_prefix}
%{__mv} %{buildroot}%{_docdir}/packages/smplayer rpmdocs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/smplayer.1*
%doc rpmdocs/*
%{_bindir}/smplayer
%{_datadir}/icons/*/*/apps/smplayer.png
%{_datadir}/applications/smplayer*.desktop
%{_datadir}/smplayer/

%changelog
* Tue Dec  2 2008 Dries Verachtert <dries@ulyssis.org> - 0.6.5.1-2
- Applied patch for centos 5, thanks to Yury V. Zaytsev.

* Sun Nov 23 2008 Dries Verachtert <dries@ulyssis.org> - 0.6.5.1-1
- Initial package.
