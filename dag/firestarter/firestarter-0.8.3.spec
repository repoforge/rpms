# Authority: dag

Summary: A firewall tool for the GNOME Desktop Environment
Name: firestarter
Version: 0.8.3
Release: 0
License: GPL
Group: Applications/Internet
URL: http://firestarter.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sourceforge.com/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gnome-libs-devel >= 1.2.3, glib-devel, gtk+-devel >= 1.2.7, gnome-core-devel >= 1.4.0
BuildRequires: sh-utils, textutils, fileutils, binutils, grep, make, gcc
BuildRequires: docbook-utils, linuxdoc-tools

%description
Firestarter is an easy-to-use, yet powerful, Linux firewall tool for GNOME.
Use it to quickly set up a secure environment using the firewall creation
wizard, or use it's monitoring and administrating features with your old
firewall scripts.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
		%{buildroot}%{_sbindir} \
		%{buildroot}%{_initrddir} \
		%{buildroot}%{_sysconfdir}/pam.d \
		%{buildroot}%{_sysconfdir}/security/console.apps
%makeinstall
%find_lang %{name}

%{__mv} %{buildroot}/%{_bindir}/firestarter %{buildroot}%{_sbindir}
%{__ln_s} -f %{_bindir}/consolehelper %{buildroot}%{_bindir}/firestarter

cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/firestarter
auth       sufficient   /lib/security/pam_rootok.so
auth       required     /lib/security/pam_stack.so service=system-auth
session    required     /lib/security/pam_permit.so
session    required     /lib/security/pam_xauth.so
account    required     /lib/security/pam_permit.so
EOF

cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/firestarter
USER=root
FALLBACK=true
PROGRAM="%{_sbindir}/firestarter"
SESSION=true
EOF

%{?rh62: install -m0755 ipchains.init %{buildroot}%{_initrddir}/firestarter}
%{?rh73: install -m0755 netfilter.init %{buildroot}%{_initrddir}/firestarter}
%{?rh80: install -m0755 netfilter.init %{buildroot}%{_initrddir}/firestarter}

%post
/sbin/chkconfig --level 0123456 ipchains off 2>/dev/null || :
/sbin/chkconfig --level 0123456 iptables off 2>/dev/null || :
/sbin/chkconfig --add firestarter
/sbin/chkconfig firestarter on

%preun
if [ $1 = 0 ]; then
	/sbin/chkconfig ipchains reset 2>/dev/null || :
	/sbin/chkconfig iptables reset 2>/dev/null || :
	/sbin/service firestarter stop >/dev/null 2>&1
	/sbin/chkconfig --del firestarter
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CREDITS README TODO
%doc %{_datadir}/gnome/help/firestarter/
%config %{_initrddir}/*
%config %{_sysconfdir}/pam.d/*
%config %{_sysconfdir}/security/console.apps/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/gnome/apps/Internet/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Jan 21 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
