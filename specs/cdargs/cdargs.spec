# $Id$
# Authority: dag

Summary: Navigate cd
Name: cdargs
Version: 1.35
Release: 1.2
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
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc contrib/cdargs-bash.sh contrib/cdargs-tcsh.csh contrib/cdargs.el
%doc %{_mandir}/man1/cdargs.1*
%{_bindir}/cdargs

%clean
%{__rm} -rf %{buildroot}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.35-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 1.35-1
- Updated to release 1.35.

* Tue Sep 20 2005 Dag Wieers <dag@wieers.com> - 1.31-1
- Initial package. (using DAR)
