# $Id$

%{!?builduser:  %define builduser  machbuild}
%{!?buildgroup: %define buildgroup machbuild}

Name:           mach
Version:        0.4.3.1
Release:        0.fdr.20040301_152240.1
Summary:        Make a chroot.

Group:          Applications/System
License:	GPL
URL:            http://thomas.apestaart.org/projects/mach/
Source:         http://thomas.apestaart.org/download/mach/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	python
Requires:	rpm
Requires:	rpm-python
Requires:	apt
Requires:	sed
Requires:	cpio

BuildRequires:	python

%description
mach makes a chroot.
Using apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.

Authors:
--------
Thomas Vander Stichele (thomas (at) apestaart (dot) org)

%prep
%setup -q

%build
%configure --enable-builduser=%{builduser} --enable-buildgroup=%{buildgroup}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/lib/mach
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/lib/mach/states
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/lib/mach/roots
install -d -m 2775 $RPM_BUILD_ROOT%{_localstatedir}/tmp/mach
install -d -m 775 $RPM_BUILD_ROOT%{_localstatedir}/cache/mach/packages
install -d -m 775 $RPM_BUILD_ROOT%{_localstatedir}/cache/mach/archives

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# create user and group mach
/usr/sbin/useradd -c "mach user" \
	-r -m mach -d %{_localstatedir}/lib/mach > /dev/null 2>&1 || :

%preun
if [ "$1" == 0 ];
then
  # last removal
  # be a good boy and clean out the dirs we filled with junk
  rm -rf %{_localstatedir}/lib/mach/states/*
  rm -rf %{_localstatedir}/lib/mach/roots/*
  rm -rf %{_localstatedir}/cache/mach/* > /dev/null 2>&1 || :
  rmdir %{_localstatedir}/lib/mach/states > /dev/null 2>&1 || :
  rmdir %{_localstatedir}/lib/mach/roots > /dev/null 2>&1 || :
  rmdir %{_localstatedir}/cache/mach > /dev/null 2>&1 || :
  rm -rf %{_localstatedir}/tmp/mach > /dev/null 2>&1 || :
fi

%postun
if [ "$1" == 0 ];
then
  # last removal
  userdel mach > /dev/null 2>&1 || : 
  groupdel mach > /dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README AUTHORS BUGS TODO FORGETMENOT RELEASE
%dir %{_sysconfdir}/mach
%config %{_sysconfdir}/mach/conf
%config %{_sysconfdir}/mach/dist
%attr(2775,mach,mach) %dir %{_localstatedir}/lib/mach
%attr(2775,mach,mach) %dir %{_localstatedir}/lib/mach/states
%attr(2775,mach,mach) %dir %{_localstatedir}/lib/mach/roots
%ghost %attr(2775,mach,mach) %dir %{_localstatedir}/tmp/mach
%attr(2775,mach,mach) %dir %{_localstatedir}/cache/mach/packages
%attr(2775,mach,mach) %dir %{_localstatedir}/cache/mach/archives
%{_bindir}/mach
%attr(04750,root,mach) %{_sbindir}/mach-helper

%changelog
* Fri Jan  9 2004 Ville Skyttä <ville.skytta at iki.fi>
- Use the bzip2'd tarball.

* Thu Jan  8 2004 Ville Skyttä <ville.skytta at iki.fi>
- Make mach chroot build user/group configurable using
  "rpmbuild --define 'build(user|group) foo'"
- Build in the %%build section.

* Wed Sep 17 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- add Requires: cpio
- change home dir to %%{_localstatedir}/lib/mach

* Mon Sep 08 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4.0-0.fdr.1: first public release.

* Sat Aug 16 2003 Ville Skyttä <ville.skytta at iki.fi>
- Add COPYING to docs.

* Wed May 21 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- added mach-helper

* Wed Apr 30 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- initial creation
