# $Id$
# Authority: dag


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Friendly interactive shell
Name: fish
Version: 1.23.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://fishshell.org

Source: http://fishshell.org/files/%{version}/fish-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, doxygen, groff, gettext, autoconf
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel, libXt-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

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

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
#echo %{_bindir}/fish >>%{_sysconfdir}/shells

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc *.html doc_src/*.txt INSTALL README user_doc/html/
#%doc %{_mandir}/man1/count.1*
%doc %{_mandir}/man1/fish.1*
%doc %{_mandir}/man1/fish_indent.1*
%doc %{_mandir}/man1/fish_pager.1*
%doc %{_mandir}/man1/fishd.1*
%doc %{_mandir}/man1/mimedb.1*
%doc %{_mandir}/man1/set_color.1*
%doc %{_mandir}/man1/xsel.1x*
%config(noreplace) %{_sysconfdir}/fish
#%config(noreplace) %{_sysconfdir}/fish_inputrc
#%config(noreplace) %{_sysconfdir}/fish.d/
#%{_bindir}/count
%{_bindir}/fish
%{_bindir}/fish_indent
%{_bindir}/fish_pager
%{_bindir}/fishd
%{_bindir}/mimedb
%{_bindir}/set_color
%{_bindir}/xsel
%{_datadir}/fish/
%exclude %{_docdir}/fish/

%changelog
* Sun Jan 13 2008 Dries Verachtert <dries@ulyssis.org> - 1.23.0-1
- Updated to release 1.23.0.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 1.22.3-1
- Updated to release 1.22.3.

* Fri Dec 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.22.2-1
- Updated to release 1.22.2.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.22.1-1
- Updated to release 1.22.1.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 1.22.0-1
- Updated to release 1.22.0.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 1.21.12-1
- Updated to release 1.21.12.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.11-1
- Updated to release 1.21.11.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 1.21.10-1
- Updated to release 1.21.10.

* Wed Jul 19 2006 Dag Wieers <dag@wieers.com> - 1.21.9-1
- Updated to release 1.21.9.

* Wed May 31 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.8-1
- Updated to release 1.21.8.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.7-1
- Updated to release 1.21.7.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.6-1
- Updated to release 1.21.6.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.5-1
- Updated to release 1.21.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.4-1
- Updated to release 1.21.4.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 1.21.3-1
- Updated to release 1.21.3.

* Sun Mar 12 2006 Dag Wieers <dag@wieers.com> - 1.21.2-1
- Updated to release 1.21.2.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.21.1-1
- Updated to release 1.21.1.

* Tue Feb 28 2006 Dag Wieers <dag@wieers.com> - 1.21.0-1
- Updated to release 1.21.0.

* Thu Jan 26 2006 Dag Wieers <dag@wieers.com> - 1.20.1-1
- Updated to release 1.20.1.

* Tue Jan 17 2006 Dag Wieers <dag@wieers.com> - 1.20.0-1
- Updated to release 1.20.0.

* Tue Dec 27 2005 Dag Wieers <dag@wieers.com> - 1.19.0-1
- Updated to release 1.19.0.

* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 1.18.2-1
- Updated to release 1.18.2.

* Fri Dec 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.18.1-1
- Updated to release 1.18.1.

* Wed Dec 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.18.0-1
- Updated to release 1.18.0.

* Thu Dec 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.17.0-1
- Updated to release 1.17.0.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.16.2-1
- Updated to release 1.16.2.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.16.1-1
- Updated to release 1.16.1.

* Tue Oct 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.15.0-1
- Updated to release 1.15.0.

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
