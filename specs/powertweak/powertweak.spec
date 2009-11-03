# $Id$

# Authority: dag

Summary: Tune system to optimal performance
Name: powertweak
Version: 0.99.5
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://powertweak.sourceforge.net/

Source: http://dl.sf.net/powertweak/powertweak-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Obsoletes: pwrtweak
Requires: pciutils
BuildRequires: libxml2-devel, gtk+-devel, gcc-c++

%description
Powertweak is a utility for tweaking your Linux system to peak performance.
It can tune the following parts of your system:
o  Tunes PCI devices to use optimal settings.
o  Enables performance enhancing features.
o  Kernel parameters
o  CPU registers
o  Chipset register settings
o  Sony VAIO backlight
To make use of all the features of this program, you need to have a Linux
kernel which supports the /proc/bus/pci interface.

%package gui
Summary: Powertweak GTK userinterface
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%description gui
This is the GTK version of the Powertweak user interface. Install
this if you have X and the GTK libraries installed.

%package text
Summary: Powertweak textmode userinterface
Group: Applications/System
Requires: powertweak

%description text
This is the text version of the Powertweak userinterface. Install
this if you don't have X installed.

%prep
%setup

%build
#libtoolize
#aclocal
#autoheader
#autoconf
#automake --add-missing
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_localstatedir}/adm/fillup-templates \
			%{buildroot}%{_sysconfdir}/powertweak

#%{__install} -p -m0755 distro/SuSE/rc.powertweakd %{buildroot}%{_initrddir}/powertweakd
#ln -s %{_initrddir}/powertweakd $RPM_BUILD_ROOT%{_sbindir}/rcpowertweakd
#install -m 644 distro/SuSE/rc.config.powertweakd $RPM_BUILD_ROOT/var/adm/fillup-templates/rc.config.powertweakd
# Touch config file placeholder
touch %{buildroot}%{_sysconfdir}/powertweak/tweaks

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/powertweak/plugins/*.a \
		%{buildroot}%{_libdir}/powertweak/plugins/*.la \
		%{buildroot}%{_libdir}/powertweak/plugins/*.so.0

find %{buildroot}%{_libdir}/powertweak/plugins/ -type f -name "\*.so.\*" -exec strip --strip-unneeded {} \;

#%post
#sbin/insserv etc/init.d/powertweakd
#echo "Updating etc/rc.config..."
#if [ -x bin/fillup ] ; then bin/fillup -q -d = etc/rc.config var/adm/fillup-templates/rc.config.powertweakd
#else
#echo "ERROR: fillup not found. This should not happen. Please compare"
#echo "/etc/rc.config and /var/adm/fillup-templates/rc.config.powertweakd and update by hand."
#fi
#%postun
#sbin/insserv etc/init.d/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING Documentation/* NEWS README TODO
#%config /etc/init.d/powertweakd
#%config(missingok,noreplace) %ghost /etc/powertweak/tweaks
#%{_sbindir}/powertweakd
#%{_sbindir}/rcpowertweakd
%{_libdir}/powertweak/
%{_datadir}/powertweak/
#/var/adm/fillup-templates/rc.config.powertweakd

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/gpowertweak

%files text
%defattr(-, root, root, 0755)
%{_bindir}/powertweak

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.99.5-0.2
- Rebuild for Fedora Core 5.

* Thu Jul 10 2003 Dag Wieers <dag@wieers.com> - 0.99.5-0
- Initial package. (using DAR)
