%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-ffnetdev
Version:        0.1.0
Release:        10.svn30%{?dist}
Summary:        Full featured network DVB device for streaming clients

Group:          Applications/Multimedia
License:        GPL
URL:            https://developer.berlios.de/projects/ffnetdev/
Source0:        http://download.berlios.de/ffnetdev/%{name}-%{version}.tar.bz2
Source1:        %{name}.conf
# Patch0 from http://zap.tartarus.org/~ds/debian/dists/sarge/main/source/misc/vdr-plugin-remote_0.3.3-5.diff.gz
#Patch0:         %{name}-poison.patch
#Patch1:		%{name}-pes2ts.patch
#Patch2:		%{name}-tsworker.patch
#Patch3:		%{name}-newpoison.patch
#Patch4:		%{name}-Active.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
Requires:       vdr(abi) = %{apiver}

%description
The purpose of this plugin is to provide an "easy" way of
connecting possible streaming clients to VDR by emulating
a full featured DVB device over the network including
OSD and TS streaming capabilities.

%prep
%setup -q
#patch0 -p1
#patch1
#patch2
#patch3 -p1
#patch4 -p1
#f=HISTORY ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f

sed -i -e s/VDRVERSION/APIVERSION/g Makefile

%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-ffnetdev.so.* $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/ffnetdev.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README CHANGELOG COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/ffnetdev.conf
%{plugindir}/libvdr-ffnetdev.so.*


%changelog
* Wed Jun 13 2007 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-10.svn30
- Update to svn revision 30.

* Wed Feb 14 2007 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-10.svn28
- Update to svn revision 28.

* Sun Jan 28 2007 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-10.svn26
- Update to svn revision 26.

* Wed Jan 17 2007 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-10.svn25
- Update to svn revision 25.

* Mon Jan 15 2007 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-10.svn23
- Rebuild for vdr-1.4.5.

* Mon Nov 13 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-9.svn23
- Rebuild for vdr-1.4.4.

* Wed Nov 01 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-8.svn23
- Rebuild for FC6.

* Tue Sep 26 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-7.svn23
- Rebuild for vdr-1.4.3.

* Fri Aug 11 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-6.svn23
- Rebuild for vdr-1.4.1-8.

* Sun Jun 11 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-5.svn23
- Update to svn revision 23.
- Rebuild for vdr-1.4.1.

* Wed May 31 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-5.svn22
- Update to svn revision 22.

* Tue May 09 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-5.svn16
- Update to svn revision 16, which supports multi-area OSD.

* Tue May 02 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-5.svn14
- Rebuild for vdr-1.4.0.
- Update to latest svn snapshot.

* Mon Apr 24 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-4
- require vdr(abi)

* Fri Apr 21 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-3
- Rebuild and patch for vdr-1.3.47.

* Thu Mar 30 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-2
- Rebuild for vdr-1.3.45.

* Tue Mar 28 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-1
- Rebuild for vdr-1.3.44.

* Tue Feb 28 2006 Andreas Müller <mail@andreas-mueller.com> - 0.1.0-0.aml.1.4
- Update to 0.1.0.
- Rebuild for vdr-1.3.43.

* Wed Feb 08 2006 Andreas Müller <mail@andreas-mueller.com> - 0.0.5-0.aml.2.4
- Rebuild for vdr-1.3.42.

* Mon Jan 30 2006 Andreas Müller <mail@andreas-mueller.com> - 0.0.5-0.aml.1.4
- New upstream version.
- Rebuild for vdr-1.3.40.

* Wed Jan 18 2006 Andreas Müller <mail@andreas-mueller.com> - 0.0.4-1.aml.9.4
- Rebuild for vdr-1.3.39.

* Thu Dec  1 2005 Andreas Müller <mail@andreas-mueller.com> - 0.0.4-0.aml.8.4
- Rebuild for vdr-1.3.37.

* Tue Nov 15 2005 Andreas Müller <mail@andreas-mueller.com> - 0.0.4-0.7.aml
- Rebuild for vdr-1.3.36.

* Sun Oct  9 2005 Andreas Müller <mail@andreas-mueller.com> - 0.0.4-0.6.aml
- Rebuild for vdr-1.3.34.

* Thu Sep 29 2005 Andreas Müller <mail@andreas-mueller.com> - 0.0.4-0.4.aml
- Rebuild for vdr-1.3.33.

* Thu Sep 22 2005 Andreas Müller <mail@andreas-mueller.com> - 0.0.4-0.1.aml
- First build.
