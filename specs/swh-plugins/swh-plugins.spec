# $Id$

# Authority: dag
# Upstream: Steve Harris <steve@plugin.org.uk>

# Distcc: 0

Summary: Steve Harris's set of audio plug-ins for LADSPA.
Name: swh-plugins
Version: 0.4.3
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.plugin.org.uk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://plugin.org.uk/releases/%{version}/swh-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ladspa-devel, fftw-devel

%description
swh-plugins is a set of audio plugins for LADSPA written by Steve Harris.
                                                                                
%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/

%changelog
* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Initial package. (using DAR)
