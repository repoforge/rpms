# $Id$
# Authority: matthias

# Python name and version, use "--define 'python python2'"
%{!?python: %{expand: %%define python python}}
%define pyminver 2.1

Summary: Creates a common metadata repository
Name: createrepo
Version: 0.4.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://linux.duke.edu/projects/metadata/
Source: http://linux.duke.edu/projects/metadata/generate/createrepo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: rpm-python, %{python} >= %{pyminver}, rpm >= 4.1.1, libxml2-python
BuildArch: noarch

%description
This utility will generate a common metadata repository from a directory of
rpm packages


%prep
%setup
# Replace interpreter's name if it's not "python"
if [ "%{python}" != "python" ]; then
    find . -type f | \
        xargs %{__perl} -pi -e 's|/usr/bin/python|/usr/bin/%{python}|g'
fi


%build


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%dir %{_mandir}/man8/createrepo.8*
%{_bindir}/createrepo
%{_datadir}/createrepo/


%changelog
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
- 0.2 - 

* Sat Jan 10 2004 Seth Vidal <skvidal@phy.duke.edu>
- first packaging

