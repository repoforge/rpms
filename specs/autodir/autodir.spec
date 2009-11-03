# $Id$
# Authority: matthias

Summary: Creates user directories on demand
Name: autodir
Version: 0.99.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.intraperson.com/autodir/
Source: http://dl.sf.net/intraperson/autodir-%{version}.tar.gz
Patch0: autodir-0.96.0-init.d.patch
Patch1: autodir-0.96.0-cflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libcap-devel, gcc-c++, libtool
#, libtool-ltdl-devel

%description
Autodir offers a simple and effective means to create directories like home
directories in a transparent manner. It relies on the autofs protocol for its
operation.


%prep
%setup
%patch0 -p1 -b .init.d
%patch1 -p1 -b .cflags
# Fix for lib64
%{__perl} -pi -e 's|/usr/lib/autodir|%{_libdir}/autodir|g' \
    misc/init.scripts/sysconfig/*


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m 0755 misc/init.scripts/autogroup \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/autogroup
%{__install} -D -m 0755 misc/init.scripts/autohome \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/autohome

%{__install} -D -m 0644 misc/init.scripts/sysconfig/autogroup \
    %{buildroot}%{_sysconfdir}/sysconfig/autogroup
%{__install} -D -m 0644 misc/init.scripts/sysconfig/autohome \
    %{buildroot}%{_sysconfdir}/sysconfig/autohome

# For whatever reason, the plugins get created without the .so extension (RHEL4
# x86_64 for 0.96.0), so fix that and remove unneeded .la and static libs.
for libname in autogroup autohome automisc; do
    %{__rm} -f %{buildroot}%{_libdir}/autodir/${libname}.{a,la}
    %{__mv}    %{buildroot}%{_libdir}/autodir/${libname}.0.0.0 \
               %{buildroot}%{_libdir}/autodir/${libname}.so || :
done
# Remove the (now broken anyway if the mv above worked) symlinks
find %{buildroot}%{_libdir}/autodir -type l | xargs %{__rm} -f


%clean
%{__rm} -rf %{buildroot}


%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add autogroup
    /sbin/chkconfig --add autohome
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service autogroup stop &>/dev/null || :
    /sbin/service autohome stop &>/dev/null || :
    /sbin/chkconfig --del autogroup
    /sbin/chkconfig --del autohome
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service autogroup condrestart &>/dev/null || :
    /sbin/service autohome condrestart &>/dev/null || :
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/Autodir-HOWTO.html NEWS README
%config(noreplace) %{_sysconfdir}/sysconfig/autogroup
%config(noreplace) %{_sysconfdir}/sysconfig/autohome
%{_sysconfdir}/rc.d/init.d/autogroup
%{_sysconfdir}/rc.d/init.d/autohome
%{_sbindir}/autodir
%{_libdir}/autodir/


%changelog
* Tue Mar 21 2006 Matthias Saou <http://freshrpms.net/> 0.99.3-1
- Update to 0.99.3.

* Mon Feb  6 2006 Matthias Saou <http://freshrpms.net/> 0.99.1-1
- Update to 0.99.1.

* Fri Dec 16 2005 Matthias Saou <http://freshrpms.net/> 0.99.0-1
- Update to 0.99.0.

* Wed Nov  2 2005 Matthias Saou <http://freshrpms.net/> 0.96.2-1
- Update to 0.96.2.

* Fri Oct 28 2005 Matthias Saou <http://freshrpms.net/> 0.96.1-1
- Update to 0.96.1.
- Add newly required libtool-ltdl-devel build dependency.

* Wed Aug 24 2005 Matthias Saou <http://freshrpms.net/> 0.96.0-1
- Initial RPM release.

