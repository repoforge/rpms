# $Id$

# Authority: dag

# Upstream: Thomas Vander Stichele <thomas@apestaart.org>

%define logmsg logger -t mach/rpm

Summary: Make a chroot.
Name: mach
Version: 0.4.3.1
Release: 0
License: GPL
Group: Applications/System
URL: http://thomas.apestaart.org/projects/mach/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://thomas.apestaart.org/download/mach/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires:python
Requires: rpm, python, rpm-python, apt, sed

%description
mach makes a chroot.
Using apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.

%prep
%setup

%build
%configure

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/mach/{roots,states} \
			%{buildroot}%{_localstatedir}/cache/mach/{archives,packages}
#			%{buildroot}%{_localstatedir}/tmp/mach/tmp

%clean
%{__rm} -rf %{buildroot}

%pre
if ! /usr/bin/id mach &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/lib/mach -s /bin/sh -c "mach user" -m mach || \
		%logmsg "Unexpected error adding user \"mach\". Aborting installation."
fi

#%preun
#if [ $1 -eq 0 ]; then
#  rm -rf %{_localstatedir}/lib/mach/states/*
#  rm -rf %{_localstatedir}/lib/mach/roots/*
#  rm -rf %{_localstatedir}/cache/mach/* > /dev/null 2>&1 || :
#  rmdir %{_localstatedir}/lib/mach/states > /dev/null 2>&1 || :
#  rmdir %{_localstatedir}/lib/mach/roots > /dev/null 2>&1 || :
#  rmdir %{_localstatedir}/cache/mach > /dev/null 2>&1 || :
#  rm -rf %{_localstatedir}/tmp/mach
#fi

%postun
if [ $1 -eq 0 ]; then
  /usr/sbin/userdel mach || %logmsg "User \"mach\" could not be deleted."
  /usr/sbin/groupdel mach || %logmsg "Group \"mach\" could not be deleted."
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FORGETMENOT README RELEASE TODO
%dir %{_sysconfdir}/mach/
%config %{_sysconfdir}/mach/conf
%config %{_sysconfdir}/mach/dist
%{_bindir}/mach
%defattr(-, mach, mach, 0755)
%dir %{_localstatedir}/lib/mach/
%dir %{_localstatedir}/lib/mach/states/
%dir %{_localstatedir}/lib/mach/roots/
#%dir %{_localstatedir}/tmp/mach
#%dir %{_localstatedir}/tmp/mach/tmp
%dir %{_localstatedir}/cache/mach/
%dir %{_localstatedir}/cache/mach/packages/
%dir %{_localstatedir}/cache/mach/archives/
%defattr(4750, root, mach, 0755)
%{_sbindir}/mach-helper

%changelog
* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.4.3-0
- Updated to release 0.4.3.

* Tue Nov 18 2003 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Added missing mach-directories from filelist. (Rudolf Kastl)

* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Updated to release 0.4.2.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
