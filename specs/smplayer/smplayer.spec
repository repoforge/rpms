# $Id$
# Authority: yury
# Upstream: <rvm$escomposlinux,org>
#
# ExclusiveDist: el5 el6

%define docpath %{_docdir}/%{name}-%{version}

Summary: Frontend for mplayer
Name: smplayer
Version: 0.6.9
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Multimedia
URL: http://smplayer.berlios.de/

Source: http://dl.sf.net/smplayer/smplayer-%{version}.tar.bz2

%if 0%{?el5}
Patch0: smplayer-0.6.9-el5-logic.patch
Patch1: smplayer-0.6.9-el5-ui.patch
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: qt4-devel
Requires: mplayer

%description
SMPlayer intends to be a complete front-end for MPlayer, from basic features 
like playing videos, DVDs, and VCDs to more advanced features like support 
for Mplayer filters and more. One of the main features is the ability to 
remember the state of a played file, so when you play it later it will resume 
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.

%prep
%setup

%if 0%{?el5}
%patch0 -p1
%patch1 -p1
%endif

%build
export PATH="%{_libdir}/qt4/bin:$PATH"
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}" DOC_PATH="\\\"%{docpath}\\\""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" DOC_PATH="%{docpath}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{docpath}
%doc %{_mandir}/man1/smplayer.1*
%{_bindir}/smplayer
%{_datadir}/applications/smplayer*.desktop
%{_datadir}/icons/*/*/apps/smplayer.png
%{_datadir}/smplayer/

%changelog
* Fri Sep 02 2011 Yury V. Zaytsev <yury@shurup.com> - 0.6.9-1
- New patches for RHEL5 for smplayer 0.6.9 by Alfred Ganz.

* Fri Jul 31 2009 Yury V. Zaytsev <yury@shurup.com> - 0.6.8-1
- New patches for CentOS 5 for smplayer 0.6.8 (HTTPS & Socks5 disabled).

* Wed Feb 11 2009 Yury V. Zaytsev <yury@shurup.com> - 0.6.6-1
- New patch for CentOS 5 for smplayer 0.6.6 (HTTPS & Socks5 disabled).

* Tue Dec  2 2008 Dries Verachtert <dries@ulyssis.org> - 0.6.5.1-2
- Applied patch for CentOS 5, thanks to Yury V. Zaytsev.

* Sun Nov 23 2008 Dries Verachtert <dries@ulyssis.org> - 0.6.5.1-1
- Initial package.
