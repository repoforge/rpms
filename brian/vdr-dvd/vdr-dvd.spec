%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-dvd
Version:        0.0
Release:        0.1.20070520%{?dist}
Summary:        DVD plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://sourceforge.net/projects/dvdplugin
Source0:        %{name}-20070520.tar.bz2
#Source1:        %{name}-waphosts
#Source2:        %{name}-wapaccess
#Source3:        %{name}-proxy.conf
Source4:        %{name}.conf
#Patch0:         %{name}-fixes.patch
#Patch1:         %{name}-nptl.patch
#Patch2:         %{name}-1.3.32.patch
#Patch3:         %{name}-1.3.36.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
BuildRequires:  libdvdcss-devel, libdvdnav-devel, a52dec-devel 
Requires:       vdr(abi) = %{apiver}

%description
The wapd plugin lets VDR listen to WAP requests to allow remote
control by WML enabled browsers.


%prep
%setup -q -n dvd-20070520
#%patch0
#%patch1 -p1
#%patch2
#%patch3
#iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY
#sed -i -e 's|/video/plugins|%{configdir}/plugins|' README


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-dvd.so.* $RPM_BUILD_ROOT%{plugindir}
#install -Dpm 755 wappasswd $RPM_BUILD_ROOT%{_bindir}/wappasswd
#install -Dpm 640 %{SOURCE1} $RPM_BUILD_ROOT%{configdir}/plugins/waphosts
#install -Dpm 640 %{SOURCE2} $RPM_BUILD_ROOT%{configdir}/plugins/wapaccess
#install -Dpm 644 %{SOURCE3} \
#  $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/vdr-wapd.conf
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/dvd.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/dvd.conf
%{plugindir}/libvdr-dvd.so.*


%changelog
* Sun May 20 2007 Andreas Müller <mail@andreas-mueller.com> 0.0-0.1.20070520cvs
- First build.
