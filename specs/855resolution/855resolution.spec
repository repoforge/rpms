# $Id$
# Authority: matthias

Summary: Change video bios resolutions on laptops with Intel graphic chipsets
Name: 855resolution
Version: 0.4
Release: 4%{?dist}
License: Public Domain
Group: Applications/System
URL: http://perso.wanadoo.fr/apoirier/
Source0: http://perso.wanadoo.fr/apoirier/855resolution-%{version}.tgz
Source1: 855resolution.init
Source2: 855resolution.pm-hook
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# This utility doesn't make sense on other archs, those chipsets are i386 only
ExclusiveArch: i386

%description
This software changes the resolution of an available vbios mode. It is useful
when the native screen resolution isn't advertised as available by the video
bios by default.

It patches only the RAM version of the video bios so the new resolution is
lost after each reboot. If you want to have the resolution set after each
boot, then you need to edit %{_sysconfdir}/sysconfig/855resolution.


%prep
%setup -n %{name}
# Add OPTFLAGS to CFLAGS
%{__perl} -pi -e 's|-Wall|-Wall \${OPTFLAGS}|g' Makefile


%build
%{__make} %{?_smp_mflags} OPTFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}

# Manually install the binary
%{__install} -D -m 0755  855resolution %{buildroot}%{_sbindir}/855resolution

# Init script
%{__install} -D -m 0755 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/855resolution

# Power Management hook, as 15 since video is 20 (for suspend to disk)
%{__install} -D -m 0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/pm/hooks/15resolution

# Default sysconfig entry.
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sysconfig/
%{__cat} > %{buildroot}%{_sysconfdir}/sysconfig/855resolution << EOF
# Mode to overwrite (use "855resolution -l" to see all available modes)
MODE="49"
# Resolution to set (i.e. "1280 768", no "x", only a space as the separator)
RESOLUTION="1280 768"
EOF

%clean
%{__rm} -rf %{buildroot}


%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add 855resolution
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del 855resolution
fi


%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt LICENSE.txt README.txt
%config %{_sysconfdir}/pm/hooks/15resolution
%config %{_sysconfdir}/rc.d/init.d/855resolution
%config(noreplace) %{_sysconfdir}/sysconfig/855resolution
%{_sbindir}/855resolution


%changelog
* Thu Mar 23 2006 Matthias Saou <http://freshrpms.net/> 0.4-4
- Add pm hook script in order to fix suspend to disk resume, as the video BIOS
  resolution needs to be overwritten before video is started upon resume too.
  Thanks to Luke Hutchison for the script and the testing.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.4-3
- Release bump to drop the disttag number in FC5 build.

* Tue Jul  5 2005 Matthias Saou <http://freshrpms.net/> 0.4-2
- Make package ExclusiveArch i386, it doesn't make sense on other archs.
- Fix init script (add subsys lock) to not have it run on each runlevel change.
- Enable service by default : People who install this package want it!

* Mon Jul  4 2005 Matthias Saou <http://freshrpms.net/> 0.4-1
- Initial RPM release.

