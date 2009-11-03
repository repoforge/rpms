# $Id$

# Authority: dag

Summary: X/Motif based schedule planner
Name: plan
Version: 1.8.6
Release: 0.2%{?dist}
License: Freely distributable with attribution
Group: Applications/Productivity
URL: http://www.bitrot.de/plan.html

Source0: ftp://ftp.fu-berlin.de/pub/unix/graphics/plan/plan-%{version}.tar.gz
Source1: netplan
Source2: plan.wmconfig
Patch0: plan-%{version}-configure.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openmotif-devel, byacc, flex
Requires: openmotif

%description
Plan displays a month calendar similar to xcal, except that every day
box is large enough to show appointments (in small
print). Appointments can be associated with the following information:
date, time and length (in time or days); an optional text message to
be printed; an optional script to be executed; early-warn and
late-warn triggers that precede the alarm time; repetitions (every nth
day, etc.); optional fast command-line appointment entry; flexible
ways to specify holidays and vacations; extensive context help;
multiuser capability using an IP server program (plan-server with
access lists); and grouping of appointments into files, per-user,
private and others.  Plan can be connected (with additional software)
to Apple Newton and PalmPilot PDAs.  You'll need either Motif or
LessTif in order to use Plan.

%package server
Summary: The network server for the plan scheduling program
Group: System Environment/Daemons
PreReq: /sbin/chkconfig , /sbin/service

%description server
Provides interactivity between individual plan client programs. The
plan package must be installed on plan clients in order for them to
use the Plan server.

%prep
%setup
%patch0 -b .orig

%build
%{__make} -C src clean all \
	CFLAGS="%{optflags}" \
	libdir="%{_libdir}" \
	MYCC="${CC:-%{__cc}}" \

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/skel/.plan.dir
%makeinstall -C src \
	MAN="%{buildroot}%{_mandir}/man"
#make RPM_BUILD_ROOT=$RPM_BUILD_ROOT MAN=%{_mandir}/man install -C src

# create a default setup for users with empty dayplans and with the US
# holidays file used by default
install -m644 holiday/* $RPM_BUILD_ROOT/etc/skel/.plan.dir
(cd $RPM_BUILD_ROOT/etc/skel/.plan.dir
	ln -sf holiday_us holiday
	touch dayplan dayplan.priv
 )

#mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d $RPM_BUILD_ROOT/etc/skel
( cd $RPM_BUILD_ROOT/etc/plan/netplan.dir
	touch ../../netplan-acl
	chown nobody.nobody $RPM_BUILD_ROOT/etc/plan/netplan.dir
	ln -sf ../../netplan-acl .netplan-acl
)

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
install -m755 $RPM_SOURCE_DIR/netplan $RPM_BUILD_ROOT/etc/rc.d/init.d/netplan
#for I in 0 1 6; do
#	mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc$I.d
#	ln -sf ../init.d/netplan $RPM_BUILD_ROOT/etc/rc.d/rc$I.d/K05netplan
#done
#for I in 3 5; do
#	mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc$I.d
#	ln -sf ../init.d/netplan $RPM_BUILD_ROOT/etc/rc.d/rc$I.d/S95netplan
#done
mkdir -p $RPM_BUILD_ROOT/etc/X11/applnk/Applications
cat > $RPM_BUILD_ROOT/etc/X11/applnk/Applications/plan.desktop <<EOF
[Desktop Entry]
Name=plan
Type=Application
Description=plan
Exec=plan
EOF

%clean
%{__rm} -rf %{buildroot}

%post server
/sbin/chkconfig --add netplan

%preun server
if [ $1 = 0 ]; then
	/sbin/service netplan stop > /dev/null 2>&1
	/sbin/chkconfig --del netplan
fi

%postun server
if [ "$1" -ge "1" ]; then
	/sbin/service netplan condrestart > /dev/null 2>&1
fi

%files
%defattr(-, root, root, 0755)
%doc HISTORY holiday README
%config %{_sysconfdir}/skel/.plan.dir/
%config %{_sysconfdir}/X11/applnk/Applications/plan.desktop
%{_bindir}/*
%{_libdir}/plan/plan*
%{_libdir}/plan/notifier
%{_mandir}/man?/plan*
#/var/catman/cat1/plan.1*
#/var/catman/cat4/plan.4*

%files server
%defattr(-, root, root, 0755)
%config %{_initrddir}/netplan
%config %{_sysconfdir}/plan/
%attr(-,nobody,nobody) %config %{_sysconfdir}/plan/netplan.dir/
%config %{_sysconfdir}/netplan-acl
%{_libdir}/plan/netplan*
%{_mandir}/man?/netplan*
#/var/catman/cat1/netplan.1*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.6-0.2
- Rebuild for Fedora Core 5.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 1.8.6-0
- Initial package. (using DAR)
