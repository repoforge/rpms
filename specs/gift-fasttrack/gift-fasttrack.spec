# $Id$
# Authority: dries

Summary: Gift plugin to access the fasttrack network
Name: gift-fasttrack
Version: 0.8.5
Release: 1
License: GPL
Group: Development/Libraries
URL: http://developer.berlios.de/projects/gift-fasttrack

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://download.berlios.de/gift-fasttrack/giFT-FastTrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gift, pkgconfig
Requires: gift

%description
giFT is a modular daemon capable of abstracting the communication between the
end user and specific filesharing protocols (peer-to-peer or otherwise). This
packages provides the plugin to access the fasttrack network.

%prep
%setup -n giFT-FastTrack-%{version}

%{__perl} -pi.orig -e '
		s|\@plugindir\@|\$(libdir)/giFT|g;
		s|\$\(datadir\)|\$(datadir)/giFT|g;
	' Makefile.in */Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config(noreplace) %{_datadir}/giFT/FastTrack/
%dir %{_libdir}/giFT/
%exclude %{_libdir}/giFT/libFastTrack.la
%{_libdir}/giFT/libFastTrack.so
%dir %{_datadir}/giFT/

%changelog
* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.8.5-1
- first packaging for Fedora Core 1

