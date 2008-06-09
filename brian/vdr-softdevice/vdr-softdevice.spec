%define pname     softdevice
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.3.1
Release:        1
Summary:        Software output device for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.berlios.de/vdr/
Source0:        http://www.berlios.de/vdr/downloads/%{name}-%{version}.tgz
Source1:        %{name}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47 alsa-lib-devel >= 1.0.13 libXv-devel >= 1.0.0 libXinerama-devel >= 1.0.0 ffmpeg-devel >= 0.4.9 directfb-devel >= 0.9.20
Requires:       vdr(abi) = %{apiver} alsa-lib libXv >= 1.0.0 libXinerama >= 1.0.0 ffmpeg >= 0.4.9 directfb >= 0.9.20

%description
This VDR plugin is designed for soft decoding the MPEG stream to get
low-budged DVB Cards (without MPEG decoder) running.

%prep
%setup -q -n softdevice-%{version}


%build
./configure
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT/usr/bin/
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -pm 755 lib%{pname}-shm.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -pm 755 lib%{pname}-xv.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -pm 755 ShmClient $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%{plugindir}/lib%{pname}-shm.so.%{apiver}
%{plugindir}/lib%{pname}-xv.so.%{apiver}
/usr/bin/ShmClient


%changelog

