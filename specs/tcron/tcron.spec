# $Id$

# Authority: dag
# Distcc: 0

Summary: Another cron daemon.
Name: tcron
Version: 0.4.5
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://tcron.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tcron/tcron-%{version}.tar.bz2
Patch: tcron.makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Tcron integrates 'cron' with the ATX power-up capability.
It can invoke multiple cron jobs and switch the computer on
and off any number of times per day.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p0 -b .orig

%build
%{__make} %{?_smp_mflags} \
	PREFIX="%{_prefix}" \
	TCRONTAB_AP_LIB="%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	DESTDIR="%{buildroot}" \
	PREFIX="%{_prefix}" \
	TCRONTAB_AP_LIB="%{_libdir}"

%{__install} -d -m0755 %{buildroot}%{_initrddir}
%{__mv} -f %{buildroot}%{_sysconfdir}/init.d/tcrond %{buildroot}%{_initrddir}

### libtcron.a contains .c files which strip does not like.
%{__rm} -f %{buildroot}%{_libdir}/*.a

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc Changelog README
%config(noreplace) %{_sysconfdir}/tcrontab/
%config %{_initrddir}/tcrond
%{_sbindir}/*
%{_bindir}/*
%{_libdir}/tcrontab-ap
%{_libdir}/*.so.*
%{_localstatedir}/spool/tcron/

%files devel
%defattr(-, root, root, 0755)
%doc README.api demo/
%{_libdir}/*.so
#{_libdir}/*.a
%{_includedir}/*.h

%changelog
* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.4.5-0
- Initial package. (using DAR)
