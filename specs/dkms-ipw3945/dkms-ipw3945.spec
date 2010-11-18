# $Id$
# Authority: matthias

# ExclusiveDist: el4

Summary: Driver for Intel® PRO/Wirelss 3945 network adaptors
Name: dkms-ipw3945
Version: 1.2.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://ipw3945.sourceforge.net/
Source: http://dl.sf.net/ipw3945/ipw3945-%{version}.tgz
Patch0: ipw3945-1.2.0-options.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires: ipw3945-firmware, ipw3945d
Requires(post): dkms
Requires(preun): dkms
Provides: ipw3945 = %{version}-%{release}

%description
Driver (Linux kernel module) for Intel® PRO/Wirelss 3945 network adaptors.


%prep
%setup -n ipw3945-%{version}
%patch0 -p1


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name ipw3945
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a *.h *.c Makefile snapshot/ \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=ipw3945
DEST_MODULE_LOCATION[0]=/kernel/drivers/net/wireless
AUTOINSTALL="YES"
EOF

# File to set special compile options (created and used by our patch)
%{__install} -p -D -m 0644 options.mak \
    %{buildroot}%{_sysconfdir}/sysconfig/ipw3945-options.mak


%clean
%{__rm} -rf %{buildroot}


%post
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
# Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all || :


%files
%defattr(-,root,root,-)
%doc CHANGES ISSUES LICENSE* README.ipw3945
%config(noreplace) %{_sysconfdir}/sysconfig/ipw3945-options.mak
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Fri May 18 2007 Matthias Saou <http://freshrpms.net/> 1.2.1-1
- Update to 1.2.1.
- Drop upstreamed previous patch.

* Mon Jan 29 2007 Matthias Saou <http://freshrpms.net/> 1.2.0-3
- Add RF kill deadlock patch (upstream #1096), Stefan Becker.

* Fri Jan 26 2007 Matthias Saou <http://freshrpms.net/> 1.2.0-2
- Extract part of the Makefile in order to make setting options possible.
- Build monitor mode option by default.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0.
- Remove now included register and ESSID patches.
- Remove no longer relevant 2.6.20 fixes patches.

* Wed Dec 20 2006 Matthias Saou <http://freshrpms.net/> 1.1.3-2
- Update to 1.1.3.
- Include ESSID fix patch.
- Include fixes for 2.6.20 but disabled since they break with earlier kernels.

* Mon Nov 27 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Update to 1.1.2.
- Add versionned plain ipw3945 provides.

* Tue Oct 10 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-2
- Add the rpm release to the dkms module version, to make updating the module
  to a fixed same version work (--rpm_safe_upgrade doesn't work as advertised).
- Force modules install so that the same version can be overwritten instead of
  uninstalled by the old package's %%preun when updating.
- Add build time quiet flag for the scriplets. Undefine to do verbose testing.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Initial RPM release.

