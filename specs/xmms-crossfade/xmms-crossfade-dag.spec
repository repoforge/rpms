# $Id$
# Authority: matthias
# Upstream: Peter Eisenlohr <p.eisenlohr@gmx.net>

%define xmms_outputdir %(xmms-config --output-plugin-dir)

Summary: Crossfade output plugin for XMMS
Name: xmms-crossfade
Version: 0.3.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.mynetcologne.de/~nc-eisenlpe2/xmms-crossfade/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.mynetcologne.de/~nc-eisenlpe2/xmms-crossfade/xmms-crossfade-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xmms-devel


%description
A neat crossfade plugin for XMMS featuring crossfading and continuous output
between songs and a gap-killer.


%prep
%setup


%build
%configure \
	--libdir="%{xmms_outputdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_outputdir}"
%{__strip} %{buildroot}/%{xmms_outputdir}/*.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{xmms_outputdir}/*.so
%exclude %{xmms_outputdir}/*.la


%changelog
* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.3.4-0
- Updated to release 0.3.4.

* Tue Oct 07 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Updated to release 0.3.3.

* Tue Apr 22 2003 Dag Wieers <dag@wieers.com> - 0.3.2-0
- Updated to release 0.3.2.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Updated to release 0.3.1.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Updated to release 0.3.0.

* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 0.2.9-0
- Initial package. (using DAR)
