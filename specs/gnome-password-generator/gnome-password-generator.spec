# $Id$
# Authority: dag
# Upstream: Chris Ladd <caladd$particlestorm,net>

Summary: Graphical secure password generator
Name: gnome-password-generator
Version: 1.6
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://gnome-password.sourceforge.net/

Source: http://dl.sf.net/gnome-password/gnome-password-generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.0, pygtk2-devel, gnome-python2
Requires: python >= 2.0, pygtk2, gnome-python2

%description
Gnome Password Generator is a graphical secure password generator.
It allows the user to generate a specified number of random
passwords of a specified length.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	datadir="%{_datadir}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/gnome-password-generator
%{_datadir}/pixmaps/gnome-password-generator.png
%{_datadir}/applications/gnome-password-generator.desktop

%changelog
* Thu Mar 27 2008 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Updated to release 1.6.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 1.0-2
- Cosmetic rebuild for Group-tag and BuildArch-tag.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
