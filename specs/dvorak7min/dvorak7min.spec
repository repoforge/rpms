# $Id$
# Authority: dries

Summary: Dvorak typing tutor
Name: dvorak7min
Version: 1.6.1
Release: 3.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.linalco.com/comunidad.html

Source: http://www.linalco.com/ragnar/dvorak7min-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ncurses-devel

%description
Dvorak7min is a ncurses based dvorak typing tutor. It features well chosen
lessons, color for easy visual feedback, and a real time characters per
second display. It's called 7min because it originally was a personal hack
written in 7 min.

%prep
%setup

%build
### force rebuild
%{__rm} -f dvorak7min *.o
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL="%{buildroot}%{_bindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.1-3.2
- Rebuild for Fedora Core 5.

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-3
- rebuild

* Tue Feb 24 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-2
- force rebuild
- check build requirements with mach

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-1
- first packaging for Fedora Core 1

