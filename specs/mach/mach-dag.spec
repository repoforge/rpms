# $Id$
# Authority: dag
# Upstream: Thomas Vander Stichele <thomas$apestaart,org>

%define logmsg logger -t mach/rpm

Summary: Make a chroot
Name: mach
Version: 0.4.5
Release: 1
License: GPL
Group: Applications/System
URL: http://thomas.apestaart.org/projects/mach/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://thomas.apestaart.org/download/mach/mach-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.0.0
Requires: rpm, python, rpm-python, apt, sed, cpio

%description
mach makes a chroot.
Using apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.

%prep
%setup

%build
%configure \
	--enable-builduser="mach" \
	--enable-buildgroup="mach"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cache/mach/{archives,packages}
%{__install} -d -m2755 %{buildroot}%{_localstatedir}/lib/mach/{roots,states} \

%clean
%{__rm} -rf %{buildroot}

%pre
if ! /usr/bin/id mach &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/lib/mach -s /bin/sh -c "mach user" -m mach || \
		%logmsg "Unexpected error adding user \"mach\". Aborting installation."
fi

%preun
if [ $1 -eq 0 ]; then
	umount %{_localstatedir}/lib/mach/roots/*/proc &>/dev/null || :
	rm -rf %{_localstatedir}/cache/mach/* &>/dev/null || :
	rmdir %{_localstatedir}/cache/mach &>/dev/null || :
	rm -rf %{_localstatedir}/tmp/mach/ &>/dev/null || :
fi

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
%config %{_sysconfdir}/mach/dist.d/
%config %{_sysconfdir}/mach/location
%{_bindir}/mach

%defattr(4750, root, mach, 0755)
%{_sbindir}/mach-helper

%defattr(-, mach, mach, 0755)
%dir %{_localstatedir}/cache/mach/
%dir %{_localstatedir}/cache/mach/packages/
%dir %{_localstatedir}/cache/mach/archives/

#%defattr(-, mach, mach, 2755)
%dir %{_localstatedir}/lib/mach/
%dir %{_localstatedir}/lib/mach/roots/
%dir %{_localstatedir}/lib/mach/states/

%changelog
* Thu May 27 2004 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.4.3-0
- Updated to release 0.4.3.

* Tue Nov 18 2003 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Added missing mach-directories from filelist. (Rudolf Kastl)

* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Updated to release 0.4.2.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
