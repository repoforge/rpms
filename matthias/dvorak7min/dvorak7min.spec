# $Id: dvorak7min.spec,v 1.2 2004/02/27 17:08:23 driesve Exp $

# Authority: dries

Summary: A ncurses based dvorak typing tutor.
Name: dvorak7min
Version: 1.6.1
Release: 2
License: GPL
Group: Applications/Educational
URL: http://www.linalco.com/comunidad.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.linalco.com/ragnar/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: ncurses-devel

%description
Dvorak7min is a ncurses based dvorak typing tutor. It features well chosen
lessons, color for easy visual feedback, and a real time characters per
second display. It's called 7min because it originally was a personal hack
written in 7 min.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
# force rebuild
rm -f dvorak7min *.o
%{__make} %{?_smp_mflags}

%install
sed -i "s/^INSTALL =.*/INSTALL = ${RPM_BUILD_ROOT//\//\\/}\/usr\/bin/g;" Makefile
strip dvorak7min
%{__make} install

%files
%defattr(-,root,root, 0755)
%doc README ChangeLog COPYING
%{_bindir}/%{name}

%changelog
* Tue Feb 24 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-2
- force rebuild
- check build requirements with mach

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-1
- first packaging for Fedora Core 1
