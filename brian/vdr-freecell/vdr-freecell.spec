%define pname     freecell
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.0.2
Release:        0.2
Summary:        Freecell solitaire plugin for VDR

Group:          Amusements/Games
License:        GPL
URL:            http://www.magoa.net/linux/index.php?view=freecell
Source0:        http://www.magoa.net/linux/files/%{name}-%{version}.tgz
Source1:        %{name}.conf
Patch0:         http://ftp.debian.org/debian/pool/main/v/vdr-plugin-freecell/vdr-plugin-freecell_0.0.2-24.diff.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
Requires:       vdr(abi) = %{apiver}

%description
The Freecell plugin is an implementation of the (well-known) card
game "Freecell" played on the on screen display of VDR.


%prep
%setup -q -n freecell-%{version}
%patch0 -p1
patch -p1 -i debian/patches/02_gcc3.4-fix.dpatch
patch -p1 -i debian/patches/92_freecell-1.3.18.dpatch
sed -i -e '/^DVBDIR/d' -e 's|-I$(DVBDIR)/include||' Makefile
sed -i -e s/VDRVERSION/APIVERSION/g Makefile


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins
cp -pR %{pname} $RPM_BUILD_ROOT%{configdir}/plugins


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CONTRIBUTORS COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{configdir}/plugins/%{pname}/
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
* Mon Jun 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.2-0.2
- Adjust for VDR 1.4.1.

* Fri Aug 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.2-0.1
- First build.
