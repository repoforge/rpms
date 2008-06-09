%define pname     reelchannelscan
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.4.3
Release:        1
Summary:        Channel scanner for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.berlios.de/vdr/
Source0:        http://www.berlios.de/vdr/downloads/%{name}-%{version}.tar.bz2
Patch1:         04_reelchannelscan-0.3.0-configdir.dpatch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47 
Requires:       vdr(abi) = %{apiver}

%description
This plugin allows VDR to scan for DVB channels and to update the channels.conf
configuration file

%prep
%setup -q -n %{pname}-%{version}
%patch1 -p1


%build
#./configure
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT%{configdir}/plugins/%{pname}
cp -r transponders  $RPM_BUILD_ROOT%{configdir}/plugins/%{pname}/
install -dm 644 $RPM_BUILD_ROOT%{configdir}/plugins/%{pname}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%{configdir}/plugins/%{pname}
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog

