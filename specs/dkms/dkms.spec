# $Id$
# Authority: dag

%{?el3:%define _without_kernel_devel 1}

Summary: Dynamic Kernel Module Support Framework
Name: dkms
Version: 2.1.1.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://linux.dell.com/dkms/

Source: http://linux.dell.com/dkms/permalink/dkms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: sed, gawk, findutils, modutils, tar, cpio, gzip, grep, mktemp
Requires: bash > 1.99, gcc, make
%{?_without_kernel_devel:Requires: kernel-source}
%{!?_without_kernel_devel:Requires: kernel-devel}

Provides: dkms-minimal

%description
DKMS stands for Dynamic Kernel Module Support. It is designed to create
a framework where kernel dependant module source can reside so that it
is very easy to rebuild modules as you upgrade kernels. This will allow
Linux vendors to provide driver drops without having to wait for new
kernel releases while also taking out the guesswork for customers
attempting to recompile modules for new kernels.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install-redhat DESTDIR="%{buildroot}" \
    SBIN="%{buildroot}%{_sbindir}" \
    VAR="%{buildroot}%{_localstatedir}/lib/dkms" \
    MAN="%{buildroot}%{_mandir}/man8" \
    ETC="%{buildroot}%{_sysconfdir}/dkms" \
    BASHDIR="%{buildroot}%{_sysconfdir}/bash_completion.d" \
    LIBDIR="%{buildroot}%{_prefix}/lib/dkms"

#%{__install} -Dp -m0755 dkms %{buildroot}%{_sbindir}/dkms
#%{__install} -Dp -m0755 dkms_mkkerneldoth %{buildroot}%{_sbindir}/dkms_mkkerneldoth
#%{__install} -Dp -m0644 dkms_framework.conf %{buildroot}%{_sysconfdir}/dkms/framework.conf
#%{__install} -Dp -m0644 template-dkms-mkrpm.spec %{buildroot}%{_sysconfdir}/dkms/template-dkms-mkrpm.spec
%{__install} -Dp -m0755 dkms_autoinstaller %{buildroot}%{_initrddir}/dkms_autoinstaller
#%{__install} -Dp -m0644 dkms_dbversion %{buildroot}%{_localstatedir}/lib/dkms/dkms_dbversion
#%{__install} -Dp -m0644 dkms.8 %{buildroot}%{_mandir}/man8/dkms.8

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_sysconfdir}/init.d/

%post
/sbin/chkconfig --add dkms_autoinstaller

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del dkms_autoinstaller
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README* sample.spec sample.conf
%doc %{_mandir}/man8/dkms.8*
%dir %{_sysconfdir}/bash_completion.d/
%config(noreplace) %{_sysconfdir}/dkms/
%dir %{_sysconfdir}/kernel/
%dir %{_sysconfdir}/kernel/postinst.d/
%dir %{_sysconfdir}/kernel/prerm.d/
%config %{_sysconfdir}/bash_completion.d/dkms
%config %{_sysconfdir}/kernel/postinst.d/dkms
%config %{_sysconfdir}/kernel/prerm.d/dkms
%config %{_initrddir}/dkms_autoinstaller
%{_localstatedir}/lib/dkms/
%{_prefix}/lib/dkms/
%{_sbindir}/dkms
%exclude %{_datadir}/apport/

%changelog
* Thu Jun 17 2010 Dag Wieers <dag@wieers.com> - 2.1.1.2-1
- Updated to release 2.1.1.2.

* Mon Aug 17 2009 Dag Wieers <dag@wieers.com> - 2.0.22.0-1
- Updated to release 2.0.22.0.

* Thu Sep 04 2008 Dag Wieers <dag@wieers.com> - 2.0.20.4-1
- Updated to release 2.0.20.4.

* Sun Aug 03 2008 Dag Wieers <dag@wieers.com> - 2.0.20.2-2
- Fixed a wrong assumption in the scripts wrt. LSB.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 2.0.20.2-1
- Updated to release 2.0.20.2.

* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 2.0.19-2
- Fixed missing files. (Alan Bartlett)

* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 2.0.19-1
- Updated to release 2.0.19.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 2.0.17.6-1
- Updated to release 2.0.17.6.
- Added make as a requirement. (Manuel Wolfshant)

* Fri Nov 09 2007 Fabian Arrotin <fabian.arrotin@arrfab.net> - 2.0.17.5-2
- Modified the Requires: for older distributions still using kernel-source

* Fri Oct 12 2007 Dag Wieers <dag@wieers.com> - 2.0.17.5-1
- Updated to release 2.0.17.5.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 2.0.17.4-1
- Updated to release 2.0.17.4.

* Sat Sep 08 2007 Dag Wieers <dag@wieers.com> - 2.0.17-1
- Updated to release 2.0.17.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 2.0.16-1
- Updated to release 2.0.16.

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 2.0.13-1
- Updated to release 2.0.13.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.31.04-0
- Initial package. (using DAR)
