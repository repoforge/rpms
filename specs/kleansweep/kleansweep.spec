# $Id$
# Authority: dries
# Upstream: Pawel Stolowski <pawel,stolowski$wp,pl>

Summary: Reclaim disk space by finding unneeded files
Name: kleansweep
Version: 0.2.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://linux.bydg.org/~yogin/

Source: http://linux.bydg.org/~yogin/kleansweep-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++, scons, rpm-devel

%description
KleanSweep allows you to reclaim disk space by finding unneeded files. It
can search for files based on several criteria: you can seek for empty
files, backup files, broken symbolic links, dead menu entries, duplicated
files, orphaned files (files not found in the RPM database), and more.

%prep
%setup

%build
scons

%install
%{__rm} -rf %{buildroot}
scons install prefix=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_datadir}/apps/kleansweep/
%{_datadir}/applnk/System/kleansweep.desktop
%{_datadir}/icons/*/*/apps/kleansweep.png
%{_bindir}/kleansweep*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1
- Updated to release 0.2.6.

* Mon Jan 16 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-1
- Updated to release 0.2.4.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.3-1
- Initial package.
