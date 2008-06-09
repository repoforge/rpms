%define pname     analogtv
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        1.0.00
Release:        3.bs%{?dist}
Summary:        Analog plugin for VDR

Group:          Multimedia/Video
License:        GPL
URL:            http://www.andreaskool.de
Source0:        http://localhost/vdr/%{name}-%{version}.tar.bz2
#Source1:        %{name}.conf
Patch0:		cpu_accel.c.patch
Patch1:		cpuinfo.c.patch
Patch2:		player-analogtv.c.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.4.4, libdvb-devel, libjpeg-devel, gcc-c++
Requires:       vdr(abi) = %{apiver}, libdvb >= 0.5.4

%description
This is a VDR plugin to integrate bttv/v4l2 compatible video cards into the VDR


%prep
%setup -q -n analogtv-%{version}
for f in HISTORY README ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done
#%patch0 -p1
#%patch1 -p1
#%patch2 -p4


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
#install -Dpm 644 %{SOURCE1} \
#  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
#%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
* Wed Jan 23 2008 Brian Schueler <brian.schueler@gmx.de> 1.0.00
- First build.
