# $Id$
# Authority: dag
# Upstream: Thomas Vander Stichele <thomas$apestaart,org>

Summary: Automatically detect and configure network settings
Name: columbus
Version: 0.1.1
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://columbus.sourceforge.net/

Source: http://thomas.apestaart.org/download/columbus/src/columbus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Columbus automatically detects your location from a set of pre-defined
locations (identified by a known host, it's IP address and it's MAC
address) and symlinks specific system files accordingly.  It also hooks
this up to apmd and together with viking, a link monitor, it can
automatically re-sync your network each time your network cable has been
unplugged.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__ln_s} -f %{_sbindir}/ifup-pre-local %{buildroot}/sbin/ifup-pre-local

%clean
%{__rm} -rf %{buildroot}

%post
chkconfig --add columbus
#if test -e /etc/sysconfig/apm-scripts/apmscript; then
#  cp /etc/sysconfig/apm-scripts/apmscript /etc/sysconfig/apm-scripts/apmscript.bak
#fi
#patch /etc/sysconfig/apm-scripts/apmscript < /usr/share/columbus/apmscript.patch

%preun
if [ $1 -eq 0 ]; then
        /sbin/service columbus stop &>/dev/null || :
        /sbin/chkconfig --del columbus
fi

%postun
/sbin/service columbus condrestart &>/dev/null || :
#if test -e /etc/sysconfig/apm-scripts/apmscript.bak; then
#  cp /etc/sysconfig/apm-scripts/apmscript.bak /etc/sysconfig/apm-scripts/apmscript
#fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%config %{_initrddir}/*
/sbin/*
%{_sbindir}/*
%{_datadir}/columbus

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.1-0.2
- Rebuild for Fedora Core 5.

* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Initial package. (using DAR)
