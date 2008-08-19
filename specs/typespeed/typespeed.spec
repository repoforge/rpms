# $Id$
# Authority: dag

Summary: Test your typing speed and get your fingers' CPS
Name: typespeed
Version: 0.6.5
Release: 1
License: GPL
Group: Applications/Text
URL: http://tobias.eyedacor.org/typespeed/

Source: http://tobias.eyedacor.org/typespeed/typespeed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Typespeed gives your fingers' cps (total and correct), typoratio and
some points to compare with your friends.

%prep
%setup
echo "%{_datadir}/typespeed/" >typespeedrc

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/typespeed/

%post
%{_bindir}/typespeed --makescores &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man6/typespeed.6*
%config %{_sysconfdir}/typespeedrc
%{_bindir}/typespeed
%{_datadir}/typespeed/
%dir %{_localstatedir}/games/
%{_localstatedir}/games/typespeed.score

%changelog
* Wed Aug 13 2008 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Sat Dec 01 2007 Dag Wieers <dag@wieers.com> - 0.6.4-1
- Updated to release 0.6.4.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.6.3-1
- Updated to release 0.6.3.

* Sat Jun 02 2007 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sat Jan 20 2007 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Fri Aug 18 2006 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Initial package. (using DAR)
