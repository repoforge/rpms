# $Id$
# Authority: matthias

# The driver(s) you want to compile in, e.g. "pctv", "serial", "any"
%define driver "pctv"

# Are we compiling drivers that will need a kernel module too
# (you'll still need to recompile an entire kernel, keep the sources, then
# recompile lirc to get the modules...)
%define kmodule 0

#%%if %{kmodule}
#%%define	kunamer	%%(uname -r)
#%%define	kver	%%(echo $(uname -r) | sed -e s/smp// -)
#%%define	karch	%%(rpm -q --qf '%%%{arch}' kernel-%%{kversion})
#%%define	krelver	%%(echo %%{kunamer} | tr -s '-' '_')
#%%endif

Summary: The Linux Infrared Remote Control package
Name: lirc
Version: 0.6.6
#%%if %{kmodule}
#Release: fr1_%{krelver}
#%%else
Release: 3
#%%endif
License: GPL
Group: System Environment/Daemons
URL: http://www.lirc.org/
Source0: http://dl.sf.net/lirc/%{name}-%{version}.tar.bz2
Source1: lircd.init
Source2: lircd.logrotate
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
PreReq: /sbin/chkconfig, /sbin/service
BuildRequires: perl
#%%if %{kmodule}
#Requires: kernel = %{kver}
#BuildRequires: kernel-source = %{kver}
#%%endif

%description
LIRC is the Linux Infrared Remote Control package.
This package features a clean lircd initscript and a logrotate config file.

The default binary build of this package will only work with the Pinnacle
PCTV serial remote, if you have a different device, you will probably need
to recompile the source RPM changing the "--with-driver=" configure option
to your device.

If your remote requires special kernel modules to run, I guess you're stuck
having to recompile a kernel and recompile lirc manually to get the modules!


%prep
%setup


%build
%configure \
    --with-driver=%{driver} \
    --disable-manage-devices
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__install} -m 755 -D %{SOURCE1} %{buildroot}/etc/init.d/lircd
%{__install} -m 644 -D %{SOURCE2} %{buildroot}/etc/logrotate.d/lircd
%{__perl} -pi -e 's|\@SBINDIR\@|%{_sbindir}|g' %{buildroot}/etc/init.d/lircd
%{__rm} -f doc/Makefile*
%{__mkdir_p} %{buildroot}/dev
%{__ln_s} -f ttyS0 %{buildroot}/dev/lirc
touch %{buildroot}/etc/lircd.conf
touch %{buildroot}/etc/lircmd.conf

%post
/sbin/ldconfig
/sbin/chkconfig --add lircd

%preun
if [ $1 = 0 ]; then
    /sbin/service lircd stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del lircd
fi

%postun
/sbin/ldconfig
if [ "$1" -ge "1" ]; then
    /sbin/service lircd condrestart >/dev/null 2>&1 || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS ChangeLog COPYING NEWS README TODO doc remotes
%doc contrib/*.conf contrib/irman2lirc contrib/lircrc contrib/lircs
/etc/init.d/lircd
/etc/logrotate.d/lircd
%ghost %config(noreplace) /etc/lircd.conf
%ghost %config(noreplace) /etc/lircmd.conf
%{_bindir}/*
%{_sbindir}/*
%{_includedir}/lirc
%{_libdir}/liblirc_*
%{_mandir}/man?/*
%if %{kmodule}
#/lib/modules/%{kver}/misc/*
%attr(0644, root, root) %dev(c, 61, 0) /dev/lirc
%else
/dev/lirc
%endif

%changelog
* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-3
- Added missing /sbin/ldconfig calls.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.6.6-2
- Rebuild for Fedora Core 2... this spec file still _really_ needs reworking!

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.6.6-2
- Rebuild for Fedora Core 1... this spec file _really_ needs reworking!

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9... this spec file needs some reworking!

* Mon Oct  7 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.6 final.

* Mon Sep 16 2002 Matthias Saou <http://freshrpms.net/>
- Updated to latest pre-version.
- Kernel modules still need to be compiled separately and with a custom
  kernel :-(

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5.
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Thu Oct  4 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

