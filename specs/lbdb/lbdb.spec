# $Id$
# Authority: dag
# Upstream: Roland Rosenfeld <roland$spinnaker,de>

Name: lbdb
Summary: Address database for mutt
Version: 0.29
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.spinnaker.de/lbdb/

Source: http://www.spinnaker.de/debian/lbdb_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Little Brother's Database (lbdb) consists of a set of small
tools which collect mail addresses from several sources and offer
these addresses to the external query feature of the Mutt mail
reader.

%prep
%setup

%{__perl} -pi.orig -e 's|^(METHODS)=.+$|$1=m_inmail m_finger m_getent|' lbdb.rc.in

%build
%configure \
	--libdir="%{_libdir}/lbdb"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}
%makeinstall \
	libdir="%{buildroot}%{_libdir}/lbdb"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/lbdb/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.26.2-1
- Initial package. (using DAR)
