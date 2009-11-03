# $Id$
# Authority: dag
# Upstream: Daniel Reed <n$ml,org>

Summary: Console AIM, ICQ, IRC, and Lily client
Name: naim
Version: 0.11.8.3.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://naim.n.ml.org/

Source: http://naim.googlecode.com/files/naim-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
naim is a console client for AOL Instant Messenger (AIM), AOL I Seek You (ICQ),
Internet Relay Chat (IRC), and The lily CMC.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/naim/
%{__rm} -rf %{buildroot}%{_includedir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FAQ INSTALL NEWS README TODO doc/*.hlp
%doc %{_mandir}/man1/naim.1*
%doc %{_mandir}/man1/nicq.1*
%doc %{_mandir}/man1/nirc.1*
%doc %{_mandir}/man1/nlily.1*
%{_bindir}/extractbuddy.sh
%{_bindir}/naim
%{_bindir}/nicq
%{_bindir}/nirc
%{_bindir}/nlily

%changelog
* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.8.3.1-1
- Updated to release 0.11.8.3.1.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.8.3-1
- Updated to release 0.11.8.3.

* Mon Nov 20 2006 Dag Wieers <dag@wieers.com> - 0.11.8.2.1-1
- Initial package. (using DAR)
