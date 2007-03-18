# $Id$
# Authority: dag

Summary: Test your typing speed and get your fingers' CPS
Name: typespeed
Version: 0.6.1
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
%{__make} CC="%{__cc}" CFLAGS="%{optflags} -D_GNU_SOURCE -I%{_includedir}/ncurses" PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 typespeed %{buildroot}%{_bindir}/typespeed
%{__install} -Dp -m0644 typespeed.6 %{buildroot}%{_mandir}/man6/typespeed.6
%{__install} -Dp -m0644 typespeedrc %{buildroot}%{_sysconfdir}/typespeedrc

%{__install} -d -m0755 %{buildroot}%{_datadir}/typespeed/
%{__install} -p -m0644 words/words.* %{buildroot}%{_datadir}/typespeed/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/games/typespeed/

%post
%{_bindir}/typespeed --makescores &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man6/typespeed.6*
%config %{_sysconfdir}/typespeedrc
%{_bindir}/typespeed
%{_datadir}/typespeed/
%dir %{_localstatedir}/games/typespeed/

%changelog
* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sat Jan 20 2007 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Fri Aug 18 2006 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Initial package. (using DAR)
