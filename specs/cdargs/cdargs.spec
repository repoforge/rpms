# $Id$
# Authority: dag

Summary: Navigate cd
Name: cdargs
Version: 1.35
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://www.skamphausen.de/software/cdargs/

Source: http://www.skamphausen.de/software/cdargs/cdargs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel

%description
Navigate cd Arguments/expand the shell built-in cd with bookmarks and browser

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 contrib/cdargs.el %{buildroot}%{_datadir}/emacs/site-lisp/cdargs.el
%{__install} -Dp -m0644 contrib/cdargs-bash.sh %{buildroot}%{_sysconfdir}/profile.d/cdargs.sh
%{__install} -Dp -m0644 contrib/cdargs-tcsh.csh %{buildroot}%{_sysconfdir}/profile.d/cdargs.csh

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/cdargs.1*
%config %{_sysconfdir}/profile.d/cdargs.sh
%config %{_sysconfdir}/profile.d/cdargs.csh
%{_bindir}/cdargs
%{_datadir}/emacs/site-lisp/cdargs.el

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 1.35-2
- Installed cdargs.el into emacs directory.
- Installed /etc/profile.d scripts by default.

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 1.35-1
- Updated to release 1.35.

* Tue Sep 20 2005 Dag Wieers <dag@wieers.com> - 1.31-1
- Initial package. (using DAR)
