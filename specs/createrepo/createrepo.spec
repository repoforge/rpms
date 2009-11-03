# $Id$
# Authority: matthias

### Ironically yum 2.4 (sqlite2) cannot be installed with createrepo (sqlite3)
# ExcludeDist: el2 rh7 rh9 el3 el4

# Python name and version, use "--define 'python python2'"
%{!?python: %{expand: %%define python python}}

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Creates a common metadata repository
Name: createrepo
Version: 0.4.10
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://linux.duke.edu/projects/metadata/

Source: http://linux.duke.edu/projects/metadata/generate/createrepo-%{version}.tar.gz
Patch0: http://people.redhat.com/mikem/software/createrepo-0.4.4-update2.1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: %{python} >= 2.1
Requires: %{python} >= 2.1, rpm >= 4.1.1, rpm-python, libxml2-python
Requires: yum-metadata-parser

%description
This utility will generate a common metadata repository from a directory of
rpm packages.

%prep
%setup
#%patch0

# Replace interpreter's name if it's not "python"
if [ "%{python}" != "python" ]; then
    %{__perl} -pi -e 's|/usr/bin/python|/usr/bin/%{python}|g' *.py
fi

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING* README
%doc %{_mandir}/man8/createrepo.8*
%{_bindir}/createrepo
%{_bindir}/modifyrepo
%{_datadir}/createrepo/

%changelog
* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 0.4.10-1
- Updated to release 0.4.10.

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Updated to release 0.4.8.

* Wed Aug 23 2006 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Updated to release 0.4.6.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.4.4-3
- Added noepoch an update2 patches.

* Fri Mar 24 2006 Dag Wieers <dag@wieers.com> - 0.4.4-2
- Added python-urlgrabber as a dependency. (Robert Hardy)

* Thu Mar 16 2006 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Updated to release 0.4.4.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-1
- Update to 0.4.1.

* Mon Oct 18 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-1
- Update to 0.4.0.

* Wed Aug 04 2004 Dries Verachtert <dries@ulyssis.org> 0.3.6-1
- Update to version 0.3.6.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Picked up package.

* Mon Jul 19 2004 Seth Vidal <skvidal@phy.duke.edu>
- re-enable groups
- update num to 0.3.4

* Tue Jun  8 2004 Seth Vidal <skvidal@phy.duke.edu>
- update to the format
- versioned deps
- package counts
- uncompressed checksum in repomd.xml

* Fri Apr 16 2004 Seth Vidal <skvidal@phy.duke.edu>
- 0.3.2 - small addition of -p flag

* Sun Jan 18 2004 Seth Vidal <skvidal@phy.duke.edu>
- I'm an idiot

* Sun Jan 18 2004 Seth Vidal <skvidal@phy.duke.edu>
- 0.3

* Tue Jan 13 2004 Seth Vidal <skvidal@phy.duke.edu>
- 0.2

* Sat Jan 10 2004 Seth Vidal <skvidal@phy.duke.edu>
- first packaging

