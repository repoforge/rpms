# $Id$

# Authority: dag

%define rversion 0.3.7.beta

Summary: A network protocol analyzer.
Name: sniffit
Version: 0.3.7
Release: 0.beta
License: Freely distributable
Group: Applications/Internet
URL: http://reptile.rug.ac.be/~coder/sniffit/sniffit.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://reptile.rug.ac.be/~coder/sniffit/files/%{name}.%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Excludearch: ia64

%description
Sniffit is a robust non-commercial network protocol analyzer or packet
sniffer.  A packet sniffer basically listens to network traffic and
produces analysis based on the traffic and/or translates packets into
some level of human readable form.

%prep
%setup -n %{name}.%{rversion}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man{5,8}/
%{__install} -m0755 sniffit   %{buildroot}%{_sbindir}
%{__install} -m0444 sniffit.5 %{buildroot}%{_mandir}/man5/
%{__install} -m0444 sniffit.8 %{buildroot}%{_mandir}/man8/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BETA-TESTING HISTORY LICENSE README.FIRST sample_config_file sniffit-FAQ
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.3.7-0.beta
- Initial package. (using DAR)
