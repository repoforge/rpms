# $Id$
# Authority: matthias
# Upstream: Matthias Wandel <mwandel$sentex,net>

Summary: Tool for handling EXIF metadata in JPEG image files
Name: jhead
Version: 2.8
Release: 1%{?dist}
License: Public Domain
Group: System Environment/Libraries
URL: http://www.sentex.net/~mwandel/jhead/
Source: http://www.sentex.net/~mwandel/jhead/jhead-%{version}.tar.gz
#Patch: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package provides a tool for displaying and manipulating non-image
portions of EXIF format JPEG image files, as produced by most digital cameras.


%prep
%setup
%{__perl} -pi.orig -e 's|-O3 -Wall|%{optflags}|' makefile
#%patch -p1

%build
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 jhead %{buildroot}%{_bindir}/jhead
%{__install} -Dp -m0755 jhead.1.gz %{buildroot}%{_mandir}/man1/jhead.1.gz


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc changes.txt readme.txt usage.html
%{_bindir}/jhead
%{_mandir}/man1/jhead.1.gz


%changelog
* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 2.2-1
- Update to 2.2.

* Wed Apr 21 2004 Matthias Saou <http://freshrpms.net/> 2.1-1
- Spec file cleanup.

* Tue Jan 08 2004 Matthias Wandel <mwandel[at]sentex.net> - 2.0-0
- Bumped version number to 2.1 for new jhead release.

* Tue Jun 03 2003 Oliver Pitzeier <oliver@linux-kernel.at> - 2.0-3
- Specfile cleanup/beautifying
- Use _smp_mflags within make
- Add versions to the changelog entries

* Mon Apr 14 2003 Matthias Wandel <mwandel[at]sentex.net> - 2.0-2
- First jhead 2.0 RPM built by me.
- Finally wrote a nice man page for jhead
- Using jhead 1.9 RPM from connectiva linux as starting point (left in the
  portugese tags)
