# $Id$
# Authority: dag

Summary: InterMezzo synchronization client
Name: intersync
Version: 0.9.5
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.inter-mezzo.org/

Source: ftp://ftp.inter-mezzo.org/pub/intermezzo/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: e2fsprogs-devel, readline-devel, curl-devel, pkgconfig, glib2-devel
Requires: webserver

%description
InterSync is a C based InterMezzo client, intended to
operate with an http server (e.g. TUX or Apache) as a server.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
### Don't build the intermezzo modules (should come with the kernel)
%{__perl} -pi.orig -e 's|fs24||g' configure Makefile.in
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0644 sampleconfigs/intersync.conf %{buildroot}%{_sysconfdir}/intermezzo/intersync.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/intermezzo/

### FIXME: Fix problem with default Makefiles (?)
### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%pre
GROUPNAME=intermezzo
grep "^${GROUPNAME}:" /etc/group &>/dev/null
if [ $? -ne 0 ]; then
    groupadd -g 4711 $GROUPNAME
    if [ $? -ne 0 -a $? -ne 9 ]; then
        err=$(groupadd $GROUPNAME)
        if [ $? -ne 0 -a $? -ne 9 ]; then
            echo "$err"
            exit $status
        fi
    fi
fi

err=$(useradd -g $GROUPNAME -d / -s /bin/true intermezzo 2>&1)
if [ $? -ne 0 -a $? -ne 9 ]; then
   echo "$err"
   exit $status
fi

%post
chkconfig --add intersync

%preun
chkconfig --del intersync || :

%postun
if [ $1 -eq 0 ]; then
     userdel intermezzo
     groupdel intermezzo
fi

%files
%defattr(-, root, root, 0755)
%doc ChangeLog NEWS
%doc doc/*.html doc/*.sgml doc/*.txt
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/intermezzo/
%config %{_sysconfdir}/init.d/*
%{_bindir}/*
%{_libdir}/intermezzo/
%{_localstatedir}/log/intermezzo/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man4/*
%{_libdir}/*.a
%{_includedir}/intermezzo/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 13 2003 Dag Wieers <dag@wieers.com> - 0.9.5
- Initial package. (using DAR)
