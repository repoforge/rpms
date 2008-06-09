%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-streamdev
Version:        0.3.4
Release:        1.bs%{?dist}
Summary:        Client/Server Streaming for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://streamdev.vdr-developer.org/
Source0:	http://streamdev.vdr-developer.org/releases/vdr-streamdev-%{version}.tgz
#Source0:       	http://mitglied.lycos.de/peterweber69/streamdev_for_VDR-1.3.23.tar.gz
#Source0:	streamdev.tar.gz
Source1:        %{name}.conf
#Patch0:		http://anssi.hopto.org/vdr/vdr-1.3.17-stream-0.3.3-pre3-geni-poison.diff	
#Patch1:		vdr-streamdev-summary.patch
#Patch2:		vdr-streamdev-gcc4.patch.old
#Patch3:		streamdev-20050922-vdr-1.3.32.diff
#Patch4:		vdr-streamdev-server-Active.patch
#Patch10:	%{name}-Makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47, gcc-c++
Requires:       vdr(abi) = %{apiver}

%description
%{summary}.

%package server
Summary:        Client/Server Streaming for VDR
Group:          Applications/Multimedia
Requires:	vdr(abi) = %{apiver}
Requires:	%{name} = %{version}-%{release}

%description server
%{summary}.

%package client
Summary:        Client/Server Streaming for VDR
Group:          Applications/Multimedia
Requires:       vdr(abi) = %{apiver}
Requires:	%{name} = %{version}-%{release}

%description client
%{summary}.

%prep
%setup -q -n streamdev-%{version}
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch10

#sed -i -e s/VDRVERSION/APIVERSION/g Makefile

%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr libvdr-streamdev-server.so libvdr-streamdev-client.so


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-streamdev-server.so.* $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-streamdev-client.so.* $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/streamdev.conf


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/streamdev.conf

%files server
%{plugindir}/libvdr-streamdev-server.so*

%files client
%{plugindir}/libvdr-streamdev-client.so*

%changelog
* Fri May  2 2008 Brian Schueler <brian.schueler@gmx.de> - 0.3.4-1
- Update to 0.3.4 release

* Wed Jun 13 2007 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-18.svn20070509
- Update to new svn version.

* Mon Jan 15 2007 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-17
- Rebuild for vdr-1.4.5.

* Mon Nov 13 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-16
- Rebuild for vdr-1.4.4.

* Wed Nov 01 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-15
- Rebuild for FC6.

* Tue Sep 26 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-14
- Rebuild for vdr-1.4.3.

* Fri Aug 11 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-13
- Rebuild for vdr-1.4.1-8.

* Sun Jun 11 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-12
- Rebuild for vdr-1.4.1.

* Tue May 02 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-11
- Rebuild for vdr-1.4.0.

* Mon Apr 24 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-10
- Require vdr(abi) instead of vdr.

* Fri Apr 21 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-9
- Rebuild and patch for vdr-1.3.47.

* Thu Mar 30 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-8
- Rebuild for vdr-1.3.45.

* Tue Mar 28 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-7
- Rebuild for vdr-1.3.44.

* Tue Feb 28 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-6.aml.2.4
- Rebuild for vdr-1.3.43.

* Sun Feb 12 2006 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-6.aml.1.4
- Rebuild for vdr-1.3.42.
- Update to new CVS version.

* Sat Oct  1 2005 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-4.aml
- Rebuilt against vdr-1.3.33.

* Wed Sep 13 2005 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-3.aml
- Rebuild against vdr-1.3.32.

* Thu Sep  9 2005 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-2.aml
- Rebuild against vdr-1.3.31.

* Wed May 11 2005 Andreas Müller <mail@andreas-muelelr.com> - 0.3.3-1.aml
- Rebuild against vdr-1.3.24.

* Wed May  4 2005 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-0.2
- Rebuild against vdr with UTF-8 patch applied.

* Mon May  2 2005 Andreas Müller <mail@andreas-mueller.com> - 0.3.3-0.1
- First build.
