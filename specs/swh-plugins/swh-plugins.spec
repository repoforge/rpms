# $Id$
# Authority: dag
# Upstream: Steve Harris <steve$plugin,org,uk>

Summary: Steve Harris's set of audio plug-ins for LADSPA
Name: swh-plugins
Version: 0.4.7
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.plugin.org.uk/

Source: http://plugin.org.uk/releases/%{version}/swh-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ladspa-devel, fftw-devel, gcc-c++

%description
swh-plugins is a set of audio plugins for LADSPA written.

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.7-1.2
- Rebuild for Fedora Core 5.

* Mon Jul 19 2004 Dag Wieers <dag@wieers.com> - 0.4.7-1
- Updated to release 0.4.7.

* Mon Jul 05 2004 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Updated to release 0.4.4.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Initial package. (using DAR)
