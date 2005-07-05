# $Id$
# Authority: matthias

Summary: Change video bios resolutions on laptops with Intel graphic chipsets
Name: 855resolution
Version: 0.4
Release: 1
License: Public Domain
Group: Applications/System
URL: http://perso.wanadoo.fr/apoirier/
Source0: http://perso.wanadoo.fr/apoirier/855resolution-%{version}.tgz
Source1: 855resolution.init
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%config %{_sysconfdir}/rc.d/init.d/855resolution
%config(noreplace) %{_sysconfdir}/sysconfig/855resolution
%{_sbindir}/855resolution


%changelog
* Mon Jul  4 2005 Matthias Saou <http://freshrpms.net/> 0.4-1
- Initial RPM release.

