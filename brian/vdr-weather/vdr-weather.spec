%define pname     weather
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.2.1e
Release:        1
Summary:        Weather report for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.berlios.de/vdr/
Source0:        http://www.berlios.de/vdr/downloads/%{name}-%{version}.tar.bz2
Patch1:         weather-02_vdr_1.3-fix.dpatch
Patch2:         weather-03_g++4.1-fix.dpatch
Patch3:         weather-04_ftp-location.dpatch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47 mdsplib-devel ftplib-devel
Requires:       vdr(abi) = %{apiver} mdsplib ftplib

%description
This plugin displays the wather report

%prep
%setup -q -n %{pname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
#./configure
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT/usr/bin/
install -pm 755 libvdr-%{pname}.so $RPM_BUILD_ROOT%{plugindir}/libvdr-%{pname}.so.%{apiver}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog

