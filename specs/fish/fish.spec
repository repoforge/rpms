# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Friendly interactive shell
Name: fish
Version: 1.14.0
Release: 1
License: GPL
Group: System Environment/Shells
URL: http://roo.no-ip.org/fish/

Source: http://roo.no-ip.org/fish/files/%{version}/fish-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, doxygen, groff
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
fish is a shell geared towards interactive use. It's features are
focused on user friendlieness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
#echo %{_bindir}/fish >>%{_sysconfdir}/shells

%files
%defattr(-, root, root, 0755)
%doc INSTALL README *.html doc_src/*.txt user_doc/html/
%doc %{_mandir}/man1/count.1*
%doc %{_mandir}/man1/fish.1*
%doc %{_mandir}/man1/mimedb.1*
%doc %{_mandir}/man1/set_color.1*
%doc %{_mandir}/man1/tokenize.1*
%doc %{_mandir}/man1/xsel.1x*
%config(noreplace) %{_sysconfdir}/fish
%config(noreplace) %{_sysconfdir}/fish_inputrc
%config(noreplace) %{_sysconfdir}/fish.d/
%{_bindir}/count
%{_bindir}/fish
%{_bindir}/mimedb
%{_bindir}/set_color
%{_bindir}/tokenize
%{_bindir}/xsel
%{_bindir}/fish_pager
%{_bindir}/fishd
%exclude %{_docdir}/fish/

%changelog
* Tue Sep 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.14.0-1
- Updated to release 1.14.0.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.13.4-1
- Updated to release 1.13.4.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.13.3-1
- Updated to release 1.13.3.

* Thu Sep 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.13.1-1
- Updated to release 1.13.1.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 1.13.0-1
- Updated to release 1.13.0.

* Fri Aug 05 2005 Dag Wieers <dag@wieers.com> - 1.12.1-1
- Updated to release 1.12.1.

* Fri Jul 15 2005 Dag Wieers <dag@wieers.com> - 1.12.0-1
- Updated to release 1.12.0.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.11.1-1
- Updated to release 1.11.1.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 1.10.1-1
- Updated to release 1.10.1.

* Sat May 28 2005 Dag Wieers <dag@wieers.com> - 1.10-1
- Initial package. (using DAR)
