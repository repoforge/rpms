# $Id$

# Authority: dag

# Upstream: <ra@maisondubonheur.com>

Summary: A graphical interface for RPM analyze.
Name: rpm-analyzer
Version: 1.0
Release: 0.r10
License: GPL
Group: Applications/System
URL: http://www.maisondubonheur.com/rpm-analyzer/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.maisondubonheur.com/rpm-analyzer/dl/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: pygtk2, python2, rpm-python, rhpl, libxml2-python
Requires: pygtk2, python2, rpm-python, rhpl, libxml2-python

%description
rpm-analyzer  provides  a  graphical  interface  that  allows 
the user to view a RPM dependencies according to the local rpm 
configuration or a user-defined rpm configuration. This tool is 
hdlist based and may require a comps.xml file for some features
so please consider installing comps.

%prep
%setup

### FIXME: Make Makefile obey the autotools rules. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\@if|#\@if|;
		s|/usr/local/bin|\$(bindir)|;
		s|\$\(MANDIR\)|\$(mandir)|;
		s|\$\(RADATADIR\)|\$(datadir)/rpm-analyzer|;
	' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall install-man

### FIXME: Fix the link to the binary. (Please fix upstream)
%{__ln_s} -f %{_datadir}/rpm-analyzer/rpm-analyzer.py %{buildroot}%{_bindir}/rpm-analyzer

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/rpm-analyzer/

%changelog
* Wed Aug 20 2003 Dag Wieers <dag@wieers.com> - 1.0-0.r10
- Updated to release 1.0-10.

* Wed Aug 20 2003 Dag Wieers <dag@wieers.com> - 1.0-0.r8
- Initial package. (using DAR)
