# $Id$
# Authority: dag
# Upstream: Janet Casey <jcasey$gnu,org>
# Upstream: <sercd$lists,lysator,liu,se>

Summary: RFC 2217-compliant serial port redirector
Name: sercd
Version: 2.3.1
Release: 1
License: GPL
Group: Applications/Communications
URL: http://www.lysator.liu.se/~astrand/projects/sercd/

Source: http://www.lysator.liu.se/~astrand/projects/sercd/sercd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
sercd is a RFC 2217 compliant serial port redirector. It is basedxi
on sredird. Other similiar projects are ser2net and msredird.

%prep
%setup

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man8/sercd.8*
%{_sbindir}/sercd

%changelog
* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 2.3.1-1
- Initial package. (using DAR)
